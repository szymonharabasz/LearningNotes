In `beans.xml` one can specify `bean-discovery-mode="all"` to make all the POJOs in the project into CDI beans
`@Stateless`, `@Stateful`, `@Singleton` beans from EJB are also managed by CDI.
Beans annotated with `@Stereotype` are created when the application starts and not when their services are requested for the first time
Usage:` @Named`, `@Inject` (on field, constructor or method which is then an initializer method (?)), `@Produces` (the latter one to annotate a factory method returning an object of a given type)
NOTE: One needs to use `@Produces` in order to be able to inject objects of types which are not beans (like enums)
Scopes of named beans:
```Java
@RequestScoped
@ConversationScoped
```
The latter useful in combination with Faces Flow:
Inject the bean, inject `javax.enterprise.cotext.Conversation`, In the code: `conversation.begin(["id"]); conversation.getId(); conversation.end();`
```Java
@SessionScoped
@ApplicationScoped
@Dependent // always injected a new object of the class
```
Qualifiers - definition:  
```Java
@Qualifier  
@Retention(RUNTIME)  
@TARGET( {METHOD, FIELD, PARAMETER, TYPE} )  
public @interface Premium {  
    @Nonbinding.        // in this case the value of the attribute  
                        // doesn't influence the interceptor lookup  
    MyCategory value();  
}
```
Otherwise, a useful technique is to use qualifier arguments for more specific qualification.
Applying:  
```Java
@Named @RequestScoped  
@Premium  
public class PremiumCustomer extends Customer { … }
```
Injection:  
```Java
@Inject  
@Premium  
private Customer customer;
```
NOTE: `@Named` is a `@Qualifier`
Predefined qualifiers:
`@Default`
`@RestClient` which allows to `@Inject` an automatically created implementation of an interface annotated with `@RegisterRestClient`
**One cannot apply qualifiers to stereotypes**
CDI Intereceptors - definition:  
```Java
@InterceptorBinding  
@Retention(RUNTIME)  
@TARGET( {METHOD, TYPE} )  
public @interface Secure {  
    @Nonbinding.        // in this case the value of the attribute  
                        // doesn't influence the interceptor lookup  
    MyCategory value();  
}
```
Applying (there is also `@AroundConstruct`):  
```Java
@Secure(MyCategory.VERY_SECURE) @Interceptor public class SecurityInterceptor 
{  
    @AroundInvoke  
    public Object interceptMethod(InvocationContext context) throws Exception 
    {  
        Object result = context.proceed();  
        return "Intercepted " + result;  
    }  
}
```
Usage:  
```Java
@Secure(MyCategory.VERY_SECURE) public class SomeBean { … }  
@Secure(MyCategory.VERY_SECURE) public void someMethod( … ) { … }
```
Or (does this way require `<interceptors>` in XML? - CHECK THIS):  
```Java
	@Interceptors(SecurityInterceptos.class) public class SomeBean { … }  
    @Interceptors(SecurityInterceptor.class) public void someMethod( … ) { … }
```
Activating by one of the methods:
- Defining `<interceptors>` in `beans.xml`
- Annotating the interceptor class with `@Priority(Interceptor.Priority.APPLICATION)` (or other value of the attribute
Alternatives: mark different classes implementing the same interface with `@Alternative`
In `beans.xml` select the alternative to be used: 
```XML
<beans.…>  
    <alernatives>  
        <class>my.package.MyConcreteClass</class>  
    </alternatives>
</beans>
```
Stereotypes: create an annotation marked with other needed annotations, add `@Stereotype` Use this new annotation on the beans.

Decorators: create an interface e.g. `Product`. Implement the interface in a bean. Implement the interface in a decorator class:  
```Java
@Decorator  
public class PriceDiscountDecorator implements Product {  
    @Inject  
    @Delegate  
    Product product;  
    @Override  
    public double calculatePrice() {  
        product.setPrice(product.getPrice * 0.5);  
        return product.calculatePrice();  
    }
}
```
Configure the actual usage of the decorator (and order if there are many) in `beans:xml`:  
```XML
<decorators>  
    <class>my.package.PriceDiscountDecorator</class>  
</decorators>
```
XML configuration is not needed if decorators are also marked with the `@Priority(int)` annotation

CDI events - emitting:  
```Java
@Inject  
private Event<NavigationInfo> navigationInfoEvent;  
.…  
navigationInfoEvent.fire(navigationInfo);

navigationInfoEvent.fireAsync(navigationInfo);
```
Handling:  
```Java
public void handle(@Observes[(during=TransactionPhase.AFTER_SUCCESS|AFTER_FAILURE|IN_PROGRESS|BEFORE_COMPLETION|AFTER_COMPLETION, notofyObserver=Reception.IF_EXISTS)]  
    NavigationInfo navigationInfo, EventMetadata eventMetadata) { … }  
public void handle(@ObservesAsync NavigationInfo navigationInfo) { … }

public void handle(@Observes  
    @Priority(Interceptor.Priority.APPLICATION) NavigationInfo navigationInfo) { … }
```
Instead of injecting many events with different qualifiers (being instance of one qualifier with different values of some parameters) one can create one event and select observers which are annotated with this qualifiers:  
```Java
userResponseEvent.select(getAnnotation(UserRegion.EU)).fireAsync(userResponse);  
//One has to provide an appropriate instance of the annotation interface: 
private MessageOption getAnnotation(final UserRegion userRegion) {  
    if (userRegion == UserRegion.EU) {  
        return new MessageOption() {  
            @Override  
            public MessageType value() { // parameter of the annotation  
                return MessageType.EMAIL;  
            }  
            @Override  
            public Class<? extends Annotation> annotationType() {  
                return MessageOption.class;  
            }  
        };  
    }  
    return new MessageOption() { // else  
        …  
    };  
}
```
Transactions in CDI with JTA - annotate a method with: 
```Java
@Transactional(TxType.MANDATORY|NEVER|SUPPORTS|NOT_SUPPORTED|REQUIRED|REQUIRES_NEW,  
        rollbackOn = MyException)
```
`ManagedExecutorService` - for executing `Runnable` in application server managed thread
`ManagedScheduledExecutorService` - for scheduling `Runnable` at given time or fixed rate

Lifecycle methods: `@PostConstruct`,

Resolving beans manually:  
```Java
@Inject  
private BeanManager manager;  
      
private <T extends NeededInterface> Repository<T> locateTargetRepository(final Class<T> targetType) {  
    ParametrizedType paramType = new ParametrizedType() {  
@Override public Type getRawType() {  
	return Repository.class;  
}  
@Override public Type getOwnerType() { return null; }  
@Override public Type[] getActualTypeArguments() {  
    return new Type[] { targetType }; // when targetType is given  
}  
  
Set<Bean<?>> beans = manager.getBeans(paramType);  
Bean<?> bean = manager.resolve(beans);  
CreationalContext<?> cc = manager.createCreationalContext(null);  
@SuppressWarning("unchecked")  
Repository<T> repo = (Repository<T>)manager.getReference(  
    bean, paramType, cc);  
    return repo;  
}
```