> **Compare:** the MicroProfile/Quarkus counterparts (MP Health, MP Metrics or Micrometer, tracing) are in [Quarkus - Observability](../Java,%20Jakarta%20EE,%20Microprofile/Quarkus%20and%20MicroProfile.md#observability).
> - A `HealthIndicator` corresponds to an MP `HealthCheck`.
> - `/actuator/health/liveness` and `/actuator/health/readiness` correspond to `/q/health/live` and `/q/health/ready`.
> - Metrics: **Micrometer is the same library in both**, so the `MeterRegistry` code below also works in Quarkus with `quarkus-micrometer`.
> - Tracing: Spring Cloud Sleuth was replaced by **Micrometer Tracing** in Boot 3. Quarkus uses OpenTelemetry.

Dependency: `spring-boot-starter-actuator`.
```properties
management.endpoints.web.exposure.include=health,info,metrics,prometheus   # only health is exposed over HTTP by default
management.endpoint.health.show-details=when-authorized
management.endpoint.health.probes.enabled=true                             # /actuator/health/liveness and /readiness (on automatically in Kubernetes)
```
Secure the endpoints with Spring Security; see [Spring Boot Security](Spring%20Security/Spring%20Boot%20Security.md) (`EndpointRequest`).

## Custom health indicator
```java
@Component
public class FurnaceHealthIndicator implements HealthIndicator {   // shown as "furnace" (the bean name without "HealthIndicator")
    @Override
    public Health health() {
        return furnaceIsHot()
            ? Health.up().withDetail("temperatureC", 1200).build()
            : Health.down().withDetail("temperatureC", 0).build();
    }
}
```

## Custom metrics (Micrometer)
```java
@RestController
public class AppraisalController {
    private final Timer appraisalTimer;
    private final DistributionSummary appraisedValue;

    public AppraisalController(MeterRegistry registry) {
        this.appraisalTimer = registry.timer("appraisals.duration");
        this.appraisedValue = DistributionSummary.builder("appraisals.value")
            .baseUnit("gold-coins")
            .register(registry);
    }

    @PostMapping("/appraisals")
    public Appraisal appraise(@RequestBody AppraisalRequest req) {
        Appraisal a = appraisalTimer.record(() -> service.appraise(req));
        appraisedValue.record(a.value().doubleValue());
        return a;
    }

    @GetMapping("/appraisals")
    @Timed("appraisals.list")              // declarative; register a TimedAspect bean to make it work on any bean
    public List<Appraisal> list() { ... }
}
```
Other meters: `registry.counter(...)`, `registry.gauge(...)`, `LongTaskTimer`.
