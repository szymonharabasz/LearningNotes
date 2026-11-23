> **Compare:** MicroProfile Config ([Quarkus - Configuration](../../Java,%20Jakarta%20EE,%20Microprofile/Quarkus%20and%20MicroProfile.md#configuration)) has no config *server*. Its answer is a pluggable `ConfigSource`. In practice Quarkus apps read Kubernetes ConfigMaps and Secrets (ordinal 270), and there is also a `quarkus-spring-cloud-config-client` extension that reads from a Spring Config Server. Spring profiles in `{application}-{profile}.properties` correspond to the `%profile.` prefixes. `@RefreshScope` has no MicroProfile equivalent, because MP Config values are read at injection time. Inject `Provider<T>` or `ConfigValue` to re-read them.

## Server
Dependency: `spring-cloud-config-server`.
```java
@EnableConfigServer
@SpringBootApplication
public class ConfigServerApplication { ... }
```
```properties
server.port=8071
spring.profiles.active=native,git                 # backends; "native" = filesystem/classpath. With several, the LAST one wins
spring.cloud.config.server.native.search-locations=classpath:/config,file:///opt/dragonbank/config
spring.cloud.config.server.git.uri=https://github.com/dragonbank/config.git
spring.cloud.config.server.git.search-paths=appraisal-service
```
Files are named `{application}-{profile}.properties` (or `.yml`), for example `appraisal-service-dev.yml`. The server serves them at:
```
http://config-server:8071/appraisal-service/default
http://config-server:8071/appraisal-service/dev
```
A profile's values override those in `default`.

## Client
Dependency: `spring-cloud-starter-config`.
```properties
spring.application.name=appraisal-service
spring.profiles.active=dev
spring.config.import=optional:configserver:http://localhost:8071   # Boot 2.4+; older: spring.cloud.config.uri in bootstrap.properties
```
Override these at startup with `java -Dspring.profiles.active=prod -jar appraisal-service.jar`, or with environment variables (for example in `docker-compose.yml`):
```yaml
appraisal-service:
  environment:
    SPRING_PROFILES_ACTIVE: "staging"
```

## Refreshing at runtime
```java
@RefreshScope          // Spring Cloud Context: the bean is re-created when the configuration is refreshed
@Component
public class CommissionSettings { @Value("${appraisal.goblin-commission}") BigDecimal commission; }
```
`POST /actuator/refresh` (which must be exposed through Actuator) reloads the configuration and re-creates `@RefreshScope` beans. This refreshes your **custom** properties; infrastructure like the data source is not rebuilt.

## Encrypted values
If the server has `encrypt.key` set (for example through the environment variable `ENCRYPT_KEY`), it exposes `POST /encrypt` and `POST /decrypt`. Encrypted values are stored with a prefix and decrypted by the server:
```properties
spring.datasource.password={cipher}d1a9f7c3...
```
