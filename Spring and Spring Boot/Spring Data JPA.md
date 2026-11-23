Spring Data JPA is a repository layer on top of **Jakarta Persistence (JPA)**. Entity mapping (`@Entity`, `@Id`, relationships, inheritance, callbacks), JPQL, the Criteria API and `EntityManager` are standard JPA. They work the same in Spring and are described in [Java Persistence API](../Java,%20Jakarta%20EE,%20Microprofile/Java%20Persistence%20API.md). This file covers only what Spring adds.

Dependency: `spring-boot-starter-data-jpa` (it brings Hibernate). Data access exceptions are translated to `DataAccessException`; see [JDBC in Spring](JDBC%20in%20Spring.md).

## Repositories
You write **only an interface**; Spring generates the implementation at runtime:
```java
public interface HoardRepository extends JpaRepository<Hoard, Long> {      // or CrudRepository, ListCrudRepository, PagingAndSortingRepository
    List<Hoard> findByDragonName(String dragonName);                       // derived query: from the method name
    Optional<Hoard> findByHoardNumber(Long hoardNumber);
    long countByDragonName(String dragonName);
    List<Hoard> findByGoldCoinsGreaterThanOrderByGoldCoinsDesc(BigDecimal min);
    Page<Hoard> findByDragonCaveKingdom(String kingdom, Pageable pageable); // property path dragon.cave.kingdom

    @Query("SELECT h FROM Hoard h WHERE h.goldCoins = 0")                  // explicit JPQL
    List<Hoard> findEmptyHoards();
}
```
Since Spring Data 3, `PagingAndSortingRepository` no longer extends `CrudRepository`. Extend both, or use `JpaRepository`.

> **Compare:**
> - **Panache repository (Quarkus):** `PanacheRepository<Hoard>` is a **class**. You implement the finders yourself with short query strings such as `find("dragonName", name)`. There are no derived queries from method names. See [Quarkus](../Java,%20Jakarta%20EE,%20Microprofile/Quarkus%20and%20MicroProfile.md#data-access). Panache also offers the active-record style (`Hoard.find(...)`), which Spring Data doesn't have.
> - **Jakarta Data** (Jakarta EE 11) standardizes the Spring Data idea: `@Repository` interfaces extending `CrudRepository`, query derivation from method names, `@Find`/`@Query`.
> - Quarkus also has `quarkus-spring-data-jpa`, which accepts Spring Data repository interfaces and implements them with Panache.

## Useful properties
```properties
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
spring.jpa.hibernate.ddl-auto=update     # none, validate, update, create, create-drop (default for embedded DBs)
spring.jpa.generate-ddl=true
```
Quarkus equivalents: `quarkus.hibernate-orm.log.sql`, `quarkus.hibernate-orm.database.generation`.

Testing the repository layer: `@DataJpaTest`, see [Testing Spring applications](Testing%20Spring%20applications.md). Exposing repositories as REST resources: Spring Data REST, see [REST with Spring Boot](REST%20with%20Spring%20Boot.md#spring-data-rest).
