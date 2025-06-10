Dependencies
```
resilience4j-spring-boot2
resilience4j-circuitbreaker
resilience4j-timelimiter
spring-boot-starter-aop
```
Enabling
```Java
@CircuitBreaker(
	name = "circuitBreakerCatsService",
	fallbackMethod = "getFallbackCats"
)
@RateLimiter(
	name = "rateLimiterCatsService",
	fallbackMethod = "getFallbackCats"
)
@Bulkhead(
	name = "bulkheadCatsService",
	fallbackMethod = "getFallbackCats",
	type = Bulkhead.Type.THREADPOOL // by default using semaphore approach
)
@Retry(
	name = "retryCatsService",
	fallbackMethod = "getFallbackCats"
)
public List<Cat> getCatsByColoration (String coloration) { ... }
public List<Cat> getFallbackCats (String coloration, Throwable t) { ... }

```
###### Circuit breaker
Configuration:
```YAML
//Part of bootstrap.yml omitted for conciseness

resilience4j.circuitbreaker:
  instances:
    circuitBreakerCatsService:
      registerHealthIndicator: true
      ringBufferSizeInClosedState: 5
      ringBufferSizeInHalfOpenState: 3
      waitDurationInOpenState: 10s
      failureRateThreshold: 50
      recordExceptions:
        - org.springframework.web.client.HttpServerErrorException
        - java.io.IOException
        - java.util.concurrent.TimeoutException
        - org.springframework.web.client.ResourceAccessException

    circuitBreakerDogsService:
      registerHealthIndicator: true
      ringBufferSizeInClosedState: 6
      ringBufferSizeInHalfOpenState: 4
      waitDurationInOpenState: 20s
      failureRateThreshold: 60
```
###### Bulkheads
Configuration
```
resilience4j.bulkhead:
  instances:
    bulkHeadCatsService:
      maxWaitDuration: 10ms
      maxConcurrentCalls: 20

resilience4j.thread-pool-bulkhead:
  instances:
    bulkHeadCatsService:
      maxThreadPoolSize: 1
      coreThreadPoolSize: 1
      queueCapacity: 1
      keepAliveDuration: 20ms
```
###### Retry
Configuration:
```
resilience4j.retry:
  instances:
    retryCatsService:
      maxRetryAttempts: 5
      waitDuration: 10000
      retry-exceptions:
        - java.util.concurrent.TimeoutException
```
###### Rate limiter
Configuration:
```
resilience4j.ratelimiter:
  instances:
    limiterCatsService:
      timeoutDuration: 1000ms
      limitRefreshPeriod: 5000
      limitForPeriod: 5
```