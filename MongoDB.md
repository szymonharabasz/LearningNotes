#### Using `mongosh`
```js
show dbs
use carsdb
show collections
```
Setting database in the JavaScript code:
```js
db = db.getSiblingDB("carsdb")
```
Loading a JavaScript file:
```js
load("path/to/the/file.js")
```
```js
config.get('editor')
config.set('editor','vim')
edit myfunc
```
Running the editor to edit the next command
```js
edit
```
#### Aggregations
Randomly sampling data:
```js
db.movies.aggregate(
{[
	$sample: { size: 1 }}
])
```