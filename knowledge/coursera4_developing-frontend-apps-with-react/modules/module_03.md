# Module 3: In-depth Understanding of Advanced React Functionality

### 1. [VIDEO TRANSCRIPT] Hooks Video • 4 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/YKJze/hooks
- **Method:** `dom_transcript` | **Length:** 3968 chars

Welcome to Hooks. After watching this video, you will be able to explain the purpose of using Hooks, list the advantages of Hooks, summarize best practices for Hook development, and contrast standard and custom Hooks. Introduced in React version 16.8, Hooks alleviate many challenges posed by writing class components. Hooks provide a way to write functional components with the same capabilities as class components. Namely, you can access a component state using Hooks with function components. The component preserves its state when it updates and re-renders. So now, function components provide the same functionality as class components, with less complexity in the code.

As the name suggests, they enable you to hook into React state and lifecycle features from function components. You can even write customized hooks. You can write a custom hook for multiple components instead of duplicating code from one component to another. Advantages of using Hooks include easier to read code. Your code chunks become more manageable in size. Hooks help to optimize your code, enabling you to write code producing complex behaviors in the UI. They simplify your code.

Hooks help you handle events and subsequent logic without classes. Hooks also provide a performance boost to your components. Now let's discuss some best practices when using Hooks. You can only use Hooks exclusively with function components. You must call a hook at the top level of a component tree. In other words, you cannot call hooks within child components. You cannot call a hook from a normal JavaScript function.

You cannot call hooks inside loops, conditional statements, or nested functions. Regarding versioning, Hooks require the Node.js version 6 JavaScript platform. In addition, they use the Node Package Manager, NPM, version 5.2 or higher. You should use the npm create vite@latest my-app --template react tool to set up your React app using Vite. It simplifies configuration and the need for multiple build tools and automatically optimizes your app. Let's explore some of the most commonly used hooks. The UseState hook allows you to access the state of the component in your function component.

The UseEffect hook manages side effects such as document changes and HTTP requests. You will use it if you need to fetch data from a database. The UseContext hook manages context changes and provides access to a context. The UseReducer hook manages redux state changes. Like a light form of Redux, this hook provides a dispatch function and a state while taking a reducer and an initial state. You will learn more about the Redux library in another lesson. Custom React hooks let you add unique functionality to your React applications.

You name custom with use as a prefix. For example, you could create custom hooks named UseLocalStorage or UseAuthentication. A custom hook is a new composition of one or multiple hooks. Since you can treat hooks as functions, they have the same features. You can reuse and combine them as needed. In this code example, this code imports the UseState hook to access the component's local state. This hook returns and assigns values with a destructed array.

The current count state is the first array element and the second variable sets the count, allowing you to make updates. The initial count is passed as a parameter in the UseState hook function. After that, you call this function from an event handler to utilize it. In this video, you learned that hooks provide function components with the same capabilities as class components. Hooks enable you to write simpler, more readable, and a lesser amount of code, providing more complex behaviors and improving performance. You must call hooks at the top of the tree and cannot call them from regular or nested functions or inside loops or conditions. Standard hooks include UseState, UseEffect, UseContext, and UseReducer.

And finally, you can add unique functionality using custom hooks.

---

### 2. [VIDEO TRANSCRIPT] Side-effects Management and Custom Hook Video • 6 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/qzVLp/side-effects-management-and-custom-hook
- **Method:** `dom_transcript` | **Length:** 5908 chars

Welcome to a video on Site Effects Management and Custom Hook. After watching this video, you will be able to Define the role of UseEffect and SiteEffects in React. Describe how UseEffect and SiteEffects works in React. Describe the various dependencies in UseEffect. Describe a custom hook in React. UseEffect is a React hook that allows you to perform SiteEffects and functional components. A SiteEffect refers to any operation that you need to execute as soon as the page loads, without calling those operations slash functionalities separately, such as fetching data from an API, subscribing to events, manipulating the DOM, or setting timers.

SiteEffects are actions that occur asynchronously, and affect the application's state or the UI. Here's a simple example to understand UseEffect and the SiteEffects in React. Suppose we have a component that fetches a list of food items from an API and displays them. In this code example, the components are as follows. State Management with UseState. The component utilizes the UseState hook to manage the state within a functional component. Specifically, it declares a state variable named foods using UseState, initializing it with an empty array.

This variable will later hold the data fetched from the API. Performing SiteEffects with UseEffect. The UseEffect hook is employed to execute SiteEffects in functional components. In this component, UseEffect is utilized to fetch data from an external API when the component mounts. Data Fetching. Inside the UseEffect hook, a fetch request is made to the specified API endpoint, as shown. The fetch function returns a promise that resolves to the response from the server.

Upon receiving the response, response.json parses the response body as JSON. The parsed JSON data is then available in the next then block, where it is logged to the console for debugging purposes and subsequently passed to setFoods to update the food state variable with the fetched data. If an error occurs during the fetch operation, it is caught in the catch block and an error message is logged to the console. Rendering the Fetched Data. In the JSX returned by the component, a list, ul, of food items is rendered. The map method is used to iterate over the foods array and generate a list item, li, for each food item. For each food item, details such as name, description, price, category, ingredients, and an image are displayed.

The image is rendered using the image tag with the URL obtained from the image underscore URL property of each food item. Component Export. Finally, the SideEffect component is exported as the default export, making it available for use in other parts of the application. In React's useEffect hook, dependencies refer to variables or values which are used to determine when useEffect should run. Dependencies are specified as an array argument to the useEffect function. The following are some dependencies. When you provide an empty dependency array, the effect runs only once when the component will load for the first time.

It does not depend on any specific variable or state changes. This behavior is used to execute tasks only once at the time of loading. For example, in the code, the page will only load once at the loading of this page. When you provide values in the dependency array, the effect runs whenever any of these values change. For example, the count value as shown in the code. If any of the dependencies have changed since the last render, React will rerun the effect. In the code, the effect runs only when the count state changes, ensuring that the useEffect hook executes whenever count is updated.

Therefore, the count variable is included in the dependency array. If you omit the dependency array entirely, the effect will run after every render, including the initial render and subsequent updates. This means that the effect will execute both after the initial render and after every rerender of the component, regardless of whether you change any values. This behavior with no dependency will cause the effect to run after every render. You can use a custom hook in React to create reusable logic. Custom hooks allow you to abstract complex logic that you can easily reuse across different components in your application. Let us understand this with an example.

You have two components, ToggleButton and UseToggle. Let's go through the ToggleButton code. The ToggleButton component imports and utilizes a custom hook named UseToggle, which uses the logic for toggling between true and false states. Within the ToggleButton component, the UseToggle hook is used to manage the state of a button. The hook returns two values, IsToggled, representing the current state, either true or false, and Toggle, a function that toggles the state between true and false when invoked. In the JSX, a button is rendered with a text content of on when the state is true and off when the state is false. Upon clicking the button, the toggle function is triggered, updating the state accordingly.

This setup provides a simple and reusable way to create toggle functionality within React components. The reusable code of the UseToggle custom hook is as shown. It manages the true and false state of the ToggleButton. The output before clicking the ToggleButton will be as shown. After clicking the ToggleButton, the output will be as shown. This toggle will be performed as long as the user clicks on the button. In this video, you learned that UseEffect is a React hook that allows you to perform side effects in functional components.

Side effects are actions that occur asynchronously, affecting the application state or UI. In React's UseEffect hook, dependencies refer to variables or values which are used to determine when UseEffect should run. Custom hooks allow you to abstract complex logic that you can easily reuse across different components in your application.

---

### 3. [VIDEO TRANSCRIPT] Connecting React to External Services Video • 5 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/fargV/connecting-react-to-external-services
- **Method:** `dom_transcript` | **Length:** 4022 chars

Welcome to a video on connecting react to external services. After watching this video, you will be able to define external services, describe how third-party services retrieve data using the fetch API method and axios library. External services are third-party platforms, applications, or systems that your application connects to over a network. These services are typically hosted outside your app's environment and provide additional features, tools, or data that your application may need. They allow your app to interact with external resources or services through APIs, application programming interfaces, enabling data exchange, feature integration, or service execution. Application programming interfaces, or APIs, let your application talk to and exchange data with outside services. Third-party services offer them.

APIs enable you to acquire data, execute operations, or add extra features to your application. Third-party services provide data you can retrieve using multiple API methods, such as fetch API method and axios library. Let us understand fetching data using API with the help of an example. In the code, a constant variable, apiUrl, is used to store the URL of the outside API from JSON placeholder, API, which is used to create fake JSON data for testing and development. Then, the fetch method sends a GET request to the given URL, apiUrl. This starts the process of getting info from the outside API. You connect the THEN method to the fetch call. This method takes a callback function as an argument and runs it when the fetch action is successful. It also takes an argument for the response object. You use the callback function to call the answer object's JSON method. This method takes the answer body as JSON and gives you a promise to work with the JSON data. You add another THEN method to deal with the JSON data that was read in the last step. This method takes a callback function as an argument. The callback function runs when the JSON parsing is complete and the parsed JSON data is given as an argument. In the callback function, you write the info to the console. You add a CATCH method to the chain to deal with errors during the fetch process. As an argument, this method takes a callback function that runs if there is an error. You log the error to the console inside the callback code so that you can use the error messages to help with debugging. Overall, this code shows how to use the fetch function to make a simple GET request to an external API, handle the return data, and properly handle any errors that may happen during the fetch operation. The output of the API fetch method code is as shown.

Axios is a popular JavaScript library for HTTP requests from web browsers. Let us see an example of axios that shows how it works and differs from the fetch API method. To use axios, you first need to install using npm install axios. Then, you need to import it using import axios from axios. Next, use the axios.get method to make a GET request to the specified URL, apiUrl. Axios automatically handles the creation and execution of the HTTP request. In this code, axios offers additional features such as automatic JSON parsing. Therefore, there is no need to call response.json separately as you did with the fetch API method. You chain a .then method to handle the response from the API. The response object is passed to the callback function when the request is successful. You access the response data using response.data and log it to the console. You add a catch method to the chain to deal with errors during the fetch process. This code generates the same output, but less is executed.

In this video, you learned that external services are third-party platforms, applications, or systems that your application connects to over a network. APIs enable you to acquire data, execute operations, or add extra features to your application. Third-party services provide data you can retrieve using multiple API methods such as fetch API method and axios library.

---

### 4. [VIDEO TRANSCRIPT] Implementing Forms Video • 5 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/BWDRN/implementing-forms
- **Method:** `dom_transcript` | **Length:** 4743 chars

Welcome to Implementing Forms. After watching this video, you'll be able to explain the purpose of forms. Compare and contrast controlled and uncontrolled form components. Summarize the benefits of the React hook library for form development. Forms allow users to interact with data on a web page. For example, you would use forms for user registration, surveys, or when a user places an order. Areas in which users interact with the data are called fields.

There are many types of fields, such as text boxes, drop-down menus, radio buttons, and checkboxes. When taking input from a user through a form, you also need to handle the submission logic and validate the data. In React, you handle these capabilities with components. You generally capture the input on the client side and temporarily store it in the component state. You do not submit the information directly from the form to a server. HTML provides some form capabilities such as input, textarea, and select. The browser manages the state of these elements.

In React, you use the component state to store input and make updates using the component's setState method. In addition to providing the data fields the users interact with, your form must also provide submission logic that tells the application when to accept the user's input. For example, you would not want to accept a user's password until they click a Submit button. This provides some degree of assurance the user input the password they intended. Regarding validation, when users create passwords, applications often require the user to type the password twice, as well as have rules for the password, such as a minimum number of characters. Generally, form validation requires the following tasks: getting the input, managing and updating the form state, validating input values, displaying appropriate error messages. React form components can be controlled or uncontrolled.

Let's discuss the difference at a high level and then examine each one more closely. With uncontrolled components, you use react to place the value on the page and the browser keeps track of the rest. With controlled components, the React state manages the form data. This means that you must explicitly write the code to create the state and tell it how to update when the data changes. Although uncontrolled components use less code and are easier to develop, ultimately, they are less robust. As the name suggests, you have little control over the former and more over the latter. When you write uncontrolled components to handle user input, the browser handles the form elements.

Similar to working with HTML form elements, the values in an uncontrolled component are stored in the DOM's input node. Inputs get updated automatically. When writing an uncontrolled component, you write a ref function to get the input values from the DOM. You do not need to write event handlers when the state changes. If you decide to use controlled components, you explicitly handle all state changes, such as responding to a key press, a mouse click, or a tap. Rather than the DOM handling the input, you tell the component where to store the data and return any values to display as a result. You write functions to handle data getting passed into the component with onChange events, such as tapping a specific location of the screen.

Often, you will use the setState method to save the updated input. You also write the event handlers to update the state of the variables. This simple controlled component handles a registration form. The component implements the useState hook to track the state of the email address. To ensure that the email address is updated when the form is submitted, you must add an input element with value and onChange attributes to it. When the user taps the Submit button, the component writes the email address to the console. You can use the React hook form library to help you with state management and validation for React applications containing forms.

This reduces the amount of code developers need to write when creating forms. It also helps improve performance by eliminating unnecessary form component re-rendering. You can install React hook form using the install react hook form command. In this video, you learned that forms provide a way for users to interact with data in a web application. Forms usually require input fields, submission logic, and validation rules to handle user interactions. The browser keeps track of data and state of elements with the DOM in uncontrolled components. Controlled components require you to explicitly manage the UI input data with the component's state.

The React hook form library optimizes performance by reducing the number of times a component renders.

---

### 5. [READING] Lesson 1 Summary: Hooks and Form Management in React Reading • 2 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/supplement/fj9Ya/lesson-1-summary-hooks-and-form-management-in-react
- **Method:** `dom_reading_cml` | **Length:** 984 chars

Congratulations! You have completed this lesson. At this point in the course, you know that:

- The useEffect hook in React enables the execution of side effects within functional components. In React's useEffect hook, dependencies refer to variables or values that determine when useEffect should run.
- Custom hooks allow you to abstract complex logic and easily reuse it across different components in your application.
- External services are any program, platform, or infrastructure your application uses to connect to and work with other applications over a network.
- APIs enable you to acquire data, execute operations, or add extra features to your application.
- Within React, components typically manage form data.
- React inputs are classified into two categories: controlled and uncontrolled. In uncontrolled input, React puts the value on the page, and the browser keeps track of the rest. Controlled inputs, require you to write the code to manage the value explicitly.

---

### 6. [VIDEO TRANSCRIPT] Introduction to Redux Video • 3 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/WCbbz/introduction-to-redux
- **Method:** `dom_transcript` | **Length:** 3452 chars

Welcome to Introduction to Redux. After watching this video, you'll be able to compare and contrast component versus application states, explain purpose of the Redux library, describe when to use Redux, summarize the benefits of using Redux. In order to understand the usefulness of the Redux library, you should first understand the differences between component and application states. An application state as opposed to a component state holds information about the entire application. You can access this state from anywhere in your application, not just a specific component. For example, consider an e-commerce application that provides users with a cart feature, you should let your users access the cart feature anywhere in the application so they can view or edit its contents or check out at any time, regardless of any particular state of a specific component. The Redux library helps you handle the application state.

Instead of individual components handling their own state, Redux can maintain the state of the application state and pass information from the application to component whenever it gets called. In general, the larger the application, the more useful Redux potentially becomes. As the number of components in your application grows, it becomes increasingly difficult to manage all of those component states. A large number of components indicates that you should turn to Redux for help rather than frequently passing props through your component tree. Also, you will likely have components that use the same data but are randomly located on the DOM tree, so passing data from one component to varying locations on the tree becomes cumbersome and hard to track. Because Redux handles states globally, you can make updates to the state from anywhere in the application. This prevents the need to create new objects with each state change.

Note that you can use the Redux library with frameworks other than React, like Angular, Vue, and just standard JavaScript. However, most developers who use React also use Redux. Redux handles multiple state changes in a place called the Redux Store. A store refers to a data structure that stores and manages data. Developers sometimes refer to the Redux store as the single source of truth. You will find using Redux beneficial for multiple reasons. Using state at the application level can reduce code complexity and improve readability.

You don't need to reason about a component's particular status to understand the application's behavior at a given point in time. Redux makes it easier to predict the application state at any particular point in time because you don't need to pass the data between components as much. Redux makes code maintenance easier by eliminating the need to trace components up and down the tree to determine their state data. Using Redux can help optimize performance because it reduces the number of page renders. It reloads only the necessary updated parts of the page rather than the entire page. In this video, you learned that an application state holds data about the entire application and you can access this data from any particular component. You can use the Redux library to manage your application's state.

You will find Redux useful when you need to pass data from one part of your component tree to another. Benefits of Redux include reducing coding complexity, improving code readability, better performance, and easier code maintenance.

---

### 7. [VIDEO TRANSCRIPT] Essential Concepts of Redux Video • 4 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/ydEVo/essential-concepts-of-redux
- **Method:** `dom_transcript` | **Length:** 3827 chars

[MUSIC] Welcome to essential concepts of Redux. After watching this video, you will be able discuss Redux concepts such as action, store, and reducer. Describe the principles behind Redux architecture. Explain the terms dispatching and action creators. Relate the concepts action, store, and reducer to a user interface example. Redux offers a centralized state management system for your application. When you use Redux, you do not need to manage component states.

Redux manages the states at the application level, not the individual components. Using this approach, you should treat the component properties as immutable. You create new state objects rather than changing existing ones. Redux uses actions, stores, and reducers when updating component properties. Lets briefly discuss each and then discuss them in more detail later. The store contains all the current states of the application. You call an action object to indicate the need for a state update, but the action does not specify how to change that state.

Instead of specifying the how in the action, you write a reducer function to how to update the state in the store. Before going into more detail, consider an e-commerce application cart. From the user's point of view, they expect the total number of items in the cart to increase by the number of items they add to the cart after selecting add to cart. Let's see what happens behind the scenes regarding actions, the store, and reducers to make this work correctly. When the user selects add to cart, it starts an action creator function. Lets say you name the function addItem. The addItem function is an action creator.

It creates and returns an action object. Your component sends that action object to the store using a dispatch function. This entire process is called dispatching an action. The store contains all application states, including the state of the cart. Part of the cart's data includes its current number of items. The store itself uses a data structure called a state tree to store and manage the application states. The tree is a JavaScript object with methods for managing its properties.

The action object describes the action that needs to be performed. It contains properties including type and payload. The store uses the actions type property to determine which reducer should process the action. The payload property stores other data needed to update the state. In our example of adding items to a cart, the payload would include the cart's increased value. The store then calls the reducer, which tells it how to change the state. When the store receives the action, it calls the appropriate reducer and passes both the action object and the state object to the reducer function to calculate the new state.

Note that the reducer is a pure function, meaning it always returns the same output when given the same inputs, it has no side effects or mutating functions. Using reducers may seem like an extra step in the Redux architecture. However, this architecture enables a predictable state container by ensuring explicit state changes. It makes reading the code easier when you need to track state changes by separating the action description and the specifics of how the state changes. In turn, this makes debugging easier and helps simplify code maintenance. In this video, you learned that the action object describes the action that needs to be performed. The store maintains all of the application's current states.

A reducer tells the store how to change the state. The dispatching action process uses an action creator function, which returns the action object and sends the object to the store using a dispatch function. The Redux architecture makes states predictable because changes are explicit through actions, reducers, and the application store. [MUSIC]

---

### 8. [VIDEO TRANSCRIPT] Async with Redux Video • 5 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/bFgvI/async-with-redux
- **Method:** `dom_transcript` | **Length:** 5209 chars

Welcome to Async with Redux. After watching this video, you will be able to Explain the differences between synchronous and asynchronous operations Explain challenges with asynchronous operations in Redux Provide examples of complications posed by asynchronous operations Describe how you can use Thunk and Saga to handle async Compare and contrast Thunk and Saga's pros and cons Code that operates in a synchronous or sync fashion Implies that, given two operations, one operation must complete execution Before the second one begins If your code has two operations and the first operation starts It blocks the second operation until the first operation finishes Asynchronous or async operations run in parallel This means that a second operation can begin execution While the first is still being processed The situation dictates which behavior you need You will generally prefer asynchronous behavior When you don't want an operation to prevent the user From continuing to use the application So operations such as network requests, memory-intensive calculations And loading large files should usually be performed asynchronously These operations can run in the background While the user completes other tasks Synchronous behavior can also pose problems Situations often require processing events one after another For example, if the user wants to add two items to a cart They first need to enter the number of items they want Then click the Add to Cart button to update the cart If the Add to Cart button event occurs before updating the number of items An incorrect number may be added In this case, you prefer synchronous behavior JavaScript behaves asynchronously However, state management in Redux requires synchronous behavior Recall the sequence of a Redux state change It begins with a call to an ActionCreator function Which returns an Action object Next, the Action object is dispatched to the store Then the store calls the appropriate reducer Based on the Action object's type property Consequently, the reducer updates the state object Dispatching actions sometimes requires asynchronous operations For example, say your user needs the application to fetch data from the server If the application behaved in a synchronous manner It would block the user from any other interactions with the application Until the server returns that data Causing a frustrating user experience In this case, you want to dispatch operations asynchronously To manage the application's states and maintain responsiveness Though required, actions and reducers will not suffice to handle this asynchronous behavior Middleware allows you to interact with asynchronous data To perform state changes, you use actions provided by the store If necessary, the middleware intercepts the actions and delays them to support asynchronous behavior Once the asynchronous process is complete The rest of the Redux flow continues as usual Where the reducer receives the action type to compute the new state The final action dispatch restores the synchronous data flow Let's discuss the two most popular middlewares used with Redux to support asynchronous behavior Thunk and Saga Recall that action creators return an action object With Thunk, the action creators also return functions These functions allow you to interact with the Redux store These functions can perform async operations Such as API calls, as well as synchronous ones from within functions The store then dispatches actions based on the results Thunk middleware is suitable for simple applications and relatively easy to learn However, concurrency issues within Thunk require careful consideration Nor does Thunk scale well if your application grows Another middleware option for handling async operations is Redux Saga It uses special functions introduced in ES6 called generators These generator functions, called Sagas, allow you to encapsulate logic for handling asynchronous operations Sagas can multitask with the Redux store dispatch process by pausing and resuming execution as needed Sagas include several features to make testing and debugging easy They are pure functions that enable time travel and complex flow logging Sagas also scales well as your application grows In turn, the robust nature of Saga middleware makes it more complicated to learn An in-depth understanding of generators is required to use them well In this video, you learned that Synchronous operations block the next operation until the previous one finishes Asynchronous operations can run in parallel JavaScript behaves asynchronously, but Redux architecture requires synchronous behavior Thunk action creators return functions that allow you to perform sync and async operations Thunk middleware is suitable for simple applications and relatively easy to learn Thunk does not scale well and requires planning to handle concurrency issues Saga uses generator functions, which allow you to multitask in conjunction with the Redux store dispatch process by pausing and resuming execution as needed Saga includes numerous features that make testing and debugging easy The robust nature of Saga makes it more complicated to learn, requiring an in-depth understanding of generators

---

### 9. [VIDEO TRANSCRIPT] Binding Redux and Flow Video • 6 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/FePvP/binding-redux-and-flow
- **Method:** `dom_transcript` | **Length:** 5031 chars

Welcome to Binding Redux and Flow. After watching this video, you will be able to: Explain concept of state change. Describe data flow in Redux. And, list the advantages of one-way data flow in Redux. In a React application, state stores the properties of a component. When the state of a component changes, React responds by triggering the re-rendering of the document object model or DOM. As the application expands, it becomes difficult to manage the state in your application.

The change in the state may involve the transfer of data between components and a long chain of props that can result in a complicated application code. The solution to this problem is offered by Redux. It is an open-source JavaScript library that can manage the state of your application. It is commonly used with ReactJS but is not limited to it, and can also be used with other JavaScript libraries such as Angular. A conventional React-Redux application comprises a single store along with a single root Reducer. As the application grows more complex, the root Reducer splits into smaller Reducers that operate on the different parts of the state tree. An alternate solution can be setting a global variable that can be accessed by different components.

However, React will not react to any changes made in the global variable. Redux provides a central store that reduces the complexity of the code and makes the state updating process easier. The Redux elements that are involved in updating of the component properties include: Central Store: The store holds the entire application list in the form of the ‘state tree’. Actions: These are information packages sent by the component with a type (description) to the reducer. Actions are simple objects which conventionally have two properties: type and payload. The type property is usually a string that identifies the action, and the payload is an optional property that contains some data that is required to perform a task. So, the main function of actions is to send data from the application to the Redux store.

Reducer: This is a simple function that receives the old state and action as input and returns an updated state. Since the state is immutable, a reducer always returns a new state, which is an updated version of the previous state. Subscription: This is triggered in the components whenever the state is updated in the store. The data flow in a React-Redux application is unidirectional. It only goes in one direction. The flow of data in a React-Redux application begins at the component level when the user interacts with the application UI. This interaction leads to the action creators dispatching an action.

So when an action is dispatched, it is received by the root reducer of the application and is passed on to all the reducers. Thus, it becomes the reducer’s task to determine if it needs to update the state based on the dispatched action. This is checked by using a simple switch statement to filter out the required actions. Each smaller reducer in the application accepts the dispatched action, and if the type of the dispatched action matches, it returns a newly updated state. It is essential to note here that the state never actually changes in Redux. Instead, the reducer always generates a new state which is a copy of the old state but with some modifications. The store then informs the component about the new state, which in turn retrieves the updated state and re-renders the component.

Earlier developers used two-way binding to change the state data such that the UI reflected the change. Robust frameworks like Angular and Ember used this type of binding. However, two-way binding was affecting the browser performance adversely with the expansion of applications. In addition, it became difficult to keep track of the data flow. Large companies had a tough time implementing trivial applications like their chat feature. In the one-way data flow paradigm, building presentational components and wrapping them in containers or store (as in Redux applications), solves the problem. Now, the advantage of one-way data flow in Redux is that building large, front-end-heavy web applications becomes much more manageable.

It is easier to manage the state when actions performed on the UI are separated from the changing and updating of the state that happens due to the action. You can use some of the same containers, actions, and reducers in React Native to quickly create apps for iOS and Android. The presentational components do change a bit when you use iOS or Android view components instead of HTML. In this video, you learned that: When the state of a component changes, React responds by triggering the re-rendering of the DOM. The Redux elements that are involved in updating of the component properties are: Central Store, Actions, Reducer, and Subscription. The data flow in a React-Redux application is unidirectional. And, it's easier to manage the state when actions performed on the UI are separated from the changing of the state.

---

### 10. [VIDEO TRANSCRIPT] Introduction to Redux Toolkit Video • 7 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/SMqZo/introduction-to-redux-toolkit
- **Method:** `dom_transcript` | **Length:** 6146 chars

[MUSIC] Welcome to a video about the Redux toolkit. After watching this video, you will be able define Redux Toolkit in the context of React, describe the Redux Toolkit utilities used to streamline Redux tasks, describe the Redux Toolkit architecture, describe the relationship between a store and a slice. In the context of React, Redux Toolkit (RTK) is an official package the Redux team provides to simplify Redux development and make it more efficient. It includes utilities that help streamline common Redux tasks, reduce boilerplate code, and simplify development. Redux Toolkit includes utilities to streamline Redux tasks. It provides a configureStore function that combines several pieces of Redux setup logic into a single function call. The function includes setting up the Redux store with commonly used middleware such as Redux Thunk for handling asynchronous actions and enabling the Redux Devtools Extension for debugging.

Redux Toolkit introduces the createSlice function, which allows developers to define slice reducers that automatically handle immutable updates to the state. The function makes it easier to write reducer logic without having to worry about mutating the state directly. Redux Toolkit significantly reduces the boilerplate code needed to set up Redux in an application. This reduction leads to cleaner, more concise code and faster development time. Using Redux Toolkit can make your Redux code base cleaner, more organized, and easier to maintain, especially in larger applications where managing state can be complex. To get started with the Redux Toolkit in a React application, you can install it through npm or yarn. Also, ensure that React Redux is installed on your application.

The Redux Toolkit contains at least one slice file and one store file. A slice in the Redux Toolkit represents a piece of your application state and the logic to update it. Slices are typically defined using the createSlice function provided by Redux Toolkit. It consists of a reducer, action creators, and an initial state. A reducer is a function that receives the current state and an action and returns a new state based on that action. Action creators are functions that create actions to be dispatched to the store. The initial state is the initial value of the state slice.

The Redux store is a single JavaScript object that holds the complete state tree of your application. It is the source of truth for your data. In the Redux Toolkit, the store is created using the configureStore function, which takes in an object with reducer functions as its argument. The store allows access to the state through the getState function, allows state updates through dispatch(action), and registers listeners through subscribe(listener). The relationship between a slice and the store can be summarized as follows. Slices define individual parts of your application state and the logic to update them. The store is where all these slices are combined to form the complete state tree of your application.

Each slice reducer is added to the Redux store during its creation using the configureStore function. The store combines all the slice reducers into a single reducer using combineReducers function. When actions are dispatched, the store delegates them to the appropriate slice reducers based on their corresponding slice. Let us understand the relationship between slices and stores using an example. Suppose you have an e-commerce application that depicts the increase in the product quantity in your cart, the total bill amount, and the number of super coins you will earn on a purchase that you can use in your next payment. In this application, you will have the following components, App.jsx is the parent component, ProductQuantity.jsx will increment the quantity of a product item, CartValue.jsx will calculate the total amount, CounterSlice.jsx will contain the reducer and any associated action creators within a single file, Store.jsx will store the Redux state, Main.jsx is the entry point. ProductQuantity.jsx displays a product's quantity and allows users to increase or decrease it.

It imports use dispatch and use selector hooks from React Redux to interact with the Redux store. useSelector is used to extract the counter state from the Redux store. The component renders buttons to increment or decrease the quantity. When these buttons are clicked, the corresponding increment or decrement action from the CounterSlice is dispatched to the Redux store using dispatch. CartValue.jsx component determines the total bill amount and displays it based on the product quantity saved in the Redux store. To get the counter information from the Redux store, it uses useSelector. The final amount is calculated using the number of items and a set price per unit. CounterSlice.jsx file defines a Redux slice named counter.

It initializes the counter state to zero and defines two reducers, increment and decrement. When the increment or decrement actions are dispatched, they update the counter state accordingly. Store.jsx file configures the Redux store using configureStore from the Redux toolkit. It imports the counterReducer from CounterSlice and sets it as the reducer for the CounterSlice. The configureStore is then exported and used in the application. The main.jsx component is the entry point of the application. It wraps the app component with the provider component from React Redux passing the Redux store as a prop.

In this video, you learned that in the context of React, Redux Toolkit, or RTK, is an official package the Redux team provides to simplify Redux development and make it more efficient. Redux Toolkit provides a configureStore function that combines several pieces of Redux setup logic into a single function call. Redux Toolkit introduces the createSlice function, which allows developers to define "slice reducers" that automatically handle immutable updates to the state. A slice in the Redux Toolkit represents a piece of your application state and the logic to update it. The Redux store is a single JavaScript object that holds the complete state tree of your application.

---

### 11. [READING] Hooks versus Redux Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/supplement/tHKn2/hooks-versus-redux
- **Method:** `dom_reading_cml` | **Length:** 5876 chars

React hooks and Redux are powerful tools for managing state in React applications, each offering unique strengths and suitable use cases. Let's learn about both the tools and their specific utilization in React applications.

### Objectives

After completing this reading, you will be able to:

- Describe the key features, benefits, and limitations of React Hooks
- Describe the key features, benefits, and limitations of Redux
- Compare Hooks and Redux use cases

### React Hooks

#### Overview

React hooks are a feature introduced in React 16.8 and are used in functional components to utilize state and other React features without writing a class. Hooks provide a way to reuse stateful logic across components.

#### Key Features

- useState: This lets functional components set up and care for their own state variables, allowing them to store data that can change over time.
- useEffect: This lets functional components do side effects like getting data or changing the DOM after every view, which is how lifecycles work.
- useContext: This property lets functional components use context values passed down from parent components. This property makes it easier for data to be shared across the component tree.
- Custom hooks: Developers can put stateful logic that can be used repeatedly into custom hooks. This hook makes code reuse easier and separates complex behavior into components.

#### Benefits

- Easy to use: Hooks are easy to use in React components by putting stateful code inside functional components.
- Code reusability: Hooks enable developers to create reusable logic that can be shared across components, improving code organization and maintainability.
- Reduced boilerplate: Hooks eliminate the need for class components and reduce boilerplate code associated with state management.

#### Limitations

- Learning curve: Developers familiar with class components may need time to adapt to the functional paradigm and the nuances of hooks.
- Complex state management: While useState and useContext are suitable for simple state management, more complex applications may require additional patterns or libraries for state management.

### Redux

#### Overview

Redux is a container for states that must be kept in JavaScript apps. It's mainly used with React, but you can use it with any other view library or framework. It provides a centralized store for managing application state and enables predictable state updates through actions and reducers.

#### Key Concepts

- Store: This holds the whole state tree of an app and is the only source of truth.
- Actions: These are just plain JavaScript objects that let you change the state.
- Reducers: They are used to instruct the app on how to change its state when you perform an action.

#### Benefits

- Predictable state management: Redux needs data to move only in one direction that cannot be changed. This movement makes it easier to understand and plan for state changes.
- Centralized state: Redux keeps all apps' state in one place, which makes it easier for all its parts to see and change data.
- Debugging and time travel: Redux DevTools have powerful debugging tools, such as time-travel debugging that lets you see how states change over time.
- Community and ecosystem: Redux has a large, active community, and its ecosystem comprises many middleware, services, and development tools.

#### Limitations

- Boilerplate: Redux often requires writing more boilerplate code than local component state management or other state management solutions.
- Learning curve: The concepts of Redux, especially actions, reducers, and middleware, can be challenging for beginners or developers unfamiliar with functional programming paradigms.
- Overkill for small applications: For smaller applications with simple state management needs, Redux may introduce unnecessary complexity.

### Comparison

#### Use Cases

- There are hooks that can be used to manage the state of a single component, share code between components, and control the state of a single component.
- When more than one part of an app needs to share complex app state, or when the app has a lot of events and complex data flow, Redux is a great tool to use.

#### Learning Curve

- Hooks: Relatively easier to learn, especially for developers already familiar with functional components and React's lifecycle methods.
- Redux: Has a steeper learning curve due to its concepts like actions, reducers, and middleware, particularly for developers new to state management patterns.

#### Scalability

- Hooks: Well-suited for small to medium-sized applications and simpler state management needs. It may become cumbersome for large-scale applications with extensive state management requirements.
- Redux: Scales well for large applications with complex state management needs, providing a structured approach to manage application state and maintainability.

#### Developer Experience

- Hooks: Offer a more streamlined and intuitive development experience for managing state within components, with less boilerplate and a more functional programming style.
- Redux: Offers a strong and reliable state management solution, which is especially helpful for big teams or applications that need to handle complex data flow.

### Conclusion

React hooks and Redux are powerful tools for managing state in React applications, each with strengths and suitable use cases. Hooks offer simplicity, code reusability, and a more functional approach to state management within components. On the other hand, Redux provides a centralized and predictable state management solution, ideal for larger applications with complex data flow requirements. The choice between Hooks and Redux depends on the application's specific needs, complexity, and scale, as well as the preferences and familiarity of the development team.

### Author

Richa Arora

---

### 12. [READING] Lesson 2 Summary: Application State Management with Redux Reading • 3 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/supplement/PKlF7/lesson-2-summary-application-state-management-with-redux
- **Method:** `dom_reading_cml` | **Length:** 928 chars

Congratulations! You have completed this lesson. At this point in the course, you know that:

- The Redux elements involved in updating the component properties include actions, the Store, and reducers.
- Redux makes use of the entire application's states as opposed to using component states.
- Within Redux, the existing application states reside within an object known as the store.
- You use action objects to communicate to the store what data you need to update and use reducers to tell the application how to make the update.
- Reducers are pure functions that receive the current state and an action object and return a new state with the actions performed.
- Synchronous operations run in a first-to-last sequence, beginning the next operation only after the previous one has finished.
- Asynchronous operations can occur in parallel. They don't require the previous operation to be completed before beginning the next.

---

### 13. [READING] Cheat Sheet: In-depth Understanding of Advanced React Functionality
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/supplement/jajIr/cheat-sheet-in-depth-understanding-of-advanced-react-functionality
- **Method:** `dom_reading_cml` | **Length:** 3754 chars

| Hooks and form management | Description | Code example |
| --- | --- | --- |
| useState() | useState() hook can manage states of the React function component where you can declare any data type, for example, boolean, object, array, string. | import React, { useState, useEffect } from 'react'; function SideEffect() { const [empId, setEmpId] = useState(100); return ( <div> <p>{empId}</p> </div> ); } export default SideEffect; |
| useEffect() | useEffect is a React hook that allows you to perform side effects in functional components. A side effect refers to any operation that you need to execute as soon as the page loads without calling those operations/functionalities separately, such as fetching data from an API. | import React, { useState, useEffect } from 'react'; function SideEffect() { const [foods, setFoods] = useState([]); useEffect(() => { fetch('https://api.npoint.io/d542b9ad99f501ab3dbf') .then(response => response.json()) .then(data => { console.log(data); setFoods(data); }) .catch(error => console.error('Error fetching users:', error)); },[]); // Empty dependency array means this effect runs only once when the component mounts return ( <div> <h1>Food List</h1> <ul> {foods.map((food)=>{ return (<> <li><h1>{food.name}</h1></li> <p>food.description</p> <p>food.price</p> <p>food.category</p> <p>food.ingredients</p> <img src={food.image_url} alt="" height='100px' width='100px' /> </> ) })} </ul> </div> ); } export default SideEffect; |
| Custom hook | You can use custom hooks in any other component. In this code snippet, there is one function component known as UseToggle, which serves as a custom hook, and another function component ToggleButton, which will use this custom hook. | //ToggleButton import { useState } from 'react'; import UseToggle from './UseToggle'; function ToggleButton() { const [isToggled, toggle] = UseToggle(false); return ( <div> <h1>Toggle Button</h1> <button onClick={toggle}> {isToggled ? 'ON' : 'OFF'} </button> </div> ); } export default ToggleButton; //UseToggle.jsx import { useState } from "react"; function UseToggle(initialValue = false) { const [value, setValue] = useState(initialValue); const toggle = () => { setValue(!value); }; return [value, toggle]; } export default UseToggle |
| fetch api method | Fetch method can fetch data using API. | const apiUrl = 'https://jsonplaceholder.typicode.com/posts'; fetch(apiUrl) .then(response => response.json()) .then(data => { console.log(data); }) .catch(error => { console.error('There was a problem with the fetch operation:', error); }); |
| axios api method | Axios method can fetch data using API. | import axios from 'axios'; const apiUrl = 'https://jsonplaceholder.typicode.com/posts'; axios.get(apiUrl) .then(response => { console.log(response.data); }) .catch(error => { console.error('There was a problem with the fetch operation:', error); }); |
| onChange | The onChange event attribute is often used in HTML and React to track when the value of an input field changes, like a text input. The onChange event occurs when a user writes something into an input field. This attribute lets you record and handle the changes. | import React, { useState } from 'react'; function FormData() { const [empName, setEmpName] = useState(''); const handleChange = event => { setEmpName(event.target.value); }; const handleSubmit = event => { event.preventDefault(); console.log('Form submitted:', empName); }; return ( <div> <h2>My Form</h2> <form onSubmit={handleSubmit}> <label> Input: <input type="text" value={empName} onChange={handleChange} /> </label> <button type="submit">Submit</button> </form> </div> ); } export default FormData; |
| Redux toolkit | Redux toolkit can be installed using npm | npm install @reduxjs/toolkit. |

---

### 14. [READING] Glossary: In-depth Understanding of Advanced React Functionality
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/supplement/6ZRNL/glossary-in-depth-understanding-of-advanced-react-functionality
- **Method:** `dom_reading_cml` | **Length:** 4799 chars

Welcome! This alphabetized glossary contains many of the terms you'll find within this course.

This comprehensive glossary also includes additional industry-recognized terms not used in course videos. These terms are important for you to recognize when working in the industry, participating in user groups, and participating in other certificate programs.

| Term | Definition |
| --- | --- |
| Action creator | An action creator is a function that returns an action object containing a type property (identifying the action) and optionally a payload property (data associated with the action). |
| Actions in Redux | Actions are payloads of information that send data from the application to the Redux store, describing "what happened" in the application. |
| Application state | A state that holds information about the entire application. |
| Asynchronous or async code | A code that runs in parallel. This means an operation can occur while another is still being processed. |
| Axios | A popular JavaScript library for HTTP requests from web browsers. |
| combineReducers () | combineReducers() is a Redux function used to combine multiple reducers into a single root reducer for the Redux store. |
|  |  |
| createSlice () | A function in RTK that allows developers to define 'slice reducers' that automatically handle immutable updates to the state. |
|  |  |
| configureStore () | A function in RTK that combines several pieces of Redux setup logic into a single function call. |
| Controlled component | A component where the React state manages the form data. You must explicitly write the code to create the state and tell it how to update when the data changes. |
| Custom hook | A new composition of one or multiple hooks. |
| fetch | A modern JavaScript API for making asynchronous HTTP requests in the browser environment. It allows you to fetch resources, such as JSON data, from servers over the network. It is commonly used for data fetching in React applications to interact with backend servers or APIs. |
| Fields | Areas in a form in which users interact with the data. |
| Forms | Allow users to interact with data on a web page. |
| getState () | A function in the store that allows access to the state. |
| Hook | A function that enables you to reuse code logic across components without changing component hierarchy or introducing unnecessary nesting. |
| Payload property | An optional property contains some data required to perform a task. |
| Reducers in Redux | Actions that return the new state. |
|  |  |
| Redux | A library that can maintain the application state and pass information about the application to a component whenever it gets called. |
| Redux store | A data structure that stores and manages data. |
| Redux Saga | A middleware that exposes a set of helper functions, or sagas, to create declarative effects that are plain JavaScript objects, and your sagas can yield them. |
| Redux Thunk | Redux Thunk is a middleware for Redux that allows action creators to return functions instead of plain objects, enabling asynchronous logic (e.g., AJAX requests) within Redux actions. |
| Redux Toolkit (RTK) | An official package the Redux team provides to simplify Redux development and make it more efficient. |
| Side effects | Refers to any operation you must execute as soon as the page loads without calling those operations/functionalities separately, such as fetching data from an API, subscribing to events, manipulating the DOM, or setting timers. |
|  |  |
| Slice | Slice in Redux Toolkit (RTK) represents a portion of the Redux state and includes the logic for updating that slice's state using reducers and action creators. |
| Store in RTK | All the slices are combined to form the complete state tree of your application. |
| Subscription | Subscriptions is a mechanism in Redux that allows components to subscribe to state changes in the Redux store, ensuring they receive updates and can react accordingly. |
| Synchronous or sync code | A code that runs in an orderly sequence from top to bottom. This means that each operation must wait for the previous one to complete before executing. |
| Type property | A string that identifies the action. |
| Uncontrolled component | A component where you use React to place the value on the page, and the browser keeps track of the rest. |
| useContext hook | A hook that manages context changes and provides access to a context. |
| useEffect hook | A hook that manages side effects such as document changes and HTTP requests. |
| useReducer hook | useReducer is a React hook that facilitates complex state logic in functional components, commonly used for managing Redux state updates. |
| useState hook | A hook that allows you to add state management functionalities to function components. |

---
