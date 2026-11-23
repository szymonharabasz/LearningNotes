Plain JUnit 5 and Mockito, the same in any project. Framework-specific test support:
- Quarkus (`@QuarkusTest`, `@InjectMock`, test resources): [Quarkus](Quarkus%20and%20MicroProfile.md#testing)
- Spring (`@SpringBootTest`, MockMvc, slices, `@MockitoBean`): [Testing Spring applications](../Spring%20and%20Spring%20Boot/Testing%20Spring%20applications.md)

## JUnit 5
| JUnit 4 | JUnit 5 |
|---|---|
| `@Before` | `@BeforeEach` |
| `@BeforeClass` | `@BeforeAll` (static, unless `@TestInstance(PER_CLASS)`) |
| `@After` | `@AfterEach` |
| `@AfterClass` | `@AfterAll` |
| `@Ignore` | `@Disabled` |
| `@RunWith` | `@ExtendWith` |

```java
@Test
@DisplayName("A cursed ring cannot be deposited")
void cursedRingRejected() {
    assertThrows(CursedTreasureException.class, () -> vault.deposit(new CursedRing()));
    assertEquals("vault.html", controller.showVault());
}
```

## Mockito
```java
@ExtendWith(MockitoExtension.class)
class AppraisalServiceTest {
    @Mock TreasureRepository treasures;           // or: TreasureRepository treasures = mock(TreasureRepository.class);
    @InjectMocks AppraisalService service;         // gets the mocks injected (constructor, then setter, then field)
    @Captor ArgumentCaptor<Appraisal> appraisalCaptor;

    @Test
    void appraisesCrown() {
        when(treasures.findById(42L)).thenReturn(Optional.of(crown));     // or BDD style:
        given(treasures.findById(42L)).willReturn(Optional.of(crown));    //   BDDMockito.given(...).willReturn(...)

        service.appraise(42L);

        verify(treasures).save(appraisalCaptor.capture());
        assertEquals(new BigDecimal("1000"), appraisalCaptor.getValue().value());
        verify(treasures, never()).delete(any());                           // same as times(0)
    }
}
```
A captor is also handy for checking what was passed to an async callback:
```java
verify(asyncResponse).resume(responseCaptor.capture());
assertThat(responseCaptor.getValue().getStatusInfo().getFamily()).isEqualTo(Response.Status.Family.SUCCESSFUL);
```
