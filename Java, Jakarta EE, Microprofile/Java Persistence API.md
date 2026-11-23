Everything here is standard JPA and works the same in Jakarta EE, Quarkus and Spring. Repository layers on top of it:
- Quarkus: Panache, either active record or repository ([Quarkus](Quarkus%20and%20MicroProfile.md#data-access))
- Spring: Spring Data JPA ([Spring Data JPA](../Spring%20and%20Spring%20Boot/Spring%20Data%20JPA.md))

Validation on persist: see [Bean Validation](Bean%20Validation.md).

## Entities and ids
```java
@Entity
@Table(name = "DRAGONS")
@SequenceGenerator(name = "DRAGON_SEQ", sequenceName = "DRAGON_SEQ", initialValue = 1, allocationSize = 50)
public class Dragon {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "DRAGON_SEQ")
    private Long id;
    ...
}
```
**Id generation strategies:** `AUTO` (the provider chooses), `IDENTITY` (an auto-increment column), `SEQUENCE` (needs a `@SequenceGenerator` and the sequence in the DB), `TABLE` (needs a `@TableGenerator` and the table in the DB):
```java
@GeneratedValue(strategy = GenerationType.TABLE, generator = "ID_GEN")
@TableGenerator(name = "ID_GEN", table = "ID_GEN_TABLE",
    pkColumnName = "GENERATOR_NAME", pkColumnValue = "HOARD_ID",   // the row for this generator
    valueColumnName = "GEN_VAL")
```
The generator annotations can go on the class or on the id field.

### Composite primary keys
The key class must be `Serializable` and implement `equals`/`hashCode`. There are two ways:
```java
// 1. @IdClass: the key fields are repeated in the entity, each with @Id
@Entity @IdClass(TreasureId.class)
public class Treasure {
    @Id private Long hoardNumber;
    @Id private Integer itemNo;
}

// 2. @EmbeddedId: the key class is @Embeddable
@Embeddable public class TreasureId { private Long hoardNumber; private Integer itemNo; }
@Entity public class Treasure { @EmbeddedId private TreasureId id; }
```

## Field mapping
```java
@Column(name = "DRAGON_NAME", nullable = false, unique = true, length = 40)   // length: for String
@Column(precision = 19, scale = 2) BigDecimal goldCoins;                      // precision/scale: for BigDecimal

@Enumerated(EnumType.STRING) TreasureType type;   // ORDINAL (the default) breaks when you reorder the constants

@Lob String biography;
@Lob @Basic(fetch = FetchType.LAZY) byte[] portrait;

@Transient int cachedFireTemperature;             // not persisted

@Temporal(TemporalType.TIMESTAMP) java.util.Date lastRaid;   // DATE | TIME | TIMESTAMP
```
`@Temporal` is **required** for `java.util.Date` and `Calendar`. Don't use it for `java.sql.*` or `java.time.*` types.

**Collections of basic values:**
```java
@ElementCollection
@CollectionTable(name = "DRAGON_NICKNAMES",
    joinColumns = @JoinColumn(name = "DRAGON_NAME", referencedColumnName = "DRAGON_NAME"))  // column of the owning entity
private List<String> nicknames = new ArrayList<>();
```

## Embedding and inheritance
```java
@Embeddable public class CaveAddress { String kingdom; String mountain; }
@Entity public class Dragon { @Embedded CaveAddress cave; }    // columns go into the DRAGONS table

@MappedSuperclass                                              // not an entity; its fields are copied into each subclass's table
public abstract class BaseEntity { @Id @GeneratedValue Long id; Instant createdDate; }

@Entity
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)          // or JOINED, TABLE_PER_CLASS; goes on the root entity
public abstract class Treasure { ... }
@Entity public class Gem extends Treasure { ... }
```

## Relationships
**The owning side is the one with the foreign key** (`@JoinColumn`). The inverse side uses `mappedBy`. Only changes on the owning side are written to the DB.

```java
// One-to-one
@Entity class VaultKey {
    @OneToOne
    @JoinColumn(name = "DRAGON_ID")              // owning side
    private Dragon dragon;
}
@Entity class Dragon {
    @OneToOne(mappedBy = "dragon")               // inverse side
    private VaultKey vaultKey;
}

// One-to-many: the "many" side is always the owning side
@Entity class Hoard {
    @ManyToOne
    @JoinColumn(name = "DRAGON_ID")
    private Dragon dragon;
}
@Entity class Dragon {
    @OneToMany(mappedBy = "dragon", fetch = FetchType.LAZY, cascade = CascadeType.ALL, orphanRemoval = true)
    private Set<Hoard> hoards;
}

// Many-to-many: either side can own it; the owner defines the join table
@Entity class Hoard {
    @ManyToMany
    @JoinTable(name = "HOARD_TREASURES",
        joinColumns        = @JoinColumn(name = "HOARD_ID",    referencedColumnName = "ID"),
        inverseJoinColumns = @JoinColumn(name = "TREASURE_ID", referencedColumnName = "ID"))
    private Collection<Treasure> treasures;
}
@Entity class Treasure {
    @ManyToMany(mappedBy = "treasures")
    private Collection<Hoard> hoards;
}
```
Default fetch types: `*ToOne` is `EAGER`, `*ToMany` is `LAZY`.

## Lifecycle callbacks and listeners
Callbacks: `@PrePersist`, `@PostPersist`, `@PreUpdate`, `@PostUpdate`, `@PreRemove`, `@PostRemove`, `@PostLoad`.
- A callback on the entity itself: `void` with no parameters.
- A callback in a listener class: `void`, taking the entity as a parameter.
```java
@Entity
@EntityListeners(AuditingEntityListener.class)
public class Hoard extends BaseEntity { ... }

public class AuditingEntityListener {
    @PrePersist
    void preCreate(BaseEntity entity) { entity.setCreatedDate(Instant.now()); entity.setLastModifiedDate(Instant.now()); }
    @PreUpdate
    void preUpdate(BaseEntity entity) { entity.setLastModifiedDate(Instant.now()); }
}
```

## EntityManager
```java
@PersistenceContext(unitName = "dragonbank")   // unitName is needed only with several persistence units in persistence.xml
EntityManager em;
@Resource UserTransaction tx;                  // or use @Transactional / an EJB

tx.begin();
em.persist(dragon);
Dragon ignatius = em.find(Dragon.class, 42L);
ignatius.setWingspan(31);                      // managed entity: the change is flushed automatically, no merge needed
em.remove(em.find(Dragon.class, 43L));
Dragon managed = em.merge(detachedDragon);     // merge is for DETACHED entities; it returns the managed copy
tx.commit();
```
Outside a container (Java SE):
```java
EntityManagerFactory emf = Persistence.createEntityManagerFactory("dragonbank");
EntityManager em = emf.createEntityManager();
em.getTransaction().begin();
// ...
em.getTransaction().commit();
```

## JPQL
```java
TypedQuery<BigDecimal> q = em.createQuery(
    "SELECT h.goldCoins FROM Hoard h WHERE h.dragon.name LIKE :name", BigDecimal.class);
q.setParameter("name", "Ign%");                // positional variant: "... LIKE ?1" with setParameter(1, "Ign%")
q.getResultList();
q.getResultStream();
q.getSingleResult();                           // throws NoResultException or NonUniqueResultException

@NamedQuery(name = "Hoard.byDragon", query = "SELECT h FROM Hoard h WHERE h.dragon.name = ?1")   // on the entity
em.createNamedQuery("Hoard.byDragon", Hoard.class).setParameter(1, "Ignatius");

// Native SQL
List<Object[]> rows   = em.createNativeQuery("SELECT d.name, d.wingspan FROM DRAGONS d").getResultList();
List<Dragon> dragons  = em.createNativeQuery("SELECT * FROM DRAGONS", Dragon.class).getResultList();
```
JPQL snippets:
```sql
SELECT t FROM Treasure t WHERE TYPE(t) = Gem
SELECT t FROM Treasure t WHERE TYPE(t) IN (Gem, Artifact)
SELECT d FROM Dragon d LEFT JOIN FETCH d.hoards h WHERE h.goldCoins > 1000   -- FETCH loads the association too (avoids N+1)
SELECT COUNT(d) FROM Dragon d WHERE d.hoards IS EMPTY
-- also: BETWEEN, NOT, MEMBER OF, AVG, MIN, MAX, SUM, GROUP BY, HAVING
```

## Criteria API
```java
CriteriaBuilder cb = em.getCriteriaBuilder();

// SELECT
CriteriaQuery<Dragon> cq = cb.createQuery(Dragon.class);
Root<Dragon> root = cq.from(Dragon.class);
cq.where(cb.like(root.get("name"), "Ign%"));          // type-safe: root.get(Dragon_.name), using the generated static metamodel
List<Dragon> result = em.createQuery(cq).getResultList();

// UPDATE
CriteriaUpdate<Dragon> cu = cb.createCriteriaUpdate(Dragon.class);
Root<Dragon> u = cu.from(Dragon.class);
Path<String> kingdom = u.get("cave").get("kingdom");      // set(String, ...) only accepts a direct attribute name
cu.set(kingdom, "New Eriador").where(cb.equal(kingdom, "Eriador"));
int updated = em.createQuery(cu).executeUpdate();

// DELETE
CriteriaDelete<Hoard> cd = cb.createCriteriaDelete(Hoard.class);
Root<Hoard> d = cd.from(Hoard.class);
cd.where(cb.or(cb.equal(d.get("goldCoins"), BigDecimal.ZERO), cb.isNull(d.get("dragon"))));
int deleted = em.createQuery(cd).executeUpdate();
```
The metamodel can also be queried at runtime: `em.getMetamodel().entity(Dragon.class).getDeclaredSingularAttribute("name", String.class)`.
