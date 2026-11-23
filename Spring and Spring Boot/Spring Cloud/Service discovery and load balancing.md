> **Compare:**
> - **Quarkus** usually relies on **Kubernetes Services/DNS** for discovery, so the client just uses `http://appraisal-service`. Otherwise it uses **SmallRye Stork**, with `quarkus.rest-client.appraisal.url=stork://appraisal-service` plus a Stork discovery provider: Consul, Eureka, Kubernetes and others.
> - **Feign** is the Spring Cloud counterpart of the **MicroProfile REST Client**: an annotated interface with a generated implementation. Feign uses Spring MVC annotations where MicroProfile uses JAX-RS annotations. See [Quarkus - Calling other services](../../Java,%20Jakarta%20EE,%20Microprofile/Quarkus%20and%20MicroProfile.md#calling-other-services).

## Eureka server
Dependency: `spring-cloud-starter-netflix-eureka-server`. Old guides also tell you to exclude Ribbon (`spring-cloud-starter-ribbon`, `ribbon-eureka`) and set `spring.cloud.loadbalancer.ribbon.enabled=false`. Ribbon has since been replaced by Spring Cloud LoadBalancer.
```java
@EnableEurekaServer
@SpringBootApplication
public class EurekaServerApplication { ... }
```
```yaml
spring.application.name: eureka-server
server.port: 8070
eureka:
  instance.hostname: localhost
  client:
    registerWithEureka: false        # the server doesn't register with itself
    fetchRegistry: false
    serviceUrl.defaultZone: http://${eureka.instance.hostname}:${server.port}/eureka/
  server.waitTimeInMsWhenSyncEmpty: 5   # don't wait for peers at startup (dev only)
```
This configuration can itself come from the [Config Server](Config%20Server.md).

## Eureka client (each service)
Dependency: `spring-cloud-starter-netflix-eureka-client`. Being on the classpath is enough to register the service. `@EnableDiscoveryClient` is optional nowadays.
```properties
spring.application.name=appraisal-service          # becomes the service id
eureka.instance.preferIpAddress=true               # register the IP, not the hostname (useful in containers)
eureka.client.registerWithEureka=true
eureka.client.fetchRegistry=true
eureka.client.serviceUrl.defaultZone=http://localhost:8070/eureka/
```

## Calling discovered services
There are three ways, from the lowest level to the highest.

**1. `DiscoveryClient`** (you choose the instance yourself):
```java
@Autowired DiscoveryClient discovery;

List<ServiceInstance> instances = discovery.getInstances("treasure-service");
String baseUri = instances.get(0).getUri().toString();
```
**2. A load-balanced `RestTemplate`/`WebClient.Builder`.** Use the service id as the host name:
```java
@Bean @LoadBalanced
RestTemplate restTemplate() { return new RestTemplate(); }

restTemplate.getForObject("http://treasure-service/v1/treasures/{id}", Treasure.class, id);
```
**3. A Feign client:**
```java
@SpringBootApplication
@EnableFeignClients
public class AppraisalServiceApplication { ... }

@FeignClient("treasure-service")                   // service id, resolved through discovery
public interface TreasureClient {
    @GetMapping(value = "/v1/treasures/{id}", consumes = "application/json")
    Treasure getTreasure(@PathVariable("id") long id);
}
```
Inject `TreasureClient` and call it. Spring 6 offers a similar built-in option without Feign: `@HttpExchange` interfaces.
