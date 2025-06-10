In dependencies, one can exclude z and include z, for example. One can add `spring-boot-devtools` with scope `runtime`
Custom application configuration in a WAR file, which doesn't execute `main() `method:
```Java
@SpringBootApplication  
public class App extends SpringBootServerInitializer {  
    protected SpringApplicationBuilder configure(
	    SpringApplicationBuilder app) {  
        return app.sourcer(App.class); // configuration classes  
    }  
}
```
There can also be a hybrid WAR which has both the above method and the `main()` method
Controller class:  
`@Controller`, `@RestController` (combination of `@Controller` and `@ResponseBody` which on the class level applies to return values of all methods)
In a web app beans can have:  
`@RequestScope`, `@SessionScope`, `@ApplicationScope`
Request mappings:
```Java
@RequestMapping("/")
@RequestMapping(value="customer", method="post")  
@PostMapping("customer")
@RequestMapping(value="customer", method="get")  
@GetMapping("customer")
@PutMapping, @PatchMapping, @DeleteMapping
```
Possible also `HttpMethod.GET|POST|PUT|DELETE|…`
Method arguments that can be injected:  
`HttpServletRequest`, `HttpSession`, `Principal`, `Locale`, …

View. In application properties:  
```
spring.mvc.view.prefix = /WEB-INF/views/ # folder under webapp folder, WEB-INF makes it private
spring.mvc.view.suffix = .jsp
```
Input JSP page or Thymeleaf template:  
```hyml
<form action="add">  
    <input type="text" name="a" />  
    <input type="text" name="b" />
```
In controller class:  
```Java
@RequestMapping("add")  
public String add(HttpServlerRequest request) {  
    int a = Integer.parseInt(request.getParameter("a"));  
    int b = Integer.parseInt(request.getParameter("b"));  
  
    int c = a + b;  
      
    HttpSession session = request.getSession();  
    session.setAttribute("c", c);  
      
    return "result";  
}
```
Returned value is the name of the view. Could be also:  
```Java
return "redirect:/confirmation"  
```
especially in the methods corresponding to POST requests
Handling request params:  
```Java
@RequestMapping("add")  
public String add(@RequestParam("a") int a, 
	@RequestParam("b", required=false) int b, HttpSession session) {  
    int c = a + b;  
      
    session.setAttribute("c", c);  
      
    return "result";  
}
```
If method parameter names are the same as request param names, the attributes in the annotation are not mandatory
Returning model and view together:  
```Java
@RequestMapping("add")  
public ModelAndView add(@RequestParam("a") int a, @RequestParam("b") int b) {
	ModelAndView mv = new ModelAndView("result");  
    int c = a + b;  
    mv.setObject("c", c);  
    return mv;  
}
```
Model as method parameter, retutning the name of the view to be rendered:  
```Java
@RequestMapping("add")  
public String add(@RequestParam("a") int a, 
	@RequestParam("b") int b, Model model) {  
    int c = a + b;
    model.addAttribute("c", c);    
    return "result";  
}
```
In the result page:  
`<%@page .…isELIgnored="false" %>` to be on the safe side  
Result is `${c}`

**Model attributes.** Model class:  
```Java
public class Addition {  
    private int a; private int b; /* getters and setters */  
    public int getC() { return a + b; } // for example  
}
```
Input page:  
```Java
<form action="add">  
    <input type="text" name="a" />  
    <input type="text" name="b" />
```
In the controller class:  
```Java
@RequestMapping("add")  
public String add(@ModelAtttribute("addition") Addition ad) {
    return "result";  
}
```
Annotation parameter is not needed if the same as the class name
In the result page:  
Result is: `${addition.c}`
```Java
@RequestParam(required = false) // default is true
```
Path variables also possible:  
```Java
@RequestMapping("/home/{color}")  
public String home(@Response("color") String col, Model model) { … }  
```
Annotation attribute again not needed if the name of the path variable is the same as the name of the method parameter
Request headers:  
```Java
@RequestMapping("/home")  
public String home(@RequestHeader("user-agent") String agent) { … }
```
In a Spring Boot application add Tomcat Jasper to Maven dependencies in order to parse JSP pages

**Validating input.** Annotate the request argument with `@Valid`. Inject `Errors errors` as the second argument of the request handler method. Check `if (errors.hasErrors()) { … }` and possibly return the form view
In the form:  
```html
<span th:if="${#fields.hasErrors('firstName')}" th:errors="*{firstName}" />  
```
Here: `#fields` is the property to access the form fields. It has a method `hasErrors()` with the parameter being the field name. The attribute `th:errors` displays errors related to the model property referenced as its value.

View controllers:  
```Java
@Configuration  
public class WebConfig implements WebMvcConfigurer {  
    @Override  
    public void addViewControllers(ViewControllerRegistry registry) {  
        registry.addViewController("/").setViewName("home");  
    }  
}
```
Without Spring Boot: in `/src/main/webapp/WEB-INF/web.xml`:  
```xml
<servlet>  
    <servlet-name>myservlet</servlet-mapping>  
    <servlet-class>org.springframework.web.servlet.DispatcherServlet
    </servlet-class>  
</servlet>  
<servlet-mapping>  
    <servlet-name>myservlet</myservlet>  
    <url-pattern>/</url-pattern>  
</servlet-mapping>
```
In `./WEB-INF/myservlet-servlet.xml`:  
```Java
<beans .…>  
    <ctx:component-scan base-package="com.example.myapp" />  
    <ctx:annotation-config />    
    <bean 
class="org.springframework.web.servlet.view.InternalResourceViewResolver">  
        <property name="prefix" value="/views/" />  
        <property name="suffix" value=".jsp" />  
    </bean>  
</beans>
```