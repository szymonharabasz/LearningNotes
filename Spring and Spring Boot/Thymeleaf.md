Basic template:  
```html
    <!DOCTYPE html>  
    <html xmlns="http://www.w3.org/1999/xhtml"  
           xmlns:th="http://www.thymeleaf.org">  
        <head>  
            <link rel="stylesheet" th:href="@{/styles.css}" />  
        </head>  
        <body>  
            <img th:src="@{/images/Cat.png}" />  
            <p th:text="${car.engine}">Engine placeholder</p>  
        </body>  
    </html>
```
Thymeleaf tag attributes:
```
th:href
th:src
th:text
th:style
th:each:  
```
```html
    <div th:each="car : ${cars}>  
        <span th:text="${car.name}">CAR NAME</span>  
    </div>
```
`th:if`
`th:value` (for `<input>`)
`th:object` (for `<form>`, corresponds to the argument of the method annotated with `@PostMapping`)
`th:action` (for `<form>`)  
```html
<form method="POST" th:action="@{/orders}" th:object="${order}">
```
Templating:
```
"@{/path/with/respect/to/context}"
"${requestAttribute}"
```
Object selection: If in the parent element there is object selection:  
```html
<div th:object="${session.user}>
```
Then in child elements its properties can be used with asterisk notation:  
```html
<span th:text="*{firstname}" />
```
In addition, the selected object is available via `#object`:  
```html
<span th:text="${#object.lastname}" />
```