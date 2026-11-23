JMS 2.0 "simplified API". For Kafka and MicroProfile Reactive Messaging see [Quarkus](Quarkus%20and%20MicroProfile.md).

Running example: knights' raids are reported to the queue `jms/RaidAlertQueue` (each alert is handled once). Bank news goes to the topic `jms/DragonNewsTopic` (every subscribed dragon gets it).

## `lookup` or `mappedName`?
`@Resource(lookup = "jms/...")` is the **standard, portable** JNDI name (since Java EE 6). `mappedName` is vendor-specific and you'll still see it in older examples; prefer `lookup`.

## Sending and receiving
The code is **the same for queues and topics**; only the injected `Destination` type differs (`Queue` or `Topic`).
```java
@Resource ConnectionFactory connectionFactory;
@Resource(lookup = "jms/RaidAlertQueue")  Queue raidAlerts;
@Resource(lookup = "jms/DragonNewsTopic") Topic dragonNews;

// JMSContext created by hand must be closed
try (JMSContext ctx = connectionFactory.createContext()) {
    ctx.createProducer().send(raidAlerts, "Sir Reginald approaches cave 7");
}

try (JMSContext ctx = connectionFactory.createContext()) {
    String alert = ctx.createConsumer(raidAlerts).receiveBody(String.class);   // blocks; there are also timeout variants
}
```
In a container you can simply `@Inject JMSContext context;`. The container manages it, so you don't close it.

**Message types:** `TextMessage`, `MapMessage`, `BytesMessage`, `StreamMessage`, `ObjectMessage`, and `Message` (headers and properties only).

## Message-driven bean
```java
@MessageDriven(activationConfig = {
    @ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "jms/RaidAlertQueue"),
    @ActivationConfigProperty(propertyName = "destinationType",   propertyValue = "jakarta.jms.Queue")
})
public class RaidAlertListener implements MessageListener {
    @Resource MessageDrivenContext mdc;

    @Override
    public void onMessage(Message message) {
        try {
            String alert = message.getBody(String.class);   // or ((TextMessage) message).getText()
            // ... wake the dragon
        } catch (JMSException e) {
            mdc.setRollbackOnly();                          // the message is redelivered
        }
    }
}
```

## Browsing a queue without consuming
```java
try (JMSContext ctx = connectionFactory.createContext()) {
    Enumeration<?> messages = ctx.createBrowser(raidAlerts).getEnumeration();
    while (messages.hasMoreElements()) {
        TextMessage msg = (TextMessage) messages.nextElement();
    }
}
```

## Durable topic subscriptions
A durable subscription keeps messages while the subscriber is offline. It is identified by the **client ID + the subscription name**:
```java
@Resource(lookup = "jms/DurableConnectionFactory")   // a factory configured with a client ID, e.g. "Ignatius"
ConnectionFactory connectionFactory;

JMSConsumer consumer = connectionFactory.createContext()
    .createDurableConsumer(dragonNews, "ignatius-news");
```
Only one connection can use a given client ID at a time. `createSharedDurableConsumer(topic, name)` (JMS 2.0) needs no client ID and lets several consumers share the subscription.
