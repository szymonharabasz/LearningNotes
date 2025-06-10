#### For the server
Add the dependency:
```
spring-cloud-starter-netflix-eureka-server
```
Exclude the dependency:
```
spring-cloud-starter-ribbon
ribbon-eureka
```
Basic local config:
```YAML
spring:
   application:
      name: eureka-server
   cloud:
      config: 
         uri: http://localhost:8071

      loadbalancer:
         ribbon:
            enabled: false
```
Config to be loaded from the config server:
```YAML
server:
   port: 8070
eureka:
   instance:
      hostname: localhost
   client:
      registerWithEureka: false
      fetchRegistry: false
      serviceUrl:
         defaultZone:
            http://${eureka.instance.hostname}:${server.port}/eureka/
   server:
      waitTimeInMsWhenSyncEmpty: 5
```
Enabling the server feature:
```Java
@EnableEurekaServer
@SpringBootApplicatio
public class EurekaServerApplication { ... }
```
#### For the client
Add the dependency
```
spring-cloud-starter-netflix-eureka-client
```
Set the properties for the service:
```
eureka.instance.preferIpAddress = true
eureka.client.registerWithEureka = true
eureka.client.fetchRegistry = true
eureka.client.serviceUrl.defaultZone = http://localhost:8070/eureka/
```
###### Discovery client
Enable discovery client:
```Java
@SpringBootApplication
@EnableDiscoveryClient
```
Inject and use it:
```Java
@Autowired
DiscoveryClient dicovery
// ...
List<ServiceInstance> instances = discovery.getInstances("cats-service");
String serverUri = instances.get(0).getUri().toString();
```
###### Enhanced REST template
```Java
@LoadBalanced
@Bean
public RestTemplate getRestTemplate() {
	return new RestTemplate();
}
```
Inject it and use as usual, but provide service ID as a server hostname.
###### Netflix Feign client
Enable Feign client
```Java
@SpringBootApplication
@EnableFeignClients
```
Define an annotated interface which mirrors a REST service:
```Java
@FeignClient("cats-service")
public interface CatsFeignClient {
	@RequestMapping(
		method = RequestMethod.GET,
		value = "/v1/cats/{catId}",
		consumes = "application/json"
	)
	Cat getCat(@PathVariable("catId") String catId);
}
```
Inject the interface and call its methods.