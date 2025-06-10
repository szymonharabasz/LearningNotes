Create an application with
```Java
@EnableConfigServer
@SpringBootApplicatio
public class ConfigServerApplication { ... }
```
In the `bootstrap.[properties|yml]`:
```
spring.profiles.active=native,git
spring.cloud.config.server.native.search-locations=
	file:///{FILE_PATH},file:///Users/szymon,classpath:/config
spring.cloud.config.server.git.uri=https://github.com/myusername/config.git
spring.cloud.config.server.git.searchPaths=catsservice
```
where `native` is the name of the profile, this one is necessary for the configuration stored in the filesystem.
In `spring.profiles.active` the last is the winner.
Configuration files have names:
```
cats-service.env.[properties|yms]
```
Can be accessed through:
```
http://config-server:port/cats-service/[default|env]
```
Properties come from `default` unless they are overriden by a specific environment.

In the client service we need to add dependency to `pom.xml`:
```
spring-cloud-starter-config
```
In the `bootstrap.[properties|yml` of the service:
```
spring.application.name=cats-service
spring.profiles.active=dev
spring.cloud.config.uri=http://localhost:8071
```
They can be overriden at startup, for example:
```sh
java -Dspring.profiles.active=prod -jar target/cats-service-0.0.1-SNAPSHOT.jar
```
They can also be overriden with environment variables, for example in `docker-compose.yml`:
```YAML
cats-service:
	environment:
		SPRING_PROFILES_ACTIVE: "stagging"
```
The annotation from Spring Boot Actuator:
```Java
@RefreshScope
@SpringBootApplication
publicClass CarServiceApplication { ... }
```
Exposes the `/refresh` endpoint that can be used to refresh **custom** Spring properties.

If a property `encrypt.key` is defined in the Config Server, perhaps as the environment variable `ENCRYPT_KEY`, additional POST endpoints are exposed: `/encrypt` and `/decrypt`. The first one can then be used to encrypt sensitive information. Then it can be used in the property file as:
```
spring.datasource.password=[cipher]<ENCRYPTED PASSWORD>
```