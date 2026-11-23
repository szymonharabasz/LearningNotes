Server-side rendered web applications. For REST controllers see [REST with Spring Boot](REST%20with%20Spring%20Boot.md); for templates see [Thymeleaf](Thymeleaf.md).

> **Compare:** Spring MVC is a front-controller framework on top of the **Servlet API**. Its `DispatcherServlet` is a normal servlet; see [Servlets](../Java,%20Jakarta%20EE,%20Microprofile/Servlets%20and%20WebSockets.md).
> - The Jakarta EE counterpart for server-side UIs is the component-based [JSF](../Java,%20Jakarta%20EE,%20Microprofile/Java%20Server%20Faces%202.3.md), which works with backing beans and component state rather than controllers that return a view name.
> - Jakarta MVC is an action-based standard much closer to Spring MVC.
> - Quarkus uses Qute templates from JAX-RS resources.

## Controllers and request mappings
```java
@Controller                          // @RestController = @Controller + @ResponseBody on every method
@RequestMapping("/appraisals")
public class AppraisalController {

    @GetMapping                      // = @RequestMapping(method = RequestMethod.GET)
    public String list(Model model) {
        model.addAttribute("appraisals", service.findAll());
        return "appraisals";         // the view name
    }

    @PostMapping                     // also @PutMapping, @PatchMapping, @DeleteMapping
    public String create(@ModelAttribute AppraisalForm form) {
        service.create(form);
        return "redirect:/appraisals/confirmation";   // Post/Redirect/Get: always redirect after a POST
    }
}
```
**Parameters that can be injected into handler methods:** `HttpServletRequest`, `HttpSession`, `Principal`, `Locale`, `Model`, `Errors`/`BindingResult`, and others.

## Request data
```java
public String appraise(@RequestParam("treasureId") long treasureId,
                       @RequestParam(required = false) Integer coins,         // required = true by default
                       @RequestParam(defaultValue = "0") int bribe,
                       @PathVariable String kingdom,                          // from @GetMapping("/kingdoms/{kingdom}")
                       @RequestHeader("User-Agent") String agent,
                       HttpSession session) { ... }
```
- The name in the annotation can be omitted if the parameter has the same name. This requires compiling with `-parameters`, which Spring Boot's build plugins enable.
- An optional parameter of a **primitive** type (`int coins` with `required = false`) fails when the parameter is missing, because `null` can't be assigned to it. Use a wrapper type, `Optional`, or `defaultValue`.

> **Compare with JAX-RS:** `@RequestParam` corresponds to `@QueryParam`/`@FormParam` (Spring uses one annotation for both). `@PathVariable` corresponds to `@PathParam`, and `@RequestHeader` to `@HeaderParam`. Required-by-default is a Spring thing: a missing JAX-RS parameter is simply `null` (or its `@DefaultValue`).

## Model and view
These three variants are equivalent:
```java
// 1. Model parameter + view name
public String result(Model model) { model.addAttribute("value", 42); return "result"; }

// 2. ModelAndView
public ModelAndView result() { ModelAndView mv = new ModelAndView("result"); mv.addObject("value", 42); return mv; }

// 3. Raw servlet API (avoid)
public String result(HttpServletRequest request) {
    int coins = Integer.parseInt(request.getParameter("coins"));
    request.getSession().setAttribute("value", coins * 2);
    return "result";
}
```
**Form-backing objects:** request parameters are bound to the properties of a POJO. The name in `@ModelAttribute("appraisalForm")` defaults to the class name with a lowercase first letter:
```java
public class AppraisalForm {
    private long treasureId; private int coins;          // + getters and setters
    public int getValueAfterCommission() { return (int) (coins * 0.9); }
}

@PostMapping("/appraise")
public String appraise(@ModelAttribute AppraisalForm appraisalForm) { return "result"; }
```
```html
<form action="appraise" method="post">
    <input type="text" name="treasureId"/>
    <input type="text" name="coins"/>
</form>
<!-- result.jsp -->
Value after the goblins' cut: ${appraisalForm.valueAfterCommission}
```

## Validating forms
The constraint annotations themselves are in [Validation](Validation.md).
```java
@PostMapping("/appraise")
public String appraise(@Valid AppraisalForm appraisalForm, Errors errors) {   // Errors must come right after the validated argument
    if (errors.hasErrors()) return "appraisal-form";                          // show the form again
    ...
}
```
```html
<span th:if="${#fields.hasErrors('coins')}" th:errors="*{coins}"></span>
```

## Views
**JSP:**
```properties
spring.mvc.view.prefix=/WEB-INF/views/     # under WEB-INF, so the pages can't be requested directly
spring.mvc.view.suffix=.jsp
```
With Spring Boot you need `tomcat-embed-jasper` to compile JSPs. To be safe, put `<%@ page isELIgnored="false" %>` on the page.

**View controllers** map a URL directly to a view, without a controller method:
```java
@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addViewControllers(ViewControllerRegistry registry) {
        registry.addViewController("/").setViewName("home");
    }
}
```

## Without Spring Boot
`src/main/webapp/WEB-INF/web.xml`:
```xml
<servlet>
    <servlet-name>dragonbank</servlet-name>
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
</servlet>
<servlet-mapping>
    <servlet-name>dragonbank</servlet-name>
    <url-pattern>/</url-pattern>
</servlet-mapping>
```
`WEB-INF/dragonbank-servlet.xml`. The name `<servlet-name>-servlet.xml` is found by convention:
```xml
<beans ...>
    <ctx:component-scan base-package="com.dragonbank"/>
    <ctx:annotation-config/>
    <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix" value="/WEB-INF/views/"/>
        <property name="suffix" value=".jsp"/>
    </bean>
</beans>
```
