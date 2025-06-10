**Returning JSON** (thanks to Jackson):  
```Java
@GetMapping("users")  
@ResponseBody  
List<User> …  
      
@GetMapping("user/{id}")  
@ResponseBody  
User getUser(@PathVariable("id") int id)
```
In `@Controller` one does need `@ResponseBody`, in `@RestController` not
Response entities:  
```Java
@GetMapping("/france")  
public ResponseEntity<Country> france() {  
    Country c = new Country("France", 67);  
    return ResponseEntity  
        .status(HttpStatus.ACCEPTED) // or e.g., .ok()  
        .header("continent", "Europe")  
        .header("capital", "Paris")  
        .body(c);  
}
```
Proper setting for POST requests:  
```Java
URI location = ServletUriComponentsBuilder  
    .fromCurrentRequestUri()  
    .path("/{itemId}")  
    .buildAndExpand(item.id())  
    .toUri();  
return ResponseEntity.creasted(location).build;
```
Response status (method annotation):  
```Java
@PutMapping("/store/order/{id}")  
@ResponseStatus(HttpStatus.NO_CONTENT) // 204  
public void …
```
Controller advices:  
```Java
@RestControllerAdvice  
public class ExceptionControllerAdvice {  
    @ExceptionHandler(NotEnoughMoneyException.class)  
    public ResponseEntity<ErrorDetails> exceptionNotEnoughMoneyHandler() {  
        ErrorDetails errorDetails = new ErrorDetails();  
        errorDetails.setMessage("Not enough money to make a payment.");  
        return ResponeEntity.badRequest().body(errorDetails);  
    }  
}  
```
One can also add an exception instance as a method argument
Instead of `status(..)` one can use:
```Java
badRequest()
```
**Exchanging XML.** Add `jackson-dataformat-xml` in `pom.xml`
Set header `Accept: application/xml` in the request
One can set `@GetMapping(path="user", produces={"application/xml"})`
```Java
@PostMapping("user", consumes={"application/json"})  
User addUser(@RequestHeader String requestId, @RequestBody User user)
```
Standard (but soon deprecated) way of consuming REST API:
Create `S` as a `@Bean`. Inject it and use:  
```Java
String uri = paymentsServiceUri + "/payment";  
HttpHeaders headers = new HttpHeaders();  
headers.add("requestId", UUID.randomUUID().toString());  
HttpEntity<Payment> entity = new HttpEntity<>(payment, headers);  
ResponseEntity<Payment> response = rest.exchange(uit,  
    HttpMethod.POST,  
    entity,  
    Payment.class);  
return response.getBody();
```
New way: crete RestTemplate
- With new operator
- (In Spring Boot) with `RestTemplateBuilder`, that can be injected:  
```Java
this.restTemplate = restTemplateBuilder.build()
```
Methods that can be used include for example:
```Java
delete(String uri, Object… urlVariables)
getForObject(String uri, Class<T> responseType, Object… uriVariables)
headForHeaders(String uri, Object… uriVariables)
optionsForAllow(String uri, Object… uriVariables)
postForLocation(String uri, Object request, Object… uriVariables)
postForObject(String uri, Object request, Class<T> uriVariables, Object… uriVariables)
put(String uri, Object request, Object… uriVariables)
patchForObject(String uri, Object request, Class<T> responseType, Object… uriVariables)
ResponseEntity<Order> entity = rest.getForEntity(...) // and similar for other verbs
entity.getStatusCode()  
entity.getHeaders()  
entity.getBody()
```
```Java
RequestEntity<OrderItem> request = RequestEntity  
    .post(new URI(itemUri))  
    .getHeaders().add(HttpHeaders.AUTHORIZATION, "Basic " + getLoginData())  
    .contentType(MediaType.APPLICATION_JSON)  
    .body(newItem);  
ResponseEntity<Void> reponse = rest.exchange(request, Void.class);
```
Handling exceptions:  
```Java
@ResponseStatus(HttpStatus.CONFLICT)  
@ExceptionHandler({ DataIntegrityViolationException.class })  
public void accountAlreadyExists(Exception ex) {  
    logger.error("Exception is: ", ex);  
}
```
**Spring Data REST.** Add dependency to `spring-boot-starter-data-rest`. Configure `spring.data.rest.basePath=/api`. To enable path queries:
```Java
@RepositoryRestResource
Public interface CarRepository extends PagingAndSortingRepository<Car, Long> {
    List<Car> findByBrand(@Param("brand") String brand);
```
Internationalizing messages. Start with defining a default `Locale`:
```Java
@Bean
public LocaleResolver localeResolver() {
	SessionLocaleResolver localeResolver = new SessionLocaleResolver();
	localeResolver.setDefaultLocale(Locale.US);
	return localeResolver;
}
```
Define a message source bean:
```Java
@Bean
public ResourceBundleMessageSource messageSource() {
	ResourceBundleMessageSource messageSource = 
		new ResourceBundleMessageSource();
	messageSource.setUseCodeAsDefaultMessage(true);
	messageSource.setBasenames("messages");
	return messaeSource;
}
```
The defines base name(s) translate to the property files in `src/main/resources` of the names like:
```
messages_en.properties
messages_it.properties
messages.properties
```
The content can be like:
```yaml
license.create.message = License created %s
license.update.message = License %s updated
license.delete.message = Deleting license with id %s for the organization %s
```
and similarly for other languages. The messages are retrieved like this:
```Java
@Autowired
MessageSource messageSource;
// ...
messages.getMessage("license.create.message", null, locale);
```
where `Locale locale` can be injected to a given parent method and `null` results in using a default `Locale`. Then it will be defined by the location of the backend server. To get it from the client, it can be injected from a HTTP header:
```Java
@RequestHeader("value = "Accept-Language", required = false) Locale locale
```
**Spring HATEOAS**
Extend `RepresentationModel` by a model class:
```Java
class License extends RepresentationModel<License> { ... }
```
Enhance the output (JSON) representation:
```Java
	license.add(
			linkTo(methodOn(LicenseConteoller.class)
			.getLicense(organizationId, license.getLicenseId()))
			.withSelfRel(),
			linkTo(methodOn(LicenseConteoller.class)
			.createLicense(organizationId, license, null))
			.withRel("createLicense"),
			...
			);
	return ResponseEntity.ok(license);
```
###### REST interceptor
Defining:
```Java
public class UserContextInterceptor implements ClientHttpRequestInterceptor {
    @Override
    public ClientHttpResponse intercept(
	    HttpRequest request, byte[] body, 
	    ClientHttpRequestExecution execution) throws IOException {
        // ...
        return execution.execute(request, body);
     }
}
```
Adding to a customized REST template
```Java
@Bean
public RestTemplate getRestTemplate(){
	RestTemplate template = new RestTemplate();
	List interceptors = template.getInterceptors();
    if (interceptors==null) {
	    template.setInterceptors(Collections.singletonList(
	        new UserContextInterceptor()));
	}else{
	    interceptors.add(new UserContextInterceptor());
	    template.setInterceptors(interceptors);
	}
	return template;
}‘
```