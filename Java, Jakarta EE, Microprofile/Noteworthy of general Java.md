Try with resources:  
```Java
try (InputStream in = Files.newInputStream(path)) { … }  
try (OutputStream out = Files.newOutputStream(path)) { … }
```
Manual storing and reading properties:  
```Java
properties.store(out, "Program settings");  
properties.load(in);
```
One can overload the `finalize()` method. It is not then called by the garbage collector.
A method cannot be both `private` and `abstract`.
There can be a method and a field with the same names.
There's a method `List.add(int index. Object o)`.
When a class implements several interfaces, compiler allows casting of a reference of the type of one interface to another one.
```Java
NumberFormat currencyFormat = NumberFormat.getCurrencyInstance();  
currentcyFormat.format(x);  
NumberFormat percentInstance = NumberFormat,getPercentIstance();
```
One can create an object of an inner class:  
```Java
var wilma = myFace.new Member("Wilma")
```
If a class gets methods with the same name from more than one interface and at least in one of them the method has a `default` implementation, then it must be implemented in the class, but in this implementation one can make use of the implementation in the interface: `MyInterface.super.getId()`.
One can create a method reference with this keyword: `this::method`, `OuterClass.this::method` and with `super` keyword: `new Thred(super::work)`.
In local inner classes and lambda expressions, variables from the scope, in which they are defined, can be accessed if they are *effective final*.
The iteration variable in the enhanced for loop is effective final. This works:  
```Java
for (var arg : args) { new Thread(() -> System.out.println(arg)).start(); }  
```
but this not:  
```Java
for (int i = 0; i < n; i++) { new Thread(() -> 
	System.out.println(i)).start(); }
```
Anonymous classes can be created to implement interfaces and to extend other classes - even those from JDK
One can mimic initialization list notation with double braces: `new ArrayList<String>(100) {{ /*...*/ }}`, where outer brace is the body of the anonymous subclass and the inner brace is its initialization block. However, this is not recommended.
With `default` method Implementation in Interfaces, the most noticeable difference between them and abstract classes is that the latter may contain instance variables and constructors. Protected access includes package access.
Subclass from other package can access protected variable only in object of the same class, not of superclass or other subclasses. 
Exceptions derived from `RuntimeException` (and Error) are unchecked.
Methods related to exceptions:  
```Java
Objects.requireNonNull(direction, "Message"); // throws an exception  
Objects.requireNonNullElse(direction, "North");  
Objects.requireNonNullElseGet(direction, () ->  
    System.getProperty("com.example.direction.default")  
);  
Objects.checkIndex(index, length);
```
To do something with an uncaught exception before the thread is closed:  
```Java
Thread.setDefaultUncaughtExceptionHandler((thread, ex) => {  
	/* save the exception somewhere */  
});
```
Getting a string with stack trace:  
```Java
var out = new ByteArrayOutputStream();  
ex.printStackTrace(new PrintWriter(out));  
String description = out.toString();
```
**Records.** One cannot create instnce variables in the record body. Instance variables of a record are automatically final. One can define instance methods and custom constructors (which at the end call the canonical constructor.. Canonical constructor can be reimplemented. One can use a compact form:
```Java
record Range(int from, int to) {  
    public Range {  
        if (from > to) {  
            int temp = from;  
            from = to;  
            to = temp;  
        }  
    }  
}  
```
which is a prelude to a canonical constructor operating on its arguments. Instance variables cannot be set in the compact constructor.

Sealed classes:
```Java
public abstract sealed class JSONValue permits JSONArray, JSONNumber, JSONString, JSONBoolean, JSONObject, JSONNull { … }
```
Allowed subclasses must be in the same package (and the same module). One can omit `permits` keyword, **then subclasses must be declared in the same file**. One can allow for inheriting from a subclass of a sealed class, it must be then marked with the keyword non-sealed.

**Enums.** May have constructors, constructor parameters must be provided in element declaration: `SMALL("S")`.
Enums may also have methods. They can be overridden in the bodies of elements, when they are provided. In general, element bodies may contain everything that anonymous inner class can contain. Static variables in enums are initialized after creating enum elements, therefore they cannot be used in the constructor. A solution is to create static initialization block. Enums declared inside a class work like static inner classes.

**Switch.** Colon notation falls through and does not require braces, arrow notation does not fall through and requires braces unless the case fits into single line. One cannot mix both notations in one switch statement.
Pattern matching in `instanceof`:  
```Java
if (animal instanceof Cat cat) { cat.meow(); }
```
With record deconstructing:  
```Java
if (obj instanceof Address(String city, String street)) { 
	System.out.println(street); }
```
Can be expressions:  
```Java
var result = switch (day) {  
    case "Monday": yield "Hate";  
    default: yield "Don't hate";  
}  
```
In the arrow notation in single line, the `yield` keyword is not needed
Pattern matching now works with switch

#### JUnit and Mockito

Useful for `then`:
```Java
verify(myMock, times(0)).myMethod(anyInt());
```
Using argument captor:  
```Java
@Captor  
ArgumentCaptor<Response> argumentCaptorResponse;  
…  
verify(asyncResponse).resume(argumentCaptorResponse.capture());  
final Response response = argumentCaptorResponse.getValue();  
    assertThat(response.getStatusInfo().getFamily()).isEqualTo(Response.Status.Family.SUCCESSFUL);
```
#### Futures
Consuming a future returned by a service:
```java
service.greeting(”Luke”)
    .thenApply(response -> response.toUpperCase())
    .thenApply(greeting -> System.out.println(greeting));
```
Composing: