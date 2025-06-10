#### Variable declarations
1. Variable with scope limited to a function `var pizza = true;`
2. Constant `const pizza = true;`
3. Variable with scope limited to a block `let pizza = true;`
#### Temaplate string
```javascript
`Hello, ${name}`
```
They preserve white spaces (new line, tabs)
#### Comparisons
```javascript
3 === 3.0 // true
42 === '42' // false
null === null // true
undefined === undefined // false
undefined === null // false
NaN === NaN // false
0 === -0 // true
Number.isNaN(NaN), Number.isNaN(-NaN), Number.isNaN(42) // true, true, false
Object.is(NaN, NaN) // true
Object.is(0, -0) // false
Object.is(3.0, 3) // true
Object.is(42, '42') // false

var a = [1,2,3]  
var b = a  
a === b // true  
a === [1,2,3] // false

42 == '42' // true  
"" == 0 // true  
1 == true // true  
9 < "10", "9" < "10" // true, false

null == false // false  
[] == false, [] == true // true, false  
{} == false, {} == true // false, false  
if ({}} { /* this will be executed */ }
```
#### Arrow functions
```javascript
var lordify = (firtName, land) => `${firstName} of ${land}`;
```
Functions defined with the `function` keyword do not *block* `this`:
```javascript
var tahoe = {  
    resorts: [ "Kirkwood", "Squaw", … ];  
    print: function(delay = 1000) { // new: default arguments!  
        setTimeout(function() {  
            console.log(this.resorts.join(", "));  
        }, delay);  
    }  
}  
tahoe.print(); // this is window, resorts are then undefined
```
Arrow functions do block `this`:
```javascript
var tahoe = {  
    resorts: [ "Kirkwood", "Squaw", … ];  
    print: function(delay = 1000) { // new: default arguments!  
        setTimeout(() => {  
            console.log(this.resorts.join(", "));  
        }, delay);  
    }  
}  
tahoe.print(); // this is tahoe, resorts get printed
```
In the above example, if `print` will be an arrow function, `this` will again be `window`.
Normal functions have access to a collection `arguments`, arrow functions do not have their own `arguments` collection and have access to the `arguments` collection of their containing function.
With functions defined with the `function` keyword:
1. If we call `Functon()`, `this` will be the object used in the current scope (for example `window`)
2. If we call `new Function()`, `this` will be the object created with the constructor `new Function()`.
#### Destructuring
From an object:
```javascript
var { bread, meat: meatName } = sandwich
```
From an array:
```javascript
var [,,third] = [ "First", "Second", "Third" ]
```
#### Enhanced object syntax
```javascript
const car = {  
    name,  
    color, // global variables  
    drive() { console.log("Broom broom broom"); }  
}
```
#### Iterator protocol
```javascript
class One {
    constructor(max) {
        this.max = max;  
        this.i = 0;
    }
    next() {
        this.i++;
        return {value: i, done: this.i >= this.max};
    }
    [Symbol.iterator]() {
        return this;
    }
}
```
Iterable objects can be used in `for (let elem of array) { ... }`
#### Spread operator (three dots)
Cloning an array
```javascript
var clone = [...original]
```
Combining arrays
```javascript
var combined = [...firstArray, ...secondArray]
var combined = Array.concat(fitstArray, secondArray)
```
First and rest
```javascript
var [first, …rest] = someArray
```
Collecting many function arguments as an array
```javascript
function myfun(...args) { /* … */ }
```
Combining objects
```javascript
var combined = {...firstObject, ...secondObject}
```
This is **not** equivalent to
```
var combined = Object.assign(firstObject, secondObject)
```
Changing an element in the `firstObject` (but not in the `secondObject`) will also change the same element in `combined`.
#### Asynchronous function calls with promises
```javascript
const doSomething = arg => new Promise((resolves, rejects) => {  
    // use arg  
    // if call is successful, call resolves with call result  
    // otherwise, call rejects(new Error(…))  
}  
doSomething("usefil).then(  
    callResult => console.log(callResult), // callback for success  
    err => console.error(…) // callback for error  
)
```
#### Classes
Traditional syntac
```javascript
function Car(name, color) {  
    this.name = name  
    this.color = color  
}  
Car.prototype.drive = function() { console.log("Broom broom broom"); }
```
Class syntac
```javascript
class Car {  
    constructor(name, color) {  
        this.name = name  
        this.color = color  
    }  
    drive() { console.log("Broom broom broom"); }  
}
```
Inheritance
```javascript
class Lorry extends Car {  
    constructor(name, color, capacity) {  
        super(name, color)  
        this.capacity = capacity  
    }  
    drive() {  
        super.drive();  
        console.log("brooooom")  
}
```
#### Modules
Exporting
```javascript
export const foo = 42 // or any JavaScript type: primitive, object, array, function
```
With only one export per file
```javascript
const foo = 42; export default foo;
```
Importing
```javascript
import for from './module1.js'  
import { bar, baz } from './modeule2.js'  
import * as fns from './module3.js'
```
#### Functional programming
```javascript
const wSchools = schools.filter(school => school[0] ==="W")
const highSchools = schools.map(school => `${school High School}`)
```
```javascript
const max = ages.reduce((max, value) => (value > max) ? value : max, 0)
```
There is also `reduceRight`.
Nice way to compose many functions
```javascript
const compose = (...fns) =>  
    (args) =>  
        fns.reduce((composed, f) => f(composed), arg)
```
#### Miscellaneous  built-ins
```javascript
Object.keys
```
```javascript
Array.filter
```
Predicate function can accept a second argument representing the index of the array element.
#### Binding function arguments
Permanently setting `this` in a function
```javascript
let func = func.bind(myThis);
```
Calling a function with `this` set just for this time
```javascript
func.call(myThis, argument1, argument2);  
func.apply(myThis, [argument1, argument2]);
```
#### Time stamp:
```js
new Date().toLocalTimeString();
```
#### Forwarding a request
```JavaScript
const forwardRequest = http.request({
	host: AUDIO_STORAGE_HOST,
	port: AUDIO_STORAGE_PORT,
	path: `/download?path=${song.audioPath}`,
	method: 'GET',
	headers: req.headers,
},
(forwardResponse) => {
	// stream the response to the client
	res.writeHeader(forwardResponse.statusCode, forwardResponse.headers);
	forwardResponse.pipe(res);
});
req.pipe(forwardRequest);
```