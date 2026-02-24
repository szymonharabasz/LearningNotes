Use `Serializable` classes when you keep references to objects in UI classes. This is required, for example, when you are using session persistence in servers such as Apache Tomcat to allow sessions to be stored in the hard drive across restarts. All the UI components and other helper classes included in Vaadin implement `Serializable`.
#### Basic components
Text, password, and numeric fields
```java
TextField textField = new TextField();
textField.setLabel("Name");
textField.setPlaceholder("enter your full name");

textField.setAutoselect(true);
textField.setAutofocus(true);
textField.setClearButtonVisible(true);
textField.setValue("John Doe");

textField.setRequired(true);
textField.setMinLength(2);
textField.setMaxLength(10);
textField.setPattern("^[a-zA-Z\\s]+");
textField.setErrorMessage("Letters only. Min 2 chars");

textField.addValueChangeListener(event -> {
    if (textField.isInvalid()) {
	    // A good way to get the value from the component, using the reference
	    // to the component in the closure couples the code of the lambda with
	    // the code that defines the component 
        Notification._show_("Invalid name: " + event.getValue());
    }
});
textField.setValueChangeMode(ValueChangeMode.EAGER);
// ...
PasswordField passwordField = new PasswordField();
passwordField.setRevealButtonVisible(true);

NumberField numberField = new NumberField("Rating");
numberField.setHasControls(true);
numberField.setMin(0.0);
numberField.setMax(5.0);
numberField.setStep(0.5);
numberField.setHelperText("From 0.0 to 5.0");

IntegerField integerField = new IntegerField("Rating");
```
Ready-to-use login form
```java
LoginI18n i18n = LoginI18n._createDefault_();
LoginOverlay loginOverlay = new LoginOverlay(i18n);
loginOverlay.setTitle("Chapter 7");
loginOverlay.setDescription("Navigation and Routing");
loginOverlay.setOpened(true);
loginOverlay.addForgotPasswordListener(event ->
    Notification._show_("Use admin/admin or user/user"));
loginOverlay.addLoginListener(event -> {});
```
Check boxes
```java
checkbox.setIndeterminate(true);
```
Date and time inputs
```java
DatePicker datePicker = new DatePicker(
	"Enter a memorable date",
	LocalDate._now_(),
	event -> showMessage(event.getValue())
);
datePicker.setAutoOpen(false);
datePicker.setClearButtonVisible(true);
datePicker.setInitialPosition(LocalDate._now_().minusMonths(1));
datePicker.setMin(LocalDate._now_().minusMonths(3));
datePicker.setMax(LocalDate._now_().plusMonths(3));
datePicker.setLocale(Locale.CANADA);

TimePicker timePicker = new TimePicker("Pick a time");
timePicker.addValueChangeListener(event -> {
    LocalTime value = event.getValue();
    Notification._show_("Time: " + value);
});

DateTimePicker dateTimePicker = new DateTimePicker("When?");
```
Selection fields
```java
ComboBox<String> comboBox = new ComboBox<>("Department");
comboBox.setItems("R&D", "Marketing", "Sales", "HR");
comboBox.setItemLabelGenerator(Department::toString);

RadioButtonGroup<Department> radio = new RadioButtonGroup<>();
radio.setItems(list);

ListBox<Department> listBox = new ListBox<>();
listBox.setItems(list);

CheckboxGroup<Department> checkboxes = new CheckboxGroup<>();
checkboxes.setItems(service.getDepartments());

MultiSelectListBox<Department> listBox = new MultiSelectListBox<>();
listBox.setItems(service.getDepartments());
Set<Department> departments = listBox.getValue();
```
File upload
```java
Receiver receiver = new MemoryBuffer();
Upload upload = new Upload(receiver);
upload.setAcceptedFileTypes("text/plain");
upload.addSucceededListener(event -> {
    InputStream in = receiver.getInputStream();
    ... read the data from in ...
});

```
There are different implementations of the `Receiver` interface:
```java
MemoryBuffer, FileBuffer, MultiFileMemoryBuffer, MultiFileBuffer
```
HTML labels
```java
checkbox.setLabelAsHtml("I'm <b>learning</b> Vaadin!");
```
Links
```java
Anchor blogLink = new Anchor("https://www.programmingbrain.com",
	"Visit my technical blog");
Anchor vaadinLink = new Anchor("https://vaadin.com",
	new Button("Visit vaadin.com"));        
```
#### Display components
Detailed information about something
```java
new Details(
	product.getName() + (product.isAvailable() ? "" : " (not available)"),
	new HorizontalLayout(
	new Button(VaadinIcon.PENCIL.create(), event -> showProductForm(product)),
	new Button(VaadinIcon.TRASH.create(), event -> delete(product))
)
```
Menu
```java
MenuBar menuBar = new MenuBar();
MenuItem file = menuBar.addItem("File");
file.getSubMenu().addItem("New");
file.getSubMenu().addItem("Open");
MenuItem edit = menuBar.addItem("Edit");
edit.getSubMenu().addItem("Copy");
edit.getSubMenu().addItem("Paste");
```
Manu item can be `setCheckable(boolean)`.
Context menu
```java
ContextMenu contextMenu = new ContextMenu(target);
```
Notifications
```java
notification.setDuration(2000);
otification.setPosition(Notification.Position.MIDDLE);
```
Dialogs
```java
new Dialog(
    new VerticalLayout(
        new H2("Title"),
        new Text("Text!"),
        new Button("Button!!!")
    )
).open();
dialog.setModal(true);
dialog.setCloseOnOutsideClick(false);
dialog.setCloseOnEsc(true);
dialog.setDraggable(true);
```
Tabs
```java
Tab order = new Tab("Order");
Tab delivery = new Tab("Delivery");
Tabs tabs = new Tabs(order, delivery);
tabs.addSelectedChangeListener(event -> {
  Tab selected = event.getSelectedTab();
  tabsContainer.removeAll();
  if (order.equals(selected)) {
    tabsContainer.add(buildOrderTab());
  } else if (delivery.equals(selected)) {
    tabsContainer.add(buildDeliveryTab());
  }
});
```
Icons
```java
VaadinIcon.YOUTUBE.create()
VaadinIcon.EDIT.create()
```
Images
```java
Image photo = new Image(
    "https://live.staticflickr.com/65535/50969482201_be1163c6f1_b.jpg",
    "Funny dog"
);
StreamResource source = new StreamResource("logo", () -> 
	getClass().getClassLoader().getResourceAsStream("vaadin-logo.png")
);
Image logo = new Image(source, "Logo");
```
#### Layout components
Scroller
```java
Scroller scroller = new Scroller(layout);
```
Flex layout
```java
var layout = new FlexLayout(
    new Button("1"),
    new Button("2"),
    new Button("3")
);
layout.setFlexDirection(FlexLayout.FlexDirection.ROW__REVERSE);
layout.setFlexWrap(FlexLayout.FlexWrap.WRAP);
layout.setAlignContent(FlexLayout.ContentAlignment.SPACE_BETWEEN);
layout.setSizeFull();
// ...
layout.setFlexShrink(1d, button1);
layout.setFlexShrink(2d, button2);
```
#### Aspects of event processing
```java
event.getSource().setVisible(false);
event.getSource().setEnabled(false);
event.getSource().setDisableOnClick(true);
```
The method `setDisableOnClick` allows to prevent sending multiple request by a user.
## Routing and sessions
With annotation (+ the most universal implementation of a view)
```java
@Route("login")
public class AppLoginForm extends Composite<Component> {
  @Override
  protected Component initContent() {
    return new VerticalLayout(components);
  }
}
```
Programatically
```java
RouteConfiguration.forSessionScope().setRoute("admin", AdminView.class);
```
Navigation to a route
```java
UI.getCurrent().navigate(AdminView.class);
UI.getCurrent().navigate("admin");
```
Link to a route
```java
new RouterLink("Go to my data", DataView.class)
```
Sessions
```java
String data = (String) VaadinSession.getCurrent().getAttribute("data");
VaadinSession.getCurrent().setAttribute("data", data);
```
Routing lifecycle hooks
```java
@Route("data")

public class DataView extends Composite<Component> implements BeforeEnterObserver {
  @Override
  public void beforeEnter(BeforeEnterEvent event) {
  }
}

@Route("data")
public class DataView extends Composite<Component> implements BeforeLeaveObserver {
  @Override
  public void beforeLeave(BeforeLeaveEvent event) {
    ContinueNavigationAction action = event.postpone();
	// ...
    action.proceed();
  }
}
```
Route parameters
```java
@Route("template-parameter/:value")
//...
@Override
public void beforeEnter(BeforeEnterEvent event) {
  Optional<String> value = event.getRouteParameters().get("value");
  setValue(value.orElse("(no value)"))
}
```
Optional parameter
```java
@Route("template-parameter/:value?")
```
Match any path
```java
@Route("api/:path*")
```
Match with regular expression
```java
@Route("companies/:companyId?([0-9]/edit")
```
One can also use `getInteger(String)`, `getLong(String)`.
Typed parameters
```java
@Route("typed-parameter")

public class TypedParameterView extends Composite<Component>
    implements HasUrlParameter<Integer> {
    @Override
    @OptionalParameter // if it is indeed optional
	public void setParameter(BeforeEvent beforeEvent,
		Integer number) {
		text.setText("" + number);
	}
}
```
Query parameters
```java
@Override
public void beforeEnter(BeforeEnterEvent event) {
	Location location = event.getLocation();
	Map<String, List<String>> list = 
		location.getQueryParameters().getParameters();
    List<String> userIds = list.get("userId");
}
```
Setting browser title bar
```java
@PageTitle("This is the title")
```
Dynamic title
```java
@Route("dynamic-page-title")
public class DynamicPageTitleView extends Composite<Component>
	implements HasDynamicTitle {
	@Override
	public String getPageTitle() {
	    return "Title at " + LocalDateTime.now();
	 }
}
```