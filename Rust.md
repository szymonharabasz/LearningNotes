#### Integers and chars
Size of `char` is always 4 bytes. It can be checked with:
```RUst
std::mem::size_of::<char>()
```
But only `u8` can be cast to `char`.

```Rust
"τὰ μετὰ τὰ φυσικά".len()
std::mem::size_of_val("τὰ μετὰ τὰ φυσικά")
```
returns the length in bytes, which is actually occupied by the string (1 byte for ASCII, 2 bytes for some European characters with diacritics, 3 or 4 bytes for Japanese or Chinese characters etc.)
```Rust
"τὰ μετὰ τὰ φυσικά".as_bytes()
```
returns the byte representation.
```Rust
"τὰ μετὰ τὰ φυσικά".chars()
```
rerurns the list of characters which can be counted with `count()`.

Largest and smallest values:
```Rust
u8::MIN
u8::MAX
```
Some methods:
```Rust
42.is_positive()
```
#### Floating point arithmetics
Epsilon values:
```Rust
f32::EPSILON
f64::EPSILON
```
Testing for NAN and finite value:
```Rust
x.is_nan()
x.is_finite()
```
#### Strings
`&str` is just a pointer to the memory plus length. It does not own the data. String literal `"abc"` creates `&str`.
`String` does own the data.
One can use also:
```Rust
let my_string = String::from("τὰ μετὰ τὰ φυσικά");
let my_string = "τὰ μετὰ τὰ φυσικά".to_string();
let my_string = format!("Metaphysics in Greek: {}", "τὰ μετὰ τὰ φυσικά");
let my_string: String = "τὰ μετὰ τὰ φυσικά".into();

let mut my_string = String::from("τὰ μετὰ τὰ φυσικά");
my_string.push_str(" is Metaphysics in Greek");

let num_words = my_string.split_whitespace().count();
```
Raw string literals:
```Rust
r#"Hello \n world"#
r##"Hello "\n"# world"##
```
String literals converted to bytes:
```Rust
b"Hello world"
```
String formatting:
`{}` needs the `Display` trait to be implemented by a type
`{:?}` needs the `Debug` trait
`{:#?}` is like `Debug` but enables *pretty printing*
`{:p}` pointer, `{:x}` hexadecimal, `{:o}` octal, `{:b}` binary
Characters fom hexadecimal representation:
```Rust
"\u{D589} \u{48} \u{5C45}"
```
Changing order of format parameters:
```Rust
"{3} {1} {2}"
```
Names for parameters:
```Rust
println!("{country}'s capital is {capital}", country = "Japan", 
	capital = "Tokyo");
```
General:
```Rust
"{name:padding_character(<|^|>)min_length.max_length}"
```
Parenthesis are used here just to deliminate alternatives: `<` - align left, `^` - align center, `>` - align right.
Some methods:
```Rust
metaphysics_in_greek.is_empty()
```
#### Collections
An array with some element repeated $n$ times can be created like:
```Rust
let a = ["a"; 5]
```
Slices:
```Rust
let slice = &a[1..3]; // exlusive
let slice = &a[1..=3]; // inclusive
```
For vectors, the compiler can infer the type of elements based on `push` calls:
```Rust
let mut my_vec = Vec::new();
vec.push(42);
```
but the type can be also specified explicitly:
```Rust
let mut my_vec: Vec<String> = Vec::new();
```
Creating with the `vec!` macro:
```Rust
let mut my_vec = vec![1, 1, 2, 3, 5, 8];
```
Capacity:
```Rust
let mut my_vec = Vec::with_capacity(8);
println!("{}", my_vec.capacity());
```
Converting arrays, the compiler can infer the type of elements:
```Rust
let mut my_vec: Vec<String> = a.into();
let mut my_vec: Vec<_> = [1, 2, 3, 4].into();
```
Tuples:
```Rust
let my_tuple = (1, "Hello", 42.0);
let second = my_tuple.1;
let (_, two, three) = my_tuple;
println!("two: {}", two); // prints "two: Hello"
```
#### Flow control

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
#### References
Mutable references are created with:
```Rust
let my_ref[ : &mut i32] = &mut my_val;
```
One can have many immutable references.
One can only have one mutable reference, and one cannot have a mutable *and* an immutable reference. But one can create an immutable reference *after* all the changes through a mutable reference have been done and the borrow *ends*.
#### Own types
Unit struct:
```Rust
struct MyNewType;
```
Tuple struct:
```Rust
struct ColorRgb(u8, u8, u8);
// ...
let my_color = ColorRgb(50, 120, 30);
println!("Green component is {}", my_color.1);
```
Named struct - **note commas!**:
```Rust
struct Shape {
	size: f32,
	color: ColorRgb,
	border_thickness: u32,
}
// ... 
let size = 42.0;
let color = ColorRgb(120, 30, 50);
let shape = Shape {
	size: size,
	color: color,
	border_thickness: 8
};
```
There is also a convenience:
```Rust
let border_thickness = 6;
let shape = Shape {
	size, color, border_thickness,
};
```
Enums can hold data:
```Rust
enum ThingsInTheSky {
	Sun(String),
	Stars(String)
}
// ...
let thing = ThingsInTheSky::Sun("Behind the clouds...");
// E.g., in some function:
	use ThingsInTheSky::*;
	let thing = ThingaInTheSky::Stars("Very many!");
```
Enums without data can be cast to numbers:
```Rust
day_of_week as u32
```
And the values can be defined:
```Rust
enum Season {
	Spring = 4,
	Summer, // will get 5
	Fall = 10,
	Winter = 20,
}
```
Allowing own structs or enums to be printed with `{:?}`:
```Rust
#[derive(Debug)]
enum ...
```
Implementing methods:
```Rust
impl Shape {
	fn new_shape() -> Self {
		Self(1.0, ColorRgb(0, 0, 0))
	}
	fn brighten(&mut self) {
		self.color = ColorRgb(
			self.color.0 + 10, 
			self.color.1 + 10,
			self.color.2 + 10)
	}
}
fn main() {
	let mut shape = Shape::new_shape();
	shape.brighten();
}
```
Structs can also be destructured (with a possibility to rename variables)!:
```Rust
let Shape {
	size: rem_sz,
	color,
	.. // rest - skip the ones we are not interested in
} = shape;
```
Destructuring can also be done in a function signature.
```Rust
fn check_border_thickness(Shape { border_thickness: thickness } : &Shape) {
	// ...
}
```
#### Standard library
Reference counting wrappers are `Rc<T>` and `Arc<T>`. To enable internal mutability, one can use `Rc<RefCell<T>>` and `Arc<Mutex<T>>`. One uses `::new()` for initialization. One can borrow the values like this:
```Rust
let val = my_rc.borrow_mut();
```
