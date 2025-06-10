Annotate class with `@WebService` and methods with `@WebMethod` (the latter one only for readability, all public methods will be exposed as web methods)
Same if the class is EJB
Generate client classes: `wsimport address?wsdl` and use them
Inside the client:  
```Java
@WebServiceRef(wsdlLocation = "address?wsdl")  
private MyService myService;
```