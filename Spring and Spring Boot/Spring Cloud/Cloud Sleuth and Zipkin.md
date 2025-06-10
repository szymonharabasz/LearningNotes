Dependency:
```
spring-cloud-starter-sleuth
```
automatically adds the tracing IDs. It can be accessed like this:
```Java
@Autowired
Tracer tracer;
// ...
String traceId = tracer.currentSpan().context().traceIdString();
```
Dependency to integrate with Zipkin:
```
spring-cloud-sleuth-zipkin
```
Configuration (assuming a Docker service):
```
zipkin.baseUrl: zipkin:9411
spring.sleuth.sampler.percentage: 0.65
```
Adding a custom span:
```Java
ScopedSpan newSpan = tracer.startScopedSpan ("readCatsDataFromRedis"); 
try { ... }
finally {
	newSpan.tag("peer.service", "redis");
	newSpan.annotate("Client received");
	newSpan.finish();
}
```
Another dependency to use the ELK stack:
```
logstash-logback-encoder
```
Then Logback has to be configured in the file `/src/main/resources/logback-spring.xml`:
```XML
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <include resource="org/springframework/boot/logging/logback/base.xml"/>
    <springProperty scope="context" name="application_name"  
	    source="spring.application.name"/>

    <appender name="logstash" 
	    class="net.logstash.logback.appender.ogstashTcpSocketAppender">
       <destination>logstash:5000</destination>
       <encoder class="net.logstash.logback.encoder.LogstashEncoder"/>
    </appender>

    <root level="INFO">
        <appender-ref ref="logstash"/>
        <appender-ref ref="CONSOLE"/>
    </root>
    <logger name="org.springframework" level="INFO"/>
    <logger name="com.optimagrowth" level="DEBUG"/>
</configuration>
```
Alternatively, one can use other encoder to have a better control over the exposed fields:
```XML
<encoder 
	class="net.logstash.logback.encoder.LoggingEventCompositeJsonEncoder">
    <providers>
        <mdc> 
            <excludeMdcKeyName>X-B3-TraceId</excludeMdcKeyName>
            <excludeMdcKeyName>X-B3-SpanId</excludeMdcKeyName>
            <excludeMdcKeyName>X-B3-ParentSpanId</excludeMdcKeyName>
        </mdc>
        <context/>
        <version/>
        <logLevel/>
        <loggerName/>
        <pattern>
            <pattern>
                <omitEmptyFields>true</omitEmptyFields>
                {
                    "application": {
                        version: "1.0"
                    },
                    "trace": {
                        "trace_id": "%mdc{traceId}",
                        "span_id": "%mdc{spanId}",
                        "parent_span_id": "%mdc{X-B3-ParentSpanId}",
                        "exportable": "%mdc{spanExportable}"
                    }
                }
            </pattern>
        </pattern>
        <threadName/>
        <message/>
        <logstashMarkers/>
        <arguments/> 
        <stackTrace/>
    </providers>
</encoder>
```
A Logstash instance can be configured like this:
```
input {
  tcp {
    port => 5000
    codec => json_lines
  }
}

filter {
  mutate {
    add_tag => [ "manningPublications" ]
  }
}

output {
  elasticsearch {
    hosts => "elasticsearch:9200"
  }
}
```