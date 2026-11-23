> **Compare:** Thymeleaf templates are plain HTML files with `th:` attributes, so they open in a browser as static prototypes. JSF Facelets use components and a component tree instead ([JSF](../Java,%20Jakarta%20EE,%20Microprofile/Java%20Server%20Faces%202.3.md)). In Quarkus the counterpart is **Qute**, which uses `{expression}` syntax and is type-safe at build time.

```properties
spring.thymeleaf.cache=false     # in development: see template changes without restarting
```

## Basic template
```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <link rel="stylesheet" th:href="@{/styles.css}"/>        <!-- @{...}: URL relative to the context path -->
</head>
<body>
    <img th:src="@{/images/dragon.png}"/>
    <p th:text="${treasure.name}">Treasure name placeholder</p>   <!-- ${...}: model attribute; the body is replaced -->

    <div th:each="t : ${treasures}">
        <span th:text="${t.name}">NAME</span>
        <span th:if="${t.cursed}" th:style="'color: red'">cursed!</span>
    </div>
</body>
</html>
```
Other attributes: `th:value` (for inputs), `th:href`, `th:src`, `th:style`, `th:if`/`th:unless`, `th:each`.

## Forms and selection expressions
`th:object` selects an object. In child elements, `*{...}` refers to its properties, and the object itself is `#object`:
```html
<form method="POST" th:action="@{/appraisals}" th:object="${appraisalForm}">   <!-- the @PostMapping method's argument -->
    <input type="text" th:field="*{coins}"/>
    <span th:if="${#fields.hasErrors('coins')}" th:errors="*{coins}"></span>
</form>

<div th:object="${session.teller}">
    <span th:text="*{name}"></span>
    <span th:text="${#object.cave}"></span>
</div>
```
