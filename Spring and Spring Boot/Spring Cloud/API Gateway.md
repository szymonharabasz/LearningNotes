> **Compare:** MicroProfile and Quarkus have no gateway component. The usual choices are a Kubernetes Ingress or Gateway API, a service mesh (Istio), or a dedicated gateway (Kong, Envoy). Spring Cloud Gateway is a reactive app built on WebFlux and Reactor, which is why its filters work with `Mono` and `ServerWebExchange`.

Dependency: `spring-cloud-starter-gateway`. The gateway should also be a Eureka client, so that it can route to `lb://service-id`; see [Service discovery](Service%20discovery%20and%20load%20balancing.md).
```yaml
spring:
  cloud:
    gateway:
      discovery.locator:             # automatic routes: /treasure-service/** -> lb://treasure-service
        enabled: true
        lowerCaseServiceId: true
      routes:                        # manual routes, on top of the automatic ones
        - id: appraisal-service
          uri: lb://appraisal-service
          predicates:
            - Path=/appraisal/**
          filters:
            - RewritePath=/appraisal/(?<path>.*), /$\{path}
```

## Built-in predicates
```yaml
- After=2026-03-11T10:00:00+01:00[Europe/Warsaw]     # also Before, Between=...,...
- Header=X-Request-Id, \d+
- Host=**.dragonbank.example
- Method=GET
- Path=/hoard/{number}
- Query=dragon, Ign.*
- RemoteAddr=192.168.3.5/24
```

## Built-in filters
```yaml
- AddRequestHeader=X-Bank, DragonBank          # also AddResponseHeader, AddRequestParameter
- RemoveRequestHeader=X-Knight-Token           # also RemoveResponseHeader
- SetResponseHeader=X-Response-ID, 123
- PrefixPath=/api
- SetPath=/{segment}
- RewritePath=/hoard/(?<path>.*), /$\{path}
- RedirectTo=302, https://dragonbank.example
- SetStatus=500
- SecureHeaders
- RequestRateLimiter=10, 20, #{@dragonKeyResolver}   # replenish rate, burst capacity, key resolver bean (needs Redis)
```

## Custom global filters
A **pre-filter** runs before the request is routed:
```java
@Order(1)
@Component
public class CorrelationIdFilter implements GlobalFilter {
    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        HttpHeaders headers = exchange.getRequest().getHeaders();
        if (!headers.containsKey("X-Correlation-Id")) {
            exchange = exchange.mutate()                              // requests are immutable: mutate() makes a copy
                .request(exchange.getRequest().mutate().header("X-Correlation-Id", UUID.randomUUID().toString()).build())
                .build();
        }
        return chain.filter(exchange);
    }
}
```
A **post-filter** runs after the downstream response comes back:
```java
@Bean
GlobalFilter responseLogger() {
    return (exchange, chain) -> chain.filter(exchange)
        .then(Mono.fromRunnable(() -> log.info("Status {}", exchange.getResponse().getStatusCode())));
}
```
