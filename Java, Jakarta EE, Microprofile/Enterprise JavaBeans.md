Annotations to create four types of beans:  
```Java
@Stateless, @Stateful, @Singleton, @MesageDriven(mappedName="jms/MyMessageQueue")  
@DependsOn("MyOtherBean")
```
Annotations related to the life-cycle:  
```Java
@Startup // created when application starts
@PostConstruct, @PreDestroy, @PrePassivate, @PostActivate // life-cycle methods, the latter two to be used in stateful beans)
```
Creating bean with remote interface (can also be local):  
```Java
@Remote  
public interface SimpleSession { … }  
@Stateless  
public class SimpleSessionBean implements SimpleSession { … }
```
Or:  
```Java
public interface SimpleSession { … }  
@Stateless  
@Remote(my.package.SimpleSession)  
public class SimpleSessionBean implements SimpleSession { … }
```
One may not annotate bean with `@Local` nor `@Remote` and not implement any interface or annotate the bean with `@LocalBean` in order to add a non-interface view
Injecting to the client code:  
```Java
@EJB  
private static SimpleBean simpleBean;
```
**Obtaining an EJB with remote interface.** The compiled remote interface must be packaged in the client project. Properties to be set
```Java
props = new Properties();  
props.setProperty("java.naming.factory.initial", 
	"com.sun.erterprise.naming.SerialInitContextFactory");  
props.setProperty("java.naming.factory.url.pkgs", 
	"com.sun.erterprise.naming");  
props.setProperty("java.naming.factory.state", 
	"com.sun.ee.impl.presentation.rmi.JNDIStateFactoryImpl");  
props.setProperty("org.omg.CORBA.ORBInitialHost","192.168.1.100");  
props.setProperty("org.omg.CORBA.ORBInitialPort","3700");  
try {  
    InitialContext ic = new InitialContext();  
    NamingEnumeration<NameClassPair> list = ic.list("");  
    while (list.hasMore()) {  
        System.out.println(list.next().getName());  
    }  
    SimpleSession simple = (SimpleSession)ic.lookup(  
        "my.package.SimpleSession");     
} catch (Exception e) {  
    e.printStackTrade(System.err);  
}
```
7. Asynchronous method invocation:  
 ```Java
@Asynchronous @Override // because comes from an interface  
public Future<Long> slowComputation() { … }
```
It can also be `void`

Methods of the interface Future:  
```Java
cancel(bool mayInterruptIfRunning), get(), get(long timeout, TimeUnit unit), isCancelled(), isDone()
```
Container-managed concurrency:  
```Java
@ConcurrencyManagement(ConcurrencyManagementType.CONTAINER) public class { …  
	@Lock(LockType.WRITE) public void setUser…  
	@Lock(LockType.READ)  
	@AccessTimeout(value = 30, unit = TimeUnit.SECONDS)  
	public string getName…
```
**Transactions in EJB - container-managed.** Methods in EJBs are by default execute within a transaction, which is also equivalent to annotating a bean with 
```Java
@TransactionManagement(value=TransactionManagementType.CONTAINER)
```
Default behaviour can be changed by 
```Java
@TransactionAttribute(value=TransactionAttributeType….)
```
`TransactionAttributeType` enumeration:  
`MANDATORY, NEVER, NOT_SUPPORTED, REQUIRED, REQUIRES_NEW, SUPPORTS`
Rolling back:  
```Java
@Resourece  
private EJBContext ejbContext;  
.…  
ejbContext.setRollbackOnly();
```

Bean-managed  
```Java
@Stateless  
@TransactionManagement(value=TransactionManagementType.BEAN)  
public class CustomerDaoBean implements CustomerDao {  
    @Resource  
    private UserTransaction userTransaction;  
    …  
    userTransaction.begin();  
    …  
    userTransaction.commit();
```
Timer service:  
```Java
@Resource  
TimerService timerService;  
.…  
Serializable info = ...  
Timer timer = timerService.createTimer(new Date, 5000, info);  
.…  
@Timeout  
public void logMessage(Timer timer) { … }  
.…  
if (timer.getInfo.equals(info)) { timer.cancel(); }
```
Cron-like expressions:  
```Java
@Schedule(hour="20, minute="10")  
public void logMessage() { … }  
@Schedules({@Schedule(…), @Schedule(…)})  
public void doSomething() { … }
```
Parameters and example values:
```Java
dayOfMonth: "3", "Last", "-2", "1st Tue"
dayOfWeek: "3", "Tue"
hour, minute, second: "14", "*/10", "25/10"
month: "3", "March", "Feb", "1-10"
year: "2019"
timezone: "America/New York"
```
For example: `second="*/12"` – every 12 seconds
**Interceptors.** Interception target:  
```Java
@Interceptors(LoggerInterceptor.class)  
public void setValue(Integer value) { … }
```
Definition of an interceptor:  
```Java
@AroundInvoke  
public Object logger(InvocationContext ic) throws Exception {  
    Object[] params = ic.getParameters();  
    logger.warning("Parameters: " + params);  
    return ic.proceed();  
}
```
Also:  `@AroundConstruct`, `@AroundTimeout`, `@PostContruct`, `@PreDestroy`. The last two can be used for interceptor mathods or directly for methods in a bean, they can then also accept `InvocationContext` as an argument.
Methods of `InvocationContext`:  
`getTarget(), getMethod(), getParameters(), setParameters(Object[]), getContextData(), proceed(), getMethod().getName(), getMethod().getDeclaringClass()`
Excluding interceptors for a class:  
```Java
@ExcludeDefaultInterceptors // those that can be configured in beans.xml  
@ExcludeClassInterceptors
```
Exceptions annotated with `@ApplicationException` don't rollback transactions, by default, this can be changed using `@ApplicationException`(rollback = true)