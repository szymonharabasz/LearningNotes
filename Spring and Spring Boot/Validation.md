Spring uses standard **Jakarta Bean Validation** (with Hibernate Validator as the implementation). The constraints, custom constraints and programmatic `Validator` are described in [Bean Validation](../Java,%20Jakarta%20EE,%20Microprofile/Bean%20Validation.md). This file covers only how Spring triggers validation.

Dependency: `spring-boot-starter-validation`. Since Spring Boot 2.3 it is no longer included in the web starter.

## Request bodies and form objects
```java
@PostMapping("/appraisals")
public Appraisal create(@Valid @RequestBody AppraisalRequest request) { ... }
```
- A REST endpoint (`@RequestBody`) throws `MethodArgumentNotValidException`, and the response is a **400**. Handle it in a `@RestControllerAdvice` for nicer error bodies; see [REST with Spring Boot](REST%20with%20Spring%20Boot.md).
- In MVC forms, add a `BindingResult`/`Errors` parameter **right after** the validated argument. The method is then called anyway and you check `hasErrors()`; see [Spring MVC](Spring%20MVC.md#validating-forms).

## Method validation
```java
@Service
@Validated                                           // Spring-specific: enables validation of method parameters and return values
public class AppraisalService {
    public Appraisal appraise(@NotNull @Positive Long treasureId) { ... }   // throws ConstraintViolationException
}
```
> **Compare:** in Jakarta EE (CDI) and Quarkus, method validation on beans works out of the box, without any class-level annotation. Spring needs `@Validated` on the class, because the validation is implemented with an AOP proxy (so self-invocation is not validated either). JAX-RS validates `@Valid` parameters automatically and also returns 400.
