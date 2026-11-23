The Jakarta counterpart is described in [CDI](../Java,%20Jakarta%20EE,%20Microprofile/Context%20and%20Dependency%20Injection.md), and configuration in [Quarkus and MicroProfile](../Java,%20Jakarta%20EE,%20Microprofile/Quarkus%20and%20MicroProfile.md#configuration).

## Application class
```java
@SpringBootApplication          // = @SpringBootConfiguration (a @Configuration) + @EnableAutoConfiguration + @ComponentScan
public class AppraisalServiceApplication {
    public static void main(String[] args) { SpringApplication.run(AppraisalServiceApplication.class, args); }
}

@EnableAutoConfiguration(exclude = DataSourceAutoConfiguration.class)   // switch off part of the auto-configuration
// or in properties: spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration
```
`@ComponentScan` scans the package of the application class and its sub-packages, so put the application class in the root package.

> **Compare:** Quarkus has no application class and no runtime classpath scanning. Beans are discovered **at build time** from the Jandex index, and "auto-configuration" is done by extensions at build time. The equivalent of excluding an auto-configuration is simply not adding the extension, or a property such as `quarkus.datasource.devservices.enabled=false`.

## Beans and dependency injection
```java
@Service                                       // also @Component, @Repository (adds exception translation), @Controller
public class AppraisalService {
    private final TreasureRepository treasures;
    public AppraisalService(TreasureRepository treasures) {   // a single constructor needs no @Autowired
        this.treasures = treasures;
    }
}

@Configuration
public class ClockConfig {
    @Bean(initMethod = "warmUp", destroyMethod = "shutdown")  // alternative to @PostConstruct/@PreDestroy
    GoblinAbacus abacus() { return new GoblinAbacus(); }
}
```
- When there are several candidates: `@Qualifier("fireproof")`, or `@Primary` on the preferred bean.
- Spring also understands the JSR-330/Jakarta annotations `@Inject` and `@Named`, and the Jakarta Annotations `@PostConstruct` and `@PreDestroy`.

> **Compare with CDI:**
> - `@Component` corresponds to a CDI bean with a bean-defining annotation. `@Bean` methods correspond to `@Produces` methods.
> - `@Qualifier("name")` is **string-based** (custom qualifier annotations work too). CDI qualifiers are type-safe annotations.
> - `@Primary` is roughly a CDI `@Alternative` with `@Priority`. Quarkus also has `@DefaultBean`, a bean that is used only if no other bean of that type exists.
> - Spring singletons are created **eagerly at startup** (unless `@Lazy`) and injected directly. CDI `@ApplicationScoped` beans are created **lazily** and injected through a client proxy.

### Scopes
| Spring | CDI counterpart |
|---|---|
| singleton (default) | `@ApplicationScoped` (but lazy and proxied) or `@Singleton` (no proxy) |
| `@Scope("prototype")` | `@Dependent` (the CDI default) |
| `@RequestScope` | `@RequestScoped` |
| `@SessionScope` | `@SessionScoped` |
| `@ApplicationScope` (per `ServletContext`) | `@ApplicationScoped` |

## Configuration
```properties
appraisal.goblin-commission=0.1
server.port=8081
server.servlet.session.timeout=5m
logging.level.root=WARN                      # TRACE, DEBUG, INFO, WARN, ERROR, OFF
logging.level.com.dragonbank=DEBUG
```
```java
@Value("${appraisal.goblin-commission:0.05}")   // ":" introduces the default value
BigDecimal commission;

@ConfigurationProperties(prefix = "appraisal")  // type-safe group; enabled via @ConfigurationPropertiesScan or @EnableConfigurationProperties
public record AppraisalProperties(BigDecimal goblinCommission, Duration timeout) { }
```
**Profiles:** `application-dev.properties` overrides `application.properties` when the `dev` profile is active. Activate it with `spring.profiles.active=dev`, `-Dspring.profiles.active=dev` or `SPRING_PROFILES_ACTIVE=dev`. Beans can be restricted with `@Profile("dev")`.

> **Compare with MicroProfile Config / Quarkus:**
> - `@Value` corresponds to `@ConfigProperty`. `@ConfigurationProperties` corresponds to `@ConfigMapping` or `@ConfigProperties`.
> - The ordering is similar in both: system properties, then environment variables, then `application.properties`. Relaxed binding of env vars is also similar (`APPRAISAL_GOBLIN_COMMISSION`).
> - Profiles: Quarkus prefers a `%dev.` prefix in a single file, although `application-dev.properties` works too. It selects them with `quarkus.profile`. `@Profile` corresponds to `@IfBuildProfile` (decided at build time) or `@LookupIfProperty`.

## Internationalization
```java
@Bean
public LocaleResolver localeResolver() {
    SessionLocaleResolver resolver = new SessionLocaleResolver();
    resolver.setDefaultLocale(Locale.US);
    return resolver;
}

@Bean
public ResourceBundleMessageSource messageSource() {
    ResourceBundleMessageSource source = new ResourceBundleMessageSource();
    source.setBasenames("messages");              // messages.properties, messages_en.properties, messages_pl.properties
    source.setUseCodeAsDefaultMessage(true);      // show the key if a translation is missing
    return source;
}
```
```properties
# messages_en.properties
appraisal.done=Treasure {0} appraised at {1} gold coins
```
```java
@GetMapping("/appraisals/{id}")
public String describe(@PathVariable long id,
                       @RequestHeader(value = "Accept-Language", required = false) Locale locale) {
    return messageSource.getMessage("appraisal.done", new Object[]{ id, value }, locale);   // a null locale means the server default
}
```

## Running and packaging
```java
@Bean
CommandLineRunner countTreasures(JdbcTemplate jdbc) {    // runs once after startup
    return args -> System.out.println(jdbc.queryForObject("SELECT COUNT(*) FROM treasure", Long.class));
}
```
- **Executable "uber" JAR:** Maven `spring-boot-maven-plugin` + `mvn package`. Gradle: `gradle bootJar` (also run by `assemble`/`build`).
- **`spring-boot-devtools`** (runtime scope, dev only) gives automatic restarts and LiveReload. Compare with `mvn quarkus:dev`.
- **WAR deployed to an external servlet container**, where `main()` is not called:
```java
@SpringBootApplication
public class AppraisalServiceApplication extends SpringBootServletInitializer {
    @Override
    protected SpringApplicationBuilder configure(SpringApplicationBuilder app) {
        return app.sources(AppraisalServiceApplication.class);
    }
    // keep main() as well to get a "hybrid" WAR that also runs with java -jar
}
```
