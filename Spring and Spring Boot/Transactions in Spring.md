Create a transaction manager:  
```Java
@Bean  
public PlatformTransactionManager(DataSource dataSource) {  
    return new DataSourceTransactionManager(dataSource);  
}  
```    
Other available implementations: `JmsTransactionManager`, `JpaTransactionManager`, `JtaTransactionManager`, `WebLogicJtaTransactionManager`, `WebSphereUowTransactionManager`
Use `@EnableTransactionManagement` on a configuration class
Annotate a method that represents an atomic unit of work with `@Transactional`
Spring supports `javax.transactional.Transactional`, but also provides its own version which has more options
One can also annotate a class
Properties of the annotation (like timeout) at the method level override those at the class level
Sice Spring 5 one can also annotate interfaces
Transactions are implemented through an AOP proxy. Therefore if a `@Transactional` method is called internally, within the same class, by another `@Transactional` method, the call is made directly and does not go through the proxy. In that situation, transaction propagation rules do not apply and the second method is executed within the same transaction.
Transaction is rolled back if a runtime exception is thrown
This can be overwritten in configuration:  
```Java
@Transactional(rollbackFor=MyCheckedException.class,  
    norRollbackFor={JmsException.class, MeilException.class})
```
Transactions will always be rolled back in tests, but only the outermost one
Test method can be annotated with `@Commit` to change this behavior
Transaction propagation levels:
```Java
@Transactional(propagation=Propagation.REQUIRED)
```
`REQUIRED` (default one) - joins an existing transaction, creates a new one if none exists
`REQUIRES_NEW` - creates a new transaction, suspends the current transaction if one exists
Database connection is automatically managed by the transaction. One can access it manually with:  
```Java
DataSourceUtils.getConnection(dataSource)
```
Simple manual transaction creation:  
```Java
TransactionStatus status = transactionManager.getTransaction(new 
	DefaultTransactionDefinition());  
// …  
transactionManager.rollback(status);
```