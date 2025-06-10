JUnit 4 annotations replaced in version 5: 

| JUnit 4      | JUnit 5     |
| ------------ | ----------- |
| @Before      | @BeforeEach |
| @BeforeClass | @BeforeAll  |
| @After       | @AfterEach  |
| @AfterClass  | @AfterAll   |
| @Ignore      | @Disabled   |
Configuring Spring context in test environment:  
```Java
@ExtendWith(SpringExtension.class)  
@ContextConfiguration(classes={SystemTestConfiguration.class})  
// or  
@SpringJUnitConfig(SystemTestConfiguration.class)  
public class TransferServiceTests {  
    @Autowired  
    private TransferService transferService;  
    …  
}
```
When using Spring Boot:  
```Java
@SpringBootTest(classes=Application.class,  
    webEnvironment=WebEnvironment.RANDOM_PORT|DEFINED_PORT|MOCK|NONE)  
public class TransferServiceTests {  
    @Autowired  
    TestRestTemplate restTemplate;  
}
```
The property classes is optional, a class annotated with `@SpringBootConfiguration` (`@SpringBootApplication`) will automatically be discovered if there is only one such class.
`TestRestTemplate` uses relative path, can go directly to Tomcat running in the test environment. Knows which random port is used. Does not throw exception on error statuses, like 404. Avoids redirections and cookies

Skipping embedded Servlet container with Mock MVC:  
```Java
@SpringBootTest(classes=Application.class,  
    webEnvironment=WebEnvironment.MOCK)  
@AutoconfigureMockMvcpublic class TransferServiceTests {  
      
    @Autowired  
    MockMvc mockMvc;  
      
    @Test  
    public void testBasicGet() {        MvcResult result = mockMvc.perform(  
        get("/accounts/{accId}","123456")  
            .accept(MediaType.APPLICATION_JSON))  
            .andDo(print())  
            .andExpect(status.isOK())        .andReturn();  
    }  
}
```
It is useful to `static import MockMvcRequestBuilders (for get(), post(), put(), delete(), fileUpload(), …)` and `MockMvcResultMatchers (for status(), content(), header(), xpath(), jsonPath(), …)`
Slice testing: For web slice `@WebMvcTest` instead of `@SprintBootTest`
For data layer slice `@DataJpaTest` instead of `@SprintBootTest`:
Loads `@Repository` beans, excludes other `@Component` beans
Auto-configures `TestEntityManager`
Uses an in-memory database

Test properties:  
```Java
@SpringJUnitConfig(SystemTestConfiguration.class)  
@TestPropertySource(properties={'username=foo", "password=bar"},  
    locations="classpath:/trasfer-test-properties)
```
Enabling specific profiles:  
```Java
@SpringJUnitConfig(SystemTestConfiguration.class)  
@ActiveProfiles({"jdbc","dev"})
```
One can use also an inner class annotated with `@Configuration`

Defining a test method
```Java
@Test  
@DisplayName("Descriptive name of the test")
```
Forcing the Spring context to be closed after the test and recreated before the new test (no caching):  
```Java
@Test  
@DirtiesContext
```
Only in tests! `@Autowired` can be used on the level of a test method argument

Mocking an object:
```Java
CarRepository repository = mock(CarRepository.class);
```
With annotations: On the test class:  
```Java
@ExtendWith(MockitoExtension.class)
```
On the mock object:  
```Java
@Mock  
private CarRepository carRepository;
```
On the dependent object:  
```Java
@InjectMocks  
private CarService carService;
```
With Spring Boot capabilities:
On the test class:  
```Java
@SpringBootTest
```
On the mock object:  
```Java
@MockBean  
private CarRepository carRepository;
```
Inside the test:  
```Java
@Test  
public void testHandleDetailsRequest() throws Exception {  
    // arrange  
    given(carRepository.findById(100L))  
        .willReturn(new Car("Porsche", "Cayenne"));  
      
    // act and assert  
    mockMvc.perform(get("/cars/100"))  
        .andExpect(status().isOk())  
        .andExpect(content().contentType(MediaType.APPLICATION_JSON))  
        .andExpect(jsonPath("brand").value("Porsche"))  
        .andExpect(jsonPath("model").value("Cayenne"));  
      
    // verify  
    verify(carRepository).findById(100L);  
}
```
Populating a database for a test:  
```Java
@Test  
@Sql(scripts="/testfiles/setupBadTransfer.sql")  
@Sql(scri[ts="/testfiles/cleanup.sql",  
    executionPhase=Sql.ExecutionPhase.AFTER_TEST_METHOD),  
    config=@SqlConfig(errorMode=ErrorMode.FAIL_ON_ERROR,  
        commentPrefix="//",  
        separator="@@"))  
```
One can also use the annotation on the class level, it is executed before each single test unless the particular test method is annotated with this annotation.

Error modes: `FAIL_ON_ERROR`, `CONTINUE_ON_ERROR`, `IGNORE_FAILED_DROPS`, `DEFAULT` (whatever is defined with `@Sql` on the class level, otherwise `FAIL_ON_ERROR`)

Defining assumptions:
```Java
given(carRepository.findById(car.getId()))  
    .willReturn(Optional.of(car));
when(carRepository.findById(car.getId()))  
    .thenReturn(Optional.of(car));
```
Verifying, that something has been called:  
```Java
verify(carRepository).setCarColor(132L, "red");
```
1Asserting that an exceptions has been thrown:  
```Java
assertThrows(CarNotFoundException.class, () -> carService.setCarColor(999L, 
	"blue"));
```
Asserting that a proper result has been returned:  
```Java
assertEquals("login.html", result);
```