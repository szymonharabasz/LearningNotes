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
#### Operators in CRUD operations
Operator `$in`:
```js
db.zips.find({
	city: { $in: ["PHOENIX", "CHICAGO"]}
})
```
Comparisons:
```js
db.sales.find({
	"customer.age": { $lte: 65 }
})
```
Querying for arrays that contain elements fulfilling certain criteria (`$elemMatch`):
```js
db.sales.find({ products: "CurrencyService" })
db.sales.find({
	items: {
		$elemMatch: { 
			name: "laptop", 
			price: { $gt: 800 }, 
			quantity: { $gte: 1 }
		},
	},
})
```
Logical operators:
```js
db.routes.find({
	$and: [
		{ $or: [{ dst_airport: "SEA" }, { src_airport: "SEA" }] 
		{ $or: [
			{ "airline.name": "American Airlines" },
			{ airplane: 320 }
		] },
	]
})
```
Often `$and [ expr1, expr2 ]` can be replaced with implicit `and`, i.e., `expr1, expr2`, but not when `expr1` and `expr2` use the same operator, because a JSON document cannot have the same key more than once.
#### Aggregations
Randomly sampling data:
```js
db.movies.aggregate(
{[
	$sample: { size: 1 }}
])
```
#### JSON validation schemas
Required fields
```json
{
	$jsonSchema: {
		required: [
			'name', 'stars'
		],
		roperties: {
			name: {
				type: 'string'
			},
			stars: {
				type: 'string'
			}
		}
	}
}
```