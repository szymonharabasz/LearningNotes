> **Compare:** the Jakarta counterpart is [CDI interceptors](../Java,%20Jakarta%20EE,%20Microprofile/Context%20and%20Dependency%20Injection.md#interceptors). The two models differ:
> - **Selecting methods.** A CDI interceptor applies only where you put its binding annotation, or `@Interceptors`. A Spring aspect selects methods with a **pointcut expression** (by package, name pattern or annotation), so the target code can stay unaware of it.
> - **Writing the advice.** CDI has `@AroundInvoke` with `InvocationContext.proceed()`. Spring has `@Around` with `ProceedingJoinPoint.proceed()`, plus the specialized `@Before`/`@After...` advice.
>
> Lifecycle callbacks (`@PostConstruct`/`@PreDestroy`) are not AOP; see [Spring core](Spring%20core%20and%20Spring%20Boot.md).

## Vocabulary
- **Join point:** a point in the program's execution. In Spring AOP this is always a method execution.
- **Pointcut:** an expression that selects join points.
- **Advice:** the code that runs at the selected join points.
- **Aspect:** a module that groups pointcuts and advice.
- **Weaving:** combining aspects with the target code. Spring AOP does it at runtime with **proxies**, while full AspectJ does it at compile or load time.

Because Spring AOP is proxy-based, **a call from one method of a bean to another method of the same bean (`this.foo()`) is not advised**. The same pitfall applies to `@Transactional`, `@Cacheable` and `@Async`.

## Setup
Spring Boot: add `spring-boot-starter-aop`. Plain Spring: add `org.springframework:spring-aspects` and put `@EnableAspectJAutoProxy` on a `@Configuration` class.

## An aspect
The aspect must be a bean:
```java
@Aspect
@Component
@Order(1)                                     // ordering between aspects; lower runs first (outermost)
public class GoblinAuditAspect {

    @Around("execution(public * com.dragonbank.appraisal.AppraisalService.appraise(..))")
    public Object audit(ProceedingJoinPoint jp) throws Throwable {
        String method = jp.getSignature().getName();
        Object[] args = jp.getArgs();
        Object result = jp.proceed(args);     // you can pass modified arguments, or skip proceed() entirely
        log.info("{}({}) on {} returned {}", method, Arrays.toString(args), jp.getTarget(), result);
        return result;                        // ...and you can return something else
    }
}
```

## Pointcut expressions
```java
"execution(public * com.dragonbank..*Service.*(..))"   // any public method of *Service classes in any sub-package
"execution(@Audited void send*(..))"                    // void methods named send* annotated with @Audited
"@annotation(com.dragonbank.Audited)"                   // methods annotated with @Audited (the annotation needs RUNTIME retention)
"within(com.dragonbank.appraisal..*)"                   // all methods of the types in a package
```
- `*`: exactly one element (return type, package segment, class, method name or argument).
- `..`: zero or more (packages, or arguments).
- A class name also matches its subclasses.
- Combine expressions with `&&`, `||` and `!`.

## Other kinds of advice
```java
@Before("@annotation(Audited)")
public void before(JoinPoint jp) { ... }

@After("@annotation(Audited)")                         // like finally: runs after both success and failure
public void after(JoinPoint jp) { ... }

@AfterReturning(value = "@annotation(Audited)", returning = "appraisal")
public void afterReturning(Appraisal appraisal) { ... }

@AfterThrowing(value = "@annotation(Audited)", throwing = "ex")
public void afterThrowing(DataAccessException ex) {
    throw new AppraisalFailedException(ex);            // exception translation
}
```
