> **Compare with MicroProfile Reactive Messaging** ([Quarkus - Reactive messaging](../../Java,%20Jakarta%20EE,%20Microprofile/Quarkus%20and%20MicroProfile.md#reactive-messaging)). The ideas map almost one to one:
>
> | Spring Cloud Stream | MicroProfile Reactive Messaging |
> |---|---|
> | binder (Kafka, RabbitMQ) | connector (`smallrye-kafka`, ...) |
> | binding | channel |
> | `spring.cloud.stream.bindings.<binding>.destination` | `mp.messaging.[incoming\|outgoing].<channel>.topic` |
> | `Consumer<T>` bean | `@Incoming` method |
> | `Supplier<T>` bean | `@Outgoing` method |
> | `Function<T,R>` bean | `@Incoming` + `@Outgoing` method |
> | `StreamBridge.send(...)` | `Emitter.send(...)` |
> | consumer `group` | Kafka `group.id` |
>
> For JMS (point-to-point queues in Jakarta EE) see [JMS](../../Java,%20Jakarta%20EE,%20Microprofile/Java%20Message%20Service.md).

Dependencies: `spring-cloud-stream` and `spring-cloud-stream-binder-kafka` (older: `spring-cloud-starter-stream-kafka`).

Running example: `knight-watch-service` publishes knight sightings, and `appraisal-service` reacts by temporarily raising its appraisal fees.

## Functional style (Spring Cloud Stream 3.1+)
```java
@Bean
public Consumer<KnightSighting> onSighting() {                  // binding name: onSighting-in-0
    return sighting -> fees.raiseFor(sighting.kingdom());
}

@Bean
public Function<KnightSighting, DragonAlarm> raiseAlarm() {     // raiseAlarm-in-0 -> raiseAlarm-out-0
    return s -> new DragonAlarm("Knight " + s.name() + " near " + s.kingdom());
}

// Sending from imperative code (e.g. a REST controller)
@Autowired StreamBridge streamBridge;
streamBridge.send("sightings-out-0", new KnightSighting("Sir Reginald", "Eriador"));
```
```properties
spring.cloud.function.definition=onSighting;raiseAlarm          # needed when there are several function beans
spring.cloud.stream.bindings.onSighting-in-0.destination=knight-sightings
spring.cloud.stream.bindings.onSighting-in-0.group=appraisal-service       # consumer group: each message goes to one instance of the group
spring.cloud.stream.bindings.raiseAlarm-out-0.destination=dragon-alarms
spring.cloud.stream.bindings.sightings-out-0.destination=knight-sightings
spring.cloud.stream.bindings.sightings-out-0.content-type=application/json # JSON is the default
spring.cloud.stream.kafka.binder.brokers=localhost:9092
```

## Annotation style (removed in Spring Cloud Stream 4)
You'll still find this in older code and books:
```java
@EnableBinding(Source.class)                 // Source = one output channel "output"; Sink = one input channel "input"
@SpringBootApplication
public class KnightWatchApplication { ... }

source.output().send(MessageBuilder.withPayload(sighting).build());

@EnableBinding(Sink.class)
public class AppraisalServiceApplication {
    @StreamListener(Sink.INPUT)
    public void onSighting(KnightSighting sighting) { ... }
}

// Custom channels
public interface WatchChannels {
    @Input("inboundSightings")   SubscribableChannel sightingsIn();
    @Output("outboundAlarms")    MessageChannel alarmsOut();
}
```
```properties
spring.cloud.stream.bindings.output.destination=knight-sightings
spring.cloud.stream.bindings.input.destination=knight-sightings
spring.cloud.stream.bindings.input.group=appraisal-service
spring.cloud.stream.bindings.inboundSightings.destination=knight-sightings
spring.cloud.stream.kafka.binder.zkNodes=localhost           # ZooKeeper; obsolete with modern Kafka
```
