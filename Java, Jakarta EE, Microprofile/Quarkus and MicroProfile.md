	Running an application in development mode:
```shell
mvn quarkus:dev
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

@POST
@Transactional
public Response createAccount(Account acount) {
	account.persist();
	return Response.status(201).entity(account).build();
}
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
```
```java
@Inject
@Channel("account-overdrawn")
Emitter<Overdrawn> emitter;
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
Subscriber method:
```java
@Incoming("overdraft-update")
public void processOverdraftUpdate(OverdraftLimitUpdate overdraftLimitUpdate) { ... }
```
Tha parameter can also be a `Message`. One can add `@Blocking` to indicate that the code should be offloaded by the framework to a separate thread.
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
MicroProfile can `@Inject` a `JsonWebToken`.
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
    .select().where(name -> name.startsWith(”l”))
    .collect().asList()
    .subscribe().with(list -> System.out.println(”User names starting with l ” + list));

Multi.createFrom().ticks().every(Duration.ofSeconds(1)).onOverflow().drop()
    .onItem().transformToUniAndConcatenate(x -> products.getRecommendedProduct());
```
