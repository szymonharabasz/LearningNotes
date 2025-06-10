Types are defined by their shape
```typescript
interface User {  
        name: string;  
        age: number;  
    }  
    const tom: User = {    name: "Tom",  
        age: 32  
    }
```
Any object can be assigned to a variable of type `any`. Compiler doesn't check the correctness of e.g. method calls, so they can throw a runtime error.
Any object can be assigned to a variable of type `unknown`, but before an object can be used, its actual type has to be tested for:
```typescript
let val: unknown = 22;  
val = new Array();  
f (val instanceof Array) {  
    val.push(33);  
}
```
Intersection types
```typescript
let obj: { name: string } & { age: number } = {  
    name: 'Tomek',  
    age: 25  
}
```
Union types
```typescript
let unionObj: null | { name: string } = null;  
unionObj = { name: 'Janek' };
```
Literal types
```typescript
let literal: "Tomek" | "Linda" | "Jarek" | "Sylwia" = "Linda";
```
Type aliases
```typescript
type Points = 20 | 30 | 40 | 50; let score: Points = 20;
```
Function types
```typescript
type Run = (miles: number) => boolean;  
let runner: Run = function (miles: number): boolean {  
    if(miles > 10){  
        return true;  
    }  
    return false;  
}
```
Syntax for arrow functions in TypeScript
```typescript
var lordify = (firtName, land): void => `${firstName} of ${land}`;
```
Classes
```typescript
class Person {  
constructor(private readonly msg: string) {}  
    speak() {  
        this.msg = "mówię: " + this.msg;  
        console.log(this.msg);  
    }  
}  
const tom = new Person("cześć");  
tom.speak();
```
Accessor methods
```typescript
class Speaker {  
    private message:  
    get Message() { return this.message; }  
    set Message(val: string) { this.message = val; }  
}  
const speaker = new Speaker("Janek");  
speaker.Message = "cześć";
```
Static properties and methods can be accessed *only* through the class name.
Inheritance is done with the keyword `extends`. Interface implementation with the keyword `implements`. At the beginning of the derived class constructor one has to call the parent class constructor:
```typescript
    super(4);
```
Namespaces are defined with the keyword `namespace`
Abstract classes and methods have a modifier `abstract`.
Type constraints in generics
```typescript
interface HasLength {  
    length: number;  
}  
function getLength<T extends HasLength>(arg: T): number {  
    return arg.length;  
}
```
Optional chaining and nullish (checking for `null` or `undefined`) coalescing
```typescript
car?.wheels?.count
const result = val ?? 42;
```