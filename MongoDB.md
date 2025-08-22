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
#### CRUD operations
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
Ascending order: `1`, descending order: `-1`.

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

Coumting documents that match a certain query:
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
db.podcasts.deleteOne|deleteMany|findOneAndDelete({category: “crime”})
```
#### Aggregations
Randomly sampling data:
```js
db.movies.aggregate([
	$sample: { size: 1 }}
])
```
Matching documents:
```js
db.movies.aggregate([
	$match: query_document}
])
```
`query_document` works exactly like in the `find()` method.

Grouping documents:
```js
db.zips.aggregate([
{
   $group: {_id: "$city", totalZips: { $count : { } }}
}])
```
`$city` is a reference to a field in the original document (from the `zips` collection), `$count` is an operator.

Sorting and limiting:
```js
db.zips.aggregate([
	{$sort: {pop: -1}},
	{$limit: 9}
])
```
Projections in pipelines:
```js
{
    $project: {
        state:1, 
        zip:1,
        population:"$pop",
        _id:0
    }
}
```
Setting new values:
```js
{
    $set: {
        place: {
            $concat:["$city",",","$state"]
        },
        pop:10000
     }
  }
```
There are also operators like: `$multiply`. `$divide`, `$sum.

Counting documents in a pipeline:
```js
{
  $count: "total_zips"
}
```
Outputting to a new (or overwriting an existing) collection:
```js
{ $out: { db: "<output-db>", coll: "<output-collection>" } }
{ $out: "<output-collection>"}
```
#### Transactions:
```js
const session = db.getMongo().startSession()
session.startTransaction() // no shell output

const account = session.getDatabase('dbname').getCollection('collname')

session.commitTransaction()
// or
session.abortTransaction() // no shell output
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
#### Indexes
Creating single field index:
```js
db.customers.createIndex({email: 1}, {unique:true})
```
Creating compound index:
```js
db.customers.createIndex({active:1, birthdate:-1,name:1})
```
The recommended order of the fields in an index is their usage in a query:
- Equality
- Sort
- Range
Fields that are used for sorting in opposite orders in queries should have opposite sorting in the index (`1` and `-1).
Viewing indexes:
```js
db.customers.getIndexes()
```
Viewing a query execution plan to check if an index was used:
```js
db.customers.explain().find(query)
```
Index may **cover** a query if it contains all the fields that are used in the query.

Hiding and deleting indexes:
```js
db.customers.dropIndex('active_1_birthdate_-1_name_1')
db.customers.dropIndex({active:1, birthdate:-1, name:1})

db.customers.dropIndex('active_1_birthdate_-1_name_1')
db.customers.dropIndex({active:1, birthdate:-1, name:1})

db.customers.dropIndexes()
db.collection.dropIndexes('index1name')
db.collection.dropIndexes(['index1name', 'index2name', 'index3name'])
```
# Using the Python client
Connecting with PyMongo:
```python
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import IbjectId

load_dotenv()
MONGO_URI = os.environ("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client.bank
accounts_collection = db.accounts
```
Inserting documents:
```python
new_account = { ... }

result = accounts_collection.insert_one(new_account)
document_id = result.inserted_id

new_accounts = [{...}, {...}]

result = accounts_collection.insert_many(new_accounts)
document_ids = result.inserted_ids

client.close()
```
Querying for a document:
```python
result = collection.find_one(query_document)
cursor = collection.findfind(query_dcument_2)

for document in cursor:
	pass
```
Updating documents:
```python
result = accounts_collection.update_one(document_to_update, add_to_balance)
print("Documents updated: " + str(result.modified_count))

result = accounts_collection.update_many(select_accounts, set_field)
print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
```
Deleting documents:
```python
result = accounts_collection.delete_one(document_to_delete)
print("Documents deleted: " + str(result.deleted_count))result = accounts_collection.delete_many(documents_to_delete)
print("Documents deleted: " + str(result.deleted_count))
```
`delete_many` with empty filter document removes all documents in a given collection.

Aggregations:
```python
results = collection.aggregate(pipeline)
```

Transactions:
```python
# Step 1: Define the callback that specifies the sequence of operations 
# to perform inside the transactions.
def callback(
    session,
    transfer_id=None,
    account_id_receiver=None,
    account_id_sender=None,
    transfer_amount=None,
):

    accounts_collection = session.client.bank.accounts

    # Transaction operations
    # Important: You must pass the session to each operation

    accounts_collection.update_one(
        {"account_id": account_id_sender},
        {
            "$inc": {"balance": -transfer_amount},
            "$push": {"transfers_complete": transfer_id},
        },
        session=session,
    )
    accounts_collection.update_one(
        {"account_id": account_id_receiver},
        {
            "$inc": {"balance": transfer_amount},
            "$push": {"transfers_complete": transfer_id},
        },
        session=session,
    )
    return

def callback_wrapper(s):
    callback(
        s,
        transfer_id="TR218721873",
        account_id_receiver="MDB343652528",
        account_id_sender="MDB574189300",
        transfer_amount=100,
    )

# Step 2: Start a client session
with client.start_session() as session:
    # Step 3: Use with_transaction to start a transaction, execute the callback, 
    # and commit (or cancel on error)
    session.with_transaction(callback_wrapper)
```