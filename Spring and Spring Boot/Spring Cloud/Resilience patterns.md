> **Compare with MicroProfile Fault Tolerance** ([Quarkus - Fault tolerance](../../Java,%20Jakarta%20EE,%20Microprofile/Quarkus%20and%20MicroProfile.md#fault-tolerance)):
> - **Where the parameters live.** In MicroProfile the parameters are attributes of the annotation, and you can override them in config (`Class/method/Retry/maxRetries`). In Resilience4j the annotation only names an **instance**, and all parameters go in `application.yml`. Several methods can share one instance.
> - **Fallback signature.** MicroProfile: the same parameters as the original method. Resilience4j: the same parameters **plus a `Throwable`** at the end.
> - **Rate limiter.** MicroProfile FT has none; SmallRye adds `@RateLimit`. Resilience4j has `@RateLimiter`.
> - **Time limiter.** `@TimeLimiter` corresponds to `@Timeout`, but Resilience4j's applies only to async methods (`CompletableFuture`).
> - **Order.** Resilience4j applies the decorators in a fixed order: `Retry( CircuitBreaker( RateLimiter( TimeLimiter( Bulkhead( method ) ) ) ) )`. This means each retry passes through the circuit breaker.

Dependencies: `resilience4j-spring-boot3` (formerly `resilience4j-spring-boot2`) plus `spring-boot-starter-aop`, or the `spring-cloud-starter-circuitbreaker-resilience4j` starter.

## Annotations
Every annotation names an instance; the instance names must match the YAML below:
```java
@CircuitBreaker(name = "treasureService", fallbackMethod = "lastKnownTreasures")
@RateLimiter(name = "treasureService", fallbackMethod = "lastKnownTreasures")
@Bulkhead(name = "treasureService", fallbackMethod = "lastKnownTreasures",
          type = Bulkhead.Type.THREADPOOL)          // default SEMAPHORE; THREADPOOL needs a CompletableFuture return type
@Retry(name = "treasureService", fallbackMethod = "lastKnownTreasures")
public List<Treasure> treasuresOf(String dragon) { ... }

public List<Treasure> lastKnownTreasures(String dragon, Throwable t) { ... }   // the original parameters + Throwable
```
Like `@Transactional`, these work through an AOP proxy, so self-invocation is not protected.

## Configuration
```yaml
resilience4j.circuitbreaker:
  instances:
    treasureService:
      registerHealthIndicator: true                 # circuit breaker state shown in /actuator/health
      slidingWindowSize: 5                          # older name: ringBufferSizeInClosedState
      permittedNumberOfCallsInHalfOpenState: 3      # older name: ringBufferSizeInHalfOpenState
      waitDurationInOpenState: 10s
      failureRateThreshold: 50                      # percent
      recordExceptions:
        - org.springframework.web.client.HttpServerErrorException
        - org.springframework.web.client.ResourceAccessException
        - java.io.IOException
        - java.util.concurrent.TimeoutException

resilience4j.bulkhead:                              # semaphore bulkhead
  instances:
    treasureService:
      maxConcurrentCalls: 20
      maxWaitDuration: 10ms

resilience4j.thread-pool-bulkhead:
  instances:
    treasureService:
      coreThreadPoolSize: 1
      maxThreadPoolSize: 1
      queueCapacity: 1
      keepAliveDuration: 20ms

resilience4j.retry:
  instances:
    treasureService:
      maxAttempts: 5                                # includes the first call; older name: maxRetryAttempts
      waitDuration: 10s
      retryExceptions:
        - java.util.concurrent.TimeoutException

resilience4j.ratelimiter:
  instances:
    treasureService:
      limitForPeriod: 5                             # 5 calls...
      limitRefreshPeriod: 5s                        # ...per 5 s
      timeoutDuration: 1s                           # how long a call waits for permission
```
`configs.default` applies to all instances, and an instance can name a base config with `baseConfig: ...`.
