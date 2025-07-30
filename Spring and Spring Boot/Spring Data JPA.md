In Java there are checked and unchecked exceptions:
Checked exceptions:
- Force developers to handle errors
- ntermediate methods have to declare exceptions from all the methods below
- Examples:  
  `SQLException`
Unchecked exceptions:
- Can go up in the call hierarchy to the best place for handling them
- Intermediate errors do not need to know about them
- Runtime exceptions belong to them
- Examples  
`DataAccessException` from Spring, it has many child exceptions

Spring always throws Runtime (unchecked) exceptions

`@SpringBootApplication` is a combination of:
```Java
@EnableAutoConfiguration
@ComponentScan
@Configuration
```
There is a possibility to disable a part of autoconfiguration:  
```Java
@EnableAutoConfiguration(exclude=DataSourceAutoConfiguration.class)
```
Producing uber-jar:
In Maven:
Add a `plugin spring-boot-maven-plugin`
Execute `mvn package`

In Gradle:
Execute `gradle assemble`

Basic ways of running application:

```Java
@Bean  
CommandLineRunner commandLineRunner(JdbcTemplate jdbc) {  
    return args -> System.out.println(jdbc.QueryForObject("…", Long.class);  
}
```