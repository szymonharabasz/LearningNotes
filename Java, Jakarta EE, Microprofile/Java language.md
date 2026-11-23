Language memos. Threads and futures are in [Java concurrency](Java%20concurrency.md).

## Classes and interfaces
- A method cannot be both `private` and `abstract`.
- A class can have a method and a field with the same name.
- `protected` includes package access. A subclass in **another package** can access an inherited protected member only through references of its own type (or a subtype), not through a reference to the superclass or a sibling subclass.
- Since interfaces can have `default` methods, the main remaining difference from abstract classes is that abstract classes can have instance fields and constructors.
- If a class inherits methods with the same signature from several interfaces and at least one of them has a `default` implementation, the class must override the method. The override can delegate to one interface: `Treasure.super.value()`.
- If a class implements several interfaces, the compiler allows casting a reference from one interface type to another.
- Inner class instance from outside: `var teller = bank.new GoblinTeller("Grizzlegut")`.
- Anonymous classes can implement interfaces or extend any non-final class, including JDK classes.
- "Double-brace initialization" `new ArrayList<String>() {{ add("crown"); }}`: the outer braces are the body of an anonymous subclass and the inner braces are its initializer block. It works but is discouraged, because it creates an extra class and captures `this`.
- Method references can use `this::method`, `Outer.this::method` and `super::method`, for example `new Thread(super::countGold)`.
- Only a method with exactly the signature `protected void finalize()` is called by the GC. An overload with a different signature is an ordinary method. Finalization is deprecated for removal anyway.

## Lambdas and effectively final variables
Lambdas and local or anonymous classes can only capture **effectively final** variables. The enhanced-for variable is effectively final (it is a fresh variable in each iteration); the classic loop counter is not:
```java
for (var dragon : dragons) { new Thread(() -> System.out.println(dragon)).start(); }  // OK
for (int i = 0; i < n; i++) { new Thread(() -> System.out.println(i)).start(); }      // compile error
```

## Records
- The fields are implicitly `private final`. You cannot declare extra instance fields in the body.
- You can add instance methods and static members, and extra constructors (which must call the canonical one).
- The canonical constructor can be rewritten, or written in **compact form**. The compact form has no parameter list; you reassign the parameters, and they are assigned to the fields afterwards. You cannot assign the fields yourself in it.
```java
record GoldRange(int from, int to) {
    GoldRange {
        if (from > to) { int tmp = from; from = to; to = tmp; }
    }
}
```

## Sealed classes
```java
public sealed interface Treasure permits GoldCoin, Gem, Artifact, CursedRing { }
public final class GoldCoin implements Treasure { }
public non-sealed class Artifact implements Treasure { }   // anyone may extend Artifact
```
- Every permitted subclass must be `final`, `sealed` or `non-sealed`.
- Permitted subclasses must be in the same module, or in the same package if the code is in the unnamed module.
- If you omit `permits`, the subclasses must be declared **in the same file**.

## Enums
- Enums can have constructors, and the arguments are given at the constant: `HATCHLING("H")`.
- Constants can have bodies that override methods; a body can contain anything an anonymous class can.
- Static fields are initialized **after** the constants are created, so constructors can't use them. Use a static initializer block instead.
- An enum nested in a class is implicitly static.

## Switch and pattern matching
- Colon form: falls through, no braces needed. Arrow form: no fall-through, and you need braces unless the case is a single expression or statement. You can't mix the two forms in one switch.
- A switch can be an expression. In the colon form, or in an arrow block, use `yield` to return a value:
```java
var mood = switch (day) {
    case "Monday": yield "Knights' visiting day";
    default:       yield "Quiet";
};

String described = switch (treasure) {
    case GoldCoin c when c.weight() > 10 -> "a heavy coin";
    case GoldCoin c                      -> "a coin";
    case Gem(var color, _)               -> "a " + color + " gem";   // record pattern; _ = unnamed
    default                              -> treasure.toString();
};
```
`instanceof` patterns, including record deconstruction:
```java
if (creature instanceof Dragon d) { d.breatheFire(); }
if (obj instanceof Cave(String kingdom, _)) { System.out.println(kingdom); }
list.stream().map(_ -> "gold").toList();   // unnamed lambda parameter (JDK 22+)
```

## Newer JDK features
- **String templates** (`STR."Hello \{name}"`) were a preview in JDK 21–22 and were **withdrawn in JDK 23**. Don't use them.
- **Instance `main` methods and compact source files** were a preview in JDK 21 and became final in JDK 25. This is a complete program:
```java
void main() {
    IO.println("Hello, dragon!");
}
```

## Exceptions
- `RuntimeException` and `Error` (and their subclasses) are unchecked.
```java
Objects.requireNonNull(cave, "A dragon needs a cave");
Objects.requireNonNullElse(cave, Cave.DEFAULT);
Objects.requireNonNullElseGet(cave, () -> Cave.of(System.getProperty("dragonbank.default-cave")));
Objects.checkIndex(index, length);

Thread.setDefaultUncaughtExceptionHandler((thread, ex) -> { /* log it somewhere */ });

// Stack trace as a String (a StringWriter needs no flush, unlike a PrintWriter over a byte stream)
var sw = new StringWriter();
ex.printStackTrace(new PrintWriter(sw));
String trace = sw.toString();
```

## Small API reminders
```java
// equals/hashCode
@Override
public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    Dragon dragon = (Dragon) o;
    return Objects.equals(name, dragon.name) && Objects.equals(cave, dragon.cave);
}
@Override
public int hashCode() { return Objects.hash(name, cave); }

try (InputStream in = Files.newInputStream(path)) { properties.load(in); }
try (OutputStream out = Files.newOutputStream(path)) { properties.store(out, "Vault settings"); }

NumberFormat.getCurrencyInstance().format(goldValue);
NumberFormat.getPercentInstance().format(interestRate);

list.add(index, element);   // List has a positional add
```

---

## Build and packaging
### JAR files
`META-INF/MANIFEST.MF`. **The file must end with a newline**, otherwise the last line is ignored:
```
Manifest-Version: 1.0
Main-Class: com.dragonbank.Main

```
```shell
java -jar dragonbank.jar                        # uses Main-Class
java -cp dragonbank.jar com.dragonbank.Other    # runs any class
```

### Gradle
```groovy
description = "DragonBank"

tasks.register('helloDragon') {      // older syntax: task helloDragon { ... }
    doLast { println 'Roar!' }
}

jar {
    manifest { attributes("Main-Class": "com.dragonbank.Main") }
}

repositories {
    mavenCentral()        // or mavenLocal(), google()
    flatDir { dirs 'libs' }
}
```
```shell
gradle tasks --all
```

JUnit and Mockito: see [Testing with JUnit and Mockito](Testing%20with%20JUnit%20and%20Mockito.md).
