Personal memos on Java, Jakarta EE, MicroProfile and related frameworks. They cover what is easy to forget, not everything.

## The running example: DragonBank
All code examples use the same made-up domain. **DragonBank** is the only bank where dragons can safely keep their gold.

| Concept | Meaning |
|---|---|
| `Dragon` | a customer; has a name, a wingspan and a fire temperature |
| `Hoard` | a dragon's deposit: `hoardNumber`, `goldCoins` |
| `Treasure` | an item in a hoard: gold, gem, artifact, or cursed ring |
| `Cave` | where a dragon lives (an address) |
| goblins | tellers, appraisers and the IT department; slow and often on strike |
| knights | raiders; they cause most of the failures and alarms |

## Files
| File | Contents |
|---|---|
| [Java language](Java%20language.md) | Language features, plus JAR and Gradle |
| [Java concurrency](Java%20concurrency.md) | Threads, executors, `CompletableFuture`, virtual threads |
| [Testing with JUnit and Mockito](Testing%20with%20JUnit%20and%20Mockito.md) | JUnit 5 and Mockito (shared by the Quarkus and Spring notes) |
| [Context and Dependency Injection](Context%20and%20Dependency%20Injection.md) | CDI: scopes, qualifiers, interceptors, decorators, events, `@Transactional` |
| [Enterprise JavaBeans](Enterprise%20JavaBeans.md) | Session beans, EJB transactions, concurrency, timers |
| [Java Persistence API](Java%20Persistence%20API.md) | Entity mapping, relationships, JPQL, Criteria API |
| [Bean Validation](Bean%20Validation.md) | Constraints, custom constraints, programmatic validation |
| [Web services - JAX-RS and JAX-WS](Web%20services%20-%20JAX-RS%20and%20JAX-WS.md) | REST resources, providers, async, SSE, JAX-RS client, SOAP |
| [Serialization and deserialization of XML and JSON](Serialization%20and%20deserialization%20of%20XML%20and%20JSON.md) | JSON-B, JSON-P, JAX-B, DOM, SAX |
| [Java Message Service](Java%20Message%20Service.md) | Queues, topics, message-driven beans |
| [Servlets and WebSockets](Servlets%20and%20WebSockets.md) | Servlets, filters, WebSocket endpoints |
| [Security](Security.md) | Jakarta Security: identity stores, authentication mechanisms |
| [Java Server Faces 2.3](Java%20Server%20Faces%202.3.md) | JSF tags, validation, conversion, AJAX, Faces Flow, push |
| [Quarkus and MicroProfile](Quarkus%20and%20MicroProfile.md) | MP Config, REST Client, Fault Tolerance, Health, Metrics, JWT, Reactive Messaging, Panache, Mutiny, containers |
| [Vaadin Flow](Vaadin%20Flow.md) | Server-side Java UI: components, routing, binding, styling |
| [Vaadin Hilla and Fusion](Vaadin%20Hilla%20and%20Fusion.md) | TypeScript/React front ends calling Java endpoints |

**Spring:** the [Spring notes](../Spring%20and%20Spring%20Boot/README.md) use the same domain. Their README has a table mapping Spring concepts to the Jakarta EE, MicroProfile and Quarkus ones. When both stacks use the same specification (JPA, Bean Validation, Servlets, JUnit/Mockito), the details are kept here, and the Spring notes link to them.

## `javax` vs `jakarta`
Java EE 8 and Jakarta EE 8 use `javax.*` packages. Since **Jakarta EE 9** the packages are `jakarta.*`, for example `jakarta.ws.rs`, `jakarta.persistence` and `jakarta.inject`. Quarkus 3 uses `jakarta.*`. The APIs are otherwise the same.
