JUnit 5 and Mockito themselves, which are the same in any Java project, are in [Testing with JUnit and Mockito](../Java,%20Jakarta%20EE,%20Microprofile/Testing%20with%20JUnit%20and%20Mockito.md). This file covers the Spring test support.

> **Compare with Quarkus testing** ([Quarkus - Testing](../Java,%20Jakarta%20EE,%20Microprofile/Quarkus%20and%20MicroProfile.md#testing)):
> - `@QuarkusTest` starts the whole app **once** for all tests, similar to a cached `@SpringBootTest` context. Tests usually call it over HTTP with REST Assured; there is no MockMvc-like layer.
> - There are no slices like `@WebMvcTest`/`@DataJpaTest`. A different setup means a `@TestProfile`, which restarts the app, much like a different Spring context.
> - `@MockitoBean` corresponds to `@InjectMock`.
> - Testcontainers: Spring Boot has `@ServiceConnection`. Quarkus starts containers automatically with **Dev Services**, or with a `QuarkusTestResourceLifecycleManager`.

## Spring test context
```java
@SpringJUnitConfig(AppraisalTestConfig.class)    // = @ExtendWith(SpringExtension.class) + @ContextConfiguration(classes = ...)
class AppraisalServiceTests {
    @Autowired AppraisalService service;

    @Test
    void appraise(@Autowired TreasureRepository repo) { ... }   // @Autowired on test method parameters: tests only
}
```
- The config can also be a static nested `@Configuration` class.
- **The context is cached** between test classes with the same configuration. `@DirtiesContext` on a test or class discards it, so the next test gets a fresh context. It is slow; use it sparingly.
- `@TestPropertySource(properties = { "appraisal.goblin-commission=0.5" }, locations = "classpath:/appraisal-test.properties")`.
- `@ActiveProfiles({"jdbc", "dev"})`.

## `@SpringBootTest`
```java
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)   // MOCK (default), RANDOM_PORT, DEFINED_PORT, NONE
class AppraisalApiTests {
    @Autowired TestRestTemplate rest;    // or WebTestClient

    @Test
    void getAppraisal() {
        ResponseEntity<Appraisal> r = rest.getForEntity("/appraisals/{id}", Appraisal.class, 42);
        assertEquals(HttpStatus.OK, r.getStatusCode());
    }
}
```
- `classes = ...` is optional. The `@SpringBootConfiguration` (that is, the `@SpringBootApplication` class) is found by searching up the package tree.
- `TestRestTemplate` takes relative URLs and knows the random port. It does **not** throw on 4xx/5xx, and doesn't follow redirects or keep cookies.

## MockMvc: the web layer without a real server
```java
@SpringBootTest                           // webEnvironment = MOCK
@AutoConfigureMockMvc
class AppraisalControllerTests {
    @Autowired MockMvc mockMvc;
    @MockitoBean TreasureRepository treasures;      // replaces the bean in the context (older: @MockBean, deprecated since Boot 3.4)

    @Test
    void returnsAppraisal() throws Exception {
        given(treasures.findById(100L)).willReturn(Optional.of(new Treasure(100L, "Crown", ARTIFACT)));

        mockMvc.perform(get("/treasures/{id}", 100).accept(MediaType.APPLICATION_JSON))
            .andDo(print())
            .andExpect(status().isOk())
            .andExpect(content().contentType(MediaType.APPLICATION_JSON))
            .andExpect(jsonPath("$.name").value("Crown"));

        verify(treasures).findById(100L);
    }
}
```
Static imports: `MockMvcRequestBuilders.*` (`get`, `post`, `put`, `delete`, `multipart`) and `MockMvcResultMatchers.*` (`status`, `content`, `header`, `jsonPath`, `xpath`).

## Slice tests (only part of the context)
- **`@WebMvcTest(AppraisalController.class)`**: only the MVC infrastructure and that controller, with MockMvc auto-configured. Mock the services with `@MockitoBean`.
- **`@DataJpaTest`**: only JPA. It loads the repositories but no other `@Component`s, auto-configures `TestEntityManager`, uses an in-memory DB, and makes every test `@Transactional` (so it rolls back; see [Transactions in Spring](Transactions%20in%20Spring.md#transactions-in-tests)).

## Database scripts per test
```java
@Test
@Sql("/testdata/disputed-appraisal.sql")
@Sql(scripts = "/testdata/cleanup.sql",
     executionPhase = Sql.ExecutionPhase.AFTER_TEST_METHOD,
     config = @SqlConfig(errorMode = SqlConfig.ErrorMode.FAIL_ON_ERROR, commentPrefix = "//", separator = "@@"))
void disputedAppraisal() { ... }
```
- `@Sql` on the class runs before **each** test, unless the method has its own `@Sql`.
- Error modes: `FAIL_ON_ERROR`, `CONTINUE_ON_ERROR`, `IGNORE_FAILED_DROPS`, `DEFAULT` (inherits the class-level setting, otherwise `FAIL_ON_ERROR`).
