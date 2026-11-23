In JAX-RS ([Web services](Web%20services%20-%20JAX-RS%20and%20JAX-WS.md)), a resource that `@Produces`/`@Consumes` JSON or XML converts objects automatically with JSON-B or JAX-B. You can also return `JsonObject` or `JsonArray` (JSON-P) directly. With Jersey, adding `jersey-media-moxy` to the classpath enables JSON support (MOXy) with no other configuration.

## JSON-B (binding objects to JSON)
```java
Jsonb jsonb = JsonbBuilder.create();
String json = jsonb.toJson(dragon);
Dragon dragon = jsonb.fromJson(json, Dragon.class);

// Generic collections need the runtime type
List<Dragon> dragons = jsonb.fromJson(json, new ArrayList<Dragon>() {}.getClass().getGenericSuperclass());

// Configuration
Jsonb jsonb = JsonbBuilder.create(new JsonbConfig()
    .withPropertyNamingStrategy(PropertyNamingStrategy.LOWER_CASE_WITH_UNDERSCORES)
        // IDENTITY, LOWER_CASE_WITH_DASHES, UPPER_CAMEL_CASE, UPPER_CAMEL_CASE_WITH_SPACES, CASE_INSENSITIVE
    .withFormatting(true)
    .withDateFormat("yy/MM/dd", Locale.getDefault())
    .withBinaryDataStrategy(BinaryDataStrategy.BASE_64_URL));
```
**Annotations:**
```java
@JsonbPropertyOrder(PropertyOrderStrategy.LEXICOGRAPHICAL)   // on the class: LEXICOGRAPHICAL, REVERSE, ANY
@JsonbNillable                                               // on the class: serialize nulls (JSON-B 3: @JsonbProperty(nillable = true))
public class Dragon {
    @JsonbProperty("dragon_name") String name;
    @JsonbTransient String vaultPin;                         // never serialized
    @JsonbDateFormat("yy/MM/dd hh:mm a") LocalDateTime lastRaid;
    @JsonbNumberFormat("#0.00") BigDecimal goldCoins;
}
```

## JSON-P (processing JSON without classes)
### Object model API
```java
// Building
JsonObject dragon = Json.createObjectBuilder()
    .add("name", "Ignatius")
    .add("wingspan", 31)
    .add("cave", Json.createObjectBuilder().add("kingdom", "Eriador"))
    .build();

JsonArray array = dragons.stream()
    .map(d -> Json.createObjectBuilder().add("name", d.getName()).build())
    .collect(JsonCollectors.toJsonArray());

// Writing
StringWriter sw = new StringWriter();
try (JsonWriter writer = Json.createWriter(sw)) { writer.writeObject(dragon); }

// Reading
try (JsonReader reader = Json.createReader(new StringReader(json))) {
    JsonObject obj = reader.readObject();          // or readArray()
    String name = obj.getString("name");
}
```
**JSON Pointer and JSON Patch:**
```java
JsonPointer pointer = Json.createPointer("/1/name");     // the name of the second dragon
JsonValue name = pointer.getValue(dragonsArray);

JsonPatch patch = Json.createPatchBuilder()
    .replace("/1/name", "Brunhilde")
    .remove("/0")
    .build();
JsonArray patched = patch.apply(dragonsArray);            // JSON values are immutable; you get a new array
```

### Streaming API (for large documents)
```java
try (JsonGenerator gen = Json.createGenerator(sw)) {
    gen.writeStartObject()
           .write("name", "Ignatius")
           .write("wingspan", 31)
       .writeEnd();
}

JsonParser parser = Json.createParser(new StringReader(json));
while (parser.hasNext()) {
    JsonParser.Event event = parser.next();
    if (event == JsonParser.Event.KEY_NAME && "name".equals(parser.getString())) {
        parser.next();
        String name = parser.getString();
    }
}
```
Events: `START_OBJECT`, `END_OBJECT`, `START_ARRAY`, `END_ARRAY`, `KEY_NAME`, `VALUE_STRING`, `VALUE_NUMBER`, `VALUE_TRUE`, `VALUE_FALSE`, `VALUE_NULL`.

## JAX-B (binding objects to XML)
Annotate the class with `@XmlRootElement`, then use it with `@Produces`/`@Consumes(MediaType.APPLICATION_XML)`. JAX-B was removed from the JDK in Java 11, so add `jakarta.xml.bind-api` plus an implementation.

## JAX-P: DOM (the whole document in memory)
```java
DocumentBuilder builder = DocumentBuilderFactory.newInstance().newDocumentBuilder();
Document doc = builder.parse(new InputSource(new StringReader(xml)));   // or parse(InputStream / File)

Element root = doc.getDocumentElement();
NodeList children = root.getChildNodes();
Node node = children.item(3);
if (node.getNodeType() == Node.ELEMENT_NODE) {
    node.getNodeName();
    node.getTextContent();                                // getNodeValue() is null for elements
    node.getAttributes().getNamedItem("type").setNodeValue("gem");
}
Attr attr = doc.createAttribute("cursed");
node.getAttributes().setNamedItem(attr);

Element treasure = doc.createElement("treasure");
treasure.setTextContent("Arkenstone-like gem");
root.appendChild(treasure);
```

## JAX-P: SAX (streaming, event callbacks)
```java
class TreasureHandler extends DefaultHandler {
    @Override public void startElement(String uri, String localName, String qName, Attributes attrs) { ... }
    @Override public void endElement(String uri, String localName, String qName) { ... }
    @Override public void characters(char[] ch, int start, int length) { ... }   // can be called several times for one text node
}

SAXParserFactory.newInstance().newSAXParser()
    .parse(new InputSource(new StringReader(xml)), new TreasureHandler());
```
