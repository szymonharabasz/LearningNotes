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
**Custom exception mapping.** Implement the interface:  
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
REST client in Java:  
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
MicroProfile REST Client:  
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
Asynchronous REST services:
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
Server-sent events:  
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
}```
**JSON handling: with Jersey.** Adding Moxy (`jersey-media-moxy`) to the `classpath` (e.g. as Maven dependency) automatically enables it and it can be used with `@Produces(MediaType.APPLICATION_JSON)` and `@Consumes(MediaType.APPLICATION_JSON).`
**Custom reponses.** Endpoint methods can return a `Reposnse` object
```Java
Response.status(200).entity("Hello").build();  
Response.ok("Hello").build();  
Response.ok("{greeting:'Hello'}", "application/json").build();  
Response.created(uri).entity(user).build();
Status.NOT_FOUND  
Status.INTERNAL_SERVER_ERROR
```