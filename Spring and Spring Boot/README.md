Memos on the Spring Framework, Spring Boot, Spring Security and Spring Cloud. The examples use the same **DragonBank** domain as the [Java/Jakarta EE notes](../Java,%20Jakarta%20EE,%20Microprofile/README.md): dragons keep gold hoards, goblins do the paperwork, and knights cause trouble.

In the Spring notes we look at DragonBank's **back office**: the goblins' `appraisal-service`, `treasure-service` and `knight-watch-service`, written in Spring Boot. In the Quarkus notes, `hoard-service` calls these services.

When Spring uses a **Jakarta specification** (JPA, Bean Validation, Servlets, Jakarta annotations), the details of that specification are in the Jakarta notes. The Spring files only describe what Spring adds on top, and link there.

## Files
| File | Contents |
|---|---|
| [Spring core and Spring Boot](Spring%20core%20and%20Spring%20Boot.md) | Beans, DI, scopes, configuration, profiles, packaging, i18n |
| [Spring AOP](Spring%20AOP.md) | Aspects, pointcuts, advice |
| [JDBC in Spring](JDBC%20in%20Spring.md) | `JdbcTemplate`, `DataAccessException`, data source |
| [Spring Data JPA](Spring%20Data%20JPA.md) | Repositories and derived queries (JPA itself is in the Jakarta notes) |
| [Transactions in Spring](Transactions%20in%20Spring.md) | `@Transactional`, propagation, transaction managers |
| [Validation](Validation.md) | Bean Validation in Spring (the constraints themselves are in the Jakarta notes) |
| [Spring MVC](Spring%20MVC.md) | Server-side rendered web apps: controllers, model, views |
| [Thymeleaf](Thymeleaf.md) | Templates |
| [REST with Spring Boot](REST%20with%20Spring%20Boot.md) | REST controllers, error handling, HATEOAS, Spring Data REST, HTTP clients |
| [Spring Boot Actuator](Spring%20Boot%20Actuator.md) | Health and metrics |
| [Testing Spring applications](Testing%20Spring%20applications.md) | Spring test context, slices, MockMvc (JUnit/Mockito basics are in the Jakarta notes) |
| [Spring Security/Spring Boot Security](Spring%20Security/Spring%20Boot%20Security.md) | Filter chain, users, password encoders, method security |
| [Spring Security/Using OAuth2](Spring%20Security/Using%20OAuth2.md) | OAuth2/OIDC, Keycloak |
| [Spring Security/Self-signed SSL certificate](Spring%20Security/Self-signed%20SSL%20certificate.md) | HTTPS for local development |
| [Spring Cloud/Config Server](Spring%20Cloud/Config%20Server.md) | Centralized configuration |
| [Spring Cloud/Service discovery and load balancing](Spring%20Cloud/Service%20discovery%20and%20load%20balancing.md) | Eureka, `@LoadBalanced`, Feign |
| [Spring Cloud/API Gateway](Spring%20Cloud/API%20Gateway.md) | Routes, predicates, filters |
| [Spring Cloud/Resilience patterns](Spring%20Cloud/Resilience%20patterns.md) | Resilience4j |
| [Spring Cloud/Cloud Stream](Spring%20Cloud/Cloud%20Stream.md) | Messaging with Kafka |

## Spring and its Jakarta EE / MicroProfile / Quarkus counterparts
| Concern | Spring | Jakarta EE / MicroProfile / Quarkus |
|---|---|---|
| Dependency injection | `@Component`, `@Bean`, `@Autowired` | CDI: `@ApplicationScoped`, `@Produces`, `@Inject` |
| Cross-cutting code | Spring AOP `@Aspect` | CDI interceptors |
| Configuration | `application.properties`, `@Value`, `@ConfigurationProperties` | MP Config: `@ConfigProperty`, `@ConfigMapping` |
| Profiles | `application-dev.properties`, `@Profile` | `%dev.` prefix, `@IfBuildProfile` |
| REST server | Spring MVC `@RestController` | JAX-RS `@Path` (RESTEasy Reactive in Quarkus) |
| Declarative REST client | Feign, `@HttpExchange` | MP REST Client `@RegisterRestClient` |
| Reactive types | Reactor `Mono`/`Flux` | Mutiny `Uni`/`Multi` |
| Persistence | Spring Data JPA (on top of JPA) | JPA, Panache, Jakarta Data |
| Transactions | Spring `@Transactional` | JTA `@Transactional`, EJB `@TransactionAttribute` |
| Validation | Bean Validation + `@Validated` | Bean Validation |
| Health and metrics | Actuator, Micrometer | MP Health, MP Metrics or Micrometer |
| Fault tolerance | Resilience4j | MP Fault Tolerance |
| Messaging | Spring Cloud Stream | MP Reactive Messaging, JMS |
| Security | Spring Security | Jakarta Security, MP JWT, Quarkus OIDC |
| Server-side templates | Thymeleaf | JSF, Qute (Quarkus) |
| Tests | `@SpringBootTest`, `@MockitoBean` | `@QuarkusTest`, `@InjectMock` |

Quarkus also has **Spring compatibility extensions** (`quarkus-spring-di`, `quarkus-spring-web`, `quarkus-spring-data-jpa`, ...). They map a subset of the Spring annotations onto CDI, JAX-RS and Panache at build time.
