#### Components
```Rust
#[component]
fn ProgressBar(
	#[prop(default=100)]
	max: u16,
	#[prop(into)]
	progress: Signal<i32>
) -> impl IntoView {
	view! {
		<progress
			max=max
			value=progress
		/>
	}
}
```
Optional props are created with
```Rust
#[prop(optional)]
```
A signal can be created from a closure:
```Rust
let double_count = = move || count.get() * 2;
// ...
<ProgressBar progress=Signal::derive(double_count)/>
```
Element attributes in "RSX":
```Rust
on.click=move |_| {
	*set_count.write() += 1;
}
// or
on.click=move |_| {
	set_count.update(move |valie| *value* += 1);
}

class:red=move || count.get() % 2 == 1
// or
class=("red", move || count.get() % 2 == 1)
// or
class=(["red", "button-20"], move || count.get() % 2 == 1)

style:background-color=move || format!("rgb({}, {}, 100)", count.get(), 100)
```
Signals are created with:
```Rust
let (count, set_count) = signal(0);
```
This is a tuple containing a `ReadSignal` and `WriteSignal`. We can also create a read-write signal:
```Rust
RwSignal::new(idx)
RwSignal::from(count)
ArcRwSignal::new(id)
```
Mounting components:
```Rust
fn main() { leptos::mount::mount_to_body(App) }
```
To create a list of attributes, one can use `view` with the spread operator as a tag name
```Rust
let spread = view! {
	<{..} aria-label="a component with attribute spreading"/>
}
```
One can pass plain HTML attributes into a component. They will be applied to all top-level HTML elements returned by the `view`:
```Rust
<SomeComponent
	attr:id="foo"
	{..} // after this everything is treated as attr:
	title="bar"

	// Use the attributes from the list defined above:
	{..spread}
```
#### Lists
Static with `Vec<_>`:
```Rust
let values = vec![0, 1, 2];
view! {
    <p>{values.clone()}</p>
    <ul>
        {values.into_iter().map(|n| view! { <li>{n}</li>})
            .collect::<Vec<_>>()}
    </ul>
    // or
    <ul> 
	    {values.into_iter().map(|n| view! { <li>{n}</li>}) 
		    .collect_view()} 
	</ul>
}
```
Dynamic with the `<For/>` component:
```Rust
let initial_counters = (0..initial_length)
	.map(|id| (id, ArcRwSignal::new(id+1)))
	.collect::<Vec<_>>();
let (counters, set_counters) = signal(initial_counters);

<For 
	each=move || counters.get()
	key=|counter| counter.0
	children=move |(id, count)| {
		let count = RwSignal::from(count);
		view! {
			<li>
				<button on:click=move |_| *count.write() += 1;>
					{count}
				</button>
			</li>
		}
	} 
```
`each` should return an iterator. Instead of the `children` attribute, one can use:
```Rust
<For ...
	let(child)

{child.some_value()}
</For>
```
or
```Rust
let(DatabseEntry {key, value})
```
Each item is only re-rendered, when the `key` changes. Therefore, to change update the items, one has to do one of these:
- Force the `key` to change when we do update (or make the key dependent on the value that we want to update):
  ```Rust
  key=|state| (state.key.clone(), state.value)
	```
- Wrap the item that we want tu update into a signal. It keeps its reactivity even if it's nested into the list item that doesn't update itself:
  ```Rust
  #[derive(Debug, Clone)] 
  struct DatabaseEntry { 
	  key: String, 
	  value: RwSignal<i32>, 
  }
  // ...
  <For
	  each=move || data.get()
	  key=|state| state.key.clone()
	  let(child)
  > 
	  <p>{child.value}</p>
  </For>
```
- Memoize the value that can be changed with `Memo`:
  ```Rust
  <For
    each=move || data.get().into_iter().enumerate()
    key=|(_, state)| state.key.clone()
    children=move |(index, _)| {
        let value = Memo::new(move |_| {
            data.with(|data| data.get(index).map(|d| d.value).unwrap_or(0))
        });
        view! {
            <p>{value}</p>
        }
    }
/>
```
- Use a global store, dependency `reactive_stores`:
  ```Rust
  #[derive(Store, Debug, Clone)]
pub struct Data {
    #[store(key: String = |row| row.key.clone())]
    rows: Vec<DatabaseEntry>,
}

#[derive(Store, Debug, Clone)]
struct DatabaseEntry {
    key: String,
    value: i32,
}
// ...
<For
    each=move || data.rows()
    key=|row| row.read().key.clone()
    children=|child| {
        let value = child.value();
        view! { <p>{move || value.get()}</p> }
    }
/>
```
#### Logging
```Rust
leptos::logging::log!("{:?}", data.get());
```