Creating elements
```jsx
var dish = React.createElement("h1", { id: "recipe-0", 'datas-type': "title" }, "Baked Salmon");
```
On the attributes list one has to use className for CSS classes. Last argument is variadic, it can also accept results of further `React.createElement` calls - it will produce child elements. Root element of a component will always have the attribute `data-reactroot`. Hint: one can use map to create a list of HTML elements from an array of objects and put it as third argument to `React.createElement`. Adding element to DOM:
```JSX
ReactDOM.render(dish, document.getElementById('react-container'))
```
#### Creating components
The oldest way, may be deprecated in the future
```JSX
const MyComponent = React.createClass({  
    displayName: "MyComponent",  
    render() { return React.createElement(  
        // make use of e.g. this.props.items  
    ) }  
})  
const myComponent = React.createElement(MyComponent, { items }, null)  
ReactDOM.render(myComponent, document.getElementById('react-container'))
```
Before the render method there can also be other arguments - helper methods.
ECMAScript 6 class:
```JSX
class MyComponent extends React.Component {  
    // other helper methods  
    render() { return React.createElement( … ) }  
}
```
Stateless functional components:
```JSX
const MyComponent = props =>  
    React.createElement( /* make use of props */ )  
// with argument destructuring:  
const MyComponent = ({items}) => ...
```
Factories
```JSX
React.DOM.h1(null, "Baked Salmon")  
// own factory:  
const MyFactory = React.createFactory(MyComponent)  
ReactDOM.render(MyFactory({list}), document.getElementById('react-container')
```
Useful shorthand
```JSX
{ render } = ReactDOM;  
render( .… )
```
JSX syntax
```JSX
React.createElement(IngredientsList, {list: […]}) 
// is equivalent to 
<IngredientsList list="[…]"/>

// Expressions and code to be evaluated is put inside curly braces:  
<h1>{ "Hello, " + this.props.name}</h1>
```
#### Property validation
Using own `createClass`
```JSX
const Summary = createClass({  
    displayName: "Summary",  
    propTypes: {  
        ingredients: PropTypes.number  
        steps: PropTypes.number.isRequired,  
        title: (props, propName) =>  
            (typeof(props[propName] !== 'string') ~  
            new Error("A title must be a string)") :  
            (props[propName].length > 20) ?  
                new Error("Title is ober 20 characters") :  
                null  
    },  
    getDefaultProps() {  
        return {  
            ingredients: 0,  
            steps: 0,  
            title: "[untitled recipe]"  
        }  
    },  
    render() { … }  
}
```
In case of ECMAScript 6 classes and stateless components, one has to set properties `propTypes` and `defaultProps` after the component definition, for example, `Summary.defaultProps`. Inside a class one can also define
```JSX
static defaultProps = { … }
```
Available types:
```JSX
React.PropTypes.array
React.PropTypes.bool
React.PropTypes.func
React.PropTypes.number
React.PropTypes.object
React.PropTypes.string
```
#### Refs
Defining
```JSX
<input ref="_title" ... />
```
Usage in a function that needs it
```JSX
const { _title } = this.refs;
```
Inverse data flow
```JSX
const logColor = (title, color) => console.log(`New color: ${title} | ${color}`);

<AddColorForm onNewColor={logColor} />

submit() { // bound to onSubmit event of the form
	const { _title, _color } = this.refs;
	this.props.onNewColor(_title.value, _color.value);
}
```
#### React Router
Definiowanie tras, wraz z komponentem układu, który otrzymuje zagnieżdżone komponenty we właściwości `children` i może je wyświetlić:
```JSX
import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';

import Layout from '../components/layout';

import Home from './home';
import MyNotes from './mynotes';
import Favorites from './favorites';

const Pages = () => {
	return (
		<Router>
			<Layout>
				<Route exact path="/" component=Home />
				<Route path="/mynotes" component={MyNotes} />
				<Route path="/favorites" component={Favorites} />			
				<Route path="/note/:id" component={NotePage} />
			</Layout>
		</Router>
	);
}

export default Pages;
```
In the component `NotePage` we can access the parameter `id` as follows:
```JSX
import { Link } from 'react-router-dom';
// ...
const id = props.match.params.id;
// ...
<Link to=`note/${id}'>Permlink</Link>
```
To use routing in components which are not routes themselves:
```JSX
const Header = () => {
	<Link to="...">...</Link>
}

export default withRouter(Header);
```
Private routes and using **Redirect**:
```JSX
const PrivateRoute = ({ component: Component, ...rest }) => {
  return (
    <Route
      {...rest}
      render={props =>
        data.isLoggedIn === true ? (
          <Component {...props} />
        ) : (
          <Redirect
            to={{
              pathname: '/signin',
              state: { from: props.location }
            }}
          />
        )
      }
    />
  );
};
```