Add dependency 
```
spring-security-oauth2-autoconfigure
```
Annotate `WebSecurityConfigurerAdapter` with `@EnableOAuth2Sso`
Implement:  
```Java
@Override  
protected void configure(HttpSecurity security) thtows Exception {  
    security.csrf().disable()  
        .authorizeRequests().  
	    .requestMatchers("/login").permitAll()  
        .anyRequest().authenticated()  
        .and().httpBasic();  
}
```
Add to `application.properties` properties for `security.oauth2.client`
In any controller define:  
```Java
@RequestMapping("user")  
@ResponseBody  
public Principal user(Principal principal) {  
    return principal;  
}
```
###### Using Keycloak
Add dependency:
```
keycloak-spring-boot-starter
keycloak-adapter-bom
```
Properties:
```
keycloak.realm = my-realm
keycloak.auth-server-url = http://keycloak:8080/auth
keycloak.ssl-required = external
keycloak.resource = ostock
keycloak.credentials.secret = 5988f899-a5bf-4f76-b15f-f1cd0d2c81ba
keycloak.use-resource-role-mappings = true
keycloak.bearer-only = true
```
Define configuration class
```Java
@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(jsr250Enabled = true)
public class SecurityConfig extends KeycloakWebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        super.configure(http);
        http.authorizeRequests()
            .anyRequest()
            .permitAll();
        http.csrf().disable();
    }

    @Autowired
    public void configureGlobal(AuthenticationManagerBuilder auth) 
	    throws Exception {
		
		KeycloakAuthenticationProvider keycloakAuthenticationProvider = 
	        keycloakAuthenticationProvider();
	    keycloakAuthenticationProvider.setGrantedAuthoritiesMapper(
	        new SimpleAuthorityMapper());
	    auth.authenticationProvider(keycloakAuthenticationProvider);
    }

    @Bean
    @Override
    protected SessionAuthenticationStrategy sessionAuthenticationStrategy() {
        return new RegisterSessionAuthenticationStrategy(
	        new SessionRegistryImpl());
    }

    @Bean
    public KeycloakConfigResolver keycloakConfigResolver() {
        return new KeycloakSpringBootConfigResolver();
    }
}
```
In a client microservice, one can use Keycloak-enables REST template:
```Java
@Autowired
public KeycloakClientRequestFactory keycloakClientRequestFactory;

@Bean
@Scope(ConfigurableBeanFactory.SCOPE_PROTOTYPE) 
public KeycloakRestTemplate keycloakRestTemplate() { 
	return new KeycloakRestTemplate(keycloakClientRequestFactory); 
}
```