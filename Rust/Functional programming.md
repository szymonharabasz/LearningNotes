###### Iterators
`.iter()` - iterator of references
`.iter_mut()` - iterator of mutable references
`.into_iter()` - iterator of values
`for` loop calls `into_iter()` if no iterator is created explicitly. Since `into_iter()` returns values, it uses *move semantics*, so it destroys original collections.

Implementing the `Iterator` trait:
```Rust
struct BookCollection(Vec<String>)

impl Trait for BookCollection {
	type Item = String;

	fn next(&mut self) -> Option<String> {
		match self.0.pop() {
			Some(book) => {
				println!("Accessing book {book}");
				Some(book)
			},
			None => {
				println!("Out of books at the library!");
				None
			}
		}
	}
}
```
###### Using iterators for functional programming
```Rust
my_vec.iter().skip(10).take(20).collect::<Vec<&i32>>();
my_vec.iter().map(|x| x * 10).collect::<Vec<i32>>();
my_mut_vec.iter_mut().for_each(|x| *x = &*x*10);
my_vec.iter().filter(|x| **x < 2).collect::<Vec<&i32>>();
my_vec.into_iter().filter_map(|x| {
	if x > 2 {
		Some((x*42) as i64)
	} else {
		None
	}
}).collect::<Vec<i64>>();

my_iter.all(|x| > 2)
my_iter.any(|x| > 2)
match my_vec.iter().find(|num| num % 3 == 0) {
	Some(number) => println!("Found: {number}"),
	None => println!("Not found")
}
match my_vec.iter().position(|num| num % 3 == 0) {
	Some(pos) => println!("Found: at {pos}"),
	None => println!("Not found")
}
my_vec.into_iter().rev().collect::<Vec<_>>();
```
Enumerating:
```Rust
my_vec.iter().enumerate().for_each(|(index, c)| println!("{index}: {c}")))'
some_keys.into_iter().zip(some_values.into_iter()).collect::<HashMap<_,_>>();
for (index, character) in "Metaphysics".char_indices() { ... }
["even", "odd'].into_iter(),cycle() // to be, e.g., zipped with other iterator
```
Striping out `Err` and `None`:
```Rust
vec!["9", "nine", "ninety-nine", "9.9"].into_iter()
	.map(|num| num.parse::<f32>())
	.flatten()
```
contains now iterator with `9.0` and `9.9`.

Folding:
```Rust
let sum = vec![9, 6, 9, 10, 11].iter().fold(0, 
	|total_so_far, next_item| total_so_far + next_item);
```
Avoiding to destroy the whole iterator:
```Rust
let mut my_iter = vec![1, 2, 3, 4, 5, 6].into_iter();
let first_two = my_iter.by_ref().take(2).collect::<Vec<_>>();
let second_two = my_iter.take(2).collect::<Vec<_>>();
```

Chunks (sliding windows with the padding equal the length) and windows (with padding equal 1):
```Rust
for chunk in num_vec.chunks(3) {
    println!("{:?}", chunk);
}
println!();
for window in num_vec.windows(3) {
    println!("{:?}", window);
}
```
Closure traits are:
```Rust
trait FnOnce
trait FnMut : FnOnce
trait Fn : FnMut
```
*`impl Trait`* with these traits can be used to return a closure:
```Rust
fn returns_a_closure() -> impl FnMut(i32) -> i32 {
	|x| x *= 2
}
```