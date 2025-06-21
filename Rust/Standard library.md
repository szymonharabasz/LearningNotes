#### Standard library
##### Internal mutability
###### Cells:
```Rust
active: Cell<bool>
// ... 
active = Cell::new(true);
active.set(false);
active.get();
```
To use `get()`, underlying type must be `Copy`.
```Rust
// ...
on_sale: RefCell<bool>
// ...
on_sale = RefCell::new(false);
// set and get
let borrowed = on_sale.borrow();
let mut_borrowed = on_sale.borrow_mut();
*mut_borrowed = true;
// Also works and it's better because we don't create two mutable
// reference variables
// *on_sale.borrow_mut() = true

// Err if mutable borrow isn't possible:
let mut_borrow_result = on_sale.try_borrow_mut();
```
###### Boxes:
```
let my_box = Box::new(4);
let val = *my_box;
let my_clone = box.clone();
drop(box);
```
They are sort of references that **own their data**. They are not `Copy`. They can be used for recursive data structures (but those are not recommended in Rust.)
They can be used to return *trait objects*:
```Rust
fn my_fn() -> Box<dyn MyTrait> { ... }
```
This is often used for the `Error` trait:
```Rust
fn my_fn() -> Result<String Box<dyn Error>> { ... }
```
One can try to downcast trait objects to concrete types:
```Rust
if let Some(my_err) = err_trait.downcast::<MyErr>() { ... }
if let Some(my_err) = err_trait.downcast_ref::<MyErr>() { ... }
if let Some(my_err) = err_trait.downcast_mut::<MyErr>() { ... }
```
###### Mutexes:
```Rust
let my_mutex = Mutex::new(5);
{
	let mutex_changer = my_mutex.lock().unwrap();
	*mutex_changer = 6;
}
// or
let my_mutex = Mutex::new(5);
let mutex_changer = my_mutex.lock().unwrap();
*mutex_changer = 6;
drop(mutex_changer);
```
`drop()` is an universal function to put a variable out of scope.
To avoid deadlocks, one can:
```Rust
mutex.try_lock()
```
and pattern-match on the result.

Read-write lock, `RwLock`, is like `Mutex` and `RefCell`. It has methods:
```Rust
my_rwlock.read().unwrap();
my_rwlock.write().unwrap();
my_rwlock.try_read();
my_rwlock.try_write();
```
Reference counting wrappers are `Rc<T>` and `Arc<T>`. To enable internal mutability, one can use `Rc<RefCell<T>>` and `Arc<Mutex<T>>`. One uses `::new()` for initialization. One can borrow the values like this:
```Rust
let my_rc = Rc::new("Kitteh");
let val = my_rc.borrow_mut();
let other_ref = Rc::clone(&my_rc);
let count = Rc::strong_count(&my_rc);
```
One can also use `my_rc.clone()`, but `Rc::clone` more clearly expresses the intent.
###### Weak references:
```Rust
let my_weak_ref = Rc::downgrade(&my_rc);
let weak_count = Rc::weak_count(&my_rc);
```
###### Cow
Can wrap a type to hold values that can be either borrowed or owned:
```Rust
struct User<'a> {
	name: Cow<'a, str>,
}
fn main() {
	let name1 = "user1";
	let name2 = "user2".to_string();
	let user1 = User { name: name1.into(), };
	let user2 = User { name: name2.into(), };
	for name in [user1.name, user2.name] {
		match name {
			Borrowed(n) => println!{"No memory allocation needed for {n}"}.	
			Owned(n) => println!("Memory allocation occred for {n}"),
		}
	}
}
```
##### Options
Methods:
```Rust
my_option.is_some();
my_option.is_none();
let my_mapped_option = my_option.and_then(|num| num * 42);
let my_combined_option = opt1.and(opt2).and(opt3);
```
`my_combined_option` is `Some(val3)` if all the options are `Some` and `opt3` is `Some(val3)`, otherwise it is `None`.
##### Results
`Result<T, E>` is an enum with `Ok(T)` and `Err(E)`.
Methods:
```Rust
my_result.is_ok();
my_result.is_err();
```
Methods for both `Option` and `Result`:
```Rust
my_opt_or_res.unwrap();
my_opt_or_res.unwrap_or(&0);
my_opt_or_res.unwrap_or_else(|| {
	let let Some(val) = my_vec.get(3) {
		val
	} else {
		&0
	}
});
my_opt_or_res.expect("My own error message");
```
Converting `Result` to `Option` (`Some` if `Result` is `Ok`, `None` if `Result` is `Err`):
```Rust
let my_option = my_result.ok();
```
Converting `Option` to `Result`:
```Rust
let my_result = my_option.ok_or("An error occured"); // or specific Error type
let my_result = my_option.ok_or_else(|| {
	let current_datetime = get_current_datetime();
	let error_message = format!"{}: an error occured", current_datetime);
	error_message
})
```

Errors often implement the trait `Error`.

**Question mark operator** `?` (also available for `Option`) return the value if the `Result` is `Ok` or immediately returns the `Err` from the function (so the enclosing function also has to return `Result` with corresponding `Err`).

Explicit panic:
```Rust
panic!("It's not Titanic");
assert!(length < 4, "Length should be smaller than 4");
assert_eq!(length, 4, "Length should be 4");
assert_ne!(length, 4, "Length should not be 4");
```
The trait `AsRef<T>` provides the method `as_ref()`. `AsRef<str>` is useful to have both `&str` and `String` as a function's input.()
#### Threads
```Rust
let handle = std::thread::spawn(|| println!("I'm printing something"));
handle.join().unwrap();
```
`spawn` requires a closure that implements the `FnOnce` trait. So it needs to capture variables from the scope by value, not by reference, so the closure must be implemented with the keyword `move`:
```Rust
let animal = String::from("Kitteh");
let handle = std::thread::spawn(move || println!("I'm printing {animal}"));
handle.join().unwrap();
```
###### Scoped threads
```Rust
thread::scope(|s|{
	s.spawn(|| println!("Inside the thread"))
});
```
They are automatically joined at the end of the scope. They can borrow non-`'static` data, and since only one mutable borrow at the same time is allowed, they also don't need `Arc`.
###### Channels
```Rust
let (sender, receiver): (Sender<i32>, Receiver<i32>) = channel();
```
or just start using the sender and the receiver to let the compiler infer the underlying type. Then
```Rust
sender.send(5);
receiver.recv(); // blocking
receiver.try_recv();
```
both return `Result`. They can be cloned and passed to other threads:
```Rust
sender.clone();
```
#### Async
```Rust
use tokio;

async fn async_give_8() -> u8 { 8 }

#[tokio::main]
async fn main() {
	let some_number = async_give_8().await;
}
```
Awaiting many futures at the same time:
```Rust
let nums = joun!(
	sleep_for_random_time_and_return(1),	
	sleep_for_random_time_and_return(2),	
	sleep_for_random_time_and_return(3)
);
```
There is also one `try_join!` which waits or fails when one of the futures fail.
Taking the result of the future that finished first:
```Rust
use std::time::Duration;
use tokie::{select, time::sleep};
// ...
let num = select!(
	first = sleep_then_string(10) => first,
	second = sleep_then_string(11) => second,
	thitd = sleep_then_num(12) => format!("Slept for {num} ms"),
	_ = slepp(Duration::from_milis(100)) => format!("Timed out after 100 ms")
);
```

#### IO
##### Standard input
```Rust
std::io::stdin().read_line(&mut input_string)
```
##### Environment variavles
```Rust
std::env::var("RUST_BACKTRACE")
std::env::set_var("RUST_BACKTRACE", "full");

for (key, value) in std::env::vars() { ... }
```
##### Command-line arguments
```Rust
for arg in std::env::args() {
	match arg.as_str { ... }
}
```
##### Files
Writing:
```Rust
use std::fs;
use std::io::Write;

fn main() -> std::io::Result<()> {
	fs::File::create("myfile.txt")?.write_all(b"Hello")?;
	//or
	fn::write("myfile2.txt", "Hello again")?;
	
	Ok(())
}
```
Reading:
```Rust
use std::fs;
use std::io::Read;

fn main -> std::io::Result<()> {
	fs::file::open("myfile.txt")?.read_to_string(&mut input_string)?;
}
```
Using open options:
```Rust
OpenOptions::new().write(true).create(true).truncate(true)
	.open("myfile3.txt")?;
// or
File::options().write(true).create(true).truncate(true)
	.open("myfile3.txt")?;
```
Available methods, mostly with a `bool` argument:
```Rust
append(), create(), create_new(), read(), truncate(), wrtie()
```
##### Defaults
```Rust
let default_i8: i8 = Default::default();
```
Trait:
```Rust
impl Default for Character {
	fn default() -> Self { 
		Self { ... }
	}
}
```
One can do (if all the struct fields implement or derive `Default`):
```Rust
let character = Size {
	height: 0.0,
	..Default::default()
};
```
#### Testing
```Rust
#[test]
fn my_test() {
	assert_eq!(2, 3);
}
```
In a separate module;
```Rust
#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn my_test() {
		assert_eq!(2, 3);
	}
	
	#[test]
	#[should_panic]
	fn panics_when_characters_not_right() {
		let calc = Subtractator;
		calc.math("7 - seven");
	}
}
```
Running with:
```Shell
rust test
```
