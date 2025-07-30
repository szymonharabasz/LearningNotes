1. Security: adding spring-boot-starter-security provides skeleton functionality. This already protects all endpoints, in the browser a pop-up window will be displayed.
2. Annotate a @Configuration class with extra @EnableWebSecurity and extend WebSecurityConfigurerAdapter  
    This already creates a rudimentary web page for login
3. Securing endpoints by creating a bean:  
    @Bean  
    public SecurityFilterChain filterChain(HttpSecurity httpSecurity) ehrows Exception {  
        httpSecurity.authorizeHttpRequests((authz) -> authz  
            .requestMatchers("/signup","/about").permitAll()  
            .requestMatchers(HttpMethod.PUT, "/accounts/edit*").hasRole("ADMIN")  
            .requestMatchers("/accounts/**").hasRole("ADMIN")  
            .requestMatchers("/admin/**").hasAnyRole("USER", "ADMIN")  
            // securing Spring Boot Actuator endpoints  
            .requestMatchers(EndpointRequest.to(HealthEndpoint.class)).permitAll()  
            .requestMatchers(EndpointRequest.toAnyEndpoint()).hasRole("ACTUATOR")  
            .anyRequest.authenticated())  
        // Basic authentication:  
        .httpBasic(withDefaults());  
        // or HTTP form authentication:  
        .formLogin(form -> form  
            .loginPage("/login")  
            .permitAll())  
        .logout(logout -> logout  
            .logoutSuccessUrl("/home")  
            .permitAll());  
         
        return httpSecurity.build();  
    }  
    @Bean  
    public WebSecurityCustomizer webSecurityCustomizer() {  
        // no filter applied, by-passing any security  
        return (web) -> web.ignoring().requestMatchers("/ignore1", "/ignore2");  
    }  
    @Bean  
    public InMemoryUserDetailsManager userDetailsManager() {  
        // Currently: BCryptPasswordEncoder (recommended), creates {bcrypt}hash  
        PasswordEncoder passwordEncoder =  
            PasswordEncoderFactories.createDelegatingPasswordEncoder();  
      
        UserDetails user = User  
            .withUsername("user")  
            .password(passwordEncoder.encode("user"))  
            .roles("USER")  
            .build();  
        UserDetails admin = User  
            .withUsername("admin")  
            .password(passwordEncoder.encode("admin"))  
            .roles("ADMIN")  
            .build();  
        return new InMemoryUserDetailsManager(user, admin);  
    }  
    // In production:  
    UserDetailsManager userDetailsManager(DataSource dataSource) {  
        return new JdbcUserFryailsManager(dataSource);  
    }
4. Securing business methods:  
    // In one of configuration methods  
    @EnableMethodSecurity  
      
    @PreAuthorize("hasRole('MEMBER') && #order.owner.name == principal.username")  
    public Item findItem(Order order, long itemNumber) { … }  
    // or  
    @PostAuthorize(…)
5. In memory user store (in the config class as described before:  
    @Override  
    protected void configure(AuthenticationManagerBuilder auth)  
        throws Exception {  
        auth  
            .inMemoryAuthentication()  
                .withUser("buzz")  
                    .password("infinity")  
                    .authorities("ROLE_USER")  
            .and()  
                .withUser("woody")  
                    .password("bullseye")  
                    .authorities("ROLE_USER");  
    }
6. JPA data store

7. Add:

8. sprring-boot-starter-data-jpa
9. mysql-connector-java

10. Define datasource properties in application.properties
11. Define user enity
12. Define user repository:  
    interface UserRepository exptends JpaRepository<User, Long> {  
        User findByUsername(String username);  
    }
13. Implement user details:  
    public class UserPrinciplal implements UserDetails {  
        private User user;  
        public UserPrincipal(User user) { this.user = user; }  
      
        @Override  
        public String getUsername() { return user.getUsername(); }  
      
        @Override  
        public String getPassword() { return user.getPassword(); }  
      
        @Override  
        public Collection<? extends GrantedAuthority> getAuthorities() {  
            return Collections.singleton(new SimpleGrantedAuthority("USER"));  
        }  
      
    }
14. Define user details service:  
    @Service  
    public class MyUserDetailsService implements UserDetailsService {  
      
        @Autowired    UserRepository userRepository;  
      
        @Override UserDetails loadUserByUsername(String unsername)  
            throws UsernameNotFoundException {  
      
            User user = userRepository.findByUsername(username);  
            if (user == null) throw new UsernameNotFoundException("User not found");  
      
            return new UserPrincipal(user);  
             
        }  
    }
15. Security configuration:  
    @Configuration  
    @EnableWebSecurity  
    public class AppSecurityCOnfig extends WebSecurityConfigurerAdapter {  
      
        @Autowired  
        private UserDetailsService userDetailsService;  
      
        @Bean  
        public AuthenticationProvider authenticationProvider() {  
            DaoAuthenticationProvider provider = new DaoAuthenticationProvider();  
            provider.setUserDetailsService(userDetailsService);  
            provider.setPasswordEncoder(new BCryptPasswordEncoder);  
        }  
      
        @Bean  
        @Override  
        protected UserDetailsService userDetailsService() {  
            List<UserDetails> users = new ArrayList<>();  
            users.add(User.withDefaultParrwordEncoder()  
                .username("alice")  
                .password("1234")  
                .rolses("USER")  
                .build());  
            return new InMemoryUserDetailsManager(users);  
        }  
    }

16. Other JDBC-based approach (in the config class extending WebSecurityConfigurerAdapter) - is it safe against injection attack?

@Autowired  
DataSource dataSource;  
  
@Override  
protected void configure(AuthenticationManagerBuilder auth) throws Exception {  
    auth  
        .jdbcAuthentication()  
        .dataSource(dataSource);  
            .usersByUsernameQuery(  
                "select username, password, enabled from Users " +    
                "where username=?")  
            .authoritiesByUsernameQuery(  
                "select username, authority from UserAuthorities " +  
                "where username=?")  
            .passwordEncoder(new StandardPasswordEncoder("53cr3t");  
}

1. BCryptPasswordEncoder— The strongest (?)
2. NoOpPasswordEncoder— Don't use

3. Pbkdf2PasswordEncoder
4. SCryptPasswordEncoder
5. StandardPasswordEncoder

6. LDAP-based:  
    @Override  
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {  
          auth.ldapAuthentication()  
              .userSearchBase("ou=people")  
              .userSearchFilter("(uid={0})")  
              .groupSearchBase("ou=groups")  
              .groupSearchFilter("member={0}")  
              .passwordCompare()  
              .passwordEncoder(new BCryptPasswordEncoder())  
              .passwordAttribute("passcode")  
              .contextSource()  
              .url("ldap://tacocloud.com:389/dc=tacocloud,dc=com");  
    }or                     .root("dc=tacocloud,dc=com");  
    when an embedded LDAP server is used
7. Using OAuth2:

8. Add dependency spring-security-oauth2-autoconfigure
9. Annotate WebSecurityConfigurerAdapter with @EnableOAuth2Sso
10. Implement:  
    @Override  
    protected void configure(HttpSecurity security) thtows Exception {  
        security.csrf().disable()  
            .authorizeRequests().  
    tchers("/login").permitAll()  
            .anyRequest().authenticated()  
            .and().httpBasic();  
    }
11. Add to application.properties properties for security.oauth2.client
12. In any controller define:  
    @RequestMapping("user")  
    @ResponseBody  
    public Principal user(Principal principal) {  
        return principal;  
    }