Basic annotations:  
```
    @Path("customer"), @Produces("text/xml"), @Consumes(MediaType.TEXT_XML),  
    @GET, @POST, @PUT, @DELETE
```
Configuring REST resource path:  
```Java
    @ApplicationPath("resources")  
    public class JaxRsConfig extends javax.ws.rs.core.Application {}
```
**Path parameters:** `{param}` in the `@Path`, then annotate the corresponding method argument with `@PathParam("param")`
**Query parameters:** annotate the corresponding method argument with `@QueryParam("param")`. Service should then be called with `?param=foobar`.
**Matrix parameters:** annotate the corresponding method argument with `@MatrixParam("param")`. Service should be called with `;param=foobar` but it can be edded to any path segment and not just to the whole request
**Form parameters:** annotate the corresponding method argument with `@FormParam("param")`
**Header parameters:** annotate the corresponding method argument with `@HeaderParam("param")`
**Bean parameters:** create a bean with fields annotated with any selection of the previous annotations. Annotate the corresponding method argument of the type of this bean with `@BeanParam`
Parameters support `@DefaultValue("1")` etc. 
Parameters can be annotated with Bean Validation annotations, e.g., `@NotNull`, `@Valid` to enforce bean validation of the bean passed as an argument
Context information  
```Java
@GET  
public void testContext(@Context UrlInfo urlInfo, @Context HttpHeaders httpHeaders) {  
    MultivalueMap<String, String> pathParams = urlInfo.getPathParameters();  
    MultivalueMap<String, String> queryParams = urlInfo.getQueryParameters(); 
    MultivalueMap<String, String> requestHeaders = 
	    httpHeaders.getRequestHeaders();  
    Map<String, String> cookies = httpHeaders.getCookies();  
        …  
}
```
#### Different provider types
###### Custom exception mapping 
Implement the interface:  
```Java
@Provider  
public class MyExceptionMapper implements ExceptionMapper<MyException> {  
    @Override public UrlInfo toResponse(MyException exception) {  
        return Response.serverError()  
            .header("X-My-Error", exception.getMessage())  
            .entity(exception.getMessage())  
            .build();  
    }  
}
```
NOTE that Response builder can be used in general to create custom HTTP responses.
When `MyException` extends `RuntimeException` it is wrapped by `EjbException`, which is logged in the application server. This is avoided by annotating this exception with `@ApplicationException`.
Good idea is to handle `ConstraintViolationException` in this way.
###### Deserializing message body
```java
@Provider
@Consumes(MediaType.APPLICATION_JSON)
public class MyJsonReader implements MessageBodyReader<Person> {
    @Override
    public boolean isReadable(Class<?> type, Type genericType, 
	    Annotation[] annotations, MediaType mediaType) {
        return type.equals(Person.class) && 
	        mediaType.isCompatible(MediaType.APPLICATION_JSON_TYPE);
    }
    @Override
    public Person readFrom(Class<Person> type, Type genericType, 
	    Annotation[] annotations, MediaType mediaType, 
		MultivaluedMap<String, String> httpHeaders, InputStream entityStream)
        throws IOException, WebApplicationException {
        String s = new BufferedReader(new InputStreamReader(entityStream))
	        .lines().collect(Collectors.joining(" ")).trim();
        if (!s.startsWith("{") || !s.endsWith("}")) {
            throw new WebApplicationException(Response.status(400).build());
        }
        Person p = new Person();
        // ... parse string into Peron object ...
        return p;
    }
}
```
###### Serializing message body
```java
@Provider
@Produces(MediaType.APPLICATION_JSON)
public class MyJsonWriter implements MessageBodyWriter<Person> {
    @Override
    public boolean isWriteable(Class<?> type, Type genericType, 
	    Annotation[] annotations, MediaType mediaType) {
        return type.equals(Person.class) && 
	        mediaType.isCompatible(MediaType.APPLICATION_JSON_TYPE);
    }
    @Override
    public void writeTo(Person p, Class<?> type, Type genericType, 
	    Annotation[] annotations, MediaType mediaType, 
		MultivaluedMap<String, Object> httpHeaders, OutputStream entityStream)
        throws IOException, WebApplicationException {
            PrintStream ps = new PrintStream(entityStream);
            // print Person object to entity stream
    }
}
```
###### Simpler solution for converting parameters
```java
@Provider
public class ColorParamConverterProvider implements ParamConverterProvider {
	@Override
	public <T> ParamConverter<T> getConverter(Class<T> rawType, 
		Type genericType, Annotation[] annotations) {
		if (rawType.equals(Color.class)) {
			return (ParamConverter<T>) new ColorParamConverter();
	    }
	    return null;
	}
}

public class ColorParamConverter implements ParamConverter<Color> {
	@Override
	public Color fromString(String value) {
	    return Color.valueOf(value.toUpperCase());
	}
	
	@Override
	public String toString(Color value) {
		return value.name();
	}
}
```
###### Intercepting requests and responses
```java
@Provider
public class WhiteSpaceRemovingReaderInterceptor implements ReaderInterceptor {
	@Override
    public Object aroundReadFrom(ReaderInterceptorContext context) 
    throws IOException, WebApplicationException {
        InputStream originalStream = context.getInputStream();
        String entity = // convert stream to string
        entity = entity.replaceAll("\\s","");
        context.setInputStream(new ByteArrayInputStream(entity.getBytes()));
        return context.proceed();
    }
}
```
###### Request filters
There could be `@PreMatching` and (default) post-matching. The latter have access to extra information about the matched endpoint.
```java
@PreMatching
@Provider
public class ApiKeyCheckFilter implements ContainerRequestFilter {
    private final Map<String, Integer> apiInvocations = 
	    new ConcurrentHashMap<>();

    @Override
    public void filter(ContainerRequestContext requestContext) 
	    throws IOException {
        String apiKey = requestContext.getHeaderString(API_KEY_HEADER);
        if (apiKey == null) {
            requestContext.abortWith(Response.status(Status.UNAUTHORIZED)
	            .build());
            return;
        }
        // get count of recent invocations for this API key 
        int currentInvocations = // ...
        if (currentInvocations == -1) {
            requestContext.abortWith(Response.status(Status.FORBIDDEN).build());
            return;
        }
        if (currentInvocations > MAX_REQUESTS_PER_INTERVAL) {
            requestContext.abortWith(Response.status(Status.TOO_MANY_REQUESTS)
	            .header(HttpHeaders.RETRY_AFTER, 5).build());
            return;
        }
    }
}
```
###### Dynamic provider selection
By annotation (cf. `@Named` annotation in CDI)
```java
@NameBinding
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.METHOD, ElementType.TYPE})
public @interface Logged {}

@Logged
@Provider
public class LoggingFilter 
	implements ContainerRequestFilter, ContainerResponseFilter {
    @Override
    public void filter(ContainerRequestContext requestContext)
	    throws IOException {
        int requestID = idCounter.incrementAndGet();
        requestContext.setProperty("request.id", requestID);
        // Actual logging
    }
    @Override
    public void filter(ContainerRequestContext requestContext, 
	    ContainerResponseContext             responseContext)
        throws IOException {
        int requestID = (int) requestContext.getProperty("request.id");
		// Actual logging
    }
    //...
}

// In a resource:
@POST
@Logged
public String postMessage(String message) { ... }
```
Or as a dynamic feature - a provider that decides whether a filter should be applied or not:
```java
@Provider
public class MyDynamicFeature implements DynamicFeature {
    @Override
    public void configure(ResourceInfo resourceInfo, FeatureContext context) {
        Method m = resourceInfo.getResourceMethod();
        if (m.getName().startsWith("get")) {
            context.register(LoggingFilter.class);
        }
    }
}
```
#### Server-Sent Events
###### One version
For one registered client
```java
@Path("/sse")
@Produces(MediaType.SERVER_SENT_EVENTS)
public class SseService {
    @GET
    public void stream3Events(@Context SseEventSink sink, @Context Sse sse) {
        Executors.newSingleThreadExecutor().submit(() -> {
            try (SseEventSink sinkToClose = sink) {
                sink.send(sse.newEventBuilder()
                    .mediaType(TEXT_PLAIN_TYPE)
                    .data("foo")
                    .name("fooEvent")
                    .id("1")
                    .build());
                Thread.sleep(500);
                // repeat for 2/bar
                Thread.sleep(500);
                // repeat for 3/baz
            } catch (InterruptedException ex) {}
        });
    }
}
```
Using a broadcaster
```java
static SseBroadcaster broadcaster;
static ScheduledExecutorService executor = 
	Executors.newSingleThreadScheduledExecutor();
    
private void startBroadcasting(Sse sse) {
    if (broadcaster == null) {
        broadcaster = sse.newBroadcaster(); //...
    }
}

@GET
@Path("/broadcast")
public void broadcast(@Context SseEventSink sink, @Context Sse sse) {
    startBroadcasting(sse);
    broadcaster.register(sink);
    broadcaster.broadcast(sse.newEventBuilder()
        .mediaType(TEXT_PLAIN_TYPE)
        .data("new registrant")
        .build());
}
```
###### Other version
```Java
@GET @Produces(MediaType.SERVER_SENT_EVENTS)  
public void sendEvents(@Context SeeEventSing sseEventSink,  
    @Context Sse sse) {  
    Executors.newSingleThreadExecutor().execute( () -> {  
        final OutboundSseEvent outboundSseEvent = sse.newEventBuilder()  
            .name("my stock ticker value");  
            .data(String.class, String.format("%.2f", value))  
            .build();  
        sseEventSink.send(outboundSseEvent);  
    });  
}
```
Receiving in JavaScript code:  
```JavaScript
function getStockTickerValue() { // to be called e.g. on load  
    var source = new EventSource("/webresources/serversentevents/");  
    source.addEventListener("my stock ticker value", function (event) {  
        document.getElementById("tickerVal").innerHTML = event.data;  
    }, false);  
}
```
#### Asynchronous REST services:
###### With  `AsyncResponse`
```java
// Could also be non-static in an @ApplicationScoped bean
static ExecutorService executor = Executors.newFixedThreadPool(5);

@GET
@Path("async/{id}")
public void getPersonAsync(@PathParam("id") int id, 
	@Suspended AsyncResponse ar) {
	executor.submit(() -> {
		ar.resume(getPerson(id));
    });
}

// Or if one wants to handle an exception
@GET
@Path("async/{id}")
public void getPersonAsync(@PathParam("id") int id, 
	@Suspended AsyncResponse ar) {
	executor.submit(() -> {
	    Optional<Person> p = Optional.ofNullable(getPerson(id));
	    if (p.isPresent())
	        ar.resume(p.get());
	    else ar.resume(new NoSuchPersonException());
	});
}

// Takes long time
private Person getPerson(int id) { ... }
```
###### With returning `CompletionStage`
```Java
@Path("upload")  
public class FileUploadResource {  
    @Resource  
    ManagedExecutorService executor;    

    @POST  
    @Consumes("application/pdf")  
    CompletionStage<String> uploadPdf(File file) {  
        CompletableFuture<String> completionStage = 
	        new CompletableFuture<>();  
        executor.execute(() -> {  
            …  
            completionStage.complete(resultString);  
            …  
            completionStage.completeExeptionally(exception);  
        });  
        return completionStage;  
    }  
}
```

#### REST clients
###### REST client in Java:  
```Java
ClientBuilder.newClient()
    .target("http://localhost:8080/myapp/resources/customer")  
    .request().put(Entity.entity(customer,"text/xml"), Customer.class);  
ClientBuilder.newClient()
    .target("http://localhost:8080/myapp/resources/customer")  
    .queryParam("id", 1L)  
    .request().get(Customer.class);
ClientBuilder.newClient()
	.target("http://localhost:8080/myapp/resources/customer")  
    .path("{id}").resolveTemplate("id", 1L)  
    .request().get(Customer.class);  
Client client = ClientBuilder.newBuilder()  
    .connectTimeout(1, TimeUnit.SECONDS)  
    .readTimeout(10, TimeUnit.SECONDS)  
    .build();
```
Asynchronous calls with `async()`:
```java
WebTarget target = ClientBuilder.newClient().target(URL);  
Future<Response> future = target.request()
	.async();
	.get();
// do something else while waiting for the response...
try (Response response = future.get()) {
    // handle response...
} finally {
    client.close();
}
```
Adding a callback:
```java
WebTarget target = ClientBuilder.newClient().target(URL);  
target.request()
	.async();
	.get(new InvocationCallback<String>() {
        @Override
        public void completed(String response) {
            sb.append(response + "\n");
        }
        @Override
        public void failed(Throwable th) {
            th.printStackTrace();
        }
    );
```
... or with `rx()`:
```Java
WebTarget target = ClientBuilder.newClient().target(URL);  
CompletionStage<String> stage = target.request()  
	.rx()  
    .post(Entity.entity(new FileInputStream(new File(FILE_PATH)),  
        "application/pdf"), String.class);  
stage.whenCompleteAsync((result, error) -> { … });
```
Retrieving generic lists:  
```Java
GenericType<List<Customer>> listType  
    = new GenericType<List<Customer>> () {}; // empty interface 
```
Implementation  
```Java
target.request().get(listType);
```
###### MicroProfile REST Client:  
```Java
@RegisterRestClient(baseUri = BASE_URI)  
@ClientHeaderParam(name = "apiKey", value = YOUR_API_KEY)  
@Path("api")  
public interface ApiClient {  
    @GET  
    @Path("user")  
    UserResponse getUser(@BeanParam UserRequest userRequest);  
}  
…  
@Inject  
@RestClient  
private ApiClient apiClient;
```
Returning `CompletionStage` allows also for asynchronous calls
#### JSON handling with Jersey 
Adding Moxy (`jersey-media-moxy`) to the `classpath` (e.g. as Maven dependency) automatically enables it and it can be used with `@Produces(MediaType.APPLICATION_JSON)` and `@Consumes(MediaType.APPLICATION_JSON).`
#### Custom responses
Endpoint methods can return a `Reposnse` object
```Java
Response.status(200).entity("Hello").build();  
Response.ok("Hello").build();  
Response.ok("{greeting:'Hello'}", "application/json").build();  
Response.created(uri).entity(user).build();
Status.NOT_FOUND  
Status.INTERNAL_SERVER_ERROR
```