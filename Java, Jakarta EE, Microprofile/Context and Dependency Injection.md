## Bean discovery
- `beans.xml` with `bean-discovery-mode="all"` turns every class into a CDI bean. The default, `annotated`, only picks up classes with a bean-defining annotation, such as a scope or a stereotype.
- EJB `@Stateless`, `@Stateful` and `@Singleton` beans are also CDI beans.
- Quarkus uses build-time CDI (ArC). It only discovers beans in its own module unless told otherwise; see `quarkus.index-dependency` in [Quarkus](Quarkus%20and%20MicroProfile.md).

## Injection and producers
- `@Inject` can go on a field, a constructor, or a method. An injected method is called an *initializer method*.
- `@Named` gives a bean an EL name, so it can be used in JSF pages as `#{hoardController}`. `@Named` is itself a qualifier.
- You need a `@Produces` method (or field) to inject things that aren't beans: enums, JDK classes, objects from third-party libraries, or objects built from config.
```java
@Produces @ApplicationScoped
Clock vaultClock() { return Clock.systemUTC(); }
```
- Lifecycle callbacks: `@PostConstruct`, `@PreDestroy`.
- Creating a bean eagerly at startup: CDI beans are created lazily, when first used. For eager creation use EJB `@Singleton @Startup`, an observer `void init(@Observes @Initialized(ApplicationScoped.class) Object o)`, or `@Startup` in Quarkus.

## Scopes
| Scope | Lifetime |
|---|---|
| `@RequestScoped` | one HTTP request |
| `@SessionScoped` | HTTP session (the bean must be `Serializable`) |
| `@ApplicationScoped` | whole application; clients get a proxy |
| `@ConversationScoped` | between `conversation.begin()` and `conversation.end()`; used with JSF |
| `@Dependent` | default; a **new instance for every injection point**, which lives as long as its owner |
| `@FlowScoped("name")` | JSF Faces Flow, see [JSF](Java%20Server%20Faces%202.3.md) |

Conversation:
```java
@Inject Conversation conversation;     // jakarta.enterprise.context.Conversation
conversation.begin();                  // or begin("hoard-opening-42")
conversation.getId();
conversation.end();
```

## Qualifiers
A qualifier tells CDI which of several implementations to inject:
```java
@Qualifier
@Retention(RUNTIME)
@Target({METHOD, FIELD, PARAMETER, TYPE})
public @interface DragonClass {
    Age value();                       // members take part in resolution...
    @Nonbinding String comment() default "";   // ...unless they are @Nonbinding
}

@DragonClass(Age.ELDER)
public class ElderDragonAccount implements Account { ... }

@Inject @DragonClass(Age.ELDER)
Account account;
```
- Built-in qualifiers: `@Default`, `@Any`, `@Named`.
- `@RestClient` (MicroProfile) injects the generated implementation of a `@RegisterRestClient` interface; see [Quarkus](Quarkus%20and%20MicroProfile.md).
- With `Instance<Account>` plus `select(...)` you can choose a bean at runtime; see [Events](#events) for `AnnotationLiteral`.

## Alternatives
You mark several implementations of the same interface with `@Alternative` and select one of them in `beans.xml`, or by putting `@Priority` on the chosen one:
```xml
<beans>
    <alternatives>
        <class>com.dragonbank.vault.FireproofVault</class>
    </alternatives>
</beans>
```

## Stereotypes
A stereotype is an annotation that bundles other annotations (a scope, interceptor bindings, `@Named`, `@Alternative`):
```java
@Stereotype
@RequestScoped
@Named
@Audited
@Retention(RUNTIME) @Target(TYPE)
public @interface GoblinController { }
```
A stereotype cannot declare qualifiers, except `@Named` with no value.

## Interceptors
An interceptor runs code before or after the methods of a bean, and can change their arguments or results.

**1. Define an interceptor binding:**
```java
@InterceptorBinding
@Retention(RUNTIME)
@Target({METHOD, TYPE})
public @interface GoblinProof {
    @Nonbinding SecurityLevel value() default SecurityLevel.HIGH;   // @Nonbinding: the value doesn't affect which interceptor is chosen
}
```
**2. Write the interceptor:**
```java
@GoblinProof @Interceptor
@Priority(Interceptor.Priority.APPLICATION)      // enables it; the alternative is <interceptors> in beans.xml
public class GoblinProofInterceptor {
    @AroundInvoke
    public Object check(InvocationContext ctx) throws Exception {
        log.info(ctx.getMethod().getDeclaringClass() + "." + ctx.getMethod().getName()
            + Arrays.toString(ctx.getParameters()));
        return ctx.proceed();
    }
}
```
**3. Apply it to a class or a method:**
```java
@GoblinProof public class VaultService { ... }
@GoblinProof(SecurityLevel.PARANOID) public void openVault() { ... }
```
**The older way, without a binding:** `@Interceptors(GoblinProofInterceptor.class)` on a class or method (from the Interceptors spec, used with EJBs). This **needs no activation** in `beans.xml`, but it couples the bean to the interceptor class.

- Other interceptor methods: `@AroundConstruct`, `@AroundTimeout` (EJB timers), `@PostConstruct`, `@PreDestroy`. In an interceptor class, the lifecycle methods take an `InvocationContext`.
- `InvocationContext` methods: `getTarget()`, `getMethod()`, `getParameters()`, `setParameters(Object[])`, `getContextData()` (a map shared along the interceptor chain), `proceed()`.
- EJB only: `@ExcludeDefaultInterceptors` (default interceptors are configured in `ejb-jar.xml`) and `@ExcludeClassInterceptors`.

## Decorators
An interceptor is generic. A decorator implements a business interface and wraps one particular bean:
```java
@Decorator
@Priority(Interceptor.Priority.APPLICATION)    // or enable it in beans.xml <decorators>; this also sets the order
public abstract class GoblinCommissionDecorator implements Treasure {
    @Inject @Delegate
    Treasure treasure;

    @Override
    public BigDecimal value() {
        return treasure.value().multiply(new BigDecimal("0.9"));   // the goblins keep 10%
    }
}
```

## Events
```java
@Inject Event<KnightSighted> sightings;
sightings.fire(new KnightSighted("Sir Reginald"));        // synchronous
sightings.fireAsync(new KnightSighted("Sir Reginald"));   // returns CompletionStage; only @ObservesAsync observers get it

public void onSighting(@Observes KnightSighted event, EventMetadata meta) { ... }
public void onSightingAsync(@ObservesAsync KnightSighted event) { ... }
public void hideGoldFirst(@Observes @Priority(Interceptor.Priority.APPLICATION) KnightSighted event) { ... }   // ordering

// Transactional observers and conditional observers
public void afterCommit(@Observes(during = TransactionPhase.AFTER_SUCCESS,   // IN_PROGRESS (default), BEFORE_COMPLETION,
                                  notifyObserver = Reception.IF_EXISTS)       // AFTER_COMPLETION, AFTER_FAILURE
                        HoardDeposited event) { ... }                         // IF_EXISTS: don't create the bean just for the event
```
**Picking observers by qualifier at runtime.** Fire one `Event` and select a qualifier instance; only observers with that qualifier are notified. Create the qualifier instance by extending `AnnotationLiteral`:
```java
public class AlarmChannelLiteral extends AnnotationLiteral<AlarmChannel> implements AlarmChannel {
    private final Channel value;
    public AlarmChannelLiteral(Channel value) { this.value = value; }
    @Override public Channel value() { return value; }
}

alarms.select(new AlarmChannelLiteral(kingdom == NORTH ? Channel.RAVEN : Channel.SMOKE_SIGNAL))
      .fireAsync(alarm);

void viaRaven(@ObservesAsync @AlarmChannel(Channel.RAVEN) Alarm alarm) { ... }
```

## Transactions (JTA)
```java
@Transactional(value = TxType.REQUIRED,             // MANDATORY, NEVER, SUPPORTS, NOT_SUPPORTED, REQUIRED (default), REQUIRES_NEW
               rollbackOn = VaultBreachedException.class,
               dontRollbackOn = MinorGoblinMistake.class)
public void depositGold(...) { ... }
```
By default only **unchecked** exceptions roll back. EJBs use their own annotations for this; see [EJB](Enterprise%20JavaBeans.md).

## Managed concurrency (Jakarta Concurrency)
These run tasks on threads managed by the application server, so the CDI context, security and JNDI are available inside them:
- `ManagedExecutorService`: like `ExecutorService`
- `ManagedScheduledExecutorService`: run at a given time or at a fixed rate
```java
@Resource ManagedExecutorService executor;
```

## Looking up beans programmatically
The simple way:
```java
@Inject Instance<Repository<Hoard>> repositories;
Repository<Hoard> repo = repositories.get();

CDI.current().select(new TypeLiteral<Repository<Hoard>>() {}).get();   // from code that isn't a bean
```
The low-level way, with `BeanManager`, for a type known only at runtime:
```java
@Inject BeanManager manager;

<T> Repository<T> locate(Class<T> entityType) {
    ParameterizedType type = new ParameterizedType() {
        @Override public Type getRawType() { return Repository.class; }
        @Override public Type getOwnerType() { return null; }
        @Override public Type[] getActualTypeArguments() { return new Type[] { entityType }; }
    };
    Bean<?> bean = manager.resolve(manager.getBeans(type));
    CreationalContext<?> cc = manager.createCreationalContext(bean);
    @SuppressWarnings("unchecked")
    Repository<T> repo = (Repository<T>) manager.getReference(bean, type, cc);
    return repo;
}
```
