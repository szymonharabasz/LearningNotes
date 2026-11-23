## Servlets
```java
@WebServlet(name = "VaultDoor", urlPatterns = "/vault-door")
public class VaultDoorServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String ip        = request.getRemoteAddr();
        String userAgent = request.getHeader("User-Agent");
        Dragon dragon    = (Dragon) request.getSession().getAttribute("DRAGON");

        if (dragon == null) { response.sendError(401); return; }

        request.getRequestDispatcher("/vault.jsp").forward(request, response);   // or include(...)
    }
}
```

### Filters
```java
@WebFilter(filterName = "KnightDetector", urlPatterns = "/*")   // or servletNames = {"VaultDoor", "Ledger"}
public class KnightDetectorFilter implements Filter {
    @Override public void init(FilterConfig config) { }          // init/destroy have default implementations since Servlet 4.0
    @Override public void destroy() { }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        if (!looksLikeAKnight(request)) {
            chain.doFilter(request, response);                   // not calling it = request stops here
        }
    }
}
```
JAX-RS has its own filters, which know about the resource method; see [Web services](Web%20services%20-%20JAX-RS%20and%20JAX-WS.md).

## WebSockets
Running example: `/cave-chat`, a chat room where dragons warn each other about knights.

### Server endpoint
```java
@ServerEndpoint("/cave-chat")           // or extend jakarta.websocket.Endpoint
public class CaveChatEndpoint {
    @OnOpen
    public void opened(Session session) { ... }

    @OnMessage
    public void broadcast(String message, Session sender) throws IOException {
        for (Session s : sender.getOpenSessions()) {
            if (s.isOpen()) s.getBasicRemote().sendText(message);   // getAsyncRemote() doesn't block
        }
    }

    @OnError public void error(Session session, Throwable t) { ... }
    @OnClose public void closed(Session session, CloseReason reason) { ... }
}
```

### Java client
```java
@ClientEndpoint
public class CaveChatClient {
    public CaveChatClient() throws Exception {
        ContainerProvider.getWebSocketContainer()
            .connectToServer(this, new URI("ws://localhost:8080/dragonbank/cave-chat"));   // context root + endpoint path
    }
    @OnMessage public void received(String message, Session session) { ... }
    // @OnOpen, @OnError, @OnClose as on the server
}
```

### JavaScript client
```javascript
const socket = new WebSocket("ws://localhost:8080/dragonbank/cave-chat");
socket.onopen    = event => { ... };
socket.onmessage = event => console.log(event.data);
socket.onerror   = event => { ... };

socket.send("Knight spotted near the north entrance!");
socket.close();
```
JSF has a higher-level push channel (`<f:websocket>` with `@Push`); see [JSF](Java%20Server%20Faces%202.3.md).
