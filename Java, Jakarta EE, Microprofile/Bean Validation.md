Standard useful constraints:  
```
@NotNull, @Email, @NotEmpty, @NotBlank, @Positive, @PositiveOrZero, @Negative, @NegativeOrZero, @Past, @PastOrPresent, @Future, @FutureOrPresent, @AssertTrue, @AssertFalse, @@DecimalMin, @DecimalMax, @Digits(integer=4, fraction=2), @Min, @Max, @Pattern, @Size,  
```    
`@Valid` - to annotate an embedded object (or collection): graph validation
Create an annotation:  
```Java
@Retention(RUNTIME)  
@Target(FIELD, METHOD, ANNOTATION_TYPE, PARAMETER)  
@Constraint(validatedBy=MyValidator.class)  
public @inteface MyConstraint {  
	String message() default "";  
    Class<?>[] groups() defailt {};  
     Class<? extends PayLoad>[] payLoad() default {};  
}
```
Existing contraints can also annotate this annotation in order to combine constraints.
Implement a validating class:  
```Java
public class MyValidator implements ConstraintValidator<MyConstraint, 
	MyTargetType> {  
    public void initialize(MyConstraint constraint) {}  
    public boolean isValid(MyTargetType target, 
	    ConstraintValidatorContext context) {  
        return target.isGood();  
    }  
}
```
Annotate `MyTargetType` instance with `@MyConstraint`
Programmatic validation:  
```Java
Validator validator = Validation.buildDefaultValidatorFactory().getValidator();  
Set<ConstraintViolation<Movie>> violations = validator.validate(invalidMovie);  
for (ConstraintViolation<Movie> violation : violations) {  
    System.err.printlln(violation.getPropertyPath());  
    System.err.println(violation.getMessage());  
}
```
5. Automatic validation: throws an exception