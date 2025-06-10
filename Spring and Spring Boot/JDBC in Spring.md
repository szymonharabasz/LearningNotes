Dependencies: `spring-boot-started-jdbc`
Database, for example embedded:  
- groupId: `com.h2databade`  
- artifactId: `h2`  
- scope: `runtime`  
- Note: There is an endpoint `localhost:8080/h2-console`
If Spring Boot is not used or one wants to customize the data source properties, then one has to create a bean:  
```Java
HikariDataSource dataSource = new HikariDataSource();  
dataSource.setJdbcUri(…);  
dataSource.setUsername(…);  
dataSource.setPassword(…);  
dataSource.setConnectionTimeout(1000);  
return dataSource;
```
Basic query:  
```
private JdbcTemplate jdbc; // injected  
public int getCarCount() {  
    String sql = "select count (*) from Car";  
    return jdbc.queryForObject(sql, Integer.class);  
}

@Override  
public Car findById(String id) {  
    return jdbc.queryForObject(  
        "select id, name, type from Car where id=?", this::mapRowToCar, id);  
}  

@Override  
public Iterable<Car> findById(String id) {  
    return jdbc.query(  
        "select id, name, type from Car", this::mapRowToCar);  
}  

@Override  
public Car save(Car car) {  
    // Returns number of affected rows    jdbc.update(  
        "insert into Car (id, name, type) values (?, ?, ?)",  
        car.getId(), car.getName(), car.getType().toString());  
    return car;  
}  

private Car mapRowToCar(ResultSet rs, int rowNum) throws SQLException {  
    return new Car(rs.getString("id"), rs.getString("name"),  
        Car.Type.valueOf(rs.getString("type")));  
}  

public Map<String, Object> getCarInfo(String id) {  
    // returns Map { id=1, name="Polonez", type="hatchback" }  
    return jdbc.queryForMap(  
        "select id, name, type from Car where id=?", id);  
}  

public List<Map<String, Object>> getAllCarsInfo() {  
    // returns:  
    // List {  
    //     Map { id=1, name="Polonez", type="hatchback" }  
    //     Map { id=2, name="Fiat 125p", type="sedan" }  
    // }  
    return jdbc.queryForList("select id, name type from Car");  
}  

@Override  
public Order findByConfirmationNumber(String number) {  
    return jdbc.query(        
		"select id, name from Order o, item i...confirmation_id = ?",  
        (ResultSetExtractor<Car>)(rs) -> {  
            Order order = null;  
            while (rs.next()) {  
                if (order == null) {  
                    order = new Order(rs.getLong("id"),rs.getString("name")); 
                }  
                order(addItem(mapItem(rs)));  
            }  
            return order;  
        },  
        number  
    );  
}
```
Older methods like `queryForInt`, `queryForLong` etc. are deprecated.
Second argument for queries can be a functional object of:
```Java
public interface RowMapper<T> {  
    T mapRow(ResultSet rs, int rowNum) throws SQLException;  
}
```
It can be implemented as anonymous object, lambda or method reference (or named object)
```Java
public interface ResultSetExtractor<Car> {  
    T extractData(ResultSet rs)        throws SQLException, DataAccessException;  
}
```
One has to build the result manually based on all the rows returned by the query
```Java
public interface RowCallbackHandler  
```
Useful when one doesn't want to return anything but process the results, e.g., write them to a file.
Using `SimpleJdbcInserter`:  
```Java
private SimpleJdbcInsert orderInserter;  
private ObjectMapper objectMapper;  
      
// In constructor:  
this.orderInserter = new SimpleJdbcInserter(jdbc)  
    .withRableName("orders")  
    .usingGeneratedKeyColumn("id");  
this.objectMapper = new ObjectMapper();  
      
// In save() method:  
@SuppressWarnings("unchecked")  
Map<String, Object> values =  
    objectMapper.convertValue(order, Map.class);  
values.put("placedAt", order.getPlacedAt());  
      
long orderId = orderInserter       .executeAndReturnKey(values)  
    .longValue();  
      
order.setId(orderId);  
return order;
```