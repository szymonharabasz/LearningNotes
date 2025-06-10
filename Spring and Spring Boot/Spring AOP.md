Definitions:
**Join Point** - a point in the execution of a program such as a method call or exception thrown
**Pointcut** - an expression that selects one of more Join Points
**Advice** - code to be executed at each selected Join Point
**Aspect** - a module that encapsulates pointcuts and advice
**Weaving** - technique by which aspects are combined with main code
There are standard Java annotations:  
```Java
@PostConstruct  
@PreDestroy
```
Alternative is to use `@Bean` annotation attributes:  
```Java
@Bean(initMethod="populateCache", destroyMethod="flushCache")
```
Most basic dependency:
```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-aspects</artifactId>
    <version>5.3.8</version>
</dependency>
```
On the configuration class:  
```Java
@Configuration  
@EnableAspectJAutoProxy  
public class MyConfig {}
```
Defining aspect:  
```Java
@Component  
@Aspect  
public class LoggingAspect {  
    @Around(  
        "execution(public * com.example.UserController.getUsers(..)) 
			throws MyException"  
    )  
    publuc Object log(ProceedingJoinPoint joinPoint) {  
        String methodName = joinPoint.getSignature().getName();  
        Object [] args = joinPoint.getArgs();  
        Object [] newArgs = {"fake news"};    
        Object returnedFromMethod = joinPoint.proceed(newArgs);  
        System.out.println("getUser method called on bean " +  
	        joinPoint.getTarget);  
        return "new returned value"; // returnedFromMethod;    
    }     
}
```
Aspect must be a bean, other methods of creating beans are also valid
Other useful pointcut definition, based on a given annotation (which should habe RUNTIME retention):
```Java
@Around("execution(@ToLog void send*(..))")  
@Around("@annotation(ToLog)")`
```
Other advices:` @Before`, `@After` (which is after `finally`), `@AfterReturning`, `@AfterThrowing`
```Java
@AfterReturning(value = "@annotation(ToLog), returning = "returnedValue")  
public void log(Returned returnedValue) { … }
```
```Java
@AfterReturning(value = "@annotation(ToLog), throwing = "exception")  
public void log(DataAccessException exception) {  
    …  
    // Optionally one can apply exception translation:  
    throw new RewardException(e);  
}
```
Aspect class can also be annotated with `@Order(1)`, `@Order(2)` etc.
Pointcut designators can be combined with `&&`, `||`, and `!`
Wildcards in pointcut designator are:
`*` - exactly one (return type, package, class, method name, argument)
`..` - zero or more (method arguments or packages)
A class name in the pointcut designator matches also subclasses