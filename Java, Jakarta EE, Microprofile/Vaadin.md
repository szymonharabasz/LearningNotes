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
```
HTML labels
```java
checkbox.setLabelAsHtml("I'm <b>learning</b> Vaadin!");
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