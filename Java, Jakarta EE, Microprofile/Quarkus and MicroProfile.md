All examples use one domain: **DragonBank**, the only bank where dragons can safely keep their gold hoards. The tellers are goblins, the treasure appraisers are goblins (slow, unreliable, and often on strike), and knights keep showing up to raid the hoards.

Main services: `hoard-service` (this app) and `goblin-appraisal-service` (a remote service that we call). Base package: `com.dragonbank`. The domain is described in the [README](README.md).

Quarkus builds on the Jakarta EE APIs described in the other notes: [CDI](Context%20and%20Dependency%20Injection.md), [JAX-RS](Web%20services%20-%20JAX-RS%20and%20JAX-WS.md), [JPA](Java%20Persistence%20API.md), [Bean Validation](Bean%20Validation.md) and [JSON-B](Serialization%20and%20deserialization%20of%20XML%20and%20JSON.md). This file covers only what Quarkus and MicroProfile add on top.

## Contents
1. [Development workflow](#development-workflow)
2. [Dependencies](#dependencies)
3. [Configuration](#configuration)
4. [Reactive programming with Mutiny](#reactive-programming-with-mutiny)
5. [Data access](#data-access)
6. [REST endpoints (RESTEasy Reactive)](#rest-endpoints-resteasy-reactive)
7. [Calling other services](#calling-other-services)
8. [Reactive messaging](#reactive-messaging)
9. [Fault tolerance](#fault-tolerance)
10. [Observability](#observability)
11. [Security](#security)
12. [Testing](#testing)
13. [Containers and Kubernetes](#containers-and-kubernetes)

---

## Development workflow
```shell
mvn quarkus:dev                                             # dev mode with live reload
mvn package -Pnative -Dquarkus.native.container-build=true  # native executable built in a container, no local GraalVM needed
./mvnw quarkus:add-extension -Dextensions="hibernate-orm-panache"
```
**Dev Services:** in dev and test mode, Quarkus starts Postgres, Kafka, Keycloak, Redis and others in containers automatically when the extension is present and no URL is configured. You don't need to `docker run` them yourself (but see [Running dependencies in Docker](#running-dependencies-in-docker)).

---

## Dependencies
| Artifact | Purpose |
|---|---|
| `org.eclipse.microprofile.config:microprofile-config-api:2.0` | Pure MP Config |
| `org.eclipse.microprofile.jwt:microprofile-jwt-auth-api:1.2` | Pure MP JWT |
| `org.eclipse.microprofile.openapi:microprofile-openapi-api:2.0` | Pure MP OpenAPI |
| `org.eclipse.microprofile.fault.tolerance:microprofile-fault-tolerance-api:3.0` | Pure MP Fault Tolerance |
| `io.quarkus:quarkus-smallrye-fault-tolerance` | Fault tolerance in Quarkus |
| `io.quarkus:quarkus-smallrye-opentracing` | Tracing (older; newer apps use `quarkus-opentelemetry`) |
| `io.quarkus:quarkus-logging-gelf` | Sending logs to Graylog / ELK in GELF format |
| `io.quarkus:quarkus-jacoco` (test) | Code coverage reports |
| `org.testcontainers:junit-jupiter:1.15.3` (test) | Testcontainers + JUnit 5 |
| `org.testcontainers:postgresql:1.15.3` (test) | Postgres container for tests |

Quarkus only discovers beans in its own module. To make it index a dependency that contains CDI beans (for example a shared commons JAR), add:
```properties
quarkus.index-dependency.commons.group-id=com.dragonbank
quarkus.index-dependency.commons.artifact-id=dragonbank-commons
```

---

## Configuration
### Reading values
```properties
# application.properties
dragonbank.greeting=Welcome, mighty dragon!
```
```java
// Injection
@Inject
@ConfigProperty(name = "dragonbank.greeting", defaultValue = "Hello, hatchling")
String greeting;

// Programmatic
Config config = ConfigProvider.getConfig();
String greeting = config.getValue("dragonbank.greeting", String.class);

// Which source did a value come from?
@Inject @ConfigProperty(name = "cave.host") ConfigValue caveHost;
caveHost.getSourceName();
caveHost.getValue();
```

### Sources and their ordinals
The source with the **higher** ordinal wins:

| Source | Ordinal |
|---|---|
| System properties | **400** |
| Environment variables | **300** |
| Kubernetes ConfigMap (client) | **270** |
| `application.yaml` | **254** |
| `application.properties` | **250** |
| `microprofile-config.properties` | **100** (also the default for custom sources) |

### Profiles and expressions
```properties
dragonbank.greeting=Welcome, mighty dragon!
%dev.dragonbank.greeting=Hello, dragon developer!
%prod.dragonbank.greeting=Welcome, mighty dragon! Please wipe your claws.
%hatchery.dragonbank.greeting=Welcome to a custom profile, little one!

# Expressions
support.email=help@dragonbank.example
goblin-support.email=${support.email}
```
You can also use separate files per profile: `microprofile-config-<profile>.properties` in MicroProfile, or `application-<profile>.properties` in Quarkus.

### Grouping properties
**MicroProfile `@ConfigProperties`.** This works with fields or with getters and setters:
```java
@ConfigProperties(prefix = "goblin-support")
public class GoblinSupportConfig {
    private String phone;
    public String email;

    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
}

@Inject
@ConfigProperties     // can override the prefix here: @ConfigProperties(prefix = "...")
GoblinSupportConfig goblinSupport;   // reads goblin-support.phone and goblin-support.email
```
**Quarkus `@ConfigMapping`.** It is interface-based, supports nesting, and can be validated with Bean Validation (requires `quarkus-hibernate-validator`):
```java
@ConfigMapping(prefix = "goblin-support-mapping")
interface GoblinSupportMapping {
    @Size(min = 12, max = 12)
    String phone();
    String email();
    NightShift nightShift();         // goblin-support-mapping.night-shift.phone, ...

    interface NightShift {
        @Size(min = 12, max = 12)
        String phone();
        String email();
    }
}

@Inject GoblinSupportMapping goblinSupport;
goblinSupport.nightShift().email();
```

### Extending MicroProfile Config
**Custom source.** Implement `org.eclipse.microprofile.config.spi.ConfigSource`. You must implement only `getPropertyNames()`, `getValue(String)` and `getName()`. The ordinal is read from the `config_ordinal` property, and defaults to 100.

**Custom converter.** Implement `org.eclipse.microprofile.config.spi.Converter<T>`.

There are two ways to register either one:
- **ServiceLoader file:** `META-INF/services/org.eclipse.microprofile.config.spi.ConfigSource` (or `...spi.Converter`), containing the fully qualified class name.
- **Building the config manually:**
```java
ConfigProviderResolver resolver = ConfigProviderResolver.instance();
Config config = resolver.getBuilder()
    .addDefaultSources()
    .withSources(new DragonCaveConfigSource())
    .withConverters(new GoldCoinConverter())
    .build();
resolver.registerConfig(config, classLoader);
```

### Useful Quarkus properties
```properties
quarkus.http.root-path=/api
quarkus.http.test-port=9999
quarkus.banner.path=banner.txt
```
Other useful properties are listed in the section they belong to.

---

## Reactive programming with Mutiny
There are two types: `Uni<T>` (0 or 1 item) and `Multi<T>` (a stream of items). Both are lazy, so **nothing happens until you subscribe**.
```java
knightSightings.subscribe().with(
    knight  -> System.out.println("Knight spotted: " + knight),
    failure -> System.out.println("Lookout goblin fell asleep: " + failure),
    ()      -> System.out.println("No more knights today"));
```

### Transforming, filtering, collecting
```java
dragons.onItem().transform(dragon -> dragon.name.toLowerCase())
    .select().when(name -> name.startsWith("b"))     // the opposite group is .skip()
    .collect().asList()
    .subscribe().with(names -> System.out.println("Dragons starting with b: " + names));

hoards.getAllHoards()
    .onItem().transformToIterable(hoard -> hoard.treasures)
    .select().distinct();

multi.collect().asMap(hoard -> hoard.hoardNumber);
Uni<Long> count = multi.collect().with(Collectors.counting());

multi.group().intoLists().of(5);                     // Multi<List<T>> in batches of 5
Multi.createBy().merging().streams(goldCoins, gems);
Uni.combine().all().unis(goldUni, gemsUni).asTuple();
Uni.createFrom().nullItem();
```

### Chaining asynchronous actions
```java
uni.onItem().transformToUni(hoard -> appraisalService.appraise(hoard));
uni.onItem().transformToMulti(dragon -> hoardsOf(dragon));

// Multi -> Multi: Concatenate keeps the order, Merge interleaves (faster)
dragons.getAllDragons().onItem().transformToMultiAndConcatenate(dragon -> hoards.getHoardsForDragon(dragon));
dragons.getAllDragons().onItem().transformToMultiAndMerge(dragon -> hoards.getHoardsForDragon(dragon));

Multi.createFrom().ticks().every(Duration.ofSeconds(1)).onOverflow().drop()
    .onItem().transformToUniAndConcatenate(tick -> treasures.getTreasureOfTheDay());
```

### Failures
```java
.onFailure().recoverWithItem(failure -> Hoard.EMPTY)
.onFailure().retry().withBackoff(Duration.ofSeconds(3)).atMost(3)
.ifNoItem().after(Duration.ofSeconds(1)).fail()          // timeout
```

### Back-pressure (a fast producer and a slow consumer)
```java
Multi.createFrom().ticks().every(Duration.ofMillis(20))  // a dragon egg hatches every 20 ms
    .onOverflow().buffer(250)                            // or .drop(egg -> log("egg lost: " + egg))
    .emitOn(Infrastructure.getDefaultExecutor())
    .onItem().transform(Hatchery::canFeedOnlyOneHatchlingPerSecond)
    .select().first(10)
    .subscribe().with(...);
```

### Observing events (side effects only)
```java
multi
    .onSubscription().invoke(sub -> ...)
    .onCancellation().invoke(() -> ...)
    .onItem().invoke(item -> ...)
    .onFailure().invoke(f -> ...)
    .onCompletion().invoke(() -> ...)
    .subscribe().with(...);
```

---

## Data access
### Datasource
```properties
quarkus.datasource.db-kind=postgresql
quarkus.datasource.username=goblin-dba
quarkus.datasource.password=Sh1nyG0ld
quarkus.datasource.jdbc.url=jdbc:postgresql://localhost:5432/dragonbank
# Hibernate Reactive uses: quarkus.datasource.reactive.url=postgresql://localhost:5432/dragonbank

# Named datasource
quarkus.datasource.raids.db-kind=postgresql

quarkus.flyway.migrate-at-start=true
```

### Panache: active record
You annotate the entity with `@Entity`, extend `PanacheEntity` (which provides the `id`) and use **public fields**. Quarkus generates getters and setters at build time and rewrites every field access to call them.
```java
@Entity
public class Hoard extends PanacheEntity {
    public Long hoardNumber;
    public String dragonName;
    public BigDecimal goldCoins;

    public static long countHoardsOf(String dragonName) {
        return count("dragonName", dragonName);
    }
    public static Hoard findByHoardNumber(Long hoardNumber) {
        return find("hoardNumber", hoardNumber).firstResult();
    }
}

Hoard.listAll();
Hoard.streamAll();     // java.util.stream.Stream, needs an active transaction

@POST
@Transactional
public Response depositHoard(Hoard hoard) {
    hoard.persist();
    return Response.status(201).entity(hoard).build();
}
```
**Reactive variant** (`quarkus-hibernate-reactive-panache`). Methods return `Uni`, and transactions are demarcated with `Panache.withTransaction` (or `@WithTransaction`) instead of `@Transactional`:
```java
Hoard.<Hoard>findById(id)
    .onItem().ifNull().failWith(new WebApplicationException("No such hoard (raided?)", Status.NOT_FOUND));

return Panache.withTransaction(hoard::persist);

return Panache.withTransaction(() -> Hoard.<Hoard>findById(id)
    .onItem().ifNotNull().invoke(entity -> entity.goldCoins = updated.goldCoins));

return Panache.withTransaction(() -> Hoard.deleteById(id)
    .map(deleted -> deleted
        ? Response.status(Status.NO_CONTENT).build()
        : Response.status(Status.NOT_FOUND).build()));
```

### Panache: repository
Here you use a plain JPA `@Entity` and put the queries in a repository:
```java
@ApplicationScoped
public class HoardRepository implements PanacheRepository<Hoard> {
    public Hoard findByHoardNumber(Long hoardNumber) {
        return find("hoardNumber = ?1", hoardNumber).firstResult();
    }
}

@Inject HoardRepository hoardRepository;

@POST
@Transactional
public Response depositHoard(Hoard hoard) {
    hoardRepository.persist(hoard);
    return Response.status(201).entity(hoard).build();
}
```

### Redis
```properties
quarkus.redis.hosts=redis://localhost:6379
```
```java
@Inject ReactiveRedisClient redis;   // newer API: ReactiveRedisDataSource

// All dragons, stored as hashes with keys like "dragon:42"
return redis.keys("dragon:*")
    .onItem().transformToMulti(keys -> Multi.createFrom().iterable(keys).map(Response::toString))
    .onItem().transformToUniAndMerge(key -> redis.hgetall(key)
        .map(fields -> toDragon(Long.parseLong(key.substring(DRAGON_HASH_PREFIX.length())), fields)));
```
Other commands: `hmset`, `hdel`.

---

## REST endpoints (RESTEasy Reactive)
In newer Quarkus versions this is called "Quarkus REST".

**Threading:** an endpoint that returns `Uni`/`Multi` runs on the **I/O (event-loop) thread**. An endpoint with a plain return type runs on a **worker thread**. You can override this with `@Blocking` / `@NonBlocking`. Never block on the event loop.

```java
@Inject Vertx vertx;

@GET @Path("/prophecy")
public Uni<Response> prophecy() {
    return vertx.fileSystem().readFile("scrolls/ancient-prophecy.txt")
        .onItem().transform(buffer -> buffer.toString("UTF-8"))
        .onItem().transform(text -> Response.ok(text).build())
        .ifNoItem().after(Duration.ofSeconds(1)).fail()
        .onFailure().recoverWithItem(Response.status(Status.NOT_FOUND).build());
}

// Raw streaming of a huge file
@GET @Path("/lore")
public Multi<String> lore() {
    return vertx.fileSystem().open("dragon-lore-vol-1-to-12.txt", new OpenOptions().setRead(true))
        .onItem().transformToMulti(AsyncFile::toMulti)
        .onItem().transform(buffer -> buffer.toString("UTF-8"));
}

// Exception mapper, declared directly in the resource (or in a global class)
@ServerExceptionMapper
public Response scrollMissing(FileSystemException ex) {
    return Response.status(Status.NOT_FOUND).entity(ex.getMessage()).build();
}
```

### OpenAPI documentation
```properties
quarkus.swagger-ui.always-include=true    # also in prod builds
```
```java
@GET @Path("/largest")
@Operation(
    summary = "Shows the largest hoard.",
    description = "Retrieves the hoard with the most gold coins from the vault.")
@APIResponses({
    @APIResponse(responseCode = "404",
        description = "The vault cannot be found (probably stolen).",
        content = @Content(mediaType = "text/plain")),
    @APIResponse(responseCode = "200",
        description = "The largest hoard has been retrieved successfully.",
        content = @Content(mediaType = "application/json",
            schema = @Schema(implementation = Hoard.class)))})
public Hoard largestHoard() { ... }
```
For the security scheme in Swagger UI, see [Security](#security).

---

## Calling other services
### MicroProfile REST Client (declarative)
You write an interface with JAX-RS annotations plus `@RegisterRestClient`:
```java
@Path("/appraisals")
@RegisterRestClient(configKey = "goblin-appraisal")
@RegisterClientHeaders                                   // propagates incoming headers, see below
@RegisterProvider(AppraisalRequestFilter.class)          // client-side providers
@RegisterProvider(TreasureNotFoundMapper.class)
@ClientHeaderParam(name = "X-Goblin-Union", value = "Local 13")
@Produces(MediaType.APPLICATION_JSON)
public interface GoblinAppraisalService {

    @GET
    @Path("/{treasureId}/value")
    @ClientHeaderParam(name = "X-Bribe", value = "{computeBribe}")  // value computed by a method
    BigDecimal getValue(@PathParam("treasureId") Long treasureId,
                        @HeaderParam("X-Dragon-Name") String dragon);

    @POST
    @Path("/{treasureId}/reappraisal")
    CompletionStage<Void> reappraiseAsync(@PathParam("treasureId") Long treasureId,
                                          BigDecimal claimedValue);  // async: return CompletionStage or Uni

    default String computeBribe() { return "3 gold coins"; }
}

@Inject @RestClient
GoblinAppraisalService appraisalService;
```
```properties
# MicroProfile style: <configKey or FQCN of the interface>/mp-rest/...
goblin-appraisal/mp-rest/url=http://goblin-appraisal:8080/api
goblin-appraisal/mp-rest/scope=jakarta.inject.Singleton
# Quarkus style
quarkus.rest-client.goblin-appraisal.url=http://goblin-appraisal:8080/api

# Headers that @RegisterClientHeaders (default factory) copies from the incoming request
org.eclipse.microprofile.rest.client.propagateHeaders=Authorization,Cookie
```
**Programmatic client.** Use the same interface without `@RegisterRestClient`:
```java
GoblinAppraisalService appraisalService = RestClientBuilder.newBuilder()
    .baseUrl(new URL(appraisalServiceUrl))
    .connectTimeout(500, TimeUnit.MILLISECONDS)
    .readTimeout(1200, TimeUnit.MILLISECONDS)     // goblins are slow
    .build(GoblinAppraisalService.class);
```
**Client-side providers:** `ClientRequestFilter`, `ClientResponseFilter`, `MessageBodyReader`/`Writer`, `ParamConverter`, `ReaderInterceptor`/`WriterInterceptor`, `ResponseExceptionMapper`.
```java
public class AppraisalRequestFilter implements ClientRequestFilter {
    @Override
    public void filter(ClientRequestContext ctx) {
        Method invoked = (Method) ctx.getProperty("org.eclipse.microprofile.rest.client.invokedMethod");
        ctx.getHeaders().add("Invoked-Client-Method", invoked.getName());
    }
}

public class TreasureNotFoundMapper implements ResponseExceptionMapper<TreasureNotFoundException> {
    @Override
    public boolean handles(int status, MultivaluedMap<String, Object> headers) {
        return status == 404;
    }
    @Override
    public TreasureNotFoundException toThrowable(Response response) {
        return new TreasureNotFoundException("The goblins claim they never saw this treasure");
    }
}
```

### Vert.x Web Client (low-level, reactive)
```java
@ApplicationScoped
public class OracleClient {
    private final WebClient client;      // io.vertx.mutiny.ext.web.client.WebClient

    @Inject
    public OracleClient(Vertx vertx) { client = WebClient.create(vertx); }

    @PreDestroy
    void close() { client.close(); }

    public Uni<JsonObject> todaysProphecy() {
        return client.getAbs("https://oracle.example/prophecies/today").send()
            .onItem().transform(response -> response.statusCode() == 200
                ? response.bodyAsJsonObject()
                : new JsonObject().put("error", response.statusMessage()));
    }
}
```

---

## Reactive messaging
### Channel configuration
```properties
mp.messaging.outgoing.hoard-depleted.connector=smallrye-kafka
mp.messaging.outgoing.hoard-depleted.topic=depleted-hoards
mp.messaging.outgoing.hoard-depleted.value.serializer=io.quarkus.kafka.client.serialization.JsonbSerializer
%test.mp.messaging.outgoing.hoard-depleted.value.serializer=org.apache.kafka.common.serialization.StringSerializer

mp.messaging.incoming.knight-sightings.connector=smallrye-kafka
%test.mp.messaging.incoming.knight-sightings.value.deserializer=org.apache.kafka.common.serialization.StringDeserializer
```

### Sending
**With an emitter**, from imperative code:
```java
@Inject @Channel("hoard-depleted")
Emitter<HoardDepleted> emitter;           // send() returns CompletionStage<Void>
// or, in Quarkus:
@Inject @Channel("hoard-depleted")
MutinyEmitter<HoardDepleted> emitter;     // send() returns Uni<Void>

// in withdrawGold(...):
if (hoard.goldCoins.signum() < 0) {
    return emitter.send(new HoardDepleted(hoard.hoardNumber, hoard.dragonName))
        .thenApply(ignored -> hoard);
}
return CompletableFuture.completedFuture(hoard);
```
**With a full `Message`**, which lets you add ack/nack callbacks:
```java
CompletableFuture<Hoard> result = new CompletableFuture<>();
emitter.send(Message.of(
    event,
    () -> {                               // ack
        result.complete(hoard);
        return CompletableFuture.completedFuture(null);
    },
    reason -> {                           // nack
        result.completeExceptionally(reason);
        return CompletableFuture.completedFuture(null);
    }));
return result;
```
**With a producer method**, which the framework calls:
```java
@Outgoing("hoard-depleted")
public Message<HoardDepleted> depletionNotification() {
    return Message.of(event)
        .addMetadata(OutgoingKafkaRecordMetadata.builder().withKey("very-angry-dragon").build());
}
```
**Overflow strategy for an emitter:**
```java
@Inject @Channel("hoard-depleted")
@OnOverflow(value = OnOverflow.Strategy.BUFFER, bufferSize = 100)
MutinyEmitter<HoardDepleted> emitter;
```
Other strategies: `UNBOUNDED_BUFFER`, `DROP`, `LATEST`, `FAIL`, `THROW_EXCEPTION`, `NONE`.

### Receiving
```java
@Incoming("knight-sightings")
@Blocking                                  // offload to a worker thread
public void onSighting(KnightSighting sighting) { ... }

// With a Message parameter you must ack it yourself; this also gives access to Kafka metadata
@Incoming("knight-sightings")
public CompletionStage<Void> onSighting(Message<KnightSighting> msg) {
    String armour = msg.getMetadata(IncomingKafkaRecordMetadata.class).get().getKey().toString();
    // ...
    return msg.ack();
}
```
**Injecting the channel as a stream (Mutiny):**
```java
@Inject @Channel("knight-sightings")
Multi<Message<KnightSighting>> sightings;      // or Multi<KnightSighting> without ack control

void init() {
    sightings.subscribe().with(message -> {
        try {
            // ... sound the alarm
            message.ack();
        } catch (Exception ex) {
            message.nack(ex);
        }
    });
}
```
### Processing (from one channel to another)
```java
@Incoming("knight-sightings")
@Outgoing("dragon-alarms")
@Retry(maxRetries = 10, delay = 1, delayUnit = ChronoUnit.SECONDS)   // fault tolerance works here too
public Message<String> raiseAlarm(Message<KnightSighting> sighting) {
    return sighting.withPayload("Hide the gold! Knight approaching: " + sighting.getPayload().name());
}
```

---

## Fault tolerance
All examples protect calls to the goblins' legacy systems.

```java
@Asynchronous                                          // runs on a separate thread
public CompletionStage<BigDecimal> countGold() {
    BigDecimal sum = goblinLedger.countEveryCoinByHand();
    return CompletableFuture.completedFuture(sum);
}

@Bulkhead(value = 10, waitingTaskQueue = 10)           // max 10 concurrent calls;
public BigDecimal askGoblinLedger() { ... }            // the queue is only used together with @Asynchronous

@Timeout(value = 1000, unit = ChronoUnit.MILLIS)

@Bulkhead
@Fallback(fallbackMethod = "guessGoldByWeight",        // same signature as the original method
    applyOn = BulkheadException.class,
    skipOn  = DragonAteTheTellerException.class)
public Response withdrawGold(Long hoardNumber, BigDecimal amount) { ... }
public Response guessGoldByWeight(Long hoardNumber, BigDecimal amount) { ... }
```
Instead of `fallbackMethod` you can use `value =` with a `FallbackHandler` class.

**`@Retry`** parameters: `retryOn`, `abortOn` (lists of exceptions), `maxRetries`, `delay`/`delayUnit`, `jitter`/`jitterDelayUnit`, `maxDuration`/`durationUnit`.

**`@CircuitBreaker`** parameters: `failOn`, `skipOn`, `requestVolumeThreshold` (size of the rolling window), `failureRatio`, `delay`/`delayUnit` (how long the circuit stays open), `successThreshold` (successful trial calls needed to close it again).

### Overriding annotations in configuration
The key format is `[<fully qualified class>/[<method>/]]<annotation>/<parameter>`:
```properties
com.dragonbank.HoardResource/withdrawGold/Timeout/value=150
com.dragonbank.HoardResource/withdrawGold/Timeout/enabled=false
com.dragonbank.HoardResource/Retry/maxRetries=5     # all methods of the class
Retry/maxRetries=3                                  # globally

# Disable everything except @Fallback, for example when a service mesh (Istio) handles resilience
MP_Fault_Tolerance_NonFallback_Enabled=false
```

---

## Observability
### Health checks
```java
@Liveness                     // or @Readiness, @Startup; Quarkus also has @HealthGroup("custom")
@ApplicationScoped
public class FurnaceLivenessCheck implements HealthCheck {
    @Override
    public HealthCheckResponse call() {
        return HealthCheckResponse.named("dragon-furnace")
            .withData("checkedAt", String.valueOf(new Date()))
            .up()
            .build();
    }
}

// Or as a CDI producer
@Produces @Readiness
HealthCheck caveEntranceCheck() {
    return () -> HealthCheckResponse.named("cave-entrance")
        .status(!knightsAreBlockingTheEntrance()).build();
}
```
```properties
quarkus.smallrye-health.ui.always-include=true
```
Endpoints: MicroProfile uses `/health/live`, `/health/ready`, `/health/started`. Quarkus serves them under `/q/health/...`.

**Probing them from Kubernetes** (the Quarkus Kubernetes extension generates this automatically):
```yaml
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      containers:
        - name: hoard-service
          readinessProbe:
            httpGet: { path: /q/health/ready, port: 8080 }
            initialDelaySeconds: 60
            periodSeconds: 15
            failureThreshold: 2
          livenessProbe:
            httpGet: { path: /q/health/live, port: 8080 }
            periodSeconds: 15
            failureThreshold: 3
          startupProbe:
            httpGet: { path: /q/health/started, port: 8080 }
            periodSeconds: 30
            failureThreshold: 4
```

### Metrics (MicroProfile Metrics)
Newer Quarkus versions recommend Micrometer instead, but the concepts are the same.
```java
@POST
@Counted(
    name = "appraise_treasure",
    absolute = true,                       // don't prefix the name with the class name
    displayName = "Appraise treasure",
    description = "How often dragons ask goblins what their stuff is worth",
    unit = MetricUnits.NONE,
    tags = { "info=appraisals", "type=meta" })
public BigDecimal appraise(Treasure treasure) { ... }
```
| Annotation | Measures |
|---|---|
| `@Counted` | number of invocations |
| `@ConcurrentGauge` | calls in progress (incremented on entry, decremented on exit) |
| `@Gauge` | the value returned by the annotated method, for example a business value such as the total gold in the vault |
| `@Metered` | invocation frequency (rate) |
| `@SimplyTimed` | total duration and count |
| `@Timed` | duration and throughput statistics |

**Injected metrics:**
```java
@Inject @Metric(name = "goblin_errors", description = "Goblin mistakes")
Counter goblinErrors;
goblinErrors.inc();

@Inject @Metric(name = "treasures_per_appraisal")
Histogram treasuresPerAppraisal;
treasuresPerAppraisal.update(treasureCount);
```
**Registering a metric manually:**
```java
@Inject @RegistryType(type = MetricRegistry.Type.APPLICATION)
MetricRegistry registry;

Metadata metadata = Metadata.builder()
    .withName("treasures_per_appraisal")
    .withDescription("How many treasures are appraised at once")
    .withDisplayName("Treasures per appraisal")
    .build();
registry.histogram(metadata).update(treasureCount);
```

### Tracing (MicroProfile OpenTracing)
Newer Quarkus versions use OpenTelemetry instead.
```java
@Traced(operationName = "withdraw-gold")
public Hoard withdrawGold(Long hoardNumber, BigDecimal amount) {
    tracer.activeSpan().setTag("hoardNumber", hoardNumber);                       // this span only
    tracer.activeSpan().setBaggageItem("withdrawnCoins", amount.toString());    // propagated to downstream services
    ...
}

@Inject Tracer tracer;
```

---

## Security
### Configuration
```properties
quarkus.http.cors=true

mp.jwt.verify.issuer=http://localhost:9080/auth/realms/dragonbank-realm
mp.jwt.verify.publickey.location=http://localhost:9080/auth/realms/dragonbank-realm/protocol/openid-connect/certs

keycloak.credentials.client-id=dragonbank
```
**Note.** MP JWT expects two claims that plain OIDC tokens don't have: `upn` (falling back to `preferred_username` and then `sub`) and `groups` (used for roles). In Keycloak, Okta and similar providers you have to add them as custom claims (mappers).

### Using the token
```java
@Inject JsonWebToken jwt;

@Inject @Claim("iat") Long issuedAt;
@Inject @Claim("sub") ClaimValue<Optional<String>> subject;   // ClaimValue re-reads the claim on every access,
                                                               // needed when the bean's scope is wider than @RequestScoped

@GET @Path("/dragons/me/claims")
@RolesAllowed("dragon")                     // or @Authenticated, @PermitAll, @DenyAll
public Map<String, Object> myClaims() {
    return jwt.getClaimNames().stream()
        .collect(Collectors.toMap(name -> name, name -> jwt.getClaim(name)));
}

@GET @Path("/dragons/me")
public Principal me(@Context SecurityContext ctx) {
    return ctx.getUserPrincipal();
}
```

### Sending the token from Swagger UI
The `securitySchemeName` and the `@SecurityRequirement` name must match:
```java
@SecurityScheme(
    securitySchemeName = "jwt",
    description = "JWT authentication with bearer token",
    type = SecuritySchemeType.HTTP,
    in = SecuritySchemeIn.HEADER,
    scheme = "bearer",
    bearerFormat = "Bearer [token]")
@OpenAPIDefinition(
    info = @Info(
        title = "DragonBank API",
        description = "Safe deposit for hoards since the Third Age",
        version = "1.0.0-SNAPSHOT",
        contact = @Contact(name = "Head Goblin Teller", email = "teller@dragonbank.example",
            url = "https://dragonbank.example")),
    security = @SecurityRequirement(name = "jwt"))
public class OpenApiConfig extends Application { }
```

---

## Testing
For plain JUnit 5 and Mockito see [Testing with JUnit and Mockito](Testing%20with%20JUnit%20and%20Mockito.md). In a `@QuarkusTest`, replace a bean with a Mockito mock using `@InjectMock`. For a comparison with Spring see [Testing Spring applications](../Spring%20and%20Spring%20Boot/Testing%20Spring%20applications.md).

### Test resources
A `QuarkusTestResourceLifecycleManager` starts something before the tests run. The map returned by `start()` overrides the application's configuration.

**Postgres:**
```java
public class PostgresResource implements QuarkusTestResourceLifecycleManager {
    private static final PostgreSQLContainer<?> DATABASE = new PostgreSQLContainer<>("postgres:13");

    @Override
    public Map<String, String> start() {
        DATABASE.start();
        return Map.of(
            "quarkus.datasource.jdbc.url", DATABASE.getJdbcUrl(),
            "quarkus.datasource.username", DATABASE.getUsername(),
            "quarkus.datasource.password", DATABASE.getPassword());
    }

    @Override
    public void stop() { DATABASE.close(); }
}
```
**Keycloak, with access tokens for test users:**
```java
public class KeycloakResource implements QuarkusTestResourceLifecycleManager {
    private static final DockerComposeContainer<?> KEYCLOAK =
        new DockerComposeContainer<>(new File("src/main/docker/keycloak-test.yml"))
            .withExposedService("keycloak_1", 9080,
                Wait.forListeningPort().withStartupTimeout(Duration.ofSeconds(30)));

    @Override
    public Map<String, String> start() {
        KEYCLOAK.start();
        String issuer = String.format("http://%s:%s/auth/realms/dragonbank-realm",
            KEYCLOAK.getServiceHost("keycloak_1", 9080),
            KEYCLOAK.getServicePort("keycloak_1", 9080));
        TokenService tokens = new TokenService();   // own helper calling the token endpoint
        Map<String, String> config = new HashMap<>();
        try {
            config.put("elder-dragon-token",
                tokens.getAccessToken(issuer, "elder-dragon", "test", "dragonbank", "mysecret"));
            config.put("hatchling-token",
                tokens.getAccessToken(issuer, "hatchling", "test", "dragonbank", "mysecret"));
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }
        config.put("mp.jwt.verify.publickey.location", issuer + "/protocol/openid-connect/certs");
        config.put("mp.jwt.verify.issuer", issuer);
        return config;
    }

    @Override
    public void stop() { KEYCLOAK.stop(); }
}
```
**Using them:**
```java
@QuarkusTest
@QuarkusTestResource(PostgresResource.class)     // newer: @WithTestResource
@QuarkusTestResource(KeycloakResource.class)
class HoardResourceTest {
    @ConfigProperty(name = "elder-dragon-token") String elderToken;
    @ConfigProperty(name = "hatchling-token") String hatchlingToken;

    @Test
    void hatchlingCannotEmptyElderHoard() {
        given().auth().oauth2(hatchlingToken)
            .when().delete("/hoards/1")
            .then().statusCode(403);
    }
}
```
### Test-related properties
```properties
%test.quarkus.kubernetes-config.enabled=false   # don't try to read ConfigMaps in tests
quarkus.test.native-image-profile=test          # config profile used by native tests
```
### Native tests
```java
@NativeImageTest                     // newer: @QuarkusIntegrationTest
class HoardResourceIT extends HoardResourceTest { }
```
Put `@DisabledOnNativeImage` (newer: `@DisabledOnIntegrationTest`) on a test in the parent class to skip it in native mode.

---

## Containers and Kubernetes
### Building images
```shell
# Image based on a native binary
mvn clean install -Pnative -Dquarkus.native.container-build=true -Dquarkus.container-image.build=true

# Use Jib instead of Docker (no Docker daemon needed)
./mvnw quarkus:add-extension -Dextensions="container-image-jib"
```
```properties
quarkus.container-image.registry=
quarkus.container-image.group=dragonbank
quarkus.container-image.name=hoard-service
quarkus.container-image.tag=1.0.0
quarkus.container-image.username=
quarkus.container-image.password=
```

### Docker cheat sheet
```shell
docker tag hoard-service dragonbank/hoard-service:1.0.0
docker push dragonbank/hoard-service:1.0.0

# Remove all containers / images of an app
docker rm  $(docker ps -aq --filter ancestor=dragonbank/hoard-service-jvm)
docker rmi $(docker images -q dragonbank/hoard-service-jvm)
```
**Multistage Dockerfile:**
```Dockerfile
FROM maven AS build
COPY . /build
WORKDIR /build
RUN mvn package

FROM open-liberty:full-java11-openj9
COPY --from=build /build/target/hoard-service.war /config/apps/
# Copy files owned by the user and group defined in the Open Liberty base image
COPY --chown=1001:0 src/main/liberty/config/server.xml /config/
```
**Simplest `docker-compose.yml`.** `deploy.replicas` only takes effect in Swarm mode (`docker stack deploy`):
```yaml
services:
  hoard-service:
    image: dragonbank/hoard-service-jvm:1.0.0
    deploy:
      replicas: 5
      restart_policy:
        condition: on-failure
    ports:
      - "8080:8080"
    networks:
      - cave-network
networks:
  cave-network:
```

### Running dependencies in Docker
```shell
docker run -d --name dragonbank-postgres \
    -e POSTGRES_USER=goblin-dba \
    -e POSTGRES_PASSWORD=Sh1nyG0ld \
    -e POSTGRES_DB=dragonbank \
    -p 5432:5432 \
    -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data \
    postgres:13

docker run -d --name dragonbank-keycloak \
    -e KEYCLOAK_USER=admin \
    -e KEYCLOAK_PASSWORD=admin \
    -e DB_VENDOR=h2 \
    -p 9080:8080 -p 8443:8443 -p 9990:9990 \
    jboss/keycloak:11.0.0
```
Newer Keycloak images are `quay.io/keycloak/keycloak ... start-dev`, with admin credentials passed via `KC_BOOTSTRAP_ADMIN_USERNAME`/`_PASSWORD`. Their URLs no longer contain `/auth`.

### Kubernetes
**ConfigMap and Secret:**
```shell
kubectl create configmap hoard-service-port --from-literal port=9081
kubectl create secret generic vault-credentials --from-literal username=Ignatius --from-literal password=Sh1nyG0ld
```
```yaml
env:
  - name: PORT
    valueFrom:
      configMapKeyRef:
        name: hoard-service-port
        key: port
        optional: true
  - name: VAULT_USERNAME
    valueFrom:
      secretKeyRef:
        name: vault-credentials
        key: username
```
**Generating env variables in the deployment (Quarkus Kubernetes extension):**
```properties
quarkus.kubernetes.env.vars.quarkus-datasource-jdbc-url=jdbc:postgresql://postgres:5432/dragonbank
quarkus.kubernetes.env.vars.mp-jwt-verify-issuer=http://keycloak-http.keycloak/auth/realms/dragonbank-realm
quarkus.kubernetes.env.vars.mp-jwt-verify-publickey-location=http://keycloak-http.keycloak/auth/realms/dragonbank-realm/protocol/openid-connect/certs
```
For health probes, see [Health checks](#health-checks).
