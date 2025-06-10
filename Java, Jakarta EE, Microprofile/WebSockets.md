In server end-point:  
```Java
@ServerEndpoint("/mywebsocket")  
public class MyWebSocket {  
	@OnOpen public void connectionOpened() { … }  
    @OnMessage public synchronized void processMessage(Session session,  
	    String message) {  
        try {  
	        for (Session session : session.getOpenSessions()) {  
	            if (session.isOpen()) {  
	                session.getBasicRemote().sendText(message);  
                }  
            }  
        } catch {IOException ioe) { … }  
    }  
    @OnClose public void connectionClosed() { … }  
}
```
Or extend `javax.websocket.Endpoint`

Java client  
```Java
@ClientEndpoint  
public class MyWebSocketClient {  
    public MyWebSocketClient() {  
        try {  
            WebSocketContainer webSocketContainer =  
                ContainerProvider.getWebSocketContainer();  
            webSocketContainer.connectToServedr(this, new URI(  
                "ws://localhost:8080/mywebsocket/mywebsocket"));  
        } catch (IOException | DeploymentException | URISyntaxException ex)  
        { … }  
    }  
        
    @OnOpen public void connectionOpened(Session session) { … }  
	@OnMessage public synchronized void processMessage(String message,  
        Session session) {  
		try {  
            for (Session session : session.getOpenSessions()) {  
		        if (session.isOpen()) {  
                    session.getBasicRemote().sendText(message);  
                }  
            }  
        } catch {IOException ioe) { … }  
    }  
    @OnError public void errorReceived(Throwable throwable) { … }  
    @OnClose public void connectionClosed(CloseReason closeReason) { … }
}
```
In JavaScript client app:  
```html
<script type="text/javascript">  

var websocket; 
function init() {  
	websocket = new WebSocket(  
		'ws://localhost:8080/mywebsocket/mywebsocket');  
    websocket.onopen = function(event) {/*do something or delegate*/}  
    websocket.onmessage = function(event) {/*do something…*/}  
	websocket.onerror = function(event) {/*do something…*/}  
}  

function sendMessage() { // to be invoked e.g. in 'onclick' of a button  
	/* do something */  
    websocket.send(someMessage);  
}  

function closeConnection() { // to be invoked e.g. in 'onclick'  
	/* do something */  
    websocket.close();  
}  
window.addEventListener("load", init);  

</script>
```
    
In an application-scoped bean:  
```Java
@Inject @Push  
private PushContext pushContext;  
// ...  
pushContext.send("hello");
```
```JSP
<f:websocket channel="pushContext" onmessage"socketListener"/>  
<script type="text/javascript">  
    function socketListener(message, channel, event) { … }  
</script>
```
