> **Compare:** Jakarta EE and Quarkus have no `JdbcTemplate`. There you inject a `DataSource` (the Agroal pool in Quarkus) and use plain JDBC, or use JPA/Panache. Spring Data JPA is in [Spring Data JPA](Spring%20Data%20JPA.md).

## Exceptions: `DataAccessException`
`SQLException` is checked, so every intermediate method would have to declare it. Spring translates it into its **unchecked** `DataAccessException` hierarchy (`DuplicateKeyException`, `EmptyResultDataAccessException`, `DataIntegrityViolationException`, ...). Exceptions can then propagate to the place that can actually handle them. All Spring data-access exceptions are unchecked. `@Repository` beans get this translation automatically.

## Data source
Dependencies: `spring-boot-starter-jdbc` plus a driver, for example H2 (`com.h2database:h2`, scope `runtime`).
```properties
spring.datasource.url=jdbc:mariadb://localhost:3306/dragonbank
spring.datasource.username=goblin-dba
spring.datasource.password=Sh1nyG0ld
spring.datasource.driver-class-name=org.mariadb.jdbc.Driver   # usually inferred from the URL

spring.sql.init.mode=always                                   # run the scripts also for non-embedded DBs
spring.sql.init.schema-locations=classpath:db/schema.sql
spring.sql.init.data-locations=classpath:db/data.sql

spring.h2.console.enabled=true                                # web console at /h2-console
```
Without Spring Boot, or to customize the pool, define the bean yourself:
```java
@Bean
DataSource dataSource() {
    HikariDataSource ds = new HikariDataSource();
    ds.setJdbcUrl("jdbc:mariadb://localhost:3306/dragonbank");
    ds.setUsername("goblin-dba");
    ds.setPassword("Sh1nyG0ld");
    ds.setConnectionTimeout(1000);
    return ds;
}
```
> **Compare:** this is the same idea as `quarkus.datasource.*`; see [Quarkus](../Java,%20Jakarta%20EE,%20Microprofile/Quarkus%20and%20MicroProfile.md#data-access). Spring Boot uses the HikariCP pool and Quarkus uses Agroal.

## `JdbcTemplate`
```java
@Repository
public class JdbcTreasureRepository {
    private final JdbcTemplate jdbc;
    public JdbcTreasureRepository(JdbcTemplate jdbc) { this.jdbc = jdbc; }

    public int count() {
        return jdbc.queryForObject("SELECT COUNT(*) FROM treasure", Integer.class);
    }

    public Treasure findById(long id) {          // throws EmptyResultDataAccessException if there are 0 rows (and an exception for >1 rows too)
        return jdbc.queryForObject("SELECT id, name, type FROM treasure WHERE id = ?", this::mapRow, id);
    }

    public List<Treasure> findAll() {
        return jdbc.query("SELECT id, name, type FROM treasure", this::mapRow);
    }

    public int save(Treasure t) {                // returns the number of affected rows
        return jdbc.update("INSERT INTO treasure (id, name, type) VALUES (?, ?, ?)",
            t.getId(), t.getName(), t.getType().name());
    }

    public Map<String, Object> info(long id) {   // {id=1, name=Crown, type=ARTIFACT}
        return jdbc.queryForMap("SELECT id, name, type FROM treasure WHERE id = ?", id);
    }

    public List<Map<String, Object>> allInfo() { // one map per row
        return jdbc.queryForList("SELECT id, name, type FROM treasure");
    }

    private Treasure mapRow(ResultSet rs, int rowNum) throws SQLException {
        return new Treasure(rs.getLong("id"), rs.getString("name"), TreasureType.valueOf(rs.getString("type")));
    }
}
```
The old `queryForInt`, `queryForLong` and similar methods are gone. Spring 6.1 added the fluent **`JdbcClient`** (`jdbcClient.sql("...").param(id).query(Treasure.class).single()`), and `NamedParameterJdbcTemplate` supports `:name` parameters.

### Callback types
| Interface | Use |
|---|---|
| `RowMapper<T>`: `T mapRow(ResultSet rs, int rowNum)` | one object per row (lambda, method reference, class) |
| `ResultSetExtractor<T>`: `T extractData(ResultSet rs)` | the whole result set to one object; you call `rs.next()` yourself; good for joins |
| `RowCallbackHandler`: `void processRow(ResultSet rs)` | processes rows without returning anything (e.g. writing to a file) |

```java
// A join: one hoard with many treasures
public Hoard findHoard(long hoardNumber) {
    return jdbc.query(
        "SELECT h.number, h.dragon, t.id, t.name, t.type FROM hoard h JOIN treasure t ON t.hoard = h.number WHERE h.number = ?",
        (ResultSetExtractor<Hoard>) rs -> {
            Hoard hoard = null;
            while (rs.next()) {
                if (hoard == null) hoard = new Hoard(rs.getLong("number"), rs.getString("dragon"));
                hoard.addTreasure(mapRow(rs, 0));
            }
            return hoard;
        },
        hoardNumber);
}
```

## `SimpleJdbcInsert`
This builds the INSERT from table metadata and returns the generated key:
```java
private final SimpleJdbcInsert hoardInserter = new SimpleJdbcInsert(jdbc)
    .withTableName("hoard")
    .usingGeneratedKeyColumns("number");

Map<String, Object> values = objectMapper.convertValue(hoard, Map.class);   // Jackson: object to column map
values.put("opened_at", hoard.getOpenedAt());
long number = hoardInserter.executeAndReturnKey(values).longValue();
```
