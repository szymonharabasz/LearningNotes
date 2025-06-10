Dependencies:
```
spring-cloud-stream
spring-cloud-starter-stream-kafka
```
In the application class:
```Java
@EnableBinding(Source.class)
@SpringBootApplication
```
Sending a message (`Source source` is injected):
```Java
source.output().send(MessageBuilder.withPayload(change) .build());
```
Properties for output:
```
spring.cloud.stream.bindings.output.destination = litterBoxChangeTopic
spring.cloud.stream.bindings.output.content-type = application/json
spring.cloud.stream.kafka.binder.zkNodes = localhost
spring.cloud.stream.kafka.binder.brokers = localhost
```
Receiving a message:
```Java
@EnableBinding(Sink.class)
public class LicenseServiceApplication {

   @StreamListener(Sink.INPUT)
   public void loggerSink(LitterBoxChangeModel boxChange) { ... }
}
```
Properties for input:
```
#Some properties removed for conciseness

spring.cloud.stream.bindings.input.destination = orgChangeTopic
spring.cloud.stream.bindings.input.content-type = application/json
spring.cloud.stream.bindings.input.group = licensingGroup
spring.cloud.stream.kafka.binder.zkNodes = localhost
spring.cloud.stream.kafka.binder.brokers = localhost
```
Custom channels:
```Java
public interface CustomChannels {
    @Input("inboundLitterBoxChanges")
    SubscribableChannel inboundBox();

	@Output("outboundLitterBoxChanges")
	MessageChannel outboundBox();
}
```
Then in the property file one has to use, for example:
```
spring.cloud.stream.bindings.inboundLitterBoxChanges.destination = litterBoxChangeTopic
```