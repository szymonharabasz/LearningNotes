For loop:
```Rust
for item in collection { ... }
```
Invalidates `collection` the the end of iteration. To avoid it. one can use references:
```Rust
for item in &collection { ... }
```
equivalent to:
```
for item in collection.iter() { ... }
```
or:
```Rust
for item in &mut collection { ... }
```
equivalent to:
```Rust
for item in collection.iter_mut() { ... }
```
There is a dummy variable `_` and ranges can be used for iteration.

Shadowing can be used even in the same block:
```Rust
let my_variable = 42;
let my_variable = 100.2;
let x = 4;
let x = x+5;
let x = x*2; // (4+5)*2
```

One can return values from blocks:
```Rust
{
	42
}
```
`if` or `break` are examples of expressions that return values: `break 123;`

For infinite loops, instead of `while true`, one should use idiomatically:
```Rust
loop { ... }
```
Loop labels can be used with `break` and `continue`. They start with apostrophe:
```Rust
'outer: for i in 10..20 {
	for j in 20..40 {
		if i + j == 55 {
			break 'outer;
		}
	}
}
```
Match syntax in Rust is:
```Rust
let a = match my_number {
	0 => "zero",
	1 => "one",
	_ => "something else",
};
```
Match (on tuple) with guardian:
```Rust
match (children, married) {
	(children, married) if children > 2 => println!("Quite some children"),
	(children, married) if !married && children > 0 => println!("Thug life"),
	(_, married) => println!("Married? {married}")
	_ => println!("Other sitution")
}
```
Matching numbers with names and on ranges:
```Rust
let answer = match input {
	number @ 4 => "Four",
	number @ 5..=9 => "Less than 10",
	_ => "Less than four or at least ten"
};
```
There are also infinite ranges: `1..`
Pattern matching in conditional statement - `if let`
```Rust
if let Some(number) = my_vec.get(index) {
	println!("The number is {number}");
}
```
Handling the case when pattern matching fails - `let ... else`:
```Rust
let Some(number) = my_vec.get(index) else {
	println!("There is no number");
}
```
Diverging code - we know that `number` is available after the code block, because of the `continue` inside of it:
```Rust
for index in 0..10 {
	let Some(number) = my_vec.get(index) else {
		continue;
	}
	println!("The number is {number}");
}
```
Looping until pattern can be matched:
```Rust
while let Some(information) = my_vec.pop() {
	if let Ok(number) = information.parse::<i32>() {
		println!("Negative of the number is {}", -number);
	}
}
```
#### References
Mutable references are created with:
```Rust
let my_ref[ : &mut i32] = &mut my_val;
```
One can have many immutable references.
One can only have one mutable reference, and one cannot have a mutable *and* an immutable reference. But one can create an immutable reference *after* all the changes through a mutable reference have been done and the borrow *ends*.
#### Lifetimes
`&'static` lives for as long as the program. String literals are `&'static str`.
Named lifetime annotations:
```Rust
struct<'a> City {
	name: &'a str
} 
```
`name` can be assigned reference to something (e.g., `&String`) that lives for at least as long as an instance of `City`.
In that case we would need to specify the lifetime annotation also for `impl`:
```Rust
impl<'a> City<'a> { ... }
```
but we can use *anonymous lifetime* if the explicit parameter is not needed:
```Rust
impl City<'_> { ... }
```
This is because, in general, we can have a struct and a trait with different lifetimes and we need to decide if and how they are related:
```Rust
impl<'a, 'b, 'c, 'd> HasSomeLifetimes<'a, 'b> for SomeStruct<'c, 'd> { ... }
// the above can be figured out by the compiler, so it is equivalent to:
implHasSomeLifetimes<'_, '_> for SomeStruct<'_, '_> { ... }
// but we can also have, e.g.,:
impl<'a, 'b> HasSomeLifetimes<'a, 'b> for SomeStruct<'a, 'b> { ... }
```
#### Const functions
```Rust
const POINTER: u8 = eight();

const fn eight() { 8 }
```
#### Macros
Writing a simple macro
```Rust
macro_rules! may_print {
	($input:expr) => {
		println!("you matched expression");
	};
	($input:stmt) => {
		println!("You matched statement");
	};
}
```
All *fragment specifiers*:
```Rust
block expr ident item // a struct, module etc.
lifetime literal mete // the information that goes inside attributed
pat // a path, like std::vec::Vec
stmt tt // token tree, matches almost everything
ty // tepa mame 
vis // visibility specifier, like pub
```
Zero or more tokens:
```Rust
($($input:tt),*) => { ... }
```
`,` indicates that tokens should be separated by commas, `*` means zero or more, `+` would be one or more, `?` - zero or one.