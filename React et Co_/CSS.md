A *clearfix hack*, when a container collapses, because all its children are floats:
```css
.self-clear::after {
	content: "";
	display: block;
	clear: both;
}
```
Drop cap:
```css
.first-paragraph::first-letter {          ①
    float: left;                          ②
    padding-top: .1em;
    padding-right: .1em;                  ③
    color: darkred;                       ③
    font-size: 5em;                       ③
    line-height: .6em;                    ③
}
```
Positioning elements:
```css
_element_ {
    position: static|relative|absolute|fixed|sticky;
    top: _measurement_|_percentage_|auto;
    right: _measurement_|_percentage_|auto;
    bottom: _measurement_|_percentage_|auto;
    left: _measurement_|_percentage_|auto;
    z-index: _integer_|auto;
}
```
To be able to add block-like (like `height`) properties to inline elements, use:
```css
display: inline-block
```
# Flexbox
Configuring the container:
```css
_container_ {
    display: flex;
    flex-direction: row|row-reverse|column|column-reverse;
    /* In the main direction: */
    justify-content: flex-start|flex-end|center|space-between|space-around|space-evenly;
    /* In the cross direciton: */
     align-items: stretch|flex-start|flex-end|center|baseline;
}
```