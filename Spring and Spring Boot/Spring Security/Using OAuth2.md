> **Compare:** the MicroProfile/Quarkus counterpart is MP JWT or `quarkus-oidc`; see [Quarkus - Security](../../Java,%20Jakarta%20EE,%20Microprofile/Quarkus%20and%20MicroProfile.md#security).
> - The issuer configuration corresponds to `mp.jwt.verify.issuer` + `mp.jwt.verify.publickey.location`.
> - **Roles:** MP JWT reads them from the `groups` claim, so Keycloak needs a mapper to add `groups`. Spring by default turns the `scope` claim into `SCOPE_xxx` authorities. To use Keycloak realm roles (`realm_access.roles`) with `hasRole`, you need a custom `JwtAuthenticationConverter`.

## Resource server (a REST API that accepts bearer tokens)
Dependency: `spring-boot-starter-oauth2-resource-server`.
```properties
spring.security.oauth2.resourceserver.jwt.issuer-uri=http://localhost:9080/realms/dragonbank-realm
```
```java
@Bean
SecurityFilterChain api(HttpSecurity http) throws Exception {
    http.authorizeHttpRequests(a -> a.anyRequest().authenticated())
        .oauth2ResourceServer(o -> o.jwt(withDefaults()))
        .csrf(csrf -> csrf.disable());              // stateless API, no session cookies
    return http.build();
}

@GetMapping("/me")
public Map<String, Object> me(@AuthenticationPrincipal Jwt jwt) { return jwt.getClaims(); }
```

## OAuth2/OIDC login (a web app where users sign in at the provider)
Dependency: `spring-boot-starter-oauth2-client`.
```properties
spring.security.oauth2.client.registration.keycloak.client-id=back-office
spring.security.oauth2.client.registration.keycloak.client-secret=...
spring.security.oauth2.client.registration.keycloak.scope=openid,profile
spring.security.oauth2.client.provider.keycloak.issuer-uri=http://localhost:9080/realms/dragonbank-realm
```
```java
http.authorizeHttpRequests(a -> a.anyRequest().authenticated()).oauth2Login(withDefaults());

@GetMapping("/user")
public Principal user(Principal principal) { return principal; }
```

## Legacy approaches
You'll find these in older books. Both are deprecated or end-of-life.
- **`spring-security-oauth2-autoconfigure` + `@EnableOAuth2Sso`** on a `WebSecurityConfigurerAdapter`, with `security.oauth2.client.*` properties (Spring Boot 1.5/2.x).
- **Keycloak Spring adapter** (`keycloak-spring-boot-starter`, deprecated by Keycloak in 2022):
```properties
keycloak.realm=dragonbank-realm
keycloak.auth-server-url=http://keycloak:8080/auth
keycloak.ssl-required=external
keycloak.resource=back-office
keycloak.credentials.secret=5988f899-a5bf-4f76-b15f-f1cd0d2c81ba
keycloak.use-resource-role-mappings=true
keycloak.bearer-only=true
```
```java
@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(jsr250Enabled = true)
public class SecurityConfig extends KeycloakWebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        super.configure(http);
        http.authorizeRequests().anyRequest().permitAll();
        http.csrf().disable();
    }

    @Autowired
    public void configureGlobal(AuthenticationManagerBuilder auth) {
        KeycloakAuthenticationProvider provider = keycloakAuthenticationProvider();
        provider.setGrantedAuthoritiesMapper(new SimpleAuthorityMapper());   // adds the ROLE_ prefix
        auth.authenticationProvider(provider);
    }

    @Bean @Override
    protected SessionAuthenticationStrategy sessionAuthenticationStrategy() {
        return new RegisterSessionAuthenticationStrategy(new SessionRegistryImpl());
    }

    @Bean
    public KeycloakConfigResolver keycloakConfigResolver() { return new KeycloakSpringBootConfigResolver(); }  // read keycloak.* from application.properties
}

// Propagating the token to other services
@Bean @Scope(ConfigurableBeanFactory.SCOPE_PROTOTYPE)
public KeycloakRestTemplate keycloakRestTemplate(KeycloakClientRequestFactory factory) {
    return new KeycloakRestTemplate(factory);
}
```
Today, token propagation is done with an OAuth2-aware `WebClient`/`RestClient` (`ServletOAuth2AuthorizedClientExchangeFilterFunction`, or a client interceptor). Compare with `@RegisterClientHeaders` + `propagateHeaders=Authorization` in the MicroProfile REST Client.
