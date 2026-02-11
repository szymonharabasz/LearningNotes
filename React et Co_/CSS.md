Text transforms:
```css
text-transform: uppercase|small-caps|...;
```
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
Size of the element includes content, padding and border and not only content (which is default):
```css
_element_ {
    box-sizing: border-box|content-box;
}
```
# Flexbox
Configuring the container:
```css
_container_ {
    display: flex;
    flex-direction: row|row-reverse|column|column-reverse;
    /* In the main direction: */
    justify-content: flex-start|flex-end|center|space-between|space-around|space-evenly;
    /* Align elements of a given line in the cross direciton: */
     align-items: stretch|flex-start|flex-end|center|baseline;
     /* Wrap rows or not */
     flex-wrap: nowrap|wrap|wrap-reverse;
     /* Arrange multiple lines in the cross direction */
     align-content: stretch|center|flex-start|flex-end|space-between|space-around|space-evenly;
}
```
Additional gaps: `column-gap`, `row-gap`.
Configuring items:
```css
_item_ {
	/* Proportion by which it will grow compared to other items */
    flex-grow: _value_;
	/* Proportion by which it will shrink compared to other items */
    flex-shrink: _value_;
    /* Suggested initial size */
    flex-basis: _value_|auto|content;
    /* ordering items */
    order: _value_;
    /* Overriding the container's alignment setting */
    align-self: stretch|flex-start|flex-end|center|baseline;
}
```
If `flex-basis` is:
- value - it is the starting value from which the element will grow or shrink
- `content` - initial width will be set to the element's content
- `auto` - initial value set based on `width` or `height`, if they are absent, `auto` is equivalent to `content`.
# Grid
Defining the layout:
```css
.container {
    display: grid;
    grid-template-columns: 100px 200px 1fr repeat(3, 200px);  
    grid-template-rows: 100px 150px;           
    /* Justification in the row direction */
    justify-content: start|end|center|stretch|space-between|space-
➥around|space-evenly;
	/* Justification in the column direction */
    align-content: start|end|center|stretch|space-between|space-
➥around|space-evenly;
	/* Alignment within columns */
    justify-items: start|end|center|stretch;
    /* Alignment  within rows */
    align-items: start|end|center|stretch;
}
```
Additional gaps: `column-gap`, `row-gap`.
Instead of specific values for rows and columns there can be also `max-content`. `fr` - proportional to a fraction.
Configuring grid items:
```CSS
.itemb {
    grid-column-start: 3;     
    grid-column-end: span 3; /* span */
    grid-row-start: 1;        
    grid-row-end: 1; /* why end is the same as start? */
}

.itemd {
    grid-column-start: 2;     
    grid-column-end: 4;       
    grid-row-start: 2;        
    grid-row-end: end; /* until the last column */
    justify-self: start|end|center|stretch;
    align-self:  start|end|center|stretch;
}
```
Named areas:
```CSS
.container {
...
    grid-template-areas:                           
        'header header header header header'       
        'nav nav nav nav nav                  
        'main   main   main   main   sidebar'
        'footer footer footer footer footer';
}
.itema {
    ...
    grid-area: header;                             ②
}
...
```

# Responsive design
Configuring browser's default viewport size:
```HTML
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
Showing something only on a large enough screen:
```CSS
.quotation {
    display: none;                                ②
}
@media (min-width: 750px) {
	.quotation {
	    display: block;
	    grid-area: quotation                                ②
	}
}
```
Images
```HTML
<img 
    src="/images/img-small.png"                
    sizes="(max-width: 700px) 100vw, 75vw"     
    srcset="/images/img-small.png 450w,        
            /images/img-medium.png 900w,       
            /images/img-large.png 1450w">      
```
```
# Special selectors:
```css
.elem:first-letter
.elem:first-child
```