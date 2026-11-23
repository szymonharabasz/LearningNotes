Jakarta Security (formerly the Java EE Security API). For token-based security (MicroProfile JWT, Keycloak), see [Quarkus](Quarkus%20and%20MicroProfile.md).

You put the definition annotations below on any CDI bean, typically an `@ApplicationScoped` configuration class.

## Identity stores (where the users and groups are kept)
**Relational database:**
```java
@DatabaseIdentityStoreDefinition(
    dataSourceLookup = "jdbc/dragonAuth",
    callerQuery = "SELECT password FROM dragons WHERE name = ?",
    groupsQuery = "SELECT g.name FROM dragon_groups dg JOIN groups g ON g.id = dg.group_id "
                + "JOIN dragons d ON d.id = dg.dragon_id WHERE d.name = ?")
```
**Gotcha:** the default `hashAlgorithm` is `Pbkdf2PasswordHash`, so the passwords in the DB must be stored as PBKDF2 hashes. Plain-text passwords will never match.

**LDAP:**
```java
@LdapIdentityStoreDefinition(
    url = "ldap://ldap.dragonbank.example:33389/",
    callerBaseDn = "ou=dragons,dc=dragonbank,dc=example",
    groupSearchBase = "ou=groups,dc=dragonbank,dc=example")
```
**Custom:** implement `IdentityStore` as an `@ApplicationScoped` bean:
```java
@Override
public CredentialValidationResult validate(Credential credential) {
    UsernamePasswordCredential login = (UsernamePasswordCredential) credential;
    if (login.compareTo("goblin-chief", "shiny")) {
        return new CredentialValidationResult("goblin-chief", Set.of("teller", "admin"));
    }
    return CredentialValidationResult.INVALID_RESULT;
}
```
To use a custom identity store in **WildFly**, first run the Elytron configuration script:
https://github.com/wildfly/quickstart/blob/main/ee-security/configure-elytron.cli

## Authentication mechanisms (how credentials are collected)
**Basic.** The browser shows its built-in login dialog:
```java
@BasicAuthenticationMechanismDefinition(realmName = "DragonBank")
```
**Form.** A plain HTML form posting to `j_security_check`:
```java
@FormAuthenticationMechanismDefinition(
    loginToContinue = @LoginToContinue(loginPage = "/login.html", errorPage = "/login-error.html"))
```
```html
<form method="POST" action="j_security_check">
    <input type="text" name="j_username"/>
    <input type="password" name="j_password"/>
</form>
```
**Custom form.** You write the login page yourself (for example in JSF) and call `SecurityContext.authenticate` from it:
```java
@CustomFormAuthenticationMechanismDefinition(
    loginToContinue = @LoginToContinue(loginPage = "/faces/login.xhtml", errorPage = ""))
```
```xml
<h:inputText   value="#{credentials.name}"/>
<h:inputSecret value="#{credentials.password}"/>
<h:commandButton action="#{loginController.login}" value="Enter the vault"/>
```
```java
@Named @RequestScoped
public class LoginController {
    @Inject SecurityContext securityContext;      // jakarta.security.enterprise.SecurityContext
    @Inject FacesContext facesContext;
    @Inject Credentials credentials;

    public void login() {
        AuthenticationStatus status = securityContext.authenticate(
            (HttpServletRequest)  facesContext.getExternalContext().getRequest(),
            (HttpServletResponse) facesContext.getExternalContext().getResponse(),
            AuthenticationParameters.withParams()
                .credential(new UsernamePasswordCredential(credentials.getName(), credentials.getPassword())));

        if (status == AuthenticationStatus.SEND_CONTINUE) {
            facesContext.responseComplete();          // the mechanism takes over (e.g. a redirect)
        } else if (status == AuthenticationStatus.SEND_FAILURE) {
            facesContext.addMessage(null, new FacesMessage("Wrong password. The dragon is watching you."));
        }
    }
}
```

## Authorization
```java
@RolesAllowed({"dragon", "teller"})       // also @PermitAll, @DenyAll; works on EJBs, CDI beans (in most servers), JAX-RS resources
public Hoard getHoard(Long hoardNumber) { ... }

securityContext.isCallerInRole("teller");
securityContext.getCallerPrincipal();
```
