Related notes:
- MicroProfile REST Client and RESTEasy Reactive: [Quarkus](Quarkus%20and%20MicroProfile.md)
- JSON/XML binding: [Serialization](Serialization%20and%20deserialization%20of%20XML%20and%20JSON.md)
- Parameter validation: [Bean Validation](Bean%20Validation.md)

## Application and resources
```java
@ApplicationPath("api")
public class DragonBankApi extends Application { }     // jakarta.ws.rs.core.Application

@Path("hoards")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class HoardResource {
    @GET @Path("{hoardNumber}")
    public Hoard get(@PathParam("hoardNumber") Long hoardNumber) { ... }

    @POST   public Response deposit(@Valid Hoard hoard) { ... }
    @PUT    @Path("{hoardNumber}") public Hoard update(...) { ... }
    @DELETE @Path("{hoardNumber}") public void close(...) { ... }
}
```

## Parameters
| Annotation | Source | Example |
|---|---|---|
| `@PathParam("id")` | `{id}` in `@Path` | `/hoards/42` |
| `@QueryParam("kingdom")` | query string | `/dragons?kingdom=Eriador` |
| `@MatrixParam("color")` | matrix parameter; can be attached to **any path segment** | `/treasures;color=red/gems` |
| `@FormParam("name")` | form body | |
| `@HeaderParam("X-Goblin-Key")` | header | |
| `@CookieParam("session")` | cookie | |
| `@BeanParam` | a class whose fields carry any of the annotations above | |

- `@DefaultValue("1")` supplies a value when the parameter is missing.
- Parameters can have Bean Validation constraints (`@NotNull`, `@Valid`).

**Context objects:**
```java
@GET
public String inspect(@Context UriInfo uriInfo, @Context HttpHeaders headers, @Context SecurityContext security) {
    MultivaluedMap<String, String> pathParams  = uriInfo.getPathParameters();
    MultivaluedMap<String, String> queryParams = uriInfo.getQueryParameters();
    MultivaluedMap<String, String> reqHeaders  = headers.getRequestHeaders();
    Map<String, Cookie> cookies = headers.getCookies();
    ...
}
```

## Responses
```java
Response.ok(hoard).build();
Response.ok("{\"greeting\":\"Roar\"}", MediaType.APPLICATION_JSON).build();
Response.status(Status.NOT_FOUND).entity("No such hoard (raided?)").build();
Response.created(uriInfo.getAbsolutePathBuilder().path(id.toString()).build()).entity(hoard).build();
Response.serverError().header("X-Goblin-Excuse", "The abacus broke").build();

throw new WebApplicationException(Status.FORBIDDEN);   // or NotFoundException, BadRequestException, ...
```
Generic lists, on the client side or in a `Response`, need a `GenericType`. It is an anonymous subclass, which keeps the type argument at runtime:
```java
List<Dragon> dragons = target.request().get(new GenericType<List<Dragon>>() {});
```

## Providers
All providers are annotated with `@Provider`, or registered in the `Application`.

### Exception mappers
```java
@Provider
public class VaultBreachedMapper implements ExceptionMapper<VaultBreachedException> {
    @Override
    public Response toResponse(VaultBreachedException ex) {
        return Response.status(Status.CONFLICT).header("X-Error", ex.getMessage()).entity(ex.getMessage()).build();
    }
}
```
- `ConstraintViolationException` is worth mapping this way.
- If the exception is thrown from an EJB and is a `RuntimeException`, it arrives wrapped in `EJBException` (and gets logged). Annotate it with `@ApplicationException` to prevent that; see [EJB](Enterprise%20JavaBeans.md).

### Entity providers (body reader and writer)
For a custom media type or format:
```java
@Provider
@Consumes("application/x-dragon-scroll")
public class ScrollReader implements MessageBodyReader<Dragon> {
    @Override
    public boolean isReadable(Class<?> type, Type genericType, Annotation[] annotations, MediaType mediaType) {
        return type == Dragon.class;
    }
    @Override
    public Dragon readFrom(Class<Dragon> type, Type genericType, Annotation[] annotations, MediaType mediaType,
                           MultivaluedMap<String, String> headers, InputStream entityStream) throws IOException {
        String scroll = new String(entityStream.readAllBytes(), StandardCharsets.UTF_8).trim();
        if (!scroll.startsWith("~~") || !scroll.endsWith("~~"))
            throw new WebApplicationException(Response.status(400).build());
        return parse(scroll);
    }
}
```
`MessageBodyWriter<Dragon>` is symmetric: `isWriteable(...)` and `writeTo(dragon, ..., OutputStream entityStream)`.

### Parameter converters
This is the simpler option when only a `@*Param` value needs converting:
```java
@Provider
public class TreasureTypeConverterProvider implements ParamConverterProvider {
    @Override
    @SuppressWarnings("unchecked")
    public <T> ParamConverter<T> getConverter(Class<T> rawType, Type genericType, Annotation[] annotations) {
        if (rawType != TreasureType.class) return null;
        return (ParamConverter<T>) new ParamConverter<TreasureType>() {
            public TreasureType fromString(String value) { return TreasureType.valueOf(value.toUpperCase()); }
            public String toString(TreasureType value)   { return value.name(); }
        };
    }
}
```
A type with a `valueOf(String)` or `fromString(String)` method, or a `String` constructor, works **without** a converter.

### Interceptors (around body reading and writing)
```java
@Provider
public class WhitespaceRemovingInterceptor implements ReaderInterceptor {   // also WriterInterceptor
    @Override
    public Object aroundReadFrom(ReaderInterceptorContext ctx) throws IOException {
        String body = new String(ctx.getInputStream().readAllBytes(), StandardCharsets.UTF_8);
        ctx.setInputStream(new ByteArrayInputStream(body.replaceAll("\\s", "").getBytes()));
        return ctx.proceed();
    }
}
```

### Filters
`ContainerRequestFilter` and `ContainerResponseFilter`. A filter is **post-matching** by default, which means it knows the matched resource method. With `@PreMatching` it runs before matching, and can even change the URI or method.
```java
@Provider
@PreMatching
public class GoblinKeyFilter implements ContainerRequestFilter {
    @Override
    public void filter(ContainerRequestContext ctx) {
        String key = ctx.getHeaderString("X-Goblin-Key");
        if (key == null) {
            ctx.abortWith(Response.status(Status.UNAUTHORIZED).build());
        } else if (rateLimiter.tooMany(key)) {
            ctx.abortWith(Response.status(Status.TOO_MANY_REQUESTS).header(HttpHeaders.RETRY_AFTER, 5).build());
        }
    }
}
```
**Request properties** pass data from the request filter to the response filter: `ctx.setProperty("request.id", id)`, then `requestCtx.getProperty("request.id")`.

### Applying a provider to selected methods only
**Name binding** is the JAX-RS counterpart of CDI interceptor bindings:
```java
@NameBinding
@Retention(RUNTIME) @Target({METHOD, TYPE})
public @interface Logged { }

@Logged @Provider
public class LoggingFilter implements ContainerRequestFilter, ContainerResponseFilter { ... }

@POST @Logged
public Response deposit(Hoard hoard) { ... }
```
**Dynamic feature:** this registers providers per method, using arbitrary logic:
```java
@Provider
public class LogGetters implements DynamicFeature {
    @Override
    public void configure(ResourceInfo resourceInfo, FeatureContext context) {
        if (resourceInfo.getResourceMethod().getName().startsWith("get")) {
            context.register(LoggingFilter.class);
        }
    }
}
```

## Asynchronous resources
**`AsyncResponse`:**
```java
@Resource ManagedExecutorService executor;     // or a plain ExecutorService in an @ApplicationScoped bean

@GET @Path("async/{id}")
public void getHoardAsync(@PathParam("id") long id, @Suspended AsyncResponse ar) {
    executor.submit(() -> {
        Hoard hoard = slowGoblinLookup(id);
        if (hoard != null) ar.resume(hoard);
        else               ar.resume(new NotFoundException());   // resume with an exception = error response
    });
}
```
**Returning `CompletionStage`:**
```java
@POST @Path("deeds")
@Consumes("application/pdf")
public CompletionStage<String> uploadDeed(File deed) {
    CompletableFuture<String> result = new CompletableFuture<>();
    executor.execute(() -> {
        try { result.complete(registerDeed(deed)); }
        catch (Exception e) { result.completeExceptionally(e); }
    });
    return result;
}
```

## Server-Sent Events
**To a single client:**
```java
@GET @Path("gold-price")
@Produces(MediaType.SERVER_SENT_EVENTS)
public void goldPrice(@Context SseEventSink sink, @Context Sse sse) {
    executor.submit(() -> {
        try (sink) {                                   // closing the sink ends the stream
            for (int i = 1; i <= 3; i++) {
                sink.send(sse.newEventBuilder()
                    .name("gold-price")
                    .id(String.valueOf(i))
                    .mediaType(MediaType.TEXT_PLAIN_TYPE)
                    .data(String.format("%.2f", currentGoldPrice()))
                    .build());
                Thread.sleep(500);
            }
        } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
    });
}
```
**Broadcasting to all registered clients:**
```java
private SseBroadcaster broadcaster;              // keep it in an @ApplicationScoped / @Singleton resource

@GET @Path("news")
@Produces(MediaType.SERVER_SENT_EVENTS)
public void subscribe(@Context SseEventSink sink, @Context Sse sse) {
    if (broadcaster == null) broadcaster = sse.newBroadcaster();
    broadcaster.register(sink);
    broadcaster.broadcast(sse.newEventBuilder().data("A new dragon joined DragonBank").build());
}
```
**Receiving in the browser:**
```javascript
const source = new EventSource("/api/hoards/gold-price");
source.addEventListener("gold-price", event => {
    document.getElementById("goldPrice").textContent = event.data;
});
```

## JAX-RS client API
```java
Client client = ClientBuilder.newBuilder()
    .connectTimeout(1, TimeUnit.SECONDS)
    .readTimeout(10, TimeUnit.SECONDS)
    .build();
WebTarget hoards = client.target("http://localhost:8080/dragonbank/api/hoards");

hoards.queryParam("dragon", "Ignatius").request().get(Hoard.class);
hoards.path("{id}").resolveTemplate("id", 42L).request().get(Hoard.class);
hoards.request().put(Entity.entity(hoard, MediaType.APPLICATION_JSON), Hoard.class);
hoards.request().get(new GenericType<List<Hoard>>() {});

// Asynchronous: Future
Future<Response> future = hoards.request().async().get();
try (Response response = future.get()) { ... }

// Asynchronous: callback
hoards.request().async().get(new InvocationCallback<String>() {
    @Override public void completed(String body) { ... }
    @Override public void failed(Throwable t)    { ... }
});

// Asynchronous: CompletionStage (rx)
hoards.path("deeds").request().rx()
    .post(Entity.entity(new FileInputStream(deedFile), "application/pdf"), String.class)
    .whenCompleteAsync((result, error) -> { ... });

client.close();
```
For the declarative MicroProfile REST Client (an interface plus `@RegisterRestClient`), see [Quarkus](Quarkus%20and%20MicroProfile.md).

---

## SOAP: JAX-WS
```java
@WebService                                    // works on a POJO or on a @Stateless EJB
public class GoblinLedgerService {
    @WebMethod                                 // optional: all public methods are exposed anyway
    public BigDecimal balance(long hoardNumber) { ... }
}
```
Client: generate the classes with `wsimport http://host/GoblinLedgerService?wsdl`, then inject the service:
```java
@WebServiceRef(wsdlLocation = "http://host/GoblinLedgerService?wsdl")
private GoblinLedgerService_Service ledgerService;
```
