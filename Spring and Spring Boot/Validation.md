Annotate properties with validation annotations
They all have attribute message
Useful annotations:  
```Java
@NotNull  
@NotBlank  
@Size(min=4, max=5)  
@CreditCardNumber (vendor-specific from Hibernate)  
@Pattern(regexp="")  
@Digits(integer=3, fraction=0)
```