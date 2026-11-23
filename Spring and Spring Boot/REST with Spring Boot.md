> **Compare:** the Jakarta counterpart is JAX-RS ([Web services](../Java,%20Jakarta%20EE,%20Microprofile/Web%20services%20-%20JAX-RS%20and%20JAX-WS.md)), which Quarkus implements with RESTEasy Reactive ([Quarkus](../Java,%20Jakarta%20EE,%20Microprofile/Quarkus%20and%20MicroProfile.md#rest-endpoints-resteasy-reactive)). JSON is handled by **Jackson** in Spring. In Jakarta EE it is JSON-B ([Serialization](../Java,%20Jakarta%20EE,%20Microprofile/Serialization%20and%20deserialization%20of%20XML%20and%20JSON.md)), and Quarkus lets you choose either. Request mapping basics (`@GetMapping`, `@PathVariable`, ...) are in [Spring MVC](Spring%20MVC.md).

| Spring | JAX-RS |
|---|---|
| `@RestController` + `@RequestMapping("/x")` | `@Path("/x")` on the class |
| `@GetMapping`, `@PostMapping`, ... | `@GET`, `@POST`, ... + `@Path` |
| `produces`/`consumes` attributes | `@Produces` / `@Consumes` |
| `@RequestBody` parameter | unannotated entity parameter |
| `ResponseEntity<T>` | `Response` |
| `@RestControllerAdvice` + `@ExceptionHandler` | `ExceptionMapper` / `@ServerExceptionMapper` |
| `@ResponseStatus` | (no direct equivalent: return a `Response` or throw `WebApplicationException`) |

## Controllers
```java
@RestController                               // in a plain @Controller each method would need @ResponseBody
@RequestMapping("/appraisals")
public class AppraisalController {

    @GetMapping
    List<Appraisal> all() { ... }

    @GetMapping(path = "/{id}", produces = { "application/json", "application/xml" })
    Appraisal one(@PathVariable long id) { ... }

    @PostMapping(consumes = "application/json")
    ResponseEntity<Appraisal> create(@RequestHeader("X-Request-Id") String requestId,
                                     @Valid @RequestBody AppraisalRequest request) {
        Appraisal a = service.create(request);
        URI location = ServletUriComponentsBuilder.fromCurrentRequestUri()
            .path("/{id}").buildAndExpand(a.id()).toUri();
        return ResponseEntity.created(location).body(a);          // 201 + Location header
    }

    @PutMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)                        // 204 for a void method
    void update(@PathVariable long id, @RequestBody AppraisalRequest request) { ... }
}
```
**`ResponseEntity`:**
```java
return ResponseEntity.status(HttpStatus.ACCEPTED)     // or .ok(), .badRequest(), .notFound(), .noContent()
    .header("X-Goblin-Mood", "grumpy")
    .body(appraisal);
```
**XML:** add `jackson-dataformat-xml`. The client then chooses the format with `Accept: application/xml`.

## Error handling
```java
@RestControllerAdvice                                  // global; an @ExceptionHandler in a controller works only for that controller
public class AppraisalErrors {

    @ExceptionHandler(TreasureNotFoundException.class)
    public ResponseEntity<ErrorDetails> notFound(TreasureNotFoundException ex) {   // the exception parameter is optional
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(new ErrorDetails(ex.getMessage()));
    }

    @ResponseStatus(HttpStatus.CONFLICT)
    @ExceptionHandler(DataIntegrityViolationException.class)
    public void duplicate(Exception ex) { log.error("Treasure already appraised", ex); }
}
```
Spring 6 also supports **RFC 7807 Problem Details** (`ProblemDetail`, `ErrorResponseException`, `spring.mvc.problemdetails.enabled=true`).

## Spring HATEOAS
Add links to the representations:
```java
class Appraisal extends RepresentationModel<Appraisal> { ... }

appraisal.add(
    linkTo(methodOn(AppraisalController.class).one(appraisal.getId())).withSelfRel(),
    linkTo(methodOn(AppraisalController.class).create(null, null)).withRel("create"));
return ResponseEntity.ok(appraisal);
```
A **model assembler** keeps the link building out of the controller:
```java
@Component
class AppraisalModelAssembler implements RepresentationModelAssembler<Appraisal, EntityModel<Appraisal>> {
    @Override
    public EntityModel<Appraisal> toModel(Appraisal a) {
        return EntityModel.of(a,
            linkTo(methodOn(AppraisalController.class).one(a.getId())).withSelfRel(),
            linkTo(methodOn(AppraisalController.class).all()).withRel("appraisals"));
    }
}
// in the controller: return assembler.toModel(appraisal);
```
> **Compare:** JAX-RS has only basic `Link` support (`Response.links(...)`, `Link.fromUri(...)`). There is no equivalent of `methodOn` link building.

## Spring Data REST
`spring-boot-starter-data-rest` exposes Spring Data repositories ([Spring Data JPA](Spring%20Data%20JPA.md)) as HAL/REST resources, with no controller:
```properties
spring.data.rest.base-path=/api
```
```java
@RepositoryRestResource(path = "treasures")
public interface TreasureRepository extends JpaRepository<Treasure, Long> {
    List<Treasure> findByType(@Param("type") TreasureType type);    // GET /api/treasures/search/findByType?type=GEM
}
```
Quarkus counterpart: the REST Data with Panache extensions generate CRUD endpoints from Panache entities or repositories.

---

## Calling other services
> **Compare:** the declarative style (an interface plus annotations) corresponds to the **MicroProfile REST Client**; see [Quarkus](../Java,%20Jakarta%20EE,%20Microprofile/Quarkus%20and%20MicroProfile.md#calling-other-services). In Spring that is a `@HttpExchange` interface (Spring 6), or Feign ([Service discovery](Spring%20Cloud/Service%20discovery%20and%20load%20balancing.md)). `WebClient` corresponds to the Vert.x Web Client, with Reactor `Mono`/`Flux` in place of Mutiny `Uni`/`Multi`.

### `RestTemplate` (synchronous, in maintenance mode)
Spring 6.1+ recommends `RestClient` (fluent and synchronous) or `WebClient` instead. Create the template with `new RestTemplate()` or with Boot's injectable `RestTemplateBuilder`:
```java
this.rest = restTemplateBuilder.build();

Treasure t = rest.getForObject(url + "/treasures/{id}", Treasure.class, 42);
ResponseEntity<Treasure> e = rest.getForEntity(url + "/treasures/{id}", Treasure.class, 42);
e.getStatusCode(); e.getHeaders(); e.getBody();
// also: postForObject, postForLocation, put, patchForObject, delete, headForHeaders, optionsForAllow

// Full control: exchange()
HttpHeaders headers = new HttpHeaders();
headers.add("X-Request-Id", UUID.randomUUID().toString());
ResponseEntity<Appraisal> response = rest.exchange(url + "/appraisals", HttpMethod.POST,
    new HttpEntity<>(request, headers), Appraisal.class);

RequestEntity<AppraisalRequest> req = RequestEntity.post(URI.create(url + "/appraisals"))
    .header(HttpHeaders.AUTHORIZATION, "Basic " + credentials)
    .contentType(MediaType.APPLICATION_JSON)
    .body(request);
rest.exchange(req, Void.class);
```
**Client interceptor**, for example to propagate a correlation id:
```java
public class CorrelationIdInterceptor implements ClientHttpRequestInterceptor {
    @Override
    public ClientHttpResponse intercept(HttpRequest request, byte[] body, ClientHttpRequestExecution execution)
            throws IOException {
        request.getHeaders().add("X-Correlation-Id", CorrelationContext.current());
        return execution.execute(request, body);
    }
}

@Bean
RestTemplate restTemplate() {
    RestTemplate template = new RestTemplate();
    template.getInterceptors().add(new CorrelationIdInterceptor());    // getInterceptors() returns a live, mutable list
    return template;
}
```
Compare: `ClientRequestFilter` in the JAX-RS / MicroProfile REST Client.

### `WebClient` (reactive, from Spring WebFlux)
```java
@Bean WebClient webClient(WebClient.Builder builder) { return builder.baseUrl(hoardServiceUrl).build(); }

public Mono<Appraisal> requestAppraisal(String requestId, AppraisalRequest request) {
    return webClient.post()
        .uri("/appraisals")
        .header("X-Request-Id", requestId)
        .bodyValue(request)                       // or .body(Mono.just(request), AppraisalRequest.class)
        .retrieve()                               // 4xx/5xx become WebClientResponseException
        .bodyToMono(Appraisal.class);             // bodyToFlux for streams
}
```
