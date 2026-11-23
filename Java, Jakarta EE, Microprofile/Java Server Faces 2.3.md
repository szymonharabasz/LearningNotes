JSF (now Jakarta Faces). Backing beans are CDI beans; see [CDI](Context%20and%20Dependency%20Injection.md) for scopes such as `@ConversationScoped`. A JSF-based login page is in [Security](Security.md).

The running example is a page where a dragon opens a new hoard.

## Setup
Without this, CDI-based features (injecting `FacesContext`, using `@Named` beans in EL) may not work:
```java
@ApplicationScoped
@FacesConfig(version = FacesConfig.Version.JSF_2_3)
public class FacesConfiguration { }
```
**Objects you can inject:** `FacesContext`, `ExternalContext`, `HttpServletRequest`, `HttpSession`, `ServletContext` (for example `servletContext.getResourceAsStream(path)`).

## Page basics
```xml
<h:head>
    <h:outputStylesheet library="css" name="styles.css"/>   <!-- library = subdirectory of src/main/webapp/resources -->
    <h:outputScript library="js" name="app.js"/>
</h:head>
<h:body>
    <h:graphicImage library="images" name="dragon.png"/>
    <h:messages globalOnly="true" styleClass="errors"/>

    <h:form id="hoardForm">
        <h:panelGrid columns="3" columnClasses="label,field,error">
            <h:outputLabel for="name" value="Dragon name"/>
            <h:inputText id="name" value="#{hoardController.dragonName}" label="Dragon name" required="true"/>
            <h:message for="name"/>

            <h:outputLabel for="pin" value="Vault PIN"/>
            <h:inputSecret id="pin" value="#{hoardController.pin}"/>
        </h:panelGrid>
        <h:panelGroup layout="block" style="color: red">...</h:panelGroup>
    </h:form>
</h:body>
```
- `<f:attribute name="required" value="true"/>` nested in a component does the same as setting the attribute directly.
- `<f:param name="dragon" value="Ignatius"/>` nested in a link adds a URL parameter.

## Selection components
They all follow the same pattern. The `selectMany*` components bind to a collection, the `selectOne*` components to a single value:
```xml
<h:selectBooleanCheckbox value="#{hoardController.insured}"/>

<h:selectManyCheckbox value="#{hoardController.treasureTypes}">
    <f:selectItem itemValue="GOLD" itemLabel="Gold"/>
    <f:selectItem itemValue="GEM"  itemLabel="Gems"/>
</h:selectManyCheckbox>

<h:selectOneMenu value="#{hoardController.cave}">
    <f:selectItems value="#{hoardController.caves}"/>   <!-- a Map<label,value> or a Collection<SelectItem> -->
</h:selectOneMenu>

<h:selectOneRadio value="#{hoardController.cave}">
    <f:selectItems value="#{hoardController.caveList}" var="c" itemLabel="#{c.name}" itemValue="#{c.id}"/>  <!-- POJOs -->
</h:selectOneRadio>
```
Others: `selectManyListbox`, `selectOneListbox`, `selectManyMenu`.

## Buttons and links
```xml
<h:commandButton value="Open hoard" action="#{hoardController.open}"/>   <!-- POST; action returns an outcome -->
<h:commandLink   value="Open hoard" action="#{hoardController.open}"/>
<h:commandButton value="Done" action="hoard-summary"/>                   <!-- static outcome = page name -->

<h:button value="Roar" onclick="window.alert('ROAR')"/>                  <!-- GET -->
<h:link value="My hoards" outcome="#{hoardController.nextPage}">
    <f:param name="dragon" value="Ignatius"/>
</h:link>
<h:outputLink value="https://www.amnesty.org" target="_blank">Plain link</h:outputLink>
```
**Navigating back.** On the main page, pass the current view as a parameter:
```xml
<h:link outcome="treasure-details"><f:param name="backref" value="#{view.viewId}"/></h:link>
<!-- on the sub-page -->
<h:outputLink value="#{request.contextPath}#{param['backref']}">Back</h:outputLink>
```

## Tables, loops, conditions
```xml
<h:dataTable value="#{hoardController.treasures}" var="t">
    <h:column>
        <f:facet name="header">Treasure</f:facet>
        #{t.name}
    </h:column>
    <h:column>
        <f:facet name="header">Value</f:facet>
        #{t.value}
    </h:column>
</h:dataTable>

<ui:repeat value="#{hoardController.treasures}" var="t">#{t.name}</ui:repeat>   <!-- render-time loop -->
<c:forEach items="#{hoardController.treasures}" var="t">#{t.name}</c:forEach>   <!-- JSTL: build-time loop -->

<h:outputText value="Cursed!" rendered="#{t.cursed}"/>
```

## Validation
```xml
<h:inputText value="#{hoardController.goldCoins}">
    <f:validateLongRange minimum="1" maximum="1000000"/>
</h:inputText>
```
Other validators: `<f:validateBean>` (Bean Validation, see [Bean Validation](Bean%20Validation.md)), `<f:validateDoubleRange>`, `<f:validateLength>`, `<f:validateRequired>`, `<f:validateRegex pattern="..."/>`.

**Custom validator class:**
```java
@FacesValidator("dragonNameValidator")
public class DragonNameValidator implements Validator<String> {
    @Override
    public void validate(FacesContext ctx, UIComponent component, String value) {
        if (!value.endsWith("the Terrible"))
            throw new ValidatorException(new FacesMessage("Every dragon needs an epithet"));
    }
}
```
```xml
<f:validator validatorId="dragonNameValidator"/>
```
**Validator method:** a bean method with the same signature as `Validator.validate`:
```xml
<h:inputText validator="#{nameValidator.validateAlpha}"/>
```

## Conversion
```xml
<f:convertDateTime pattern="yyyy-MM-dd HH:mm" type="date|time|both"
                   dateStyle="short|medium|long|full" timeZone="#{bean.timeZone}" locale="#{bean.locale}"/>
<f:convertNumber type="number|currency|percent" currencyCode="EUR" groupingUsed="true"
                 minFractionDigits="2" maxFractionDigits="4" pattern="#{bean.decimalFormat}"/>
<f:converter converterId="treasureConverter"/>
```
```java
@FacesConverter("treasureConverter")      // or @FacesConverter(forClass = Treasure.class) to apply it automatically
public class TreasureConverter implements Converter<Treasure> { ... }
```

## Listeners
```xml
<h:commandButton value="Open" action="#{hoardController.open}">
    <f:actionListener type="com.dragonbank.faces.AuditListener"/>
    <f:setPropertyActionListener target="#{hoardController.cave}" value="North Peak"/>
</h:commandButton>
```
```java
public class AuditListener implements ActionListener {
    @Override
    public void processAction(ActionEvent event) throws AbortProcessingException { ... }
}
```
Also: `<f:valueChangeListener>` (implements `ValueChangeListener`) and `<f:phaseListener>` (implements `PhaseListener`).

## AJAX
```xml
<h:inputText id="name" value="#{hoardController.dragonName}">
    <f:ajax event="keyup" execute="@this" render="greeting"/>
</h:inputText>
<h:outputText id="greeting" value="Welcome, #{hoardController.dragonName}!"/>
```
- `execute`: the components whose values are sent and processed.
- `render`: the components to re-render. Both also accept `@this`, `@form`, `@all` and `@none`.
- `event`: any DOM event (`blur`, `change`, `click`, `dblclick`, `focus`, `keydown`, `keyup`, `mouseover`, `select`, ...) or `valueChange`/`action`.
- `immediate="true"` processes the component in an earlier phase, which skips validation of the other components.
- Wrapping several components in `<f:ajax>` applies it to all of them, with each one's default event.

## File upload
```xml
<h:form enctype="multipart/form-data">
    <h:inputFile value="#{deedController.upload}"/>
    <h:commandButton value="Upload deed" action="#{deedController.submit}"/>
</h:form>
```
```java
@Named @RequestScoped
public class DeedController {
    private Part upload;                                    // jakarta.servlet.http.Part
    public void submit() throws IOException {
        try (InputStream in = upload.getInputStream()) {
            Files.copy(in, Path.of(deedDir, upload.getSubmittedFileName()));
        }
    }
}
```

## HTML5-friendly markup
- **Plain HTML elements with JSF attributes:** `<input type="text" jsf:id="name" jsf:value="#{hoardController.dragonName}"/>`, with the namespace `xmlns:jsf="http://xmlns.jcp.org/jsf"`.
- **HTML5 attributes that JSF doesn't know**, passed through to the output: `<h:inputText p:placeholder="Dragon name"/>`, with the namespace `xmlns:p="http://xmlns.jcp.org/jsf/passthrough"`.

## Faces Flow
A flow is a group of pages with its own bean scope:
```
hoardopening/                      (directory named after the flow, in the webapp root)
    hoardopening-flow.xml          (can be empty)
    hoardopening.xhtml             (entry page = flow name)
    hoardopening-page2.xhtml
    hoardopening-page3.xhtml
hoardopening-return.xhtml          (outside the flow)
```
The pages navigate to each other by name. Their controller has:
```java
@Named @FlowScoped("hoardopening")
public class HoardOpeningFlow implements Serializable { ... }
```

## Push (WebSocket)
```java
@Inject @Push                 // channel name = field name ("raidAlerts"), or @Push(channel = "...")
PushContext raidAlerts;
// ...
raidAlerts.send("Knight approaching!");
```
```xml
<f:websocket channel="raidAlerts" onmessage="onRaidAlert"/>
<script>
    function onRaidAlert(message, channel, event) { ... }
</script>
```
For plain WebSockets see [Servlets and WebSockets](Servlets%20and%20WebSockets.md).
