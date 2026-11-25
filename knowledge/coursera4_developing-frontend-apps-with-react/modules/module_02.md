# Module 2: Understanding Function Components with Array and DOM Manipulation

### 1. [VIDEO TRANSCRIPT] Working with Function Components: Props and Event Handling Video • 6 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/7wRHz/working-with-function-components-props-and-event-handling
- **Method:** `dom_transcript` | **Length:** 5727 chars

Welcome to Working with Function Components – Props and Event Handling. After watching this video, you will be able to Explain the value of props and default props in components Summarize how to use props to pass data between components Describe props principles Discuss how events work in conjunction with props. In Function Components, properties are referred to as props. Primarily, props allow you to pass data from one component to another. Essentially, a prop works similarly to an object. A prop stores the attributes of a component and allows you to pass these attributes from a parent component to its child. However, you should note that you cannot change these attributes.

Props are immutable, meaning the data is read-only, and you cannot change them within a child component. In this example, this App component functions as the primary component of the project. Inside the App Function component, data gets passed into a child component named EmployeeData. The App's return statement assigns the EmployeeData component's name attribute to John. Note that these examples do not include import or export statements. Now, examine the EmployeeData component, shown here. You can see the Props parameter passed into the component.

You could provide any object name instead of props. But conventionally, you should use props to improve readability. Inside the H1 element within the return statement, you use the name with the dot operator. The Props object contains all the properties passed to a component. When you use a component and pass it an attribute, such as name equals John, that attribute becomes a property of the Props object within the component. You can also pass the data in other formats as well. In this example, change the App component's return statement.

Notice that in this version, you declare a const named EmployeeID and assign the value 111. You can pass this prop dynamically to the EmployeeData component using curly braces. Also, the KeyDepartmentID prop is set to the static value 567 directly in the return statement. To do this, use curly braces around the 567 prop value. The structure discussed establishes the foundation for rendering UI elements and passing data within the React application. You can then access these details using the Props object and render these attributes on the front end using the dot operator. You can define default values for a component's props.

If the Parent component does not provide a value for a particular prop, its Child component will use the default value specified in the Child component's DefaultProps object. This statement appears immediately before the Export statement. The default value of the EmployeeData component ensures consistent rendering even if you do not explicitly provide these values in the Parent component. In this case, if the Parent component does not pass in the dept_name attribute, the component supplies the default value, HumanResources, to the DepartmentName prop. The principles behind the usefulness of props and function components include reusability, unidirectional data flow, customization, and composition. Let's discuss each of these. Regarding reusability, passing different props allows you to create variations of the same component without duplicating code.

You can customize the behavior and appearance of your components based on different conditions or data. The unidirectional flow of data makes it easy to see how data gets passed and updated throughout your application, enabling errors to be spotted easily. Props enable customization. You can write code that is simple yet robust. You can use the same components, but the props provide flexibility. Props facilitate component composition throughout communication among these simpler components to build complex UIs. Let's also consider using event handling with props as an example.

In this app example, we pass an attribute named Increase with a value of $10,000. In this component named Props, the UseState hook manages the state of the ShowIncrease value. Showing an increase determines whether or not to display the annual salary increase information. Hooks and states are important parts of React function components. Here's how the UseState hook and the click event work in the component. The UseState hook creates state variables. In this case, the ShowIncreaseState variable holds a boolean value indicating whether the app should display the annual salary increase data.

When the user selects the Display Annual Salary Increase button, it triggers an arrow function defined within the OnClick event handler called the SetShowIncreaseTrue inside this arrow function. This function sets the state of ShowIncrease to be true, indicating that the UI should display the annual salary increase. The component uses the conditional double and expression for conditional rendering. If ShowIncrease is true, the yearly increase information displays within a div element. Otherwise, the component does not display this value. This image shows the output of this code. You can see that when the ShowIncrease boolean value is false, the increase amount is not displayed.

When the user clicks the button, the button label changes and the UI displays the value of the increase attribute. In this video, you learned a prop stores the attributes of a component and allows you to pass these attributes from parent to child. You pass a prop's object as a parameter into a component. Define the data using the dot operator in the format prop's dot attribute name. Prop's principles include reusability, unidirectional data flow, customization, and composition. You can use the UseState hook in conjunction with an event to control a child component.

---

### 2. [VIDEO TRANSCRIPT] Component Composition Video • 4 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/b6JCv/component-composition
- **Method:** `dom_transcript` | **Length:** 4153 chars

Welcome to Component Composition. After watching this video, you will be able to Describe the purpose of component composition Explain principles of function component composition Provide an example of component composition You can combine multiple components using composition. With function components, you combine multiple smaller components To create complex functionality. You can build a larger UI structure using small building blocks. Let's discuss a few principles of function component composition Including abstraction, reusability, hierarchy, props and children And higher-order components, also called HOCs. Let's discuss these aspects, starting with abstraction. The abstraction principle means you can make reusable components That encapsulate UI features.

It provides a way to break down a large abstract UI Into smaller chunks of code. Component composition allows you to reuse these chunks of code Making it easier to organize and maintain. You avoid duplicating the same code. The hierarchy principle allows you to arrange components in a hierarchy With parent and child components. This hierarchical structure also assists with organization and modular design. Component composition allows you to pass data From one component to another easily. Props allow you to pass data from a parent component to its child.

Components allow you to pass the entire component into other components. You can write functions, called higher-order components That accept components as input Or return a component with enhanced functionality. Higher-order components allow you to add components' features Such as state management or logic Without modifying its implementation. Let's walk through an example Demonstrating the use case of these composition principles. Consider a blog for writing about novels. The following code examples encapsulate specific features To create a generic blog post for novels Such as title, author, type, and description. In a real application, you would organize these components Into separate files for better code organization and maintainability.

In this example, each component implements one feature. Each primary feature has a similar structure. Let's take a look. Here, you see the title component. Notice the structure. Import the React library. Define the function with its name and its parameter.

Return the formatted content. Export the component. Recall we need additional components for author, type, and description. Let's look at these in comparison to the title component. Here's the author component. Note the similarity in their structures. You simply replace the function name and its parameter.

Then you format the content with appropriate HTML tags. Last, you change the name of the exported component. Similarly, you make the same replacements with the description component. Change the name of the function. Change the HTML. And change the export statement. And same for the type component.

Change the function name, the HTML, and the name of the exported component. Now let's look at the code for a higher-order component. This component pulls in the other components to create a page containing all of the data and formatting. Note that each component we discussed gets imported. Title, author, type, and description. You name the function NovelBlog. Then take each imported component as the function's parameters.

You return the component styled with appropriate HTML tags. This component is a function that takes components as its parameters and then returns a more complex component. Then finally, you will see the main application component code here. Let's walk through it. You import the components into the main app component, where you define the app function and compose them to create the front end. You create an instantiation of the novel component with appropriate data for the title, author, description, and type components. In this lesson, you learned that you use component composition to combine smaller components to create a complex UI.

Principles of component composition include abstraction, reusability, hierarchy, props and children, and higher-order components.

---

### 3. [VIDEO TRANSCRIPT] State Management in Function Components Video • 7 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/wsZaR/state-management-in-function-components
- **Method:** `dom_transcript` | **Length:** 6305 chars

Welcome to State Management in Function Components. After watching this video, you will be able to explain the concept of state management, explain the value of state management when developing function components, describe the syntax of the useState hook, manipulate a component's state using the useState hook. In React, you will use states to manage data that can change over time within a component. A component's state refers to the condition of that component at a specific time. The state of an object holds information that influences its behavior and renders it based on that information. Before the introduction of hooks, React could not manage the state of function components. Now, function components have local state management capabilities.

You will see a demonstration of the useState hook function in this video. Hooks enable you to reuse code logic across components without changing component hierarchy or introducing unnecessary nesting. They also make it easier to share and compose functionality across different components. Let's look at a commonly used hook named useState. The useState hook allows you to add state management functionalities to function components. It returns a stateful value using one variable and a function to update the value of that variable. You can see the syntax here.

You call the useState function and pass in the initial state as a parameter. Assign the return value to a const array variable. The array has two values: the stateName and the stateName prefixed with the keyword, set. Let's take a closer look at each of these tokens. This syntax uses array destructuring for the const variable. Array destructuring allows you to extract values from an array and assign them to individual variables. Using this feature to assign variables with an array simplifies your code when accessing array elements by avoiding repetitive indexing.

In this case, it extracts two values from the array returned by useState and assigns them to variables named stateName and setStateName, respectively. The stateName variable stores the current state value. This variable represents the current state of the component. You can access it and update it as needed. You can use the setStateName function provided by the useState hook to update the state value. When you call setStateName, React will re-render the component with the updated state value, triggering any necessary UI updates. You pass the initial state value into the useState function as a parameter.

This value initializes the stateName variable when first rendering the component. Next, you will see this syntax demonstrated with an example. Let's look at the code used to develop a UI similar to what is shown here. Before the user selects the button, the interface displays "The name is John." After the button selection, the interface will display "The name is John Doe." You can use this component, StateManagement, to manage and display the component's state with the useState hook. The component imports the necessary dependencies from the React package, including React and the useState hook.

Inside the component function, you declare a state variable name function, setName, to update the name state variable using the useState hook. The code sets the initial value of the nameState variable to John. The useState hook returns an array with two elements: the current state value of the name variable and a function, setName, to update that state value. You use array destructuring syntax to assign these elements to variables. The component returns JSX elements encapsulated within a fragment. It includes an H1 element displaying the title "State Management using useState," and a paragraph element showing the current value of the name state variable using JSX interpolation. Next, we take a closer look at the purpose of set state.

Say you initialize the name value to John as in the previous example, and now you want to update the user's name from John to John Doe when the user selects a button. In this code, we named the object setName. You should use this set state function for this. This code adds a button element to the JSX returned by the component. This button has an onClick event handler attached to it. When the user clicks the button, it calls the updatedName function, which in turn calls the setName function embedded in the updatedName function with the argument, John Doe. The setName function updates the name state variable to John Doe.

As a result, after pressing the button, the component re-renders and displays the name "John Doe." After the button click, it becomes disabled with the help of the buttonClicked useState variable. Let's examine another example where you define a component named ToggleMessage. You could use this component to show or hide a message. Inside the component, use the useState hook to declare a state variable named isVisible and initialize it to true. This variable represents the visibility state of the message. Define a function toggleVisibility that toggles the value of isVisible when the user clicks a button.

It negates the current value of isVisible, thus toggling between true and false. The JSX code renders a div element containing an H2 heading, a button, and a paragraph. The button has an onClick event handler that calls the toggleVisibility function when clicked. The button text changes dynamically based on the value of isVisible. If isVisible is true, the button text displays "Hide message." Otherwise, it displays "Show message." The paragraph conditionally renders based on the value of isVisible.

If isVisible is true, the UI shows the paragraph "This is a hidden message." When the value is false, it remains hidden. In this video, you learned state management allows you to manage data that can change over time within a component. The useState hook enables function components to manage the component's state locally. You can use this syntax when using the useState hook. Call the useState function and pass in the initial state as a parameter. Assign the return value to a const array variable using a destructured array.

The array has two values: the stateName and the stateName prefixed with the word set. You should use the useState hook when you need to make a component dynamic and interactive.

---

### 4. [VIDEO TRANSCRIPT] Function Component Lifecycle Video • 6 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/Bf2Sd/function-component-lifecycle
- **Method:** `dom_transcript` | **Length:** 5362 chars

[MUSIC] Welcome to Function Component Lifecycle. After watching this video, you will be able define functional components in React, recognize the four different phases of a functional component in React. In React, functional components are the fundamental building blocks for creating user interfaces. Understanding the lifecycle of functional components is essential for managing the behavior and state of components throughout their existence. While functional components lack traditional lifecycle methods found in class components, developers can achieve similar functions using hooks such as useState, useEffect, and useReducer, among others. The lifecycle of a functional component in React undergoes four distinct phases, mounting phase, updating phase, unmounting phase, and error handling phase. The first phase is the mounting phase, during the mounting phase, React initializes the functional component, preparing it for rendering on the DOM.

The important steps involved in the mounting phase include initialization, state initialization, and side effects. The first step is initialization. In this step, React runs the function body of the functional component, setting up the initial structure and behavior of the component. After initialization, React performs state initialization, in this step, React utilizes the useState hook to declare and initialize state variables within the component. These state variables hold data that may change over time, triggering re-renders of the component when modified. Let us look at an example. In this example, the useState hook creates a state variable called count initialized to 0.

This state variable can be actively updated using the setCount function triggering re-renders of the component whenever its value changes. Finally, React performs side effects such as data fetching subscriptions or DOM manipulation using the useEffect hook with an empty dependency array. This step ensures that side effects execute only once after the initial render, optimizing performance and preventing unnecessary re-execution. Here is an example. In this example, the useEffect hook fetches data from https//api.example.com/data when the component mounts. It then sets the retrieved data using setData, which with an empty dependency array to ensure the effect runs only once after the initial render. We will now discuss the updating phase.

During the updating phase, React responds to changes in the component state or props by re-invoking the function body of the component. This phase triggers a re-evaluation of the JavaScript XML (JSX), allowing React to determine the new UI to render. Here is an example. In the updating phase of the functional component myComponent, the useState hook initializes the count state variable to 0 point. On clicking the button, the increment function invokes updating the count state by incrementing its previous value by one, using setCount. This step triggers a re-render of the component displaying the updated count value on the screen. The updating phase involves responding to user actions and state modifications, ensuring your UI stays in sync with the underlying data.

Let's now learn about the unmounting phase. During the unmounting phase, React executes cleanup operations when removing a component from the DOM. These operations involve the component itself, actively cleaning up event listeners, subscriptions, timers, or any other resources it created during its lifecycle. Here is an example. In the unmounting phase of the functional component, myComponent, the setInterval function within the useEffect actively sets up an interval timer. This timer executes a callback method every 1000 milliseconds, logging interval tick to the console. The component actively returns a cleanup function from the useEffect hook to ensure proper cleanup and prevent memory leaks.

This cleanup function uses clearInterval to clear the interval timer when the component unmounts, thereby freeing up the resources associated with it. This active cleanup mechanism ensures that the interval timer's resources are released when the component is removed from the DOM, thus preventing potential issues or memory leaks. But what happens if an error occurs during rendering or within a child component's lifecycle method in React? React will handle the error in such cases by routing it to the nearest error boundary. This error-handling mechanism is the final phase of the functional component's lifecycle. Error boundaries are special components in react that catch errors during the rendering phase or lifecycle methods of their child components. Instead of crashing the entire application, error boundaries display a fallback UI, preventing the error from propagating further up the component tree and ensuring the rest of the application remains functional despite the error in a specific component.

In this video, you learned that React's lifecycle phase includes mounting, updating, unmounting, and error handling. The mounting phase initializes the component, sets up the initial state, and performs side effects. In the updating phase, React re-invokes the function body and re-evaluates JSX. In the unmounting phase, React executes cleanup operations when removing a component from the DOM. React handles the error by routing it to the nearest error boundary. [MUSIC]

---

### 5. [VIDEO TRANSCRIPT] Testing React Components Video • 7 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/1g90e/testing-react-components
- **Method:** `dom_transcript` | **Length:** 6285 chars

Welcome to this video on testing React components. After watching this video, you will be able to Apply user-centric testing principles by demonstrating how to write tests that validate user-facing behavior rather than internal implementation details And handle asynchronous rendering in tests by using React Testing Library's asynchronous utilities to manage deferred updates and suspense states. Imagine a self-driving car. You don't pop up the hood to inspect the engine. You take it for a drive and see how it responds to real-world conditions. Similarly, modern React testing focuses on user experience, interactions, loading states, and asynchronous updates rather than internal mechanics. Let's explore React's new features.

React's new features Concurrent rendering Automatic batching Transitions And improved suspense Enhance user experience But change testing practices Tests should focus on user-facing behavior, simulating real interactions, and validating UI outcomes, not internal implementation or lifecycle methods. Modern tools like React Testing Library or RTL and Jest are recommended, while other libraries like Enzyme are deprecated. Now let's understand why testing changed in React. React's new concurrent renderer allows React pausing, resuming, or batching updates for better performance. This implies three key points. First, updates are not always synchronous. Next, the Document Object Model, or DOM, might not reflect changes immediately after a state update.

And finally, tests that assume synchronous rendering can fail or behave inconsistently. Therefore, modern testing in React focuses on waiting for UI updates rather than checking the DOM immediately after interactions. Next, let's move on to the goals of testing in React. There are four main objectives when testing React components. Starting with validating user behavior, not implementation details. Test how the component responds to inputs, clicks, or network responses. Next is handling asynchronous rendering safely.

React may batch or defer status updates, so tests should use asynchronous query methods like findBy or utilities like waitFor. Another goal of React is to simulate real-world usage by using libraries that mimic how users interact with the browser, such as @testing-library/user-event. React's final goal is to ensure components behave correctly under concurrency. Components like useTransition, suspense, or dataFetching should be tested for both loading and final states. Now let's go over the recommended testing libraries in React. Starting with RTL, the standard for testing React components. It emphasizes user experience over internal logic, automatically handles act calls, and works seamlessly with concurrent rendering.

RTL promotes readable tests and offers async queries like findBy and waitFor, plus role-based queries that mimic real-user interactions. Next, Jest is the most popular test runner and assertion library for React. It offers a complete testing environment with mocking, snapshots, and setup hooks, integrates seamlessly with React Testing Library, supports mock timers and network request mocking, and is actively maintained for full React compatibility. There is @testing-library/jest-dom that adds custom DOM matchers to Jest for better assertions. Some example matchers are toBeInTheDocument, toHaveTextContent, toBeVisible. It is actively used and maintained, fully compatible with React. Then there is @testing-library/user-event.

It provides realistic user interactions such as typing, clicking, and selecting text. It is strongly recommended for testing user behavior in React. Another recommended testing library is Mock Service Worker or MSW that mocks API calls at the network level, simulating real requests without manually mocking Fetch or Axios. It ensures components using suspense or async data work correctly and is the preferred tool for API mocking in React. The final recommendation tool is Vitest, offering hot reload and seamless integration with React Testing Library. It's recommended for Vite-based projects. You also need to know about deprecated testing tools such as Enzyme.

It relies on React's internal APIs that changed with concurrent rendering. No official adapter for React was released, and it fails to support the new root API. Let's dive into the testing best practices in React. Starting with the first best practice, always test from the user's perspective. Follow on visible output and behavior, not on internal state or function calls. Next, you need to use asynchronous utilities. Replace getBy with findBy when dealing with data fetching, transitions, or suspense.

Use waitFor to check for updates after asynchronous events. The third best practice is to avoid testing implementation details. Don't test private methods or state variables. Test how the component behaves after interactions. Next, you must simulate real user behavior. Use user-event for realistic interactions like typing, clicking, or tab navigation. Moving on to the next testing best practice, you should handle suspense and lazy loading.

Test both the fallback or loading state and the resolved UI after lazy components load. Next, you need to use MockServiceWorker or MSW for APIs. MSW gives more reliable API simulations than manually mocking fetch. Another best practice you need to note is to keep tests deterministic. Ensure tests do not depend on real network requests or timeouts. Finally, use E2E tools for full integration. For complex flows involving multiple components, use Cypress or Playwright to validate behavior in a real browser environment.

In this video, you learned that Modern testing emphasizes visible behavior over internal state or lifecycle methods. Modernized rendering is managed with utilities like findBy or waitFor, including support for suspense. Reliable tests are built using libraries such as React Testing Library, Jest, @testing-library/jest-dom, @testing-library/user_event, MSW, and Vitest. Enzyme is considered obsolete because it depends on outdated React internals and lacks concurrent rendering support. Deterministic tests replicate actual user interactions rather than implementation details. Deterministic and predictable tests are essential for stability and maintainability.

---

### 6. [READING] Lesson 1 Summary: Introduction to Function Components Reading • 3 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/supplement/GcApg/lesson-1-summary-introduction-to-function-components
- **Method:** `dom_reading_cml` | **Length:** 1260 chars

Congratulations! You have completed this lesson. At this point in the course, you know that:

- Props principles include reusability, unidirectional data flow, customization, and composition.
- You can use the "useState" hook with an event to control a child component.
- You use component composition to combine smaller components to create a complex UI.
- Principles of component composition include abstraction, reusability, hierarchy, props and children, and higher-order components.
- State management allows you to manage data that can change over time within a component.
- The useState hook enables function components to manage the component's state locally.
- You can use this syntax when using the useState hook: - Call the "useState" function and pass in the initial state as a parameter. - Assign the return value to a const array variable using a destructured array. - The array has two values: the state name and the state name prefixed with the keyword "set."
- The mounting phase initializes the component, sets up the initial state, and performs side effects.
- In the updating phase, React re-invokes the function body and re-evaluates JSX.
- In the unmounting phase, React executes cleanup operations when removing a component from the DOM.

---

### 7. [VIDEO TRANSCRIPT] Working with Arrays in React Components Video • 7 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/33QpM/working-with-arrays-in-react-components
- **Method:** `dom_transcript` | **Length:** 6084 chars

Welcome to Working with the Arrays in React Components. After watching this video, you will be able to define arrays and their importance in React components. Describe how to declare arrays in React. Describe how to traverse arrays in React components. Describe how to work with arrays in React. An array is a data structure in JavaScript used to store multiple values in a single variable. It is defined by enclosing a comma-separated list of elements within square brackets.

Arrays can contain elements of any data type, including numbers, strings, objects, or even other arrays. In React, arrays are commonly used to manage lists of data and are essential for building dynamic and interactive user interfaces. React components often render arrays of elements or data, and there are various ways to declare arrays in React and traverse their elements within components. You can declare an array using the array literal notation as shown. Arrays can be stored in component state using the useState hook as shown. Arrays can be constructed dynamically based on application logic or received data as shown. Traversing arrays in React components is a common task, especially when rendering dynamic content or managing lists of data.

By using methods like map, forEach, for...of loops, or index-based traversal, you can efficiently work with arrays in React components to create dynamic and interactive user interfaces. The map method is commonly used to iterate over each element of an array and return a new array of React elements as shown. The forEach method iterates over each element of an array and executes a callback function as shown. You can use the for...of loop to iterate over the elements of an array as shown. You can access elements of an array using their indexes as shown. You can render a list of items by mapping over an array and returning a JSX element for each item. Array declaration.

Inside the component function, an array named items is declared and initialized with four string elements: autumn, spring, summer, and winter. These represent the seasons. JSX rendering. The component returns JSX markup representing the structure of the component's output. It includes a div element containing an h1 heading, season names, and an unordered list (ul) element. Mapping array elements. Within the ul element, the map method is utilized to iterate over the items array.

For each element of the array, a "li" list item element is dynamically generated. The key attribute is assigned to the index parameter of the map function to help React efficiently identify each list item. In the output, the items in the array are displayed under the heading Season Names as autumn, spring, summer, and winter. You can add or remove items from an array using state and React's set state method as shown in the code as follows. State management. The component utilizes the useState hook from React to manage its state. Two state variables are declared.

Items. Holds an array of strings representing seasons, initially set to autumn, spring, summer, winter. Input value. Represents the value of the input field used for adding new items to the array, initially set to an empty string. Adding items. The addItem function is called when the Add button is clicked. It appends the current value of input value to the items array using the setItems function and then resets inputValue to an empty string.

Removing items. The removeItem function is triggered when the Remove button next to each list item is clicked. It creates a new array, newItems, by copying the items array and removes the item at the specified index using the splice method. The updated array is then set as the new state using setItems. Rendering JSX. The component returns JSX markup, representing the structure of the component's output. It includes an h1 heading, Seasons, an unordered list, ul, and a dynamic list of list items, li, generated using the map method.

Each list item displays a season from the items array and contains a Remove button. Clicking the button triggers the removeItem function for the corresponding index. Below the list, an input field allows users to add new items to the array. The inputValue state variable controls the value of the input field. Clicking the Add button appends the current value of the input field to the items array and clears the input field for the next entry. The output displays as shown with a Remove button against each array item and an Add button at the bottom. After entering data in the input field, the output will display as shown.

The output shows monsoon has been added in the array list. If you want to remove, then click on the Remove button against an item, and the item will be deleted. Suppose you have clicked on Autumn Remove button like shown in the image, then the array list will look like as shown. You can conditionally render components based on the content of an array. For example, the explanation for the code is as follows. State management. The component uses the useState hook from React to manage its state.

One state variable is declared. Items. Holds an array of strings representing front-end languages. Rendering JSX. The component returns JSX markup representing the structure of the component's output. It includes an h1 heading. Front-end languages.

It conditionally renders either an unordered list, ul, containing list items, li, representing front-end languages, using the map method, if items is not empty, or a paragraph p, stating, No Front-end language is available, if items is empty. The output will display as shown. In this lesson, you learned that arrays are basic data structures that are often used to store groups of items in a single variable. Some important array methods are map, which makes it easier to make new arrays by applying a function to each element, forEach, which runs a function on each array element without creating a new array. Also, push and splice methods can be used to add and remove elements. Arrays are a powerful data structure for quickly changing and traversing data.

---

### 8. [VIDEO TRANSCRIPT] Virtual DOM Manipulation in React Video • 7 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/M4DfS/virtual-dom-manipulation-in-react
- **Method:** `dom_transcript` | **Length:** 7045 chars

Welcome to a video on how Virtual DOM works in React. After watching this video, you will be able to define document object model, DOM and its components. Describe the working of a virtual DOM in React. List the advantages of virtual DOM in React. Compare normal and virtual DOMs. The document object model, DOM is an interface for web pages and documents used to represent an HTML structure as a tree-like structure. Each node represents a part of the document, such as elements, attributes, and text.

The DOM allows programs to access and manipulate web document's content, structure, and style dynamically. The components of a DOM are nodes, elements, attributes, and events. The DOM represents the document as a tree structure composed of nodes. There are different types of nodes, such as element, text, attribute, and so on. Elements are the building blocks of HTML documents. They represent the content of the document. Attributes provide additional information about elements.

They can specify properties, styles, or behavior. DOM events allow JavaScript code to respond to user interactions or other actions in the document. The virtual DOM is a concept used in frameworks like React to optimize the performance of web applications. It is an abstraction of the actual DOM implemented in memory and is kept in sync with the real DOM by React's reconciliation process. Let's discuss how the virtual DOM works. Upon the first rendering of a React component, a virtual model of the DOM is created. When changes are made to the state or props of a component, React creates a new virtual DOM representation.

React uses a diffing algorithm to compare the new virtual DOM with the previous one and identify the smallest changes required to update the real DOM. React uses batching to optimize changes by grouping and applying them to the real DOM efficiently as a patch, which helps minimize wasteful re-renders and DOM operations. Virtual DOM is important in React. It offers speed enhancement, simple development, cross platform compatibility, state management, and debugging and testing. The virtual DOM boosts web application speed by reducing the frequency of DOM changes. Developers can concentrate on developing declarative code without being concerned about the intricacies of DOM manipulation. Due to its cross platform compatibility, React virtual DOM abstraction enables efficient component rendering on various platforms, such as web browsers and mobile devices.

React state management in conjunction with the virtual DOM, facilitates effective updates and re-renders in response to alterations in the application state. Virtual DOM simplifies debugging and testing React apps by allowing developers to examine the virtual version of the DOM while developing. The advantages of virtual DOM in React are efficient updates, component reusability, easy updating to declarative syntax, and improved server side rendering. React's virtual DOM ensures that only the necessary changes are made to the actual DOM leading to better performance and faster rendering. Virtual DOM allows developers to create reusable components that can be composed and updated efficiently. React's declarative syntax allows developers to describe the intended UI state and React updates the virtual DOM and renders the components accordingly. Virtual DOM enables server side rendering in React, improving the initial page load performance and web application search engine optimization, SEO.

The normal and virtual DOM differ in their loading process. In the normal DOM, when a web page loads in a browser, the browser analyzes the HTML content and creates the DOM tree from the HTML code. The process includes analyzing the HTML markup, generating the DOM nodes, and displaying the content on the screen. Rendering complex web pages with huge DOM trees can be expensive. In contrast to the regular DOM, the virtual DOM is an abstraction that resides in memory and is not connected to the browser's rendering engine, which means it will not update the changes directly in the real DOM. Upon loading an application, react creates a virtual DOM tree representation in memory called the virtual DOM. This virtual DOM is constructed based on the React components initial state and properties.

When updates are made to the DOM, such as changing the content of an element or modifying its attributes, the browser directly manipulates the corresponding DOM nodes. In contrast, in the virtual DOM, React compares the current virtual DOM with a new form that shows the updated state when changes are made to a React app. Then React figures out the smallest changes that need to be made to the DOM to represent the new state. These changes are made all at once and then applied to the real DOM. So, there are as few transitions and updates as possible. The reconciliation process in React makes sure that only the necessary changes are made to the DOM. This makes it faster and more efficient.

Each update triggers a reflow and repaint of the affected parts of the document, which can impact performance, especially in large applications. Let's create a simple React example with two components, a parent component, app.jsx, a first child component, and a second child component. The first child component renders a list of items, and the parent component updates only one item without re-rendering the entire list. But it will also make sure that the second child component will not re-render again. In this example, the app component maintains the state of a list of items. The first child component has a list of array items with one button to update the first element of that item. The second child component only shows information related to that component.

The output of the above code is as shown. If you inspect the console logs, you'll notice the following behavior. For the first time loading, all the components will render. When you select to update the item, only the first child component will be re-rendered. Neither the app component nor the second child component will change. React's virtual DOM compares the updated app with the previous virtual DOM and determines that only the state of the first child component has changed. Therefore, it only updates the relevant part of the DOM, the child component, without re-rendering the entire list.

This example demonstrates how React's virtual DOM updates only the necessary parts of the DOM, improving the application's performance, especially in scenarios where only specific components or elements need to be updated. In this video, you learned that the DOM allows programs to access and manipulate web document's content, structure, and style dynamically. Virtual DOM is an abstraction of the actual DOM implemented in memory and kept in sync with the real DOM by React's reconciliation process. React's virtual DOM updates only the necessary parts of the DOM improving the performance of the application. Especially in scenarios where only specific components or elements need to be updated.

---

### 9. [READING] Style in React Reading • 5 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/supplement/pkHUj/style-in-react
- **Method:** `dom_reading_cml` | **Length:** 2531 chars

Styling in React can be done in various ways, including inline styles, CSS modules, styled components, and more. Let's explore each approach briefly.

### Objective

After completing this reading, you will be able to explore various styles in React

### Inline styles

- The <div> element has inline styles applied directly using the style attribute.
- The styles are specified as a JavaScript object where the keys are CSS property names, and the values are the corresponding CSS property values
- Similarly, the <p> element inside <div> has inline styles applied using the style attribute.
- The above component will render a <div> with a light blue background, padding, and border-radius. Inside the <div>, there's a <p> element with white text color and a font size of 18 pixels, all styled using inline styles.

### CSS modules

toggleMessage.module.css

- Import styles from ./toggleMessage.module.css;: This imports the CSS module toggleMessage.module.css as an object named styles. In CSS, a module typically refers to a file (usually with a.module.css extension) that contains a set of CSS rules scoped to a particular component or module in your application. These CSS rules are locally scoped to prevent unintended style conflicts between components.
- const [isVisible, setIsVisible] = useState(true);: This initializes a state variable isVisible using the useState hook. It represents whether the message paragraph should be visible or not, and it defaults to true.
- const toggleVisibility = () => {...};: This is a function that toggles the visibility of the message paragraph by updating the state variable isVisible when the button is clicked.
- <p className={isVisible ? styles.message : ''}>This is a hidden message.</p>: This paragraph element displays the message. Its class name is conditionally set based on the value of isVisible. If isVisible is true, it applies the message class from the CSS module, otherwise, it applies an empty string, effectively removing any additional styles.

### Styled components:

CSS can also be applied in React components using JavaScript objects, similar to the messageStyle object in the provided React component.

For example, in the following code there is one object with name  messageStyle { color: 'green', fontSize: '18px' } represents CSS properties for color and font size. It also has a conditional styling. For example, { display: isVisible ? 'block' : 'none' } that dynamically sets the display property based on the value of isVisible.

### Author

Richa Arora

---

### 10. [READING] Lesson 2 Summary: Array in React and DOM Manipulation Reading • 3 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/supplement/2uZYm/lesson-2-summary-array-in-react-and-dom-manipulation
- **Method:** `dom_reading_cml` | **Length:** 848 chars

Congratulations! You have completed this lesson. At this point in the course, you know that:

- You use the array data structures often to store groups of items in a single variable.
- Two important array methods include: - map(), which makes it easier to make new arrays by applying a function to each element - forEach(), which runs a function on each array element without creating a new array
- The DOM allows access to and dynamically manipulates web documents’ content, structure, and style.
- React's virtual DOM abstracts the actual DOM implemented in memory and keeps the virtual DOM in sync with the real DOM by React’s reconciliation process.
- React’s virtual DOM updates only the necessary parts of the DOM, improving the application's performance, especially in scenarios where only specific components or elements need to be updated.

---

### 11. [READING] CheatSheet: Understanding Function Components with Array and DOM Manipulation
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/supplement/IDBNe/cheatsheet-understanding-function-components-with-array-and-dom-manipulation
- **Method:** `dom_reading_cml` | **Length:** 5652 chars

| Function Component with Array and DOM | Description | Code Example |
| --- | --- | --- |
| Function Component with function keyword | Function component starts with function keyword along with name of the component and includes html tags within return. It also exports component name by default | import React from 'react' function Extra() { return ( <> <p>This is paragraph</p> </> ) } export default Extra |
| Function Component with arrow function | Function component starts with variable type along with name of the component and includes html tags within return. It also exports component name by default | import React from 'react' const Extra = () => { return ( <div>Extra</div> ) } export default Extra |
| Props in function component | Props can be sent from parent component as attribute along with child component | import React from 'react' import ChildComponent from './ChildComponent' function ParentComponent () { let title='Project Manager'; return ( <> <ChildComponent title={title}/> </> ) } export default ParentComponent |
| Access Props within child function component | Props can be accessed easily within the child function component using props.variable_name | import React from 'react' const ChildComponent = (props) => { return ( <> <p>The title is {props.title}</p> </> ) } export default ChildComponent |
| Event handling in class component | Events such as click event can be performed by calling function which is declared before return of function component | import React from 'react' const Extra = (props) => { function show(){ console.log('Show function'); } return ( <> <p>The title is {props.title}</p> <button onClick={()=>show()}>Click Here</button> </> ) } export default Extra |
| State management in function component | State management can be done easily with useState() hook | import React, { useState } from 'react' const StateManagement = () => { const[name,setName]=useState('John'); return ( <> <h1>State Management using useState</h1> <p>The name is {name}</p> </> ) } export default StateManagement |
| Array Declaration | Array can be declared in square brackets | const names = ['Alice', 'Bob', 'Charlie']; |
| Stateful Array | Array can be declared using useState | const [todos, setTodos] = useState(['Learn React', 'Build Project']); |
| Dynamically Constructed Arrays | Arrays can be constructed dynamically based on application logic or received data | const numbers = []; for (let i = 0; i < 10; i++) { numbers.push(i); } |
| Array map() method | The map() method is commonly used to iterate over each element of an array and return a new array of React elements | const items = ['Apple', 'Banana', 'Orange']; const itemList = items.map((item, index) => <li key={index}>{item}</li>); return <ul>{itemList}</ul>; |
| for...of Loop | You can use the for...of loop to iterate over the elements of an array: | const items = ['Apple', 'Banana', 'Orange']; for (const item of items) { console.log(item); } |
| Rendering a List of Items | You can render a list of items by mapping over an array and returning a JSX element for each item | import React from 'react'; function ArrayComponent() { const items = ['Autumn', 'Spring', 'Summer','Winter']; return ( <div> <h1> Seasons Names</h1> <ul> {items.map((item, index) => ( <li key={index}>{item}</li> ))} </ul> </div> ); } export default ArrayComponent; |
| Adding and removing items in array | You can add or remove items from an array using state and React's setState method | import React, { useState } from 'react'; function MyComponent() { const [items, setItems] = useState([‘Autumn’, ‘Spring’, ‘Winter’,’Summer’]); const [inputValue, setInputValue] = useState(''); const addItem = () => { setItems([...items, inputValue]); setInputValue(''); }; const removeItem = (index) => { const newItems = [...items]; newItems.splice(index, 1); setItems(newItems); }; return ( <div> <h1>Fruits</h1> <ul> {items.map((item, index) => ( <li key={index}> {item} <button onClick={() => removeItem(index)}>Remove</button> </li> ))} </ul> <input type="text" value={inputValue} onChange={(e) => setInputValue(e.target.value)} /> <button onClick={addItem}>Add</button> </div> ); } |
| Conditional rendering using ternary operator | You can conditionally render components based on the content of an array | import React, { useState } from 'react'; function ArrayComponent() { const [items, setItems] = useState(['React JS','Vue JS','Angular JS','Vanilla JS']); return ( <div> <h1>Front End Languages</h1> {items.length > 0 ? ( <ul> {items.map((item, index) => ( <li key={index}>{item}</li> ))} </ul> ) : ( <p>No Front End language is available</p> )} </div> ); } export default ArrayComponent; |
| inline style in react | Inline style can be applied within the tag as an attribute within double curly braces | import React from 'react'; function MyComponent() { return ( <div style={{ backgroundColor: 'lightblue', padding: '20px', borderRadius: '5px' }}> <p style={{ color: 'white', fontSize: '18px' }}>This is a paragraph with inline styles.</p> </div> ); } export default MyComponent; |
| Style using object | Style can be applied as an object like inline style | import React, { useState } from 'react'; function ToggleMessage() { const [isVisible, setIsVisible] = useState(true); const toggleVisibility = () => { setIsVisible(!isVisible); }; const messageStyle = { display: isVisible ? 'block' : 'none', color: 'green', fontSize: '18px', marginTop: '10px' }; return ( <div> <h2>Toggle Message</h2> <button onClick={toggleVisibility}> {isVisible ? 'Hide Message' : 'Show Message'} </button> <p style={messageStyle}>This is a hidden message.</p> </div> ); } |

---

### 12. [READING] Glossary: Understanding Function Components with Array and DOM Manipulation
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/supplement/c51jK/glossary-understanding-function-components-with-array-and-dom-manipulation
- **Method:** `dom_reading_cml` | **Length:** 4662 chars

Welcome! This alphabetized glossary contains many of the terms you'll find within this course.

This comprehensive glossary also includes additional industry-recognized terms not used in course videos. These terms are important for you to recognize when working in the industry, participating in user groups, and participating in other certificate programs.

| Term | Definition |
| --- | --- |
| Abstraction principle | A principle that provides a way to make reusable components that encapsulate UI features. |
|  |  |
| Array | A data structure in JavaScript used to store multiple values in a single variable. |
|  |  |
| Array destructuring | A feature that allows you to extract values from an array and assign them to individual variables. |
|  |  |
| Array literal | A syntax in JavaScript for creating arrays. It allows you to define an array by enclosing a comma-separated list of elements within square brackets. |
|  |  |
| Attributes | Provide additional information about elements. They can specify properties, styles, or behavior. |
|  |  |
| Component composition | A combination of multiple smaller components to create complex functionality. |
|  |  |
| Document object model (DOM) | An interface for web pages and documents used to represent an HTML structure as a tree-like structure. |
|  |  |
| Elements | Are the building blocks of HTML documents. |
|  |  |
| forEach() | A method that iterates over each element of an array and executes a callback function. |
|  |  |
| Hierarchy principle | A principle that allows you to arrange components in a hierarchy, with parent and child components. |
|  |  |
| Higher-order component | A function that allows you to add components' features, such as state management or logic, without modifying its implementation. |
|  |  |
| Hook | A function that enables you to reuse code logic across components without changing component hierarchy or introducing unnecessary nesting. |
|  |  |
| Initialization | A step in which React runs the function body of the functional component, setting up the initial structure and behavior of the component. |
|  |  |
| map() | A method commonly used to iterate over each element of an array and return a new array of React elements. |
|  |  |
| Mounting phase | A functional component lifecycle phase in which React initializes the functional component, preparing it for rendering on the DOM. |
|  |  |
| Props Default | Is default value for props using defaultProps. This ensures that if a prop is not provided, the component will still render with the default value, enhancing predictability and robustness in component behavior. |
|  |  |
| Properties (props) | A fundamental concept in React for passing data from parent to child components. They enable communication and customization between different parts of a React application. |
|  |  |
| Rendering Array | Involves dynamically generating and displaying elements based on the contents of the array. This is commonly done using JavaScript's map() function to iterate over the array and generate React elements for each item. |
|  |  |
| Reuse principle | A principle to reuse chunks of code, making it easier to organize and maintain. |
|  |  |
| Side effects | A step that includes data fetching, subscriptions, or DOM manipulation using the 'useEffect' hook with an empty dependency array. |
|  |  |
| State | The condition of a component at a specific time and it holds information that influences the object's behavior and renders it based on that information. |
|  |  |
| State management | Involves handling and updating the data over time, allowing components to dynamically change their appearance and behavior in response to user actions or other events. |
|  |  |
| State initialization | A step in which React utilizes the 'useState' hook to declare and initialize state variables within the component. |
|  |  |
| Updating phase | A functional component lifecycle phase in which React responds to changes in the component's state or props by re-invoking the function body of the component. |
|  |  |
| Unmounting phase | A functional component lifecycle phase in which React executes cleanup operations when removing a component from the DOM. |
|  |  |
| useState hook | A built-in React Hook that allows functional components to manage state. It provides a way to declare state variables and update them within a functional component. When the state changes, React automatically re-renders the component to reflect the updated state. |
|  |  |
| Virtual DOM | An abstraction of the actual DOM implemented in memory and is kept in sync with the real DOM by React's reconciliation process. |

---
