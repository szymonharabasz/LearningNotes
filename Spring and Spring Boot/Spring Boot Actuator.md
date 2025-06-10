Registering a custom timer:  
```Java
@Controller  
public class OrderController {  
    private Timer timer;  
    public OrderController(MeterRegistry registry) {  
        this.timer = registry.timer("orders.submit");  
    }  
      
    @PostMapping("/orders")  
    public Order placeOrder(…) {  
        return timer.record(() -> {
	        /* lambda expression placing an order */
	    });  
    }  
      
    // more aspect oriented  
    @GetMapping("/orders")  
    @Timed("orders.summary")  
    public List<Order> orderSummary() {…}  
}
```
Registering a summary:  
```
@Controller  
public class RewardController {  
    private final DistributionSummary summary;  
    public RewardController(MeterRegistry registry) {  
        this.summary = DistributionSummary.builder()  
            .baseUnit("dollars")  
            .register(meter);  
    }  
      
    @PostMapping(value = "/rewards")  
    public ResponseEntity<Void> crearte(@RequestBody Reward reward) {  
        summary.record(reward.amount);  
    }  
}
```
Creating custom health indicator  
```
@Component  
public class MyCustomHealthCheck implements HealthIndicator {  
    @Override  
    public Health health;  

	if (!customHealthValidationCheck()) {  
        return Health  
            .down().  
            .withDetail("metricName", 0)  
            .build();  
    } else {  
        …  
    }  
}
```