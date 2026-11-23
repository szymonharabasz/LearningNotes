EJBs are also CDI beans. Interceptors (`@Interceptors`, `@AroundInvoke`, `@AroundTimeout`, ...) are covered in [CDI](Context%20and%20Dependency%20Injection.md). Message-driven beans are in [JMS](Java%20Message%20Service.md). `@RolesAllowed` is in [Security](Security.md).

## Bean types and lifecycle
```java
@Stateless                        // pooled; no client state
@Stateful                         // one instance per client
@Singleton                        // one instance per application
@MessageDriven(...)               // consumes JMS messages

@Startup                          // (@Singleton) create at deployment, not on first use
@DependsOn("VaultKeyring")        // (@Singleton) initialization order

@PostConstruct @PreDestroy
@PrePassivate @PostActivate       // @Stateful only: before/after the bean is swapped out to disk
```

## Views (local, remote, no-interface)
```java
@Remote
public interface VaultSession { ... }
@Stateless
public class VaultSessionBean implements VaultSession { ... }

// or declare it on the bean:
@Stateless
@Remote(VaultSession.class)                // or @Local(...)
public class VaultSessionBean implements VaultSession { ... }
```
A bean with no `@Local`/`@Remote` and no interfaces gets a **no-interface view** automatically. If it does implement interfaces, add `@LocalBean` to get the no-interface view as well.

Injection into a client: `@EJB VaultSession vault;` (or `@Inject`). Fields must not be `static`; the only exception is the main class of an application client.

**Looking up a remote EJB from a standalone client.** The client must have the compiled remote interface on its classpath. The properties are server-specific; these are for GlassFish:
```java
Properties props = new Properties();
props.setProperty("java.naming.factory.initial", "com.sun.enterprise.naming.SerialInitContextFactory");
props.setProperty("java.naming.factory.url.pkgs", "com.sun.enterprise.naming");
props.setProperty("java.naming.factory.state", "com.sun.corba.ee.impl.presentation.rmi.JNDIStateFactoryImpl");
props.setProperty("org.omg.CORBA.ORBInitialHost", "192.168.1.100");
props.setProperty("org.omg.CORBA.ORBInitialPort", "3700");

InitialContext ic = new InitialContext(props);
NamingEnumeration<NameClassPair> names = ic.list("");    // see what is bound
while (names.hasMore()) System.out.println(names.next().getName());
VaultSession vault = (VaultSession) ic.lookup("com.dragonbank.VaultSession");
```

## Asynchronous methods
```java
@Asynchronous                              // jakarta.ejb.Asynchronous; MicroProfile has its own, see Quarkus notes
public Future<BigDecimal> countAllGold() {
    BigDecimal sum = ...;                  // slow: goblins count by hand
    return new AsyncResult<>(sum);
}
```
The method can also return `void` (fire and forget). `Future` methods: `get()`, `get(timeout, unit)`, `cancel(mayInterruptIfRunning)`, `isCancelled()`, `isDone()`.

## Concurrency in `@Singleton`
Container-managed concurrency is the default. The default lock is **`WRITE`**, which means all methods are serialized:
```java
@Singleton
@ConcurrencyManagement(ConcurrencyManagementType.CONTAINER)   // or BEAN: you synchronize yourself
public class GoldPriceCache {
    @Lock(LockType.READ)
    @AccessTimeout(value = 30, unit = TimeUnit.SECONDS)
    public BigDecimal getPrice() { ... }

    @Lock(LockType.WRITE)
    public void setPrice(BigDecimal price) { ... }
}
```

## Transactions
**Container-managed** (the default, `@TransactionManagement(TransactionManagementType.CONTAINER)`). Every business method runs in a transaction (`REQUIRED`) unless you change it:
```java
@TransactionAttribute(TransactionAttributeType.REQUIRES_NEW)
// MANDATORY, NEVER, NOT_SUPPORTED, REQUIRED, REQUIRES_NEW, SUPPORTS

@Resource EJBContext ctx;               // or SessionContext
ctx.setRollbackOnly();
```
**Bean-managed:**
```java
@Stateless
@TransactionManagement(TransactionManagementType.BEAN)
public class HoardDaoBean {
    @Resource UserTransaction tx;

    public void transfer(...) throws Exception {
        tx.begin();
        // ...
        tx.commit();
    }
}
```
**Exceptions and rollback:**
- *System exceptions* (unchecked, not annotated) roll the transaction back, are wrapped in `EJBException`, and the server logs them.
- *Application exceptions* (checked exceptions, or anything annotated `@ApplicationException`) reach the client unwrapped and **don't** roll back, unless you use `@ApplicationException(rollback = true)`.

Annotating your runtime exceptions with `@ApplicationException` also stops them from being wrapped before a JAX-RS `ExceptionMapper` sees them; see [Web services](Web%20services%20-%20JAX-RS%20and%20JAX-WS.md).

The CDI equivalent of all this is `@Transactional`; see [CDI](Context%20and%20Dependency%20Injection.md).

## Timers
**Programmatic:**
```java
@Resource TimerService timerService;

Timer timer = timerService.createIntervalTimer(new Date(), 5000, new TimerConfig("gold-count", false));

@Timeout
public void onTimer(Timer timer) {
    if ("gold-count".equals(timer.getInfo()) && vaultEmpty()) timer.cancel();
}
```
**Calendar-based:**
```java
@Schedule(hour = "3", minute = "0")                 // nightly gold count
public void countGold() { ... }

@Schedules({ @Schedule(dayOfWeek = "Mon"), @Schedule(dayOfMonth = "Last") })
public void sendStatements() { ... }
```
**Defaults:** `second = "0"`, `minute = "0"`, `hour = "0"`, and `*` for the day and month fields. So `@Schedule(minute = "*/5")` fires only between 00:00 and 00:59; you also need `hour = "*"`. Timers are `persistent = true` by default, so they survive restarts.

| Attribute | Example values |
|---|---|
| `second`, `minute`, `hour` | `"14"`, `"*/10"` (every 10), `"25/10"` (from 25, every 10) |
| `dayOfMonth` | `"3"`, `"Last"`, `"-2"`, `"1st Tue"` |
| `dayOfWeek` | `"3"`, `"Tue"`, `"Mon-Fri"` |
| `month` | `"3"`, `"March"`, `"Feb"`, `"1-10"` |
| `year` | `"2019"` |
| `timezone` | `"America/New_York"` |
