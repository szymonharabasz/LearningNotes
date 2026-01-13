Running an application in development mode:
```shell
mvn quarkus:dev
```
Building a native executable in a container, without having GraalVM installed on a local host:
```shell
mvn package -Pnative -Dquarkus.native.container-build=true
```
Creating a Docker image based on a native binary:
```shell
mvn clean install -Pnative -Dquarkus.native.container-build=true \
	-Dquarkus.container-image.build=true
```
Tagging a built image:
```shell
docker tag image username/repository:tag
```
Pushing image to registry:
```shell
docker push username/repository:tag
```
To build images with Jib instead of Docker:
```shell
./mvnw quarkus:add-extension -Dextensions="container-image-jib
```
Removing containers related to a given app:
```shell
docker ps -a | awk '{ print $1,$2 }' | grep username/sample-jvm | awk '{print $1 }' | xargs -I {} docker rm {}
```
Removing images related to a given app:
```shell
docker images | awk '{ print $1":"$2 }' | grep username/sample-jvm | xargs -I {} docker rmi {}
```
Properties to customize image building:
```
quarkus.container-image.group
quarkus.container-image.name
quarkus.container-image.tag
quarkus.container-image.registry
quarkus.container-image.username
quarkus.container-image.password
```
Simplest docker-compose.yml
```yaml
version: "3"
services:
  web:
    image: nebrass/sample-jvm:1.0.0-Final
    deploy:
      replicas: 5
      restart_policy:
        condition: on-failure
    ports:
      - "8080:8080"
    networks:
      - webnetwork
networks:
  webnetwork:
```
Running Postgres in a Docker container:
```shell
docker run -d --name demo-postgres \
        -e POSTGRES_USER=developer \
        -e POSTGRES_PASSWORD=someCrazyPassword \
        -e POSTGRES_DB=demo \
        -p 5432:5432 \
        -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data \
        postgres:13
```
Running Keycloak in a Docker container:
```shell
docker run -d --name docker-keycloak \
          -e KEYCLOAK_USER=admin \        
          -e KEYCLOAK_PASSWORD=admin \    
          -e DB_VENDOR=h2 \               
          -p 9080:8080 \                  
          -p 8443:8443 \                  
          -p 9990:9990 \                  
          jboss/keycloak:11.0.0
```
#### MicroProfile configuration
Programmatic access:
```java
Config config = ConfigProvider.getConfig();
String greeting = config.getValue("myapp.greeting", String.class);
```
Annotation access:
```java
@Incject
@ConfigProperty(name="myapp.greeting", defaultValue="Hello, Default")
String greeting;
```
in `application.properties`:
```
myapp.greeting=Hello, World!
```
Grouping properties with `@ConfigProperties`
```java
@ConfigProperties(prefix="bank-support")
public class BankSupportConfig {
	private String phone;
	publc string email;

	public String getPhone() { return this.phone; }
	public void setPhone(String phone) { this.phone = phone; }
}
```
This can be injected:
```java
@ConfigProperties(prefix="bank-support")
BankSupportConfig supportConfig
```
and provides properties `bank-support.email` and `bank-support.phone`.

Sources (those with higher ordinal take precedence):
- System properties - ordinal **400**
- Environment variables - ordinal **300**
- Kubernetes ComfigMap client - ordinal **270**
- `application.yaml` - ordinal **254**
- `application.properties` - ordinal **250**
- `microprofile-config.properties` - ordinal **100**

###### Configuration features added in Quarkus
Config profiles:
```
myapp.greeting=Hello, World!
%dev.myapp.greeting=Hello, Dev!
%prod.myapp.greeting=Hello, User!
%myprof.myapp.greeting=Hello, welocme in a custom profile!
```
Expressions in properties:
```
support.email=support@defaultbank.com
bank-support.email=${support.email}
```
Config Mapping:
```Java
@ConfigMapping(prefix="bank-support-mapping)
interface BankSupportConfigMapping {
	@Size(min=12, max=12)
	String phone();
	String email();
	Business business();

	interface Business {
		@Size(min=12, max=12)
		String phone();
		String email();
	}
}
```
It can be accessed through:
```java
inject BankSupportConfigMapping configMapping;
// ...
configMapping.business().email();
```
#### Useful configuration properties
```properties
quarkus.http.root-path=/api
quarkus.flyway.migrate-at-start=true
quarkus.smallrye-health.ui.always-include=true

### Security
quarkus.http.cors=true  

# MP-JWT Config
mp.jwt.verify.issuer=http://localhost:9080/auth/realms/quarkushop-realm   
mp.jwt.verify.publickey.location=http://localhost:9080/auth/realms/quarkushop-realm/protocol/openid-connect/certs   

# Keycloak Configuration
keycloak.credentials.client-id=quarkushop

### REST Client
product-service.url=http://product:8080/api
com.example.order.client.ProductRestClient/mp-rest/url=${product-service.url}     
com.example.order.client.ProductRestClient/mp-rest/scope=javax.inject.Singleton   

### Disable Kubernetes support in tests:
%test.quarkus.kubernetes-config.enabled=false
quarkus.test.native-image-profile=test

###Indexing common package for injectable objects
quarkus.index-dependency.commons.group-id=com.example
quarkus.index-dependency.commons.artifact-id=myapp-commons

### Getting some properties as environment variables in Kubernetes
quarkus.kubernetes.env.vars.quarkus-datasource-jdbc-url=jdbc:postgresql://postgres:5432/demo
quarkus.kubernetes.env.vars.mp-jwt-verify-publickey-location=http://keycloak-http.keycloak/auth/realms/quarkushop-realm/protocol/openid-connect/certs
quarkus.kubernetes.env.vars.mp-jwt-verify-issuer=http://keycloak-http.keycloak/auth/realms/quarkushop-realm

quarkus.http.test-port=9999
```
#### Database access with Quarkus and Panache
Simplified configuration
```
quarkus.datasource.db-kind=postgresql
quarkus.datasource.username=database-user
quarkus.datasource.password=database-pwd
quarkus,datasource.jdbc.url=jdbc:postgresql://localhost:5432/my_database

quarkus.datasource.orders.db-kind=postgresql
...
```
###### Active record approach
With Panache, one only needs to annotate a POJO with `@Entity` and extend `PanacheEntity`. Field getters and setters are automatically generated at build time:
```java
@Entity
public class Account extends PanacheEntity {
	public Long accountNumberl;
	public Long customerNumber;
	public String customerName;
	// ...
	public static long totalAccountsPerCustomer(Long customerNumber) {
		return find("customerNumber", customerNumber).count();
	}
	public static Account findByAccountNumber(Long accountNumber) {
		return find("accountNumber", accountNumber).firstResult();
	}
}
```
Some methods:
```java
Account.listAll();
Account.streamAll(); // reactive stream

@POST
@Transactional
public Response createAccount(Account acount) {
	account.persist();
	return Response.status(201).entity(account).build();
}
// Reactive:
Customer.<Customer>findById(id)
    .onItem().ifNull().failWIth(new WebApplicationException(”Failed to find customer”, 
        Response.Status.NOT_FOUND));
```
Transaction in this approach:
```java
return Panache.withTransaction(customer::persist);
return Panache.withTransaction(() -> Customer.<Customer>findById(id)
    .onItem().ifNotNull().invoke(entity -> entity.name = customer.name));
return Panache.withTransaction(() -> Customer.deleteById(id)
    .map(deleted -> deleted ? Response.ok().status(Response.Status.NO_CONTENT).build() : 
        Response.ok().status(Response.Status.NOT_FOUND).build()));

```
###### Data repository approach
One creates a "normal" JPA `@Entity` and then a repository:
```java
@ApplicationScoped
public class AccountRepository implements PanacheRepository<Account> {
	public Account findByAccountNumber(Long accountNumber) {
		return find("accountNumber = ?1", accountNumber).firstResult();
	}
}
// ...
@Inject
AccountRepository accountRepository;

accountRepository.listAll();

@POST
@Transactional
public Response createAccount(Account acount) {
	accountRepository.persist(account);
	return Response.status(201).entity(account).build();
}
```
#### Vert.x web client
```java
@Inject
public webClient(Vertx vertx) {
    client = WebClient.create(vertx);
}
@PreDestroy
public void close() { client.close(); }

public Uni<JsonObject> invokeService() {
    return client.getAbs(”https://httpbin.org/json”).send()
        onItem().transform(response -> {
            if (response.statusCode() == 200) { return response.bodyAsJsonObject(); }
            else { return new JsonObject().put(”error”, response.statusMessage()); }
        });
}
```
#### MicroProfile REST client
Annotate an interface with standard JAX-RS annotations and `@RegisterRestClient`:
```java
@Path("/accounts")
@RegisterRestClient(configKey="account-service")
@RegisterClientHeaders // if needed
@ClientHeaderParam(
	name = "class-level-param", 
	value = "AccountService interface")
@Produces(MediaType.APPLICATION_JSON)
public interface AccountService {
	@GET
	@Path("/{acctNumber}/balance")	
	@ClientHeaderParam(
		name = "method-level-param", 
		value = "{generatedValue}")
	BigDecimal getBalance(@PathParam("acctNumber") Long accountNumber);

	default String generatedValue() {
		return "Value generated in method";
	}
}
```
To use it:
```java
@Inject
@RestClinet
AccountService accountService;
```
Alternatively, one can use a programmatic client. One defines the same interface, but without `@RegisterRestClient` and then creates the client with the Builder pattern:
```java
AccountServiceProgrammatic accountService = RestClientBuilder.newBuilder()
	.baseUrl(new URL(accountServiceUrl))
	.connectTimeout(500, TimeUnit.MILLISECONDS)
	.readTimeout(1200, TimeUnit.MILLISECONDS)
	build(AccountServiceProgrammatc.class);
```
For asynchronous endpoints, one has to return `CompletionStage:
```java
@POST
@Path("/{accountNumber}/transaction")
public CompletionStage<Void> transactAsync(
	@PathParam("acctNumber") Long accountNumber, BigDecimal amount);
```
For header parameters one can also use just `@HeaderParam` on the method parameter.

Client-side JAX-RS providers:
```java
ClientRequestFilter
ClientResponseFilter
MessageBodyReader
MessageBodyWriter
ParamConverter
ReaderInterceptor
WriterInterceptor
ResponseExceptionMapper
```
Example request filter
```java
public class AccountRequestFilter implements ClientRequestFilter {
	@Override
	public void filter(ClientRequestContext requestContext) 
		throws IOException 
	{
		String invokedMethod = (String) requestContext.getProperty(
			"org.eclipse.microprofile.rest.client.invokedMethod");
		requestContext.getHeaders().add(
			"Invoked-Client-Method", invokedMethod);
	}
}
```
Example response exception mapper:
```java
public class AccountExceptionMapper 
	implements ResponseExceptionMapper<AccountNotFoundException> 
{
	@Override
	public AccountNotFoundException toThrowable(Response reponse) {
		return new AccountNotFoundException("Failed to retrieve account");
	}

	@Override
	public boolean handles(int status, MultivalueMap<String, Object> hdrs) {
		return status == 404;
	}
}
```
Example usage:
```java
// ...
@RegisterProvider(AccountRequestFilter.class)
public interface AccountService { ... }
```
#### RESTEasy Reactive
An endpoint can be annotated with `@NonBlocking`. They can return `Uni` or `Multi`. One can also directly interact with the Vert.x library
```java
@Inject
Vertx vertx;
// …
Uni<String> uni = vertx.fileSystem().readFile(path)
    .onItem().transform(buffer -> buffer.toString(”UTF-8”));
```
Customizing the response:
```java
.onItem().transform(content -> Response.ok(content).build())
.onFailure().recoverWIthItem(Response.status(Response.Status.NOT_FOUND).build());
```
Registering an exception mapper:
```java
@ServerExceptionMapper
public Response mapFileSystemException(FileSystemException ex) {
    return Response.status(Response.Status.NOT_FOUND).entity(ex.getMessage()).build();
}
```
Handling timeouts:
```java
return vertx.fileSystem().readFile(”slow.txt”).onItem(…)
    .ifNotItem().after(Duration.ofSeconds(1)).fail();
```
Raw streaming:
```java
return vertx.fileSystem().open(”war-and-peace.txt”, new OpenOptions.setRead(true))
    .onItem().transformToMulti(AsyncFile::toMulti)
    .onItem().transform(b -> b.toString(”UTF-8”));
```
###### Using Redis
Configuration:
```properties
quarkus.redis.hosts=redis://localhost:6379
```
Injecting a client:
```java
@Inject
ReactiveRedisClient redis;
````
Retrieving all customers:
```java
return redis.keys(”*”).onItem().transformToMulti(response -> {
    return Multi.createFrom().iterable(response).map(Response::toString);
}).onItem().transformToUniAndMerge(key -> redis.hgetall(key).map(resp ->
    constructCustomer(Long.parseLong(key.substring(CUSTOMER_HASH_PREFIX.length())), resp)
))
```
Other command: `hmset`, Mutiny`hdel`.
#### Custom health check
```java
@ApplicationScoped
@Liveness
public Always HealthyLovenessCheck implements HealthCheck {
	@Override
	public HealthCheckResponse call() {
		return HealthCheckResponse
			.named()
			.withData("time", String.valueOf(new Date()))
			.up()
			.build();
	}
}
```
Instead of `@Liveness` there can be `@Readines` or, in Quarkus, `@HealthGroup("custom")`.
#### Resilience patterns
**Making a long running method call asynchronous:**
```java
@Asynchornous
public String invokeLongRunningOperation() { 
	callLongRunningRemoteService();
}
```
**Limiting the number of concurrent invocations:**
```java
@Bulkhead(value = 10, waitingTaskSequence = 10) 
public String invokeLegacySystem() { 
	...
}
```
When `@Bulkhead` is used with `@Asynchronous`, `waitingTaskSequence` specifies the size of the request thread queue.
**Fallback:**
```java
@Bulkhead
@Fallback(
	fallbackMethod="bulkheadFallbackGetBalance",
	applyOn = { BulkheadException.class },
	skipOn = { MyOtherException.class }
)
public Response newTransaction(...) { ... }

public Response bulkheadFallbackGetBalance(...) { ... }
```
Alternatively to `fallbackMethod`, one can use `value` parameter and provide and `ExceptionHandler` class.
**Execution timeout:**
```java
@Timeout(value = 1000, unit = ChronoUnit.MILLIS)
```
**Retries:**
Using the annotation `@Retry` with parameters:
`retryOn`, `abortOn` (list of exceptions), `delay`, `delayUnit`, `jitter`, `jitterDelayUnit`, `maxDuration`, `durationUnit`, `maxRetries`.
**Circuit breaker**
Using the annotation `@CircuitBreaker` with parameters:
`failOn`, `skipOn`, `requestVolumeThreshold` (size of the sliding window), `failuteRatio`, `delay` (how long it stays open), `delayUnit`, `successThreshold` (number of successful trials), .

Annotations can be enabled or disabled and their parameter values can be changed in `applicaiton.properties`, for example
```
# [[CLASS]/METHOD]/<annotation>/enabled=false
io.quarkus.transactions.TransactionResource/Timeout/enabled=false
io.quarkus.transactions.TransactionResource/getBalance/Timeout/value=150

```
#### Reactive messaging
Channel configuration:
```
mp.messaging.outgoing.account-overdrawn.connector=smallrye-kafka
mp.messaging.outgoing.account-overdrawn.topic=overdrawn
mp.messaging.outgoing.account-overdrawn.value.serializer=
	io.quarkus.kafka.client.serialization.JsonSerializer
%test.mp.messaging.outgoing.account-overdrawn.value.serializer=
	org.apache.kafka.common.serialization.StringSerializer
%test.mp.messaging.outgoing.account-overdrawn.value.deserializer=
	org.apache.kafka.common.serialization.StringDeserializer
```
```java
@Inject
@Channel("account-overdrawn")
Emitter<Overdrawn> emitter;
// or with Quarkus:
@Channel("account-overdrawn")
MutinyEmitter<Overdrawn> emitter;
// ...
if (accountOverdrawn) {
	return emitter.send(payload).thenCompose(empty -> 
		CompletableFuture.completedFuture(entity));
}
return entity;
```
One can also emit a full `Message` including handlers for acknowledgement, successful or with failure:
```java
List<Throwable> failures = new ArrayList<>();
// ...
CompletableFuture<Account> future = new CompletableFuture<>();
emitter.send(Message.of(
	payload,
	() => {
		future.complete(entity);
		return completableFuture.completedFuture(null);
	},
	reason => {
		failures.add(reason);
		future.completeExceptionally(reason);
		return completableFuture.completedFuture(null);
	}
));
return future
```
Emitter method:
```java
@Outgoing
public Message<Overdrawn> overdraftNotification() {
	// ...
	return Message.of(...);
}
```
Adding Kafka metadata:
```java
Message.of(…).addMetadata(OutgoingKafkaRecordMetadata.builder().withKey(”light”).build());
```
Subscriber method:
```java
@Incoming("overdraft-update")
public void processOverdraftUpdate(OverdraftLimitUpdate overdraftLimitUpdate) { ... }
```
The parameter can also be a `Message`. In the method body, the message should be acked. Reading Kafka metadata:
```java
// Message<Person> person
person.getMetadata(IncomingKafkaRecordMetadata.class).get().getKey();
```
One can add `@Blocking` to indicate that the code should be offloaded by the framework to a separate thread. 
Incoming channel with Mutiny:
```java
@Channel(”my-channel”)
Multi<Paeson> streamOfPersons;
void init() {
    streamOfPersons.subscribe().with(…);
}
```
With messages (ack and nack):
```java
Multi<Message<Paeson>> streamOfPersons;
void init() {
    streamOfPersons.subscribe().with(message -> 
        try {
            // ….
            message.ack();
        } catch (Exception ex) {
            message.nack();
        }
     );
}
```
Connecting messages:
```java
@Incoming(”ticks”)
@Outgoing(”hello”)
public Message<String> hello(Message<String> tick) {
    return tick.withPayload(”Hello ” + tick.getPayload());
}
```
Handling an overflow:
```java
@Channel(”channel”)
@OnOverflow(value = OnOverflow.Strategy.BUFFER, bufferSIze = 100)
MutinyEmitter<Person> emitter;
```
Other strategies: `UNBOUNDED_BUFFER`, `DROP`, `LATEST`, `FAIL`. `THROW_EXCEPTION`.
Retrying processing a message 
```java
@Incoming(…)
@Outgoing(…)
@Retry(maxRetries = 10, delay = 1, delayUnits = ChronoUnit.SECONDS)
public String hello(long tick) { … }
```
#### Metrics
Created with different annotations, for example:
```java
@POST
@Counted(
	name = "convert_currency", 
	absolute = true, // meaning absolute name
	displayName = "Convert currency method", 
	description = "Method to convert one currency to the other", 
	unit = MetricUnits.NONE,
	tags = { "info=conversions", "type=meta" })
```
Annotations to create different types of metrics:
`@Counted`
`@ConcurrentGauge` - incremented when an annotated element is entered and decremented when it is existed
`@Gauge` - to annotate a method (for example in an `@ApplicationScoped` bean) that returns some meaningful value, for example from the business point of view
`@Metered` - returns the frequency of invocations of an annotated element
`@SimplyTimed` - measures duration of execution and count
`@Timed` - measures duration and throughput statistics

Injecting metrics:
```java
@Inject
@Metric(name = ..., description = ...)
Counter errorMapperCounter;
// ...
errorMapperCounter.inc();

@Inject
@Metric(name = ..., description = ...)
Histogram conversionCountHistogram;
// ...
conversionCountHistogram.update(conversionCount);
```
Manual registering a metric:
```java
@Inject 
@RegistryType(type = MetricRegistry.Type.APPLICATION)
MetricRegistry metricRegistry;
// ...
Metadata metadata = Metadata.builder()
	.withName("count_conversions_histogram") 
	.withDescription("A histogram for the count of conversions") 
	.withDisplayName("A histogram")
	.build();
Histogram conversionCountHistogram = registry.histogram(metadata);
conversionCountHistogram.update(conversionCount);
```
#### Tracing
Enabling for a given resource:
```java
@Traced(operationName = "withdraw-from-account")
```
Manual steering spans
```java
@Inject
Tracer tracer;
// ...
tracer.activeSpan().setTag("accountNumber", accountNumber);
tracer.activeSpan().setBaggageItem("withdrawalAmount", withdrawalAmount);
```
#### Security
MicroProfile can `@Inject` a `JsonWebToken`. One can see all the claims in the token:
```java
@GET
@Path("/current/info/claims")
public Map<String, Object> getCurrentUserInfoClaims() {     ③
    return jwt.getClaimNames()
        .stream()
        .map(name -> Map.entry(name, jwt.getClaim(name)))
        .collect(Collectors.toMap(
            entry -> entry.getKey(),
            entry -> entry.getValue())
    );
}
```
Principal can also be extracted from the security context:
```java
@GET
@Path("/current/info-alternative")
public Principal getCurrentUserInfoAlternative(@Context SecurityContext ctx) {
    return ctx.getUserPrincipal();
}
```
Methods can be annotated with `@Authenticated` or `@RolesAllowed`

Making Swagger UI include the access token in all REST API requests:
```java
@SecurityScheme(
    securitySchemeName = "jwt",             ①
    description = "JWT authentication with bearer token",
    type = SecuritySchemeType.HTTP,         ①
    in = SecuritySchemeIn.HEADER,           ①
    scheme = "bearer",                      ①
    bearerFormat = "Bearer [token]")        ①
@OpenAPIDefinition(
    info = @Info(                           
	    title = "MyApp API",
        description = "Sample application",
        contact = @Contact(name = "John Doe", email = "johndoe@gmail.com", 
	        url = "https://blog.john.doe"),
		version = "1.0.0-SNAPSHOT"

    ),
    security = @SecurityRequirement(name = "JWT") ③
)
public class OpenApiConfig extends Application { }
```
A test resource for a Keycloak:
```java
public static DockerComposeContainer KEYCLOAK = new DockerComposeContainer(
    new File("src/main/docker/keycloak-test.yml"))
       .withExposedService("keycloak_1", 9080,
           Wait.forListeningPort().withStartupTimeout(Duration.ofSeconds(30)));

public class KeycloakRealmResource implements 
	QuarkusTestResourceLifecycleManager {
    @ClassRule
    public static DockerComposeContainer KEYCLOAK = new DockerComposeContainer(
        new File("src/main/docker/keycloak-test.yml"))
	        .withExposedService("keycloak_1", 9080,
				Wait.forListeningPort()
					.withStartupTimeout(Duration.ofSeconds(30)));

    @Override
	public Map<String, String> start() {
		KEYCLOAK.start();
		String jwtIssuerUrl = String.format(
			"http://%s:%s/auth/realms/quarkus-realm",
			KEYCLOAK.getServiceHost("keycloak_1", 9080),
			KEYCLOAK.getServicePort("keycloak_1", 9080)
		);
		TokenService tokenService = new TokenService();
		Map<String, String> config = new HashMap<>();

		try {
			String adminAccessToken = tokenService.getAccessToken(jwtIssuerUrl,
				"admin", "test", "quarkus-client", "mysecret"
			);
			String testAccessToken = tokenService.getAccessToken(jwtIssuerUrl,
				"test", "test", "quarkus-client", "mysecret"

            );
			config.put("quarkus-admin-access-token", adminAccessToken);
			config.put("quarkus-test-access-token", testAccessToken);
			
```
Using it:
```java
@QuarkusTest
@QuarkusTestResource(TestContainerResource.class)
@QuarkusTestResource(KeycloakRealmResource.class)
class CategoryResourceTest {
    static String ADMIN_BEARER_TOKEN;
	static String USER_BEARER_TOKEN;

	@BeforeAll
	static void init() {
		ADMIN_BEARER_TOKEN = System.getProperty("quarkus-admin-access-token");
		USER_BEARER_TOKEN = System.getProperty("quarkus-test-access-token");
    }
    ...
}
```
#### Reactive streams with Mutiny
Subscribing to a stream:
```java
stream.subscribe().with(
    item -> System.out.println(”Received an item ” + item),
    failure -> System.out.println(”Oh, no! Received a failure ” + failure),
    () -> System.out.println(”Received a completion”)
);
```
###### Operators
```java
stream.onItem().transform(circle -> toSquare(circle))
    .subscribe().with(…);

stream.onFailure().recoverWIthItem(failure -> getFallbackForFailure(failure))
    .subscribe.with(…);

Multi.createBy().merging().streams(circles, squares)
    .subscribe.with(…);

Multi.createFrom().ticks().every(Duration.ofMillis(20))
    .onOverflow().buffer(250)
    .emitOn(Infrastructure.getDefaultExecutor());
    .onItem().transform(BufferingExample::canOnlyConsumeOneItemPerSecond)
    .subscribe().with(…);

Multi.createFrom().ticks().every(Duration.ofMillis(20))
    .onOverflow().drop(x -> System.out.println(”Dropping item ” + x))
    .emitOn(Infrastructure.getDefaultExecutor());
    .onItem().transform(BufferingExample::canOnlyConsumeOneItemPerSecond)
    .transform().byTakingFirstItems(10)
    .subscribe().with(…);

multi.onItem().transform(user -> user.name.toLowerCase())
    .select().when(name -> name.startsWith(”l”))
    .collect().asList()
    .subscribe().with(list -> System.out.println(”User names starting with l ” + list));

Multi.createFrom().ticks().every(Duration.ofSeconds(1)).onOverflow().drop()
    .onItem().transformToUniAndConcatenate(x -> products.getRecommendedProduct());

Uni.createFrom.nullItem();

stream.onItem().transform(l -> Long.toString(l))
    .group().intoLists().of(5);
```
###### Observing events
```java
multi
    .onSubscribe().invoke(sub -> …)
    .onCancellation().invoke(() -> …)
    .onItem().invoke(s -> …)
    .onFailure().invoke(f -> …)
    .onCompletion().invoke(() -> …)
    .subscribe.with(…);
```
###### Chaining asynchronous actions
```java
uni.onItem().transformToUni(item -> callMyRemoteService(item)).subscribe().with(…);
uni.onItem().transformToMulti(item -> getMulti(item)).subscribe().with(…);

users.getAllUsers().onItem().transformToMultiAndConcatenate(user ->
    user -> orders.getOrdersForUser(user));
users.getAllUsers().onItem().transformToMultiAndMerge(user ->
    user -> orders.getOrdersForUser(user));
```
###### Recovering from failures
```java
.onFailure().retry().withBackoff(Duration.ofSeconds(3)).atMost(3);
```
###### Combining items
```java
uni.combine.all().unis(uni1, uni2).asTuple().onItem()…
```
###### Selecting items
One example - distinct elements
```java
orders.getAllOrders().onItem().transformToIterable(order -> order.products)
    .select().distinct();
```
Mutiny provides a `skip` group which is opposite to `select`.
###### Collecting items
```java
multi.collect().asMap(item -> getKeyFor(item));
Uni<Long> count = multi.collect().with(Collectors.counting());
```
#### Other GraalVM aspects
Creating a test that is run in a native image:
```java
@NativeImageTest
class CartResourceIT extends CartResourceTest { }
```
To disable a given parent test class in native mode:
```java
@DisabledOnNativeImage
```