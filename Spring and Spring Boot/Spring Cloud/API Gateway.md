Dependencies
```
spring-cloud-starter-gateway
```
Should also be an Eureka client.
Configuration:
```YAML
spring:
  cloud:
    gateway:
        discovery.locator:
          enabled: true
          lowerCaseServiceId: true
          
        # Manual rootes on top of those discovered automatically" 
        routes:
        - id: dogs-service
          uri: lb://dogs-service

          predicates:
          - Path=/dog/**

          filters:
          - RewritePath=/dog/
                       (?<path>.*), /$\{path}
```
###### Builtin predicates:
```YAML
Before=2020-03-11T...
After=2020-03-11T...
Between=2020-03-11T...,2020-04-11T...
Header=X-Request-Id, \d+
Host=**.example.com
Method=GET
Path=/organization/{id}
Query=id, 1
RemoteAddr=192.168.3.5/24
```
###### Builtin filter factories
```YAML
AddRequestHeader=X-Organization-ID,F39s2
AddResponseHeader=X-Organization-ID,F39s2
AddRequestParameter=X-Organization-ID,F39s2
PrefixPath=/api
RequestRateLimiter=10, 20, #{@userKeyResolver}
RedirectTo=302, http://localhost:8072
RemoveNonProxy
RemoveRequestHeader=X-Request-Foo
RemoveResponseHeader=X-Request-Foo
RewritePath=/organization/(?<path>.*), /$\{path}
SecureHeaders
SetPath=/{organization}
SetStatus=500
SetResponseHeader=X-Response-ID,123
```
###### Custom pre-filter
```Java
@Order(1)
@Component
public class TrackingFilter implements GlobalFilter {
	@Override
    public Mono<Void> filter(ServerWebExchange exchange,
                      GatewayFilterChain chain) {

       HttpHeaders requestHeaders = 
           exchange.getRequest().getHeaders();
       // ...
	   return chain.filter(exchange);
    }
}
```
For example, adding a custom header:
```Java
public ServerWebExchange setRequestHeader(ServerWebExchange exchange, String name, String value) { 
	return exchange.mutate().request( 
		exchange.getRequest().mutate() 
		.header(name, value) 
		.build()) 
	.build(); 
}
```
###### Custom post-filter
```Java
@Bean
public GlobalFilter postGlobalFilter() {
    return (exchange, chain) -> {
	    return chain.filter(exchange).then(
		    Mono.fromRunnable(() -> { ... })
		);
    };
}
```