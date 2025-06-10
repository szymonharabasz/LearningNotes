Sending a message to a queue:  
```Java
@Resource  
private ConnectionFactory connectionFactory;  
@Resource(lookup="jms/MyMessageQueue")  
Queue queue;  
.…  
JMSProducer producer = connectionFactory.createContext().createProducer();  
.…  
jmsProducer.send(queue,"Some message");
```
Sending message to a topic:  
```Java
@Resource  
private ConnectionFactory connectionFactory;  
@Resource(lookup="jms/MyMessageTopic")  
Topic topic;  
.…  
JMSProducer producer = connectionFactory.createContext().createProducer();  
.…  
jmsProducer.send(topic,"Some message");
```
One can also directly `@Inject JMSContext`
Retrieving message from a queue:  
```Java
@Resource  
private ConnectionFactory connectionFactory;  
@Resource(mappedName="jms/MyMessageQueue")  
Queue queue;  
.…  
JMSConsumer consumer =  
    connectionFactory.createContext().createConsumer(queue);  
.…  
message = consumer.receiveBody(String.class);
```
Retrieving message from a topic:  
```Java
@Resource  
private ConnectionFactory connectionFactory;  
@Resource(mappedName="jms/MyMessageTopic")  
Topic topic;  
.…  
JMSConsumer consumer =  
    connectionFactory.createContext().createConsumer(topic);  
.…  
message = consumer.receiveBody(String.class);
```
One publication shows `mappedName` in `@Resource`, another lookup, CHECK IT!
Types of messages:
```Java
TextMessage
MapMessage
BytesMessage
StreamMessage
ObjectMessage
Message
```
Consuming in Message Driven Beans (modern way):  
```Java
@MessageDriven(  
    activationConfig = @ActivationConfigProperty(  
           propertyName = "destinationType",  
        propertyValue = "javax.jms.Queue"  
    ),  
    mappedName = "jms/MyMessageQueue")  
public class MyMessageListener implements MessageListener {  
    @Resource  
    private MessageDrivenContext mdc;  
    @Override  
    public void onMessage(Message message) {  
        try {  
            … ((TextMessage)message).getText() …  
        } catch (JMSException e) { … }  
    }  
}
```
8. Browsing message queue:  
```Java
@Resource  
private ConnectionFactory connectionFactory;  
@Resource(mappedName="jms/MyMessageQueue")  
Queue queue;  
.…  
QueueBrowser browser =  
    connectionFactory.createContext().createBrowser(queue);  
Enumeration messageEnumeration = browser.getEnumeration();  
.…  
while (messageEnumeration.hasMoreElements()) {  
    textMessage = (TextMessage)messageEnumeration.nextElement();  
}
```
Creating durable consumer:  
```Java
@Resource(mappedName="jms/MyDurableConnectionFactory")  
private ConnectionFactory connectionFactory;  
@Resource(mappedName="jms/MyMessageTopic")  
Topic topic;  
.…  
JMSConsumer consumer = connectionFactory.createContext()  
    .createDurableConsumer(topic,"Subscriber1");  
```
The property `ClientId` of the connection factory has to be set to `Subscriber1`. Only one JMS client can use this client id.
