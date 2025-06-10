Basic tags:
`<h:head>`, `<h:body>`
`<h:oputputStyleSheet library="css" name="styles.css" />`
`<h:oputputStyleSheet library="js" name="webpack.js" />`
`<h:graphicImage library="images" name="image.png" />`
Note: In the abpve library is a subdirecotry of `src/main/webapp/resources``<h:form id="…"> … </h:form>``
`<h:messages styleClass="…" globalOnly="true" />`
`<h:message for="elementId" />``<h:panelGrid columns="3" columnClasses="…"> … </h:panelGrid><h:panelGroup layout="block" style="color: red" > … </h:panelGroup>`
`<h:outputLabel for="…" value="…"/>`
`<h:inputText id="…" value="…" label="…" required="true" />`
`<h:inputSecret … />`
`<f:attribute name="required" name="true" />` to be nested in other elements instead of putting attributes directly
`<f:param name="name" value="Szymon" />` to be nested e.g. in a `commandLink` to generate URL parameters
Selecting things:
`<h:commandButton action="…" actionListener="…" value="…" />`
`<h:selectBooleanCheckbox value="#{someClass.check}"/>`
```JSP
<h:selectManyCheckbox value="#{someClass.stringList}">  
	<f:selectItem itemValue="v1" itemLabel="Item 1"/>  
	<f:selectItem itemValue="v2" itemLabel="Item 2"/>  
	<f:selectItem itemValue="v3" itemLabel="Item 3"/>  
</h:selectManyCheckBox>
```
```JSP
<h:selectManyCheckbox value="#{someClass.stringList}">  
	<f:selectItems value="#{someClass.mapStringToString}"/>  
</h:selectManyCheckBox>
```
```JSP
<h:selectManyListbox value="#{someClass.stringList}"> 
	<f:selectItems value="#{someClass.mapStringToString}"/>  
</h:selectManyListBox>
```
```JSP
<h:selectOneListbox value="#{someClass.stringList}">  
	<f:selectItems value="#{someClass.mapStringToString}"/>  
</h:selectOneListBox>
```
```JSP
<h:selectManyMenu value="#{someClass.stringList}">  
	<f:selectItems value="#{someClass.mapStringToString}"/>  
</h:selectManyMenu>
```
```JSP
<h:selectOneMenu value="#{someClass.stringList}">  
	<f:selectItems value="#{someClass.mapStringToString}"/>  
</h:selectOneMenu>
```
```JSP
<h:selectOneRadio value="#{someClass.stringList}">  
	<f:selectItems value="#{someClass.mapStringToString}"/>  
</h:selectOneRadio>
```
Alternatively:  
```JSP
<h:selectManyCheckbox value="#{someClass.stringList}">  
	<f:selectItems value="#{someClass.collectionOfSelectItem}"/>  
</h:selectManyCheckBox>
```
Alternatively:  
```JSP
<h:selectManyCheckbox value="#{someClass.stringList}">  
	<f:selectItems value="#{someClass.collectionOfPOJOs}" 
		var="itm" itemLabel="#{itm.lab}" itemValue="#{itm.val}"/>  
</h:selectManyCheckBox>
```
Buttons and links:
```JSP
<h:outputLink value="http://www.amnesty.org" target="_blank"/>
<h:button value"Go" onclick="window.alert('Hi')"/>
<h:link value="Link text" outcome="#{myClass.whereToGoNext}"/>  
	<f:param name="param1" value="42/>  
	<f:param name="param2" value="Hello"/>  
</h:link>  
<h:link value="Link text" outcome="result_page"/>

<h:commandButton value"Submit" action="#{controller.register}"/><h:commandLink value"Submit" action="#{controller.register}"/><h:commandButton value"Submit" action="result_page"/>
```
Creating an HTML table:  
```JSP
<h:dataTable value="#{someClass.collection}" var="v">  
	<h:column>  
		<f:facet name="header">First name</f:facet>  
            #{v.firstName}  
    </h:column>  
    <h:column>  
		<f:facet name="header">Last name</f:facet>  
            #{v.lastName}  
    </h:column>  
</h:dataTable>
```
Conditions:  
```JSP
<h:outputText rendered="#{someClass.render} … >
```
Loops:  
```JSP
<ui:repeat value="#{someClass.collection}" var="x">  
	Do something with x  
</ui:repeat>
```
Uploading a file:
```
<h:form enctype="multipart/form-data" action="#{controller.submit}">  
    <h:inputFile value="#{controller.upload}" />  
</h:form>
```
```Java
@Named  
@...Scoped  
public class Controller implements Serializable {  
	private Part upload;  
    public void submit() {  
        try (InputStream input = upload.getInputStream()) {  
		    String n = upload.getSubmittedFileName();  
            String path = "…";  
            String name = "…";  
            Files.copy(input, new File(path + File.separator + name).toPath());  
        } catch (Exception e) {  
            e.printStackTrace(System.err);  
        }  
    }  
}
```
Validation tags (to be neasted in an input field):

```JSP
<f:validateBean> <!-- to use Bean Validation in the surrounding element -->
<f:validateDoubleRange minimum="…" maximum="…"/>
<f:validateLongRange minimum="…" maximum="…"/>
<f:validateLength minimum="…" maximum="…"/>
<f:validateRequired/>
<f:validateRegex/>
```
Conversion tags (also to be nested):
```JSP
<f:convertDate pattern="yyyy-MM-dd HH:mm:ss" type="date|time|both" 
		dateStyle="default|short|medium|long|full" 
		timeStyle="default|short|medium|long|full" locale="#
		{someClass.theLocale}" timeZone="#{someClass.theTimeZone}"/>
<f:convertNumber currencyCode="CNY" currencySymbol="CNY" groupingUsed="true" 
	integerOnly="true" locale="#{someClass.theLocale}" maxFractionDigits="4" 
	minFractionDigits="2" maxIntegerDigits="4" minIntegerDigits="2" pattern="#
	{someClass.decimalFormatString}" type="number|currency"percent" />
<f:converter converterId="com.example.MyConverter"/>  
```
```Java
@FacesConverter("com.example.MyConverter")  
public class TheConverter implements Converter {/*implementation*/}
```
Event listener tags:
```JSP
<h:commandButton value="Submit" action="#{user.register}">  
	<f:actionListener type="com.example.listeners.RegisterListener"/>  
</h:commandButton>  
```
```Java
public class RegisterListener implements ActionListener {  
    @Override  
	public void processAction(ActionEvent event) throws AbortProcessingEvent 
	{  
		System.out.println("action!");  
	}      
}
```
```JSP
<h:valueChangedListener> … implements ValueChangedListener
<h:phaseListener> … implements PhaseListener
<h:setPropertyActionListener value="valueToSet" target="#
	{myClass.fieldToReceiveValue}"/>
```
Other useful tags:
```JSP
<c:forEach items="#{userController.userList}" var="user">  
	<br/> #{user}  
</c:forEach>****
```
Using expression language: `value="#{custromerController.firstName}"`
Custom validation using Validator annotation:
```Java
@FacesValidator(name="emailValidator")  
public class EmailValidator implements Validator {

// If not valid:  
FacesMessage facesMessage = .…  
throw new ValidastorException(facesMessage);
```
```JSP
<f:validator validatorId="emailValidator/>
```
Custom validation using validation method - request scoped bean with method with the same arguments and the same behaviour as in the Validator interface
```JSP
<h:inputText validator="#{alphaValidator.validateAlpha}"/>
```
Then one possibility is a nested tag inside e.g. a `commandButton`.
AJAX:
```JSP
<f:ajax execute="…" renders="…" event="action" immediate="true"/>  
```
execute: ids of elements which have to be executed to get up-to-date values in the controller  render: Id(s) of element(s) that have to be rendered by the Ajax call
For, e.g., `inputText` one can use `event"keyup"` or other JavaScript event: `blur`, `change`, `click`, `dbclick`, `focus`, `keydown`, `keypress`, `keyup`, `mousedown`, `mousemove`, mouseup, `mouseover`, `select`, `valueChange`
One can wrap several elements in `<f:ajax>`, then the default event will be used.
`immediate` serves for short-circuiting the processing

HTML 5-friendly markup:

Normal `<!DCTYPE html>` with `<head>`, `<body>`,` <form>` etc. and JSF-specific attributes like `jsf:value="#{customerController.firstName}"` (appropriate `xmlns` is needed)
Facelets page with passthrough namespace for new HTML 5 attributes like `p:placeholder="First Name"`
Faces Flow:
Directory structure:  
```
WEB-INF  
-  customerinfo  
	    -- customerinfo-flow.xml (can be empty)  
	    -- customerinfo-page2.xhtml  
	    -- customerinfo-page3.xhtml  
	    -- customerinfo-page4.xhtml  
	    -- customerinfo.xhtml  
	    - customerinfo-return.xhtml
``` 
Pages navigate between each other
Their controller is a named beam wtth  
```Java
@FlowScoped("customerinfo")
```
Beans which can be automatically injected:
```Java
FacesContext
HttpServletRequest
ExternalContext
ServletContext

.getResourceAsStream(path);

HttpSession
```

Configuration to inject named beans into JSF pages, injecting FacesContext may not work without this:  
```Java
    @AllpicationScope  
    @FacesConfig(version=FacesConfig.Version.JSF_2_3)  
    public class ConfigurationBean {}
```
Navigating backwards:
On the main page, inside a button which links to a subpage:  
```JSP
<f:param name="backref" value="#{view-viewId}"/>
```
On the subpage:  
```JSP
	    <h:outputLink value="#{request.contextPath}#{param['backref']}">
```