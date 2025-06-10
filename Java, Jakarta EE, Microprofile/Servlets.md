Definiting.a servlet
```Java
@WebServlet(name="Servlet1", urlPatterns="/cdi-example")  
public class ExampleServlet extends HttpServlet {  
	@Override  
    protected void doGet(HttpServletRequest request,  
        HttpServletResponse response) { … }  
}
```
Defining a filter
```Java
@WebFilter(filterName="LogAccess", urlPatterns="/")  
public class LogAccessFilter implements Filter {  
    public void init(FilterConfig config) throws ServletException { … }  
    public void destroy() { … }  
    public void doFIlter(ServletRequest request, ServletResponse response,  
	    FilterChain chain) throws ServletException, IOException {  
        if (…) { chain.doFilter(request, response);  
    } 
}
```
Other way of binding a filter
```Java
@WebFilter(filterName="LogAccess", servletNames={"Servlet1", "Servlet2"})
```
Extracting useful request-related information
```Java

String ip = httpServletRequest.getRemoteAddr();  
String userAgent = httpServletRequest.getHeader("UserAgent");  
httpServletRequest.getSession().getAttribute("USER");  
httpServlet.getServletContext().getRequestDispatcher("/resultPage.jsp")  
    .proceed(request, response);  
httpServletResponse.sendError(401);
    ```