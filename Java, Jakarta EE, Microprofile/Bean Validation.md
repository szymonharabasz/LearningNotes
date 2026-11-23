Other notes that use Bean Validation:
- JSF `<f:validateBean>` ([JSF](Java%20Server%20Faces%202.3.md))
- Vaadin `BeanValidationBinder` ([Vaadin Flow](Vaadin%20Flow.md))
- Quarkus `@ConfigMapping` validation ([Quarkus](Quarkus%20and%20MicroProfile.md))
- Spring: `@Valid` on controller arguments and `@Validated` for method validation ([Spring Validation](../Spring%20and%20Spring%20Boot/Validation.md))

## Built-in constraints
```
@NotNull, @NotEmpty, @NotBlank, @Email, @Pattern(regexp = ...), @Size(min, max),
@Min, @Max, @DecimalMin, @DecimalMax, @Digits(integer = 4, fraction = 2),
@Positive, @PositiveOrZero, @Negative, @NegativeOrZero,
@Past, @PastOrPresent, @Future, @FutureOrPresent, @AssertTrue, @AssertFalse
```
Every constraint has a `message` attribute (and `groups`, `payload`).

Hibernate Validator, the reference implementation used by Quarkus, Spring and most servers, adds non-standard constraints such as `@CreditCardNumber`, `@URL`, `@Length` and `@Range` (package `org.hibernate.validator.constraints`).

`@Valid` cascades validation into a nested object or the elements of a collection (graph validation).

## Where validation runs automatically
- **JAX-RS:** constrained parameters (`@Valid Dragon dragon`, `@NotNull @QueryParam(...)`). A violation throws `ConstraintViolationException`, which becomes a 400 response. Map it yourself for nicer errors.
- **JPA:** entities are validated on persist and update.
- **CDI:** constraints on method parameters and return values of beans.

## Custom constraint
```java
@Retention(RUNTIME)
@Target({FIELD, METHOD, PARAMETER, ANNOTATION_TYPE})
@Constraint(validatedBy = NotCursedValidator.class)
public @interface NotCursed {
    String message() default "Cursed treasure cannot be deposited";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}

public class NotCursedValidator implements ConstraintValidator<NotCursed, Treasure> {
    @Override public void initialize(NotCursed annotation) { }
    @Override public boolean isValid(Treasure treasure, ConstraintValidatorContext ctx) {
        return treasure == null || !treasure.isCursed();    // let @NotNull handle null
    }
}

@NotCursed Treasure treasure;
```
**Composing constraints:** put existing constraints (for example `@NotNull @Size(...)`) on your annotation, and they are applied together with it.

## Programmatic validation
```java
Validator validator = Validation.buildDefaultValidatorFactory().getValidator();   // or @Inject Validator
Set<ConstraintViolation<Dragon>> violations = validator.validate(dragon);
for (ConstraintViolation<Dragon> v : violations) {
    System.err.println(v.getPropertyPath() + ": " + v.getMessage());
}
```
