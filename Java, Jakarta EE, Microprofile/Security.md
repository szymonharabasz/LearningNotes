**Security stores.** In a relational database: annotate application config class with:  
```Java
@DatabaseIdentityStoreDefinition(  
    dataSourceLookup = "jdbc/userAuth",  
    callerQuery = "select password from users where name = ?",  
    groupQuery = "select g.GROUP NAME from USER_GROUPS ug, users u, GROUPS g" 
        + "where u.USERNAME=? and ug.USER_ID = u.user_id and g.GROUP_ID = ug.GROUP_ID")
```
In an LDAP database: annotate with:  
```Java
@LdapIdentityStoreDefinition(  
    url = "ldap://myldapserver:33389/",  
    callerBaseDn = "ou=caller,dc=packtpub,dc=com",  
    groupSearchBase = "ou=group,dc=packtpub,dc=com")
```
Custom: implement `IdentityStore`:  
```Java
@Override  
public CredentialValidationResult validate(Credential credential) {  
    UsernamePasswordCredential usernamePasswordCredential  
        = (UsernamePasswordCredential)credential;  
    CredentialValidationResult credentialValidationResult;  
    if (usernamePasswordCredential.compareTo("admin","admin1")) {  
        credentialValidationResult = new CredentialValidationResult(  
            "admin",userAdminRoleSet); // Set<String>  
    } else {  
        credentialValidationResult = 
	        CredentialValidationResult.INVALID_RESULT;  
    }  
    return credentialValidationResult;  
}
```
To use own identity store in **WIldFly**, one has to execute the script from
[https://github.com/wildfly/quickstart/blob/main/ee-security/configure-elytron.clix](https://github.com/wildfly/quickstart/blob/main/ee-security/configure-elytron.clix)**

**Authentication mechanisms.** Basic, web browser displays standard window asking for username and password: annotate with  
```Java
@BasicAuthenticationMechanismDefinition(realmName = "My Realm")
```
Form authentication: using a standard HTML form:  
```HTML
<form method="POST action="j_security_check">  
    <input type="text" name="j_username"/>  
    <input type="passowrd" name="j_password"/>  
</form>  
```    
and annotade the secured resource with:  
```Java
@FormAuthenticationMechanismDefinition(  
    loginToCOntinue = @LoginToContinue(  
        loginPage = "/login.html", errorPage="/loginerror.html"))
```
Custom form authentication - element to authenticate:  
```Java
@CustomFormAuthenticationDefinitionMechanism(  
    loginToCOntinue = @LoginTOContinue(  
        loginPage = "/faces/login.xhtml", errorPage=""))  
}  
```
In the login Faces page:  
```JSP
<h:inputText id="userName" value="#{user.userName}"/>  
<h:inputSecret id="password" value="#{user.password}"/>  
<h:commandButton action="#{loginController.login}" value="Login"/>  
```    
Controller 
```Java
@Named @RequestScoped public class LoginController {  
	@Inject private SecurityContext securityContext;  
	…  
    UsernamePasswordCredential usernamePasswordCredential  
        = new UsernamePasswordCredential(user.getUserName(), 
	        user.getPassword());  
    AuthenticationParameters authenticationParameters = 
		AuthenticationParameters.withParams()
			.credential(usernamePasswordCredential);     AuthenticationStatus
	authenticationStatus = 
		securityContext.authenticate(  
	        facesContext.getExternalContext().getRequest(),  
            facesContext.getExternalContext().getResponse(),  
            authenticationParameters);  
    if (authenticationStatus.equals(AuthenticationStatus.SEND_CONTINUE)) {  
		facesContext.responseComplete();  
    } else if 
	    (authenticationStatus.equals(AuthenticationStatus.SEND_FAILURE)) {  
        facesContext.addMessage(null, new FacesMessage("Login error"));  
    }  
}
```
9. In EJB:  
```Java
@RolesAllowed( {"appuser", "appadmin"} ) public User getUser(Long userId) { … }
```