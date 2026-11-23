Vaadin Flow is a server-side Java UI framework. For TypeScript/React front ends see [Vaadin Hilla and Fusion](Vaadin%20Hilla%20and%20Fusion.md).

The running example is the goblin tellers' desk application at DragonBank.

**Keep UI state `Serializable`.** Session persistence, for example Tomcat storing sessions on disk across restarts, requires every object referenced from UI classes to be serializable. All Vaadin components already are.

## Views
`Composite<Component>` is the most universal way to build a view: you expose only the content you return, not a layout's API.
```java
@Route("hoards")
@PageTitle("Hoards")
public class HoardsView extends Composite<Component> {
    @Override
    protected Component initContent() {
        return new VerticalLayout(new H2("Hoards"), grid);
    }
}
```

## Input components
**Text, password and number fields:**
```java
TextField name = new TextField("Dragon name");
name.setPlaceholder("e.g. Ignatius the Terrible");
name.setAutofocus(true);
name.setAutoselect(true);
name.setClearButtonVisible(true);
name.setRequired(true);
name.setMinLength(2);
name.setMaxLength(40);
name.setPattern("^[a-zA-Z\\s]+");
name.setErrorMessage("Letters only, at least 2");
name.setValueChangeMode(ValueChangeMode.EAGER);        // fire on every keystroke, not on blur
name.addValueChangeListener(event -> {
    if (name.isInvalid()) {
        // event.getValue() is better than name.getValue(): it doesn't couple the lambda to the field variable
        Notification.show("Invalid name: " + event.getValue());
    }
});

PasswordField pin = new PasswordField("Vault PIN");
pin.setRevealButtonVisible(true);

NumberField fireRating = new NumberField("Fire rating");
fireRating.setHasControls(true);
fireRating.setMin(0.0); fireRating.setMax(5.0); fireRating.setStep(0.5);
fireRating.setHelperText("From 0.0 to 5.0");

IntegerField goldCoins = new IntegerField("Gold coins");
```
**Date and time:**
```java
DatePicker lastRaid = new DatePicker("Last raid", LocalDate.now(), event -> show(event.getValue()));
lastRaid.setMin(LocalDate.now().minusMonths(3));
lastRaid.setMax(LocalDate.now());
lastRaid.setInitialPosition(LocalDate.now().minusMonths(1));
lastRaid.setAutoOpen(false);
lastRaid.setLocale(Locale.CANADA);

TimePicker feedingTime = new TimePicker("Feeding time");
DateTimePicker appointment = new DateTimePicker("Appointment with a teller");
```
**Selection:**
```java
ComboBox<Cave> cave = new ComboBox<>("Cave");
cave.setItems(service.getCaves());
cave.setItemLabelGenerator(Cave::getName);

RadioButtonGroup<TreasureType> type = new RadioButtonGroup<>();
ListBox<TreasureType> typeList = new ListBox<>();
CheckboxGroup<TreasureType> types = new CheckboxGroup<>();
MultiSelectListBox<TreasureType> multi = new MultiSelectListBox<>();
Set<TreasureType> selected = multi.getValue();          // all of them: setItems(...)

Checkbox insured = new Checkbox("Insured");
insured.setIndeterminate(true);
insured.setLabelAsHtml("Insured against <b>knights</b>");
```
**File upload:**
```java
MemoryBuffer buffer = new MemoryBuffer();               // also FileBuffer, MultiFileMemoryBuffer, MultiFileBuffer
Upload upload = new Upload(buffer);
upload.setAcceptedFileTypes("application/pdf");
upload.addSucceededListener(event -> {
    InputStream deed = buffer.getInputStream();
    // ...
});
```
**Ready-made login dialog:**
```java
LoginOverlay login = new LoginOverlay(LoginI18n.createDefault());
login.setTitle("DragonBank");
login.setDescription("Tellers only");
login.setOpened(true);
login.addForgotPasswordListener(e -> Notification.show("Ask the head goblin"));
login.addLoginListener(e -> { ... });
```

## Display components
```java
new Anchor("https://dragonbank.example", "DragonBank homepage");
new Anchor("https://dragonbank.example", new Button("Visit"));

new Details(treasure.getName() + (treasure.isCursed() ? " (cursed)" : ""),
    new HorizontalLayout(
        new Button(VaadinIcon.PENCIL.create(), e -> edit(treasure)),
        new Button(VaadinIcon.TRASH.create(),  e -> delete(treasure))));

MenuBar menu = new MenuBar();
MenuItem hoards = menu.addItem("Hoards");
hoards.getSubMenu().addItem("Open new");
hoards.getSubMenu().addItem("Close");               // MenuItem.setCheckable(true) for toggles
new ContextMenu(grid);                              // right-click menu on a target component

Notification n = new Notification("Knight spotted!");
n.setDuration(2000);
n.setPosition(Notification.Position.MIDDLE);

Dialog dialog = new Dialog(new VerticalLayout(new H2("Confirm"), new Text("Close this hoard?"), new Button("Yes")));
dialog.setModal(true);
dialog.setCloseOnOutsideClick(false);
dialog.setCloseOnEsc(true);
dialog.setDraggable(true);
dialog.open();

Tab deposit = new Tab("Deposit"), withdraw = new Tab("Withdraw");
Tabs tabs = new Tabs(deposit, withdraw);           // Tabs only switch; you swap the content yourself
tabs.setOrientation(Tabs.Orientation.VERTICAL);
tabs.addSelectedChangeListener(e -> {
    content.removeAll();
    content.add(e.getSelectedTab() == deposit ? depositForm() : withdrawForm());
});

new Image("https://dragonbank.example/ignatius.jpg", "Ignatius");
new Image(new StreamResource("logo", () -> getClass().getClassLoader().getResourceAsStream("logo.png")), "Logo");
```

## Layouts
```java
new Scroller(longContent);

FlexLayout flex = new FlexLayout(new Button("1"), new Button("2"), new Button("3"));
flex.setFlexDirection(FlexLayout.FlexDirection.ROW_REVERSE);
flex.setFlexWrap(FlexLayout.FlexWrap.WRAP);
flex.setAlignContent(FlexLayout.ContentAlignment.SPACE_BETWEEN);
flex.setFlexShrink(2d, button2);
flex.setSizeFull();

FormLayout form = new FormLayout();                  // responsive: the number of columns depends on the width
form.setResponsiveSteps(
    new FormLayout.ResponsiveStep("0", 1),
    new FormLayout.ResponsiveStep("600px", 2),
    new FormLayout.ResponsiveStep("800px", 3));

public class TellerAppLayout extends AppLayout {     // navbar + drawer
    public TellerAppLayout() {
        addToNavbar(new DrawerToggle(), logo);
        addToDrawer(tabs);
    }
}
```

## Events
```java
button.addClickListener(e -> e.getSource().setEnabled(false));
button.setDisableOnClick(true);     // disabled on the client immediately, so double clicks can't send two requests
```

## Routing
```java
@Route("hoards")                                          // declarative
RouteConfiguration.forSessionScope().setRoute("admin", AdminView.class);                       // programmatic
RouteConfiguration.forSessionScope().setRoute("admin", AdminView.class, TellerLayout.class);   // with a layout

UI.getCurrent().navigate(AdminView.class);                // or navigate("admin")
new RouterLink("My hoards", HoardsView.class);
```
### Route templates
```java
@Route("hoard/:hoardNumber")                  // required
@Route("hoard/:hoardNumber?")                 // optional
@Route("archive/:path*")                      // wildcard, matches the rest of the path
@Route("hoard/:hoardNumber?([0-9]*)/edit")    // with a regex

@Override
public void beforeEnter(BeforeEnterEvent event) {
    Optional<String> value = event.getRouteParameters().get("hoardNumber");   // also getInteger, getLong
    Map<String, List<String>> query = event.getLocation().getQueryParameters().getParameters();
}
```
**Typed parameters.** This is the alternative to templates:
```java
@Route("treasure")
public class TreasureView extends Composite<Component> implements HasUrlParameter<Integer> {
    @Override
    public void setParameter(BeforeEvent event, @OptionalParameter Integer itemNo) { ... }
}
```
### Navigation lifecycle
```java
public class HoardView ... implements BeforeEnterObserver, BeforeLeaveObserver {
    public void beforeEnter(BeforeEnterEvent event) { /* check access, read parameters, maybe event.rerouteTo(...) */ }
    public void beforeLeave(BeforeLeaveEvent event) {
        ContinueNavigationAction action = event.postpone();   // e.g. ask "discard changes?"
        // ... later:
        action.proceed();
    }
}
```
### Page title
`@PageTitle("Hoards")` sets a static title. For a dynamic one, implement `HasDynamicTitle`:
```java
public String getPageTitle() { return "Hoards at " + LocalTime.now(); }
```
### Router layouts
```java
public class TellerLayout extends Composite<Component> implements RouterLayout {
    private final Div container = new Div();     // the spot where views are inserted

    @Override
    public void showRouterLayoutContent(HasElement content) {
        container.removeAll();
        container.getElement().appendChild(content.getElement());
    }
}

@Route(value = "hoards", layout = TellerLayout.class)
```
### Session attributes
```java
VaadinSession.getCurrent().setAttribute("teller", teller);
Teller teller = (Teller) VaadinSession.getCurrent().getAttribute("teller");
```

## Data binding
```java
Binder<Hoard> binder = new Binder<>(Hoard.class);
binder.bind(dragonName, Hoard::getDragonName, Hoard::setDragonName);   // explicit getter/setter
binder.bind(cave, "cave");                                             // by property name (needs the class in the constructor)
binder.bind(caveContact, "cave.contactPhone");                         // nested property

binder.bindInstanceFields(this);           // automatic: matches field names to properties
@PropertyId("dragonName")                  // ...or you name the property explicitly
private TextField nameField = new TextField("Dragon name");

binder.setBean(hoard);                     // two-way: every change goes straight into the bean
// or readBean(hoard) / writeBean(hoard) for buffered editing
```
**Converters and validators:**
```java
binder.forField(itemCode)
    .asRequired("Every treasure needs a code")
    .withValidator(code -> code.length() > 3, "Code too short")
    .withConverter(new StringToTreasureCodeConverter())
    .bind(Treasure::getCode, Treasure::setCode);

public class StringToTreasureCodeConverter implements Converter<String, TreasureCode> {
    @Override
    public Result<TreasureCode> convertToModel(String value, ValueContext ctx) {
        for (TreasureType t : TreasureType.values())
            if (value.startsWith(t.prefix()))
                return Result.ok(new TreasureCode(t, value.substring(t.prefix().length())));
        return Result.error("Unknown treasure code");
    }
    @Override
    public String convertToPresentation(TreasureCode code, ValueContext ctx) {
        return code.type().prefix() + code.number();
    }
}
```
Built-in validators: `EmailValidator`, `RegexpValidator`, `StringLengthValidator`, `RangeValidator`, and `*RangeValidator` for every numeric and date type.

**Validating on save:**
```java
save.addClickListener(e -> {
    if (binder.validate().isOk()) saveListener.run();
    else Notification.show("Please fix the errors");
});
```
**Bean Validation annotations instead of binder validators:** `new BeanValidationBinder<>(Hoard.class)`; see [Bean Validation](Bean%20Validation.md).

## JavaScript interop
```java
@JsModule("./dragon-effects.js")              // a module that defines e.g. window.ns = { roar(el) {...}, init(el, view) {...} }
public class EffectsView extends Div {

    void roar() {
        UI.getCurrent().getPage()
            .executeJs("return ns.roar($0)", image)       // $0, $1... = arguments; elements are passed as DOM nodes
            .then(result -> Notification.show(result.asString()));
    }

    void wire() { UI.getCurrent().getPage().executeJs("ns.init($0, $1)", image, this); }

    @ClientCallable                           // callable from JS
    public void clicked(int x, int y) { Notification.show("Clicked at " + x + ", " + y); }
}
```
```javascript
window.ns = {
    init(element, view) {
        element.onclick = e => view.$server.clicked(e.clientX, e.clientY);
    }
};
```

## Styling
```java
@Theme(themeClass = Lumo.class, variant = Lumo.DARK)   // Vaadin 14; newer: @Theme("my-theme") on the AppShellConfigurator
button.addThemeVariants(ButtonVariant.LUMO_PRIMARY);
div.addClassName("hoard-card");

@CssImport("./styles/custom.css")
@CssImport(value = "./styles/grid.css", themeFor = "vaadin-grid")   // styles INSIDE a component's shadow DOM
```
`grid.css` uses `:host`, which selects the Web Component (here `<vaadin-grid>`) from inside its shadow DOM:
```css
:host th { background: var(--lumo-primary-color-10pct); }
```
**Lumo theme properties** are set in global CSS. Each family comes in sizes `xxs` ... `xxxl` or in percentages:
```css
html {
    --lumo-font-family: "Courier New", monospace;
    --lumo-font-size-m: 1.125rem;          /* also -xxs ... -xxxl */
    --lumo-line-height-m: 1.4;             /* -xs, -s, -m */
    --lumo-border-radius: 0px;
    --lumo-size-m: 2.5rem;                 /* component heights, -xs ... -xl */
    --lumo-space-m: 0.5rem;                /* spacing, -xs ... -xl */
    --lumo-shade: hsl(0, 0%, 10%);         /* plus --lumo-shade-5pct ... -90pct */
    --lumo-primary-color: hsl(22, 96%, 47%);       /* dragon-fire orange; plus -50pct, -10pct, --lumo-primary-text-color */
    --lumo-error-color: hsl(0, 81%, 50%);          /* same variants */
    --lumo-success-color: hsl(159, 76%, 57%);      /* same variants, plus --lumo-success-contrast-color */
}
```
