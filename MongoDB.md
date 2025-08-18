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
#### CRUD operation
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
Sorting results:
```js
mycursor.sort({name: 1, surname: -1})
```
Asending order: `1`, descending order: `-1`.
Projections:
```js 
// Inclusion approach:
db.inspections.find(
  { sector: "Restaurant - 818" },
  { business_name: 1, result: 1 }
)
// Exclusion approach:
db.inspections.find(
  { result: { $in: ["Pass", "Warning"] } },
  { date: 0, "address.zip": 0 }
)
```
Only in case of the `_id` field inclusion approach can be combined with exclusion approach.
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
Coumtinh documents that match a certain query:
```js
db.trips.countDocuments({ tripduration: { $gt: 120 }, usertype: "Subscriber" })
```
###### Updating documents
Setting a value with optional upsert operation:
```js
db.podcasts.updateOne|updateMany(
  { title: "The Developer Hub" },
  { $set: { topics: ["databases", "MongoDB"] } },
  { upsert: true }
)

db.podcasts.findAndModify({
  query: { _id: ObjectId("6261a92dfee1ff300dc80bf1") },
  update: { $inc: { subscribers: 1 } },
  new: true,
})
```

Adding a new alement to an array:
```js
db.podcasts.updateOne(
  { _id: ObjectId("5e8f8f8f8f8f8f8f8f8f8f8") },
  { $push: { hosts: "Nic Raboy" } }
)
```
###### Deleting documents
```js
db.podcasts.deleteOne|deleteMany({category: “crime”})
```
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