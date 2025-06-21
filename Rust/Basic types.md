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

let has_physics = my_string.contains("physics");
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
"42".parse::<i32>(); // return Result

'a'.is_alphabetic();
```
#### Collections
###### Arrays
An array with some element repeated $n$ times can be created like:
```Rust
let a = ["a"; 5]
```
Can be destructured:
```Rust
let [first, .., last] = a;
```
###### Slices
```Rust
let slice = &a[1..3]; // exlusive
let slice = &a[1..=3]; // inclusive
```
###### Vectors
The compiler can infer the type of elements based on `push` calls:
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
###### Tuples:
```Rust
let my_tuple = (1, "Hello", 42.0);
let second = my_tuple.1;
let (_, two, three) = my_tuple;
println!("two: {}", two); // prints "two: Hello"
```
###### Maps and sets
`HashMap` and `BTreeMap` - the latter has ordered keys. `insert(key, value)` returns an `Option` of old value.
`entry(key)` returns (code simplified):
```Rust
enum Entry<K, V> {
	Occupied(OccupiedEntry<K, V>),
	Vacant(VacantEntry<K, V>),
}
```
This enum has a method:
```Rust
fn or_insert(self, default: V) -> &mut V {
	match self {
		Occupied(entry) => entry.into_mut(),
		Vacant(entry) => entry.insert(default),
	}
}
```
Therefore, the combination of `entry()` and `or_insert()` allows to implement a counter of elements:
```Rust
for book in book_collection {
	// if the key exists in the HashMap it is returned, otherwise 0 is
	// inserted, in both cases, reference to the value, new or already
	// existing, is returned
	let return_value = book_hashmap_counter.entry(book).or_insert(0);
	// and in any case, the refered value is incremented
	*return_value += 1;
}
```
One can do more complicated things with the returned `&mut`:
```Rust
survey.entry(item.0).or_insert(Vec::new()).push(item.1);
```
`HashSet` and `BTreeSet` are implemented as maps with value `()`.

**`BinaryHeap`** is a *priority queue*, it always has the largest element in front (accessible through `.pop()`) and remaining elements unordered.

**`VecDeque`** is optimized to pop elements from the back  (`.pop_back()`) and from the front (`.pop_front()`). It is implemented with a ring buffer. It can be easily created `::from` a vector.