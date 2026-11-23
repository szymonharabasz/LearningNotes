> **Compare:**
> - **Jakarta Security** ([Security](../../Java,%20Jakarta%20EE,%20Microprofile/Security.md)) has the same two building blocks under different names. An *identity store* (database, LDAP, custom) corresponds to Spring's `UserDetailsService`/`AuthenticationProvider`. An *authentication mechanism* (`@BasicAuthenticationMechanismDefinition`, form login) corresponds to `httpBasic()`/`formLogin()`.
> - **Quarkus** configures URL rules in properties (`quarkus.http.auth.permission.<name>.paths=/api/*`, `.policy=authenticated`) instead of with a `SecurityFilterChain` bean. It uses `@RolesAllowed`/`@Authenticated` on methods.
> - Token-based security is in [Using OAuth2](Using%20OAuth2.md).

Adding `spring-boot-starter-security` **secures every endpoint immediately**. You get a generated login page, HTTP Basic, and a user `user` whose random password is printed in the log.

## The security filter chain
Spring Security 6 style: configure `SecurityFilterChain` beans. `WebSecurityConfigurerAdapter` was removed in Spring Security 6; see the legacy section below.
```java
@Configuration
@EnableWebSecurity
@EnableMethodSecurity(jsr250Enabled = true)            // @PreAuthorize/@PostAuthorize; jsr250Enabled adds @RolesAllowed
public class SecurityConfig {

    @Bean
    SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth             // the first matching rule wins, so put specific rules first
                .requestMatchers("/signup", "/about").permitAll()
                .requestMatchers(EndpointRequest.to(HealthEndpoint.class)).permitAll()   // Actuator
                .requestMatchers(HttpMethod.PUT, "/appraisals/**").hasRole("APPRAISER")
                .requestMatchers("/admin/**").hasAnyRole("HEAD_GOBLIN", "ADMIN")
                .anyRequest().authenticated())
            .httpBasic(withDefaults())                      // and/or:
            .formLogin(form -> form.loginPage("/login").permitAll())
            .logout(logout -> logout.logoutSuccessUrl("/home").permitAll());
        return http.build();
    }

    @Bean
    WebSecurityCustomizer ignoring() {                      // no security filters at all for these paths
        return web -> web.ignoring().requestMatchers("/css/**", "/images/**");
    }
}
```
**Roles vs authorities:** `hasRole("ADMIN")` checks for the authority **`ROLE_ADMIN`**. `.roles("ADMIN")` adds the prefix for you, but `.authorities(...)` and your own `GrantedAuthority` implementations don't.

## Method security
```java
@PreAuthorize("hasRole('DRAGON') and #hoard.owner.name == authentication.name")
public Treasure findTreasure(Hoard hoard, long itemNo) { ... }

@PostAuthorize("returnObject.owner == authentication.name")
public Hoard getHoard(long number) { ... }

@RolesAllowed("ADMIN")                                  // JSR-250 / Jakarta: same annotation as in Jakarta EE and Quarkus
public void closeHoard(long number) { ... }
```
> **Compare:** `@RolesAllowed` works out of the box in Jakarta EE and Quarkus. Spring needs `jsr250Enabled = true`. SpEL expressions like `@PreAuthorize` have no standard Jakarta equivalent; Quarkus has `@PermissionsAllowed`.

## Users
**Password encoders:**
```java
PasswordEncoder encoder = PasswordEncoderFactories.createDelegatingPasswordEncoder();
// stores "{bcrypt}$2a$10$...": the prefix records the algorithm, so you can migrate later
```
`BCryptPasswordEncoder` (the default, recommended), `Pbkdf2PasswordEncoder`, `SCryptPasswordEncoder`, `Argon2PasswordEncoder`. **Don't use** `NoOpPasswordEncoder` or the legacy `StandardPasswordEncoder`.

**In memory** (demos and tests):
```java
@Bean
InMemoryUserDetailsManager users(PasswordEncoder encoder) {
    return new InMemoryUserDetailsManager(
        User.withUsername("grizzlegut").password(encoder.encode("shiny")).roles("APPRAISER").build(),
        User.withUsername("head-goblin").password(encoder.encode("shinier")).roles("ADMIN").build());
}
```
**JDBC** (the standard `users`/`authorities` tables):
```java
@Bean
UserDetailsManager users(DataSource dataSource) { return new JdbcUserDetailsManager(dataSource); }
```
**Custom store, for example with JPA.** Dependencies: `spring-boot-starter-data-jpa` plus a driver. You implement `UserDetailsService`:
```java
public interface GoblinRepository extends JpaRepository<Goblin, Long> {
    Optional<Goblin> findByUsername(String username);
}

@Service
public class GoblinUserDetailsService implements UserDetailsService {
    private final GoblinRepository goblins;
    public GoblinUserDetailsService(GoblinRepository goblins) { this.goblins = goblins; }

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        return goblins.findByUsername(username)
            .map(GoblinPrincipal::new)
            .orElseThrow(() -> new UsernameNotFoundException("No such goblin"));
    }
}

public class GoblinPrincipal implements UserDetails {
    private final Goblin goblin;
    public GoblinPrincipal(Goblin goblin) { this.goblin = goblin; }
    @Override public String getUsername() { return goblin.getUsername(); }
    @Override public String getPassword() { return goblin.getPasswordHash(); }
    @Override public Collection<? extends GrantedAuthority> getAuthorities() {
        return List.of(new SimpleGrantedAuthority("ROLE_" + goblin.getRole()));   // the ROLE_ prefix is needed for hasRole()
    }
}
```
A `UserDetailsService` bean plus a `PasswordEncoder` bean is enough; Boot wires up the `DaoAuthenticationProvider` for you.

> **Compare:** this corresponds to a custom `IdentityStore` in Jakarta Security. In Quarkus it corresponds to `quarkus-security-jpa`, where you annotate the entity with `@UserDefinition`, `@Username`, `@Password` and `@Roles`, and there is no service to write.

**LDAP:**
```java
@Bean
EmbeddedLdapServerContextSourceFactoryBean contextSource() {     // embedded server, for development
    return EmbeddedLdapServerContextSourceFactoryBean.fromEmbeddedLdapServer();
}
// real server instead: new DefaultSpringSecurityContextSource("ldap://ldap.dragonbank.example:389/dc=dragonbank,dc=example")

@Bean
AuthenticationManager ldapAuthenticationManager(BaseLdapPathContextSource contextSource) {
    LdapPasswordComparisonAuthenticationManagerFactory factory =
        new LdapPasswordComparisonAuthenticationManagerFactory(contextSource, new BCryptPasswordEncoder());
    factory.setUserDnPatterns("uid={0},ou=goblins");
    factory.setPasswordAttribute("passcode");
    return factory.createAuthenticationManager();
}
```

## Legacy style (Spring Security 5.x and older)
You will still see this in older code and books. `WebSecurityConfigurerAdapter` was deprecated in 5.7 and removed in 6.0:
```java
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Autowired DataSource dataSource;

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.inMemoryAuthentication()
                .withUser("grizzlegut").password("{noop}shiny").authorities("ROLE_APPRAISER");
        // or JDBC. The "?" placeholders are bound as PreparedStatement parameters, so this is safe against SQL injection:
        auth.jdbcAuthentication().dataSource(dataSource)
            .usersByUsernameQuery("SELECT username, password, enabled FROM goblins WHERE username = ?")
            .authoritiesByUsernameQuery("SELECT username, authority FROM goblin_authorities WHERE username = ?")
            .passwordEncoder(new BCryptPasswordEncoder());
        // or LDAP
        auth.ldapAuthentication()
            .userSearchBase("ou=goblins").userSearchFilter("(uid={0})")
            .groupSearchBase("ou=groups").groupSearchFilter("member={0}")
            .passwordCompare().passwordEncoder(new BCryptPasswordEncoder()).passwordAttribute("passcode")
            .and().contextSource().url("ldap://ldap.dragonbank.example:389/dc=dragonbank,dc=example");
            // .root("dc=dragonbank,dc=example") for an embedded LDAP server
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests().antMatchers("/admin/**").hasRole("ADMIN").anyRequest().authenticated()
            .and().httpBasic();
    }
}
```
