Plain Java SE concurrency. For the server-side versions see:
- `ManagedExecutorService` in [CDI](Context%20and%20Dependency%20Injection.md)
- `@Asynchronous` in [EJB](Enterprise%20JavaBeans.md) and in MicroProfile Fault Tolerance ([Quarkus](Quarkus%20and%20MicroProfile.md))
- Mutiny `Uni`/`Multi` in [Quarkus](Quarkus%20and%20MicroProfile.md)

## Threads
```java
Thread thread = new Thread(Vault::countGold);    // pass a Runnable...
thread.setName("gold-counter");
thread.start();
thread.join();
Thread.currentThread().getName();

class GoblinWorker extends Thread {              // ...or extend Thread
    GoblinWorker(String name) { super(name); }
    @Override public void run() { System.out.println(getName() + " is counting coins"); }
}
new GoblinWorker("Grizzlegut").start();
```

### Handling `InterruptedException`
Never swallow it. Restore the interrupted flag so that code further up the stack can see it:
```java
catch (InterruptedException e) {
    Thread.currentThread().interrupt();
    throw new RuntimeException(e);
}
```

## Executors
`ExecutorService` is `AutoCloseable` since JDK 19. `close()` waits for the submitted tasks to finish:
```java
try (ExecutorService executor = Executors.newFixedThreadPool(5)) {
    for (int i = 0; i < 10; i++) {
        final int hoardNumber = i;
        executor.submit(() -> appraise(hoardNumber));
    }
}

// Fork/Join: work stealing, good cache affinity for divide-and-conquer tasks
new ForkJoinPool().submit(() -> { /* ... */ }).join();
```

## Virtual threads
```java
Thread.startVirtualThread(() -> System.out.println(appraiser.appraise("crown")));

Thread unstarted = Thread.ofVirtual().unstarted(() -> System.out.println("Roar!"));   // also Thread.ofPlatform()
unstarted.start();

try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    executor.submit(this::countGold);
}
```

## `CompletableFuture`
```java
CompletableFuture.runAsync(() -> countGold());              // no result
CompletableFuture.supplyAsync(() -> appraise("crown"));     // with a result
future.get();                                               // blocks; join() is the unchecked variant

// Transform and consume
appraiser.appraise("crown")
    .thenApply(value -> value.multiply(GOBLIN_COMMISSION))
    .thenAccept(value -> System.out.println("Worth " + value));

// Sequential: the second call needs the first result
appraiser.appraise("crown")
    .thenCompose(crownValue -> appraiser.appraise("sceptre")
        .thenApply(sceptreValue -> crownValue.add(sceptreValue)));

// Parallel: both calls run at the same time
CompletableFuture<BigDecimal> crown   = appraiser.appraise("crown").toCompletableFuture();
CompletableFuture<BigDecimal> sceptre = appraiser.appraise("sceptre").toCompletableFuture();
crown.thenCombine(sceptre, BigDecimal::add).thenAccept(System.out::println);
CompletableFuture.allOf(crown, sceptre).thenRun(() -> System.out.println(crown.join() + " " + sceptre.join()));

// Failures
appraiser.appraise("cursed ring").exceptionally(ex -> BigDecimal.ZERO);
```
