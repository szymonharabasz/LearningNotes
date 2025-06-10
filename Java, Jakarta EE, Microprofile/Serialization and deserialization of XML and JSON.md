**JAX-B** Annotate the class which should be converted to/from XML with `@XmlRootElement`. Use with `@Consumes``/@Produces`
**JAX-P** 
```Java
String xml = …;  
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();  
DocumentBuilder builder = factory.newDocumentBuilder();  
Document document = builder.parse(  
    new InputStream(new ByteArrayInputStream(xml.getBytes())));  
Node root = document.getDocumentElement();
NodeList nodes = node.getChildrenNodes()
Node node = nodes.item(3)
node.getNodeType() == Node.ELEMENT_NODE
node.getNodeName()
node.getNodeValue()
node.setNodeValue("value")
node.getAttributes().getNamedItem("item").setNodeValue("value")
Attr attr = document.createAttribute("attribute");  
node.getAttributes().setNamedItem(attr);
Node newNode = document.createElement("newNode");  
newNode.setTextContent("text content");  
node.appendChild(newNode);
```
**SAX**
```Java
class UserHandler extends DefaultHandler {  
    @Override  
    public void startElement(String uri, String localName,  
        String qName, Attributes attributes) throws SAXException {}  
    @Override  
    public void endElement(String uri, String localName,  
        String qName) throws SAXException {}  
    @Override  
    public void characters(char ch[], int start, int length) throws 
	    SAXException {}

SAXParserFactory factory = SAXParserFactory.newInstance();  
SAXParser parser = factory.newSAXParser();  
parser.parse(  
    new InputStream(new ByteArrayInputStream(xml.getBytes())),  
    new UserHandler());
```
**JSON-P** Generating with JSON-P Model API:  
```Java
JsonObjectBuilder builder = Json.createObjectBuilder();  
JsonObject jsonObject = builder.add("firstName","John")  
    .add("lastName","Smith")  
    .add("email","smith@example.com")  
    .build();  
StringWriter stringWriter = new StringWriter();  
try (JSonWriter writer = Json.createWriter(stringWriter)) {  
    writer.writeObject(jsonObject);  
}  
String jsonString = stringWriter.toString();
```
Pattern for creating JsonArray:  
```Java
myList.stream().map(elem -> Json.createObjectBuilder().  
    .add("firstName", elem.getFirstName())  
    .add("lastName", elem.getLastName())  
    .build())  
.collect(JsonCollectors.toJsonArray());
```
In JAX-RS web services, one can directly return JsonObject or JsonArray
Parsing with JSON-P Model API:  
```Java
JsonObject jsonObject;  
try (JsonReader reader = Json.createReader(new StringReader(jsonString))) {  
    jsonObject = reader.readObject();  
}  
String firstName = jsonObject.getString("firstName");
```
Parsing using JSON Pointer:  
```Java
JsonArray jsonArray;  
try (JsonReader reader = Json.createReader(new StringReader(jsonString))) {  
    jsonArray = reader.readArray();  
    JsonPointer jsonPointer = Json.createPointer("/1/firstName/");  
}  
String firstName = jsonPointer.getValue(jsonArray).toString();
```
Updating using JSON Patch:  
```Java
JsonArray jsonArray;  
try (JsonReader reader = Json.createReader(new StringReader(jsonString))) {  
    jsonArray = reader.readArray();  
    JsonPatch jsonPatch = Json.createPatchBuilder()  
        .replace("/1/firstName/","Adam")  
         .build();  
    JsonArray modifiedArray = jsonPatch.apply(jsonArray);  
}
```
Generating with JSON-P Streaming API:  
```Java
StringWriter stringWriter = new StringWriter();  
try (JSonGenerator generator = Json.createGenerator(stringWriter)) {  
     generator.writeStartObject()  
    .write("firstName","John")  
    .write("lastName","Smith")  
    .write("email","smith@example.com")  
    .writeEnd();  
}  
String jsonString = stringWriter.toString();
```
Parsing with JSON-P Streaming API:  
```Java
JsonParser parser = Json.createParser(new StringReader(jsonString));  
while (parser.hasNext()) {  
    JsonParser.Event event = parser.next();  
    if (event.equals(Event.VALUE_STRING)) {  
        value = parser.getString();  
    }  
}
```
Possible events:  
`START_OBJECT`, `END_OBJECT`, `START_ARRAY`, `END_ARRAY`, `KEY_NAME`, `VALUE_TRUE`, `VALUE_FALSE`, `VALUE_NULL`, `VALUE_NUMBER`, `VALUE_STRING`

**JSON-B**
Consuming or producing z in a JAX-RS web service automatically serializes and deserializes a JSON object
Annotate a property with `@JsonbTransient` to not serialize it
Annotate a property with `@JsonbProperty("newName")` to render it in JSON with `newName`
One can annotate a property with:  
```Java
@JsonbDateFormat("yy/MM/dd hh:mm a");  
@JsonbNumberFormat("#0.00")
```
One can annotate the entity class with:  
```Java
@JsonbPropertyOrder(PropertyOrderStrategy.LEXICOGRAPHICAL|REVERSE|ANY)  
@JsonbNullable to display nulls
```
Populating Java object:  
 ```Java
Jsonb jsonb = JsonbBuilder.create();  
JsonbConfig config = new JsonbConfig()  
    .withPropertyNamingStrategy(  
            PropertyNamingStrategy.UPPER_CAMEL_CASE|UPPER_CAMEL_CASE_WITH_SPACES|  
                IDENTITY|LOWER_CASE_WITH_DASHES|LOWER_CASE_WITH_UNDERSCORES|  
                CASE_INSENSITIVE)  
    .withFormatting(true)  
    .withDateFormat("yy/MM/dd", Locale.getDefault())  
    .withBinaryDataStrategy(BinaryDataStrategy.BASE_64_URL);  
jsonb = JsonbBuilder.create(config);Customer customer = jsonb.fromJson(
	/* String */ customerJson, Customer.class);
```
Generating JSON string:  
```Java
String json = jsonb.toJson(filteredCustomerList);  
ArrayList<Customer> list = jsonb.fromJson(json,  
    new ArrayList<Customer>(){}.getClass.getGenericSuperclass());
```