> **Compare:** Spring accepts the standard **`jakarta.transaction.Transactional`** (JTA), which is described in [CDI](../Java,%20Jakarta%20EE,%20Microprofile/Context%20and%20Dependency%20Injection.md#transactions-jta). It also has its own `org.springframework.transaction.annotation.Transactional` with more options (`readOnly`, `timeout`, `isolation`, `NESTED` propagation, `transactionManager`). The rollback rules are the same as in JTA and EJB: **unchecked exceptions roll back, checked exceptions don't**. EJB transactions are in [EJB](../Java,%20Jakarta%20EE,%20Microprofile/Enterprise%20JavaBeans.md#transactions).

## Setup
Spring Boot auto-configures a transaction manager for the data access technology you use. Without Boot:
```java
@Configuration
@EnableTransactionManagement
public class TxConfig {
    @Bean
    PlatformTransactionManager transactionManager(DataSource dataSource) {
        return new DataSourceTransactionManager(dataSource);
        // others: JpaTransactionManager, JmsTransactionManager, JtaTransactionManager (XA, server-managed)
    }
}
```
A Jakarta EE server always uses JTA. Spring uses a local (resource) transaction unless you configure `JtaTransactionManager`.

## `@Transactional`
```java
@Transactional(propagation = Propagation.REQUIRED,
               rollbackFor = AppraisalDisputedException.class,               // also roll back on this checked exception
               noRollbackFor = { GoblinTypoException.class },
               timeout = 30, readOnly = false)
public void appraiseHoard(long hoardNumber) { ... }
```
- It can go on a class (applies to all public methods) or on a method. Method-level settings override class-level ones. Since Spring 5 it also works on interfaces.
- **Propagation:** `REQUIRED` (default; join the current transaction or start a new one), `REQUIRES_NEW` (suspend the current one and start a new one), `MANDATORY`, `SUPPORTS`, `NOT_SUPPORTED`, `NEVER`, and Spring-only **`NESTED`** (a savepoint inside the current transaction).
- **Proxy pitfall:** the transaction is applied by an AOP proxy (see [Spring AOP](Spring%20AOP.md)). When a `@Transactional` method calls another method **of the same class**, the call doesn't go through the proxy, so the inner method's settings (for example `REQUIRES_NEW`) are **ignored**, and it simply runs in the outer transaction.

## Programmatic access
```java
Connection con = DataSourceUtils.getConnection(dataSource);   // the connection bound to the current transaction

TransactionStatus status = transactionManager.getTransaction(new DefaultTransactionDefinition());
try {
    // ...
    transactionManager.commit(status);
} catch (RuntimeException e) {
    transactionManager.rollback(status);
    throw e;
}
// more convenient: transactionTemplate.execute(status -> { ... })
```
Compare: the JTA `UserTransaction` (`begin`/`commit`), or `QuarkusTransaction.requiringNew().run(...)` in Quarkus.

## Transactions in tests
A test method (or class) annotated with `@Transactional` runs in a transaction that is **rolled back after the test**. Use `@Commit` (or `@Rollback(false)`) to keep the changes.

This only works when the code under test runs in the test's thread. With `@SpringBootTest(webEnvironment = RANDOM_PORT)`, the HTTP request is handled in a server thread with its own transaction, so nothing is rolled back.

Quarkus equivalent: `@TestTransaction`.
