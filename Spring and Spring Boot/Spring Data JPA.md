Necessary dependencies if not using Spring Boot:
- `hibernate-core`
- `spring-orm`
- `spring-tx`
- Connector for the specific database e.g. `mysql-connector-java`
- Pooling engine e.g. `c3p0`
Necessary dependencies in the Spring Boot case:
- `spring-boot-data-jpa`
- `mysql-connector-java`
Add schema to `myservlet-servlet.xml` for `spring-tx`
Create (copy-paste) beans:
- `TransactionManager`
- `SessionFactory`
Entity must be annotated with `@Entity`, primary key with `@Id`, optionally with:  
```Java
@GeneratedValue(generator="uuid2")  
@GenericGenerator(name="uuid2", strategy="uuid2")  
```
or  
```Java
@GeneratedValue(strategy=GenerationType.AUTO)
```
`@DiscriminatorValue("ADMIN")`, `@DiscriminatorValue("MEMBER")` etc. on the entity classes extending some parent entity causes the creation of an additional column `dtype` in the database table
If column properties have to be modified, one can annotate the respective field with:  
```Java
@Column(columnDefinition="varchar(36)", unique=true, nullable=false, 
	length=512)
```
One can use:
```Java
@CreationTimeStamp      
Date created;
@UpdateTimeStamp  
Date modified;
```
Constrains: `@NotNull`, `@NotBlank`, `@NotEmpty` (not null and not blank) `@Email`
```Java
@JsonProperty(access = JsonProperty.Access.WRITE_ONLY)
```
On the class: `@JsonInclude(JsonInclude.Include.NON_NULL)` - null fields will not be serialized to JSON
Relation annotations, like in Java EE
```Java
@AttributeOverride(name="value",column=@Column(name="ALLOCATION_PERCENTAGE"))
private Percentage allocationPercentage; 
``` 
populates `Percerntage.value` with the `ALLOCATION_PERCENTAGE` column of the relevant table to which the class in which the property was defined is mapped
Event handlers:  
```Java
@PrePersist,
```
In DAO:  
```Java
@Component  
public class AlienDao {  
    @Autowired  
    private SessionFactory sessionFactory;  
      
    @Transactional  
    public List<Alien> getAliens() {  
        Session session = sessionFactory.getCurrentSession();  
        List<Alien> aliens = session.createQuery("from Alien", 
	        Alien.class).list();  
        return aliens;  
    }
}
```
One-to-many relations - one owner can have many cars, but a car can have only one owner. On the Car side:
```Java
@ManyToOne(fetch = FetchType.LAZY)  
@JoinColumn(name = "owner")  
private Owner owner;
```
On the ManyToOne side default fetch is `EAGER`, so it has to be specified to be `LAZY`
On the Owner side:
```Java
@OneToMany(cascade = CascadeType.ALL, mappedBy="owner")  
private List<Car> cars;
```
Many-to-many relations - one owner can have many cars, and a car can have many owners. On the Car side:
```Java
@ManyToMany(mappedBy = "cars")  
private Set<Owner> owners;
```
On the Owner side:  
```Java
@ManyToMany(cascade = CascadeType.MERGE)
@JoinTable(name = "car_owner", joinColumns = { 
	@JoinColumn(name = "ownerid") },  
    inverseJoinColumns = { @JoinColumn(name = "id") })  
private Set<Car> cars = new HashSet<Car>(0);
```
Cascading means, that if an owner is deleted from the database, all the cars, which belong to him are also deleted.
To avoid infinite recursion when marshalling entities with references to other entities to JSON:  
```Java
@Entity  
@JsonIgnoreProperties({"hibernateLazyInitializer","handler"})  
class Owner {  
    @JsonIgnore  
    private List<Car> cars;  
}
```
With Spring Boot it's necessary and sufficient to add to `application.properties`:  
```Java
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQLDialect  
spring.datasource.url=jdbc:mysql://localhost:3306/mydb  
spring.datasource.username=root  
spring.datasource.password=123456
```
One can extend the interface
```Java
JpaRepository<MyEntityClass, Integer>
CrudRepository<MyEntityClass, Integer>
PagingAndSortingRepository<MyEntityClass, Integer>
```
the second type parameter is the identifier type
`PagingAndSortingRepository` provides new methods:
```Java
Iterable<T> findAll(Sort sort)
Page<T> findAll(Pageable pageable)
```
Define bean of this interface type
Eventually implement this interface, but default implementation will be provided by Spring Data JPA
Query DSL: If an entity has a property with a given name, e.g. `firstName`, one declares a method `findByFirstName` (or `getByFirstName`) in the repository interface. Then Spring Data JPA will generate an appropriate implementation of the method
Other possibilities:
```Java
findByFirstNameOrderByLastNameDesc
```
Operators `And`, `Or`
Synonyms for `find`: `get`, `read`
`IsAfter`, `After`, `IsGreaterThan`, `GreaterThan`
`IsGreaterThanEqual`, `GreaterThanEqual`
`IsBefore`, `Before`, `IsLessThan`, `LessThan`
`IsLessThanEqual`, `LessThanEqual`
`IsBetween`, `Between`
`IsNull`, `Null`
`IsNotNull`, `NotNull`
`IsIn`, `In`
`IsNotIn`, `NotIn`
`IsStartingWith`, `StartingWith`, `StartsWith`
`IsEndingWith`, `EndingWith`, `EndsWith`
`IsContaining`, `Containing`, `Contains`
`IsLike`, `Like`
`IsNotLike`, `NotLike`
`IsTrue`, `True`
`IsFalse`, `False`
`Is`, `Equals`
`IsNot`, `Not`
`IgnoringCase`, `IgnoresCase`
Alternative - query (better performance!):  
```Java
@Query("from User where firstName=:first")  
List<User> find(@Param("first") String firstName) { … }  
@Query("from User where firstName=?1")  
List<User> find(String firstName) { … }
```
Alternative - named query:  
```
@NamedQuery(  
    name = "User.findWithFirstName",  
    query = "from User where firstName=?1")  
public class User { … }  
      
interface UserRepository extends CrudRepository<User, String> {  
    Iterable<User> findWithFirstName(String firstName) { … }  
}
```
Modifying (`CREATE`, `UPDATE`, `DELETE` etc.) querries need to be annotated with
```Java
@Modifying
```
#### Spring Boot specific
Configuration class can be annotated with:      
```Java
@AttributeOverride(name="value",column=@Column(name="ALLOCATION_PERCENTAGE"))EntityScan("rewards.internal")
```
Customize package to scan for repositories:  
```Java
@Configuration  
@EnableJpaRepositories(basePackage="com.acme.repository")
```