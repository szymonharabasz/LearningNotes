**Consuming REST API with Web Client.** Create `WebClient` as a `@Bean`:  
```Java
return WebClient.builder().build();
```
Inject and use:  
```Java
public Mono<Payment> createPayment(String requestId, Payment payment) {  
    return webClient.post()  
        .uri(url + "/payment")  
        .header("requestId", requestId)  
        .body(Mono.just(payment), Payment.class)  
        .retrieve()  
         .bodyToMono(Payment.class);  
    }
```