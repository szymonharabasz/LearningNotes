Entity annotations:
```Java
@Entity, @Table(name = "CUSTOMERS"), @Id,
@GeneratedValue(strategy = GenerationType.AUTO|TABLE|SEQUENCE|IDENTITY)
@GeneratedValue(strategy = GenerationType.SEQUENCE, generator="MY_SEQ")  
```
assuming that the entity class (or maybe the id field) is annotated with:  
```Java
@SequenceGenerator(name="MY_SEQ", initialValue=1, allocationSize=50)  
```
and a sequence `MY_SEQ` is created in the database
```Java
@GeneratedValue(strategy = GenerationType.TABLE, generator="ID_GEN")  
```
assuming that the `id` field (or maybe the entity class) is annotated with:  
```Java
@TableGenerator(name="ID_GEN", table="ID_GEN_TABLE", pkColumnName="GENERATOR_NAME", pkColumnValue="GENERATED_VALUE", valueColumnName="GEN_VAL")  
```
and the specifiec table `ID_GEN_TABLE` with appropriate columns is created in the database

Some annotations for fields:
```Java
@Column(name="FIRST_NAME", nullable=false, unique=true, length=20 /* for String */, precision=19, scale=2 /* for BigInt... */),
@Enumerated(EnumType.ORDINAL) enum…, @Enumerated(EnumType.STRING) enum…
@Lob String dataChunck;  
@Lob @Basic(fetch = FetchType.Lazy) private byte[] picture;
@Transient
```
Mandatory for the `java.util.Date` or `java.util.Calendar` fields, but not for types from the java.sql package and not for temporal types from Java 8:
```Java
@Temporal(TemporalType.TIMESTAMP|DATE|TIME)
```
```Java
@CollectionTable(  
	name = "movie_genres",  
    joinColumns = @JoinColumn(name = "movie_title", 
    referencedColumnName = "title"))  // name in the table corresponding to the owning ("current") entity
@ElementCollection  
private List<String> genres = new ArrayList<>();  
@Inheritance(strategy = InheritanceType.SINGLE_TABLE|JOINED|TABLE_PER_CLASS)
```
For example in a DAO object:  
```Java
@PersistenceContext(unitName = "prod") // param needed if there are many databases and  
                                           // persistence-units defined in persistence.xml  
private EntityManager entityManager;  
@Resource private UserTransaction userTransaction;  
.…  
userTransaction.begin();  
entityManager.persist(customer);  
customer2 = entityManager.find(Customer.class, 42L);  
entityManager.remove(customer2);  
ustomer3 = entityManager.find(Customer.class, 43L);  
customer3.setName("Gerald");  
entityManager.merge(customer3);  
userTransaction.commit();
```

Other way:  
```Java
EntityManagerFactory factory = Persistence.createEntiryManagerFactory("prod");  
EntityManager entityManager = factory.createEntityManager();  
…  
entityManager.getTransaction().begin();  
…  
entityManager.getTransaction().commit();
```

Relationships: annotations have attributes like:
```Java
cascade = CascadeType.ALL
fetch = FetchType.EAGER 

```
Field of the type of a non-entity class can be annotated with `@Embedded` to embed it in the table corresponding to the enity class
Similarly, we can annotate a superclass of entities with `@MappedSuperclass` to add its fields to the tables corresponding to classes that will inherit from this superclass.
One-to-one:  
```Java
@OneToOne // on the non-owning side  
@JoinColumn(name="CUSTOMER_ID)  
private Customer customer;  
.…  
@OneToOne(mappedBy="customer") // on the owning side  
private LoginInfo loginInfo;
```
One-to-many (the "many" side is always the owning one):  
```Java
@ManyToOne // on the owning side  
@JoinColumn(name="CUSTOMER_ID)  
private Customer customer;  
.…  
@OneToMany(mappedBy="customer",  // on the non-owning side  
	fetch=FetchType.EAGER, orphanRemoval=true, cascade=CascadeType.All  
)  
private Set<Order> orders;
```
Many-to-many  
```Java
@ManyToMany  
@JoinTable(name="ORDER_ITEMS",  
	joinColumns = @JoinColumn(name="ORDER_ID", referencedColumnName="ORDER_ID"),  
    inverseJoinColumns = @JoinColumn(name = "ITEM_ID", "referencedColumnName = "ITEM_ID"))  
private Collection<Item> items;  
.…  
@ManyToMany(mappedBy="items")  
private Collection<Order> orders;
```
Composed primary keys:
```Java
public class implementing Serializable with appropriate keys
```
In the entity:  
```Java
@Entity @Table(name="…")  
@IdClass(value=MyPrimaryKey.class)
```
Each field which is part of the key is annotated with `@Id`.
Second way
```Java
// @IdClass is not needed:
public class MovieId { … }
@EmbeddedId  
private MovieId movieId;
```

```Java
@MappedSuperclass  
public abstact class BaseEntity { ... }
```
Embedded objects (similar to embedded ids):
```Java
@Embeddable  
public class MovieId { … }
@Embedded  
private MovieId movieId;
```
Callback methods: `@PrePersist`, `@PreUpdate`, `@PostLoad`, `@PostRemove`. On entity methods - `void` and no parameter. On entity listener methods - `void` and take parameter of `final Object` entity. The listener is registered with entity class using (on the entity class):  
```Java
@EntityListeners({AuditingEntityListener.class})
```
Example of a listener:
```java
public class AuditingEntityListener {
    @PrePersist
    void preCreate(AbstractEntity auditable) {
        Instant now = Instant.now();
        auditable.setCreatedDate(now);
        auditable.setLastModifiedDate(now);
    }

    @PreUpdate
    void preUpdate(AbstractEntity auditable) {
        Instant now = Instant.now();
        auditable.setLastModifiedDate(now);
    }
}
```
Java Persistence Query Language (JPQL) - Read operation (inside a transaction and a` try-catch` block):
Dynamic query:  
```Java
Query query = entityManager.createQuery(  
	"SELECT state.population FROM UsState state WHERE state.usStateName LIKE :name");  
query.setParameter("name", "New%");  
Query query = entityManager.createQuery(  
	"SELECT state.population FROM UsState state WHERE state.usStateName LIKE ?1");  
query.setParameter(1, "New%");  
matchingStatesPopulationStream = query.getResultStream();  
matchingStatesPopulationList = query.getResultList();  
matchingStatePopulation = query.getSingleResult();
```
Named query:  
```Java
@NamedQuery(name = "fetchPopulation", query = "SELECT state.population FROM UsState state WHERE state.usStateName LIKE ?1")  
…  
Query query = entityManager.createNamedQuery("fetchPoulation");
```
Native query:  
```Java
Query query = entityManager.createNativeQuery("SELECT m.title, m.producer 
	FROM Movie m");  
List<Object[]> results = query.getResultList();  
Query query = entityManager.createNativeQuery("SELECT m.title, m.producer 
	FROM Movie m", Movie.class);  
List<Movie> results = query.getResultList();
```
```SQL
AND type(person) = Director  
AND type(person) in (Actor, Director)  
EMPTY, BETWEEN, NOT, ...
SELECT u.userCredentials FROM User u [LEFT ]JOIN[ FETCH] u.userCredentials c WHERE c…
SELECT COUNT(u) FROM USER u WHERE …  
AVG, MIN, MAX, SUM
```
Criteria API (all operations inside transaction and `try-catch` block):
Read operation:  
```Java
CriteriaBuilder criteriaBuilder = entityManager.getCriteriaBuilder();  
CriteriaQuery<UsState> criteriaQuery = 
	criteriaBuilder.createQuery(UsState.class);  
Root<UsState> root = criteriaQuery.from(UsState.class);  
EntityType<UsState> usStateEntityType = entityManager.getMetaModel()  
    .entity(UsState.class);  
SingularAttribute<UsState, String> usStateAttribute = usStateEntityType  
    .getDeclatedSingularAttribute("usStateName", String.class);  
Path<String> path = root.get(usStateAttribute);  
Predicate predicate = criteriaBuilder.like(path, "New%");  
criteriaQuery = criteriaQuery.where(predicate);  
TypedQuery typedQuery = entityManager.createQuery(criteriaQuery);  
matchingStatesStream = typedQuery.getResultsStream();
```
Update operation:  
```Java
CriteriaBuilder criteriaBuilder = entityManager.getCriteriaBuilder();  
CriteriaUpdate<Address> criteriaUpdate =  
	criteriaBuilder.createCriteriaUpdate(Address.class);  
Root<Address> root = criteriaUpdate.from(Address.class);  
	citeriaUpdate.set("city", "New York");  
	criteriaUpdate.where(criteriaBuilder.equal(root.get("city"), "York"));  
Query query = entityManager.createQuery(criteriaUpdate);  
int updatedRows = query.executeUpdate();
```
Delete operation:  
```Java
CriteriaBuilder criteriaBuilder = entityManager.getCriteriaBuilder();  
CriteriaDelete<Address> criteriaDelete =  
    criteriaBuilder.createCriteriaDelete(Address.class);  
Root<Address> root = criteraDelete.from(Address.class);  
criteriaUpdate.where(criteriaBuilder.or(  
    criteriaBuilder.equal(root.get("city"), "York"),  
    criteriaBuilder.equal(root.get("city"), " New York")));  
Query query = entityManager.createQuery(criteriaDelete);  
int deletedRows = query.executeUpdate();
```