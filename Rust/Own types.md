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
Implementing methods only for types which have a certain trait (example `Cell` from standard library):
```Rust
impl<T: Copy> Cell<T> { ... }
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
###### Implementing Deref
```Rust
stuct HoldANumber(i8);

impl Deref for HoldANumber {
	type Target = i8;

	fn deref(&self) -> &Self::Target {
		&self.0
	}
}
```
Now one can use the `*` operator and all the methods of the `Target` type (here `i8`).

For mutable references, one has to implement `DerefMut` whose signature is:
```Rust
trait DerefMut: Mut {
	fn deref_mut(&mut self) -> &mut Self::Target;
}
```
#### Generics
Many types with many constraints:
```Rust
fn compare_and_display_a<T: Display, U: Display + PartialOrd>(
	statement: T, a: U, b: U
) { ... }
```
or
```Rust
fn compare_and_display_b<T, U>(statement: T, a: U, b: U)
where T: Display, U: Display + PartialOrd
{ ... }
```
or
```Rust
fn compare_and_display_c(statement: impl Display, 
	a: impl Display + PartialOrd, b: Display + PartialOrd
) { ... }
```
Now we can do:
```Rust
compare_and_display_a::<u8>("Result is: ", 2, 5);
```
But we cannot do:
```Rust
// compare_and_display_c::<u8>("Result is: ", 2, 5);
```
###### Const generics:
```Rust
struct Buffers<T, const N: usize> { 
	array; [T; N],
}
```
In that case `T` and `N` can be inferred:
```Rust
let my_buf = Buffer { array: [u8; 128] };
```

#### Traits
Do nothing and use default implementation in the code of a trait:
```Rust
impl FightClose for Wizard {}
impl FightClose for Ranger {}
```
Typical implementation of `fmt::Display`:
```Rust
impl fmt::Display for Cat {
	fn fmt(&self, f: &mut fmt::Formattet<'_>) -> fmt::Result {
		write!(f, "{} is a cat who is {} years old", self.name, self.age)
	}
}
```
Trait bonds, necessary traits, allow assuming that `&self` in the default implementation will have some specific behavior:
```Rust
trait FightClose: Debug { ... }
```
**Orphan rule:** you cannot implement someone else's traits for someone else's types.

A trait implemented for every type:
```Rust
trait SaysHello {
	fn hello(&self) {
		println!("Hello");
	}
}

impl<T> SaysHello for T {}
// ...
8.hello();
// ...
struct Nothing;
Nothing.hello();
// ...
().hello();
```
In a *blanket trait* implementation `T` is usually bounded by another trait, e.g., `T: Debug`.
#### Modularity
Imports can be renamed:
```Rust
use String as S;
use Animals::{ // enum
	Cat as Kitteh,
	Dog as Doge
}
```
Type aliases:
```Rust
type CarVec = Vec<char>;
```
Inside a nested module, one can refer to elements from a parent module with `crare::` or `super::`
```Rust
super::super::print_country(contry);
crate::country::print_country(country);
```
Additional files have to be declared in `libs.rs`, like:
```Rust
mod functions;
```
for `functions.rs`.