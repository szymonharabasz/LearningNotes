## Components
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
tabs.setOrientation(Tabs.Orientation.VERTICAL);
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
###### Router layouts
```java
public class MainLayout extends Composite<Component> implements RouterLayout {
```
To have the elements of the view added somewhere inside of the layput:
```java
@Override
public void showRouterLayoutContent(HasElement content) {
    container.removeAll();
    container.getElement().appendChild(content.getElement());
}
```
`container` is an component defined in the layout class and placed somewhere in the layout. It is then filled with the content of the view that uses this layout.
In a view that should use the layout
```java
@Route(layout = MainLayout.class)
```
When navigating to a view
```java
RouteConfiguration.forSessionScope().setRoute("admin", AdminView.class, 
	MainLayout.class);
```
## Data binding
```java
Binder<Product> binder = new Binder<>();
binder.bind(name, Product::getName, Product::setName);
binder.bind(manufacturer, Product::getManufacturer, Product::setManufacturer);
binder.bind(available, Product::isAvailable, Product::setAvailable);
binder.setBean(product);
```
Other way
```java
Binder<Product> binder = new Binder<>(Product.class);
binder.bind(manufacturer, "manufacturer");
```
Automatic binding
```java
Binder<Product> binder = new Binder<>(Product.class);
binder.bindInstanceFields(this);
binder.setBean(product);
```
One can define names by which the binding happens
```java
@PropertyId("name")
private TextField nameTextField = new TextField("Name");
```
More complicated conversions
```java
public class StringToCodeConverter implements Converter<String, Code> {
	@Override
	public Result<Code> convertToModel(String value, ValueContext context) {
	    for (Type t : Type.values()) 
			if (value.startsWith(t.toString())) {
				Code code = new Code(t, value.substring(t.toString().length()));
				return Result.ok(code);
			}
		}
		return Result.error("Error parsing the code");
    }
	@Override
	public String convertToPresentation(Code code, ValueContext context) {
		return code.getType().toString() + code.getNumber();
    }
}
```
Using it
```java
binder.forField(codeTextField)
    .withConverter(new StringToCodeConverter())
    .bind(Product::getCode, Product::setCode);
```
###### Validation
Adding validators
```java
binder.forField(name)
	.asRequired("The name of the product is required")
    .withValidator(value -> value.length() > 7, "Invalid phone number")
    .bind("manufacturer.phoneNumber");
```
Available validators
```java
EmailValidator, EmailValidator, LongRangeValidator, DateTimeRangeValidator, BigDecimalRangeValidator, FloatRangeValidator, ShortRangeValidator, BigIntegerRangeValidator, IntegerRangeValidator, DoubleRangeValidator, DateRangeValidator, ByteRangeValidator, StringLengthValidator, RangeValidator, RegexpValidator
```
Performing the validation
```java
event -> {
	binder.validate();
	if (binder.isValid()) {
		saveListener.run();
	} else {
		Notification._show_("Please fix the errors");
	}
})
```
Validating with Jakarta Bean Validation
```java
private BeanValidationBinder<Product> binder = 
	new BeanValidationBinder<>(Product.class);
```
## Interoperability with JavaScript
Loading a module
```java
@JsModule("script.js")
public class JavascriptIntegrationView extends Div { }
```
If the module contains a function added to a global object,
```js
window.ns = {
	toggle: function() { }
}
```
it can be called like this
```java
UI._getCurrent_().getPage().executeJs("ns.toggle()");
```
Passing function arguments and accessing returned value
```java
  UI.getCurrent().getPage()
      .executeJs("return ns.toggle($0)", image)
      .then(value -> Notification.show(value.asString()));
```
###### Calling Java methods from JavaScript
Annotating a method
```java
@ClientCallable
public void showClickNotification(Integer x, Integer y) {
	var message = String.format("Clicked at %d, %d", x, y);
	Notification.show(message, 3000, Position.BOTTOM_END);
}
```
Passing the view to the function
```java
UI.getCurrent().getPage().executeJs("return ns.init($0, $1)", image, this);
```
Accepting a view in a JavaScript function a calling the method
```js
window.ns = {
	init: function(element, view) {
	    element.onclick = event =>
	        view.$server.showClickNotification(event.clientX, event.clientY);
}
```
## Styling the app
Selecting a theme and a variant
```java
@Theme(themeClass = Material.class)
@Theme(themeClass = Lumo.class, variant = Lumo.DARK)
```
Selecting a variant for a component
```java
button.addThemeVariants(ButtonVariant.LUMO_PRIMARY);
```
Applying a CSS
```java
@CssImport("./custom-styles.css")
public class CustomCss extends Composite<Component> { }
```
Setting theme properties
```css
html {
  --lumo-font-family_: "Courier New", Courier, monospace;
  --lumo-font-size_: 1rem;
  --lumo-font-size-xxxl_: 3rem;
  --lumo-font-size-xxl_: 2.25rem;
  --lumo-font-size-xl_: 1.75rem;
  --lumo-font-size-l_: 1.375rem;
  --lumo-font-size-m_: 1.125rem;
  --lumo-font-size-s_: 1rem;
  --lumo-font-size-xs_: 0.875rem;
  --lumo-font-size-xxs_: 0.8125rem;
  --lumo-line-height-m_: 1.4;
  --lumo-line-height-s_: 1.2;
  --lumo-line-height-xs_: 1.1;
  --lumo-border-radius_: 0px;
  --lumo-size-xl_: 4rem;
  --lumo-size-l_: 3rem;
  --lumo-size-m_: 2.5rem;
  --lumo-size-s_: 2rem; 
  --lumo-size-xs_: 1.75rem;
  --lumo-space-xl_: 1.75rem;
  --lumo-space-l_: 1.125rem;
  --lumo-space-m_: 0.5rem;
  --lumo-space-s_: 0.25rem;
  --lumo-space-xs_: 0.125rem;
  --lumo-shade-5pct_: rgba(26, 26, 26, 0.05);
  --lumo-shade-10pct_: rgba(26, 26, 26, 0.1);
  --lumo-shade-20pct_: rgba(26, 26, 26, 0.2);
  --lumo-shade-30pct_: rgba(26, 26, 26, 0.3);
  --lumo-shade-40pct_: rgba(26, 26, 26, 0.4);
  --lumo-shade-50pct_: rgba(26, 26, 26, 0.5);
  --lumo-shade-60pct_: rgba(26, 26, 26, 0.6);
  --lumo-shade-70pct_: rgba(26, 26, 26, 0.7);
  --lumo-shade-80pct_: rgba(26, 26, 26, 0.8);
  --lumo-shade-90pct_: rgba(26, 26, 26, 0.9);
  --lumo-primary-text-color_: rgb(235, 89, 5);
  --lumo-primary-color-50pct_: rgba(235, 89, 5, 0.5);
  --lumo-primary-color-10pct_: rgba(235, 89, 5, 0.1);
  --lumo-error-text-color_: rgb(231, 24, 24);
  --lumo-error-color-50pct_: rgba(231, 24, 24, 0.5);
  --lumo-error-color-10pct_: rgba(231, 24, 24, 0.1);
  --lumo-success-text-color_: rgb(62, 229, 170);
  --lumo-success-color-50pct_: rgba(62, 229, 170, 0.5);
  --lumo-success-color-10pct_: rgba(62, 229, 170, 0.1);
  --lumo-shade_: hsl(0, 0%, 10%);
  --lumo-primary-color_: hsl(22, 96%, 47%);
  --lumo-error-color_: hsl(0, 81%, 50%);
  --lumo-success-color_: hsl(159, 76%, 57%);
  --lumo-success-contrast-color_: hsl(159, 29%, 10%);
```
Adding CSS classes
```java
div.addClassName("styled-div");
```
###### Style for Web Components
Style rules
```css
:host th {
	background: var(--lumo-primary-color-10pct);
}
```
`:host` selects the Shadow DOM of a Web Component. The component is specified with
```java
@CssImport(value = "./vaadin-grid.css", themeFor = "vaadin-grid")
public class CssClassesView extends Composite<Component> { }
```
`<vaading-grid>` is a Web Component that Vaadin creates.

The Form Layout component is responsive, one can set its responsive steps
```java
form.setResponsiveSteps(
    new ResponsiveStep("1px", 1),
    new ResponsiveStep("600px", 2),
    new ResponsiveStep("800px", 3)
);
```
App Layout
```java
public class BusinessAppLayout extends AppLayout {
	public BusinessAppLayout() {
	// ...
	addToNavbar(new DrawerToggle(), logo);
	// ...
	addToDrawer(tabs);
```
## Vaadin Fusion
###### A simple Lit component
```js
import { LitElement, html } from 'lit';
import { customElement } from 'lit/decorators.js';

@customElement('hello-web-component')
export class HelloWebComponent extends LitElement {
	render() {
	return html`
		<div>Hello, World!</div>`;
	}
}
```
###### Client components
One has to create `index.html` and `index.ts` in `frontend` directory, whose location depends on the packaging type. The easiest way is to copy them from the `target` directory.
In the `index.html`, one has to import styles consistent with those of server components:
```html
<custom-style>
	<style include=_"lumo-typography"_></style>
</custom-style>
```
In the `index.ts` file, one has to import the theme
```ts
import '@vaadin/vaadin-lumo-styles/all-imports';
```
One can create a client view as a Lit component, then import it and define a route that leads to it:
```ts
import './fusion-view';

const routes = [
	{ path: 'fusion', component: 'fusion-view'},
	...serverSideRoutes // IMPORTANT: this must be the last entry in the array
];
```
Importing existing Vaadin components
```ts
import '@vaadin/vaadin-button/vaadin-button';
```
Other component names
```xml
<vaadin-vertical-layout theme="padding">
<vaadin-horizontal-layout>
<vaadin-combo-box placeholder='Select a language...'
	items='["Java", "TypeScript", "JavaScript"]'></vaadin-combo-box>
<vaadin-button><iron-icon icon="vaadin:check"></iron-icon>
	Select
</vaadin-button>
```
Event listeners
```xml
<vaadin-button @click='${this.clickHandler}'>Click me!</vaadin-button>
```
Implementation
```ts
clickHandler() {
  ... logic here ...
}
```
For modifying other HTML elements
```ts
// In a class extendingLitElement
@query('#greeting-notification')
private notification: any;
// ...
setName(newName: string) {
	this.name = newName;
	this.notification.close();

}

greet() {
	let message:string = 'Hello, ' + this.name;
    this.notification.renderer = (root:any) =>
		root.textContent = message;
	this.notification.open();
}

// In render() method
<vaadin-text-field id='name' label="What's your name?"
	@value-changed='${(event:any) => this.setName(event.detail.value)}'>
</vaadin-text-field>
...
<vaadin-button @click='${this.greet}'>
	Send
</vaadin-button>
...
<vaadin-notification id='greeting-notification'></vaadin-notification>
```
###### State
```ts
@state()
private notificationOpen = false;

@state()
private name = '';

// In the render() method
<vaadin-notification
	.opened="${this.notificationOpen}"
	.renderer=${this.greetingRenderer}>
</vaadin-notification>

// Again in the class
greetingRenderer = (root: HTMLElement) => {
	let message = 'Hello, ' + this.name;
	root.textContent = message;
}
```
## Hilla
A framework that combines Spring Boot backend wth React frontend in a coherent way.
Creating a Java service that will be available to be called from TypeSctipt:
```java
@Endpoint
@AnonymousAllowed
public class CounterEndpoint {
    public int addOne(int number) {
        return number + 1;
    }
}
// or
@BrowserCallable
@AnonymousAllowed
public class CounterService {
    public int addOne(int number) {
        return number + 1;
    }
}
```
Methods inherited from base class are normally not exposed, unless they are annotated with:
```java
@EndpointExposed
public class ExposedClass {
    public String fromExposedClass() { 
        return "Hello from ExposedClass";
    }
}
```
#### Reactive endpoints
They return `Flux` or `EndpointSubscription`, a wrapper for `Flux` which allows to execute some logic on the server when the client cancels a subscription 
```java
@AnonymousAllowed
public Flux<@NonNull String> getClock() {
    return Flux.interval(Duration.ofSeconds(1)).onBackpressureDrop()
            .map(_interval -> new Date().toString());
}

@AnonymousAllowed
public EndpointSubscription<@NonNull String> getClockCancellable() {
    return EndpointSubscription.of(getClock(), () -> {
        LOGGER.info("Subscription has been cancelled");
    });
}
```
It is consumed on the client side with:
```ts
import { Subscription } from '@vaadin/hilla-frontend';
import { Button } from '@vaadin/react-components/Button.js';
import { TextField } from '@vaadin/react-components/TextField.js';
import { getClockCancellable } from 'Frontend/generated/ReactiveEndpoint';

export default function ReactiveView() {
  const serverTime = useSignal("");
  const subscription = useSignal<Subscription<string> | undefined>(undefined);

  const toggleServerClock = async () => {
    if (subscription) {
      subscription.cancel();
      subscription.value = undefined;
    } else {
      subscription.value = getClockCancellable().onNext((time) => {
        serverTime.value = time;
      });
    }
  }

  return (
    <section className="flex p-m gap-m items-end">
      <TextField label="Server time" value={serverTime.value} readonly />
      <Button onClick={toggleServerClock}>Toggle server clock</Button>
    </section>
  );
}
```
There is also `onError`, `onComplete` etc.
#### Client middleware
Basic structure
```typescript
import { Middleware, MiddlewareContext, MiddlewareNext } 
	from '@vaadin/hilla-frontend';

// A middleware is an async function, that receives the `context` and `next`
export const MyLogMiddleware: Middleware = async function(
  context: MiddlewareContext,
  next: MiddlewareNext
) {
  const {endpoint, method, params} = context;
  console.log(
    `${endpoint} - method: ${method} parameters: ${JSON.stringify(params)} `
  );

  // Fetch API Request and Reponse types
  const request: Request = context.request;
  const response: Response = await next(context);

  // The response is a Fetch API `Response` object.
  console.log(`Received response: ${response.status} ${response.statusText}`);

  // A middleware returns a response.
  return response;
  // or
  return await next(context);
}
```
Using it if the Hilla TypeScript client is instantiated:
```typescript
import { ConnectClient } from '@vaadin/hilla-frontend';
import { MyLogMiddleware } from './my-log-middleware';

const client = new ConnectClient({
  prefix: '/connect',
  middlewares: [MyLogMiddleware]
});

export default client;
```
Or when generated client is used
```typescript
import client from 'Frontend/generated/connect-client.default';
import { MyLogMiddleware } from './my-log-middleware';

client.middlewares = [MyLogMiddleware];
```
Middleware can modify request and response, e.g.,
```typescript
const url = context.request.url.replace(
  'https//my-app.example.com',
  'https://external-endpoint.example.com'
);
context.request = new Request(url, context.request);
// ...
return new Response('{}');
```
#### Client-side routes
Views defined in `src/main/frontend/views`. Special names:
`_starting-with-underscore.tsx` - ignored by the router
`@index.tsx` - index page
`@layout.tsx` - layout for other routes defined in the same (sub-)directory
In the component, one should render `<Outlet />`
`{parameter}.tsx` - route with mandatory parameter
`{{optionalParameter}}.tsx` - route with mandatory parameter
`{...wildcard}.tsx` - route that matches any character
The parameters can be accessed like this in `{productId}.tsx`:
```tsx
import { useParams } from 'react-router';
// ...
const { productId } = useParams();
```
With React Router, the wildcard parameter is always named `*`, for convenience, one can use destructuring rename:
```tsx
const { "*": wildcard } = useParams();
```
#### Creating menu from routes
```tsx
import { createMenuItems } from '@vaadin/hilla-file-router/runtime.js';
import { SideNav } from '@vaadin/react-components/SideNav.js';
import { SideNavItem } from '@vaadin/react-components/SideNavItem.js';
import { Outlet, useNavigate, useLocation } from 'react-router';

export default function MainMenu() {
  const navigate = useNavigate();
  const location = useLocation();

  return (
    <SideNav onNavigate={({path}) => path && navigate(path)} location={location}>
      {
        createMenuItems().map(({ to, icon, title }) => (
          <SideNavItem path={to} key={to}>
            {icon && <Icon icon={icon} slot="prefix"/>}
            {title}
          </SideNavItem>
        ))
      }
    </SideNav>
  );
}
```