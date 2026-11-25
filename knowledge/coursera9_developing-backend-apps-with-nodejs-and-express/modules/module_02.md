# Module 2: Asynchronous I/O with callback programming

### 1. [VIDEO TRANSCRIPT] Asynchronous I/O with Callback Programming Video • 6 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/jRaHS/asynchronous-i-o-with-callback-programming
- **Method:** `dom_transcript` | **Length:** 5436 chars

[Music] Welcome to Asynchronous I/O with Callback Programming. After watching this video, you should be able to: Explain the concept of asynchronous callback functions and handle inbound hypertext transfer protocol (HTTP) method calls for a server resource. Network operations run in an asynchronous manner. For example, the response from a web service call might not return immediately. When an application blocks (or waits) for a network operation to complete, that application wastes processing time on the server. Node.js makes all network operations in a non-blocking manner. Every network operation returns immediately.

To handle the result from a network call, write a callback function that Node.js calls when the network operation completes. This sequence diagram for a scenario shows the interaction between the application, the Node.js framework, the web service call to the remote server, and the call back to the callback function. In the first step, the application makes a call to HTTP.request. This function makes a call to the remote web server and requests the web service. Before the Node.js framework receives the HTTP response message from the remote web server, it immediately returns a result for the HTTP.request function call. This result simply indicates that the request message was sent successfully. It does not say anything about the response message.

When the Node.js framework receives an HTTP response message from the remote server, it calls the callback function that you defined during the HTTP.request function call. This function handles the HTTP response message. In a slightly more complex scenario, your application calls a custom Node.js module, which then makes an HTTP.request function call. The Node.js framework then calls the remote server's web service by sending an HTTP request message. In the same manner as in the first scenario, the Node.js framework returns a value to the HTTP function call in the Node.js module. This response simply states that the HTTP request was successfully sent out. The Node.js module then returns from the exported function call.

At this point, the application continues processing on to the next step, while the response message has not yet been sent. When the remote server returns an HTTP response message, the Node.js framework calls the callback function defined by the custom Node.js module. The purpose of the callback function is to handle two events: request.on('data') and request.on('end'). In this case, the callback function simply prints the HTTP response message body to the console log. This code example shows you how to make an HTTP request call from a function inside a Node.js module. The first parameter in the HTTP request function is an options variable. The options variable included at least two variables: the hostname of the remote server, and a uniform resource locator (URL) resource path that you want to act upon.

In the example here, you are making a call to the US National Weather Service to retrieve the weather observation from San Francisco International Airport (KSFO). The second parameter of the HTTP request function is a callback function. In this case, it is an anonymous function that receives one parameter: the response object. When the Node.js module calls this anonymous function, events occur while it is receiving parts of the HTTP response object. In this example, there are two specific events: a 'data' event and an 'end' event. For these two events, you define more callback functions to handle each event type. In the actual coding, you may need to use HTTPS instead of HTTP.

The result object is passed into the callback function of a parseString module. The HTTP.request function takes in a URL and a set of options. If both are passed, the two are merged, with options taking precedence. You can define the host, ports, authentication, protocol, and other headers in the options object. The HTTP.request method also accepts an optional callback function that is invoked immediately once a response is received. When HTTP.request calls the callback function, it passes a response object in the first parameter of the callback function. This callback function has the response object as the first parameter.

The Node.js framework emits several events during the course of the request function. You can listen to these events by using the object.on() method and passing in the event name as the first parameter. If the request is successful, a 'data' event is emitted on the response object every time data comes in, followed by an 'end' event when the response finishes. If the request fails, there is an 'error' event followed by the 'close' event. Let's see how to handle such errors. The request method returns an object of type HTTP.ClientRequest. This object represents the request in progress.

You can append to the request body, make changes to the headers, and listen for error events as shown here. The code simply outputs the error message if there is an error. To end the request, call clientRequest.end(). In this video, you learned that: When an application blocks for a network operation to complete, that application wastes processing time on the server. Node.js makes all network operations in a non-blocking manner. and when the Node.js framework receives an HTTP response message from the remote server, it calls the callback function that handles the HTTP response message.

---

### 2. [VIDEO TRANSCRIPT] Creating Callback Functions Video • 6 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/LJzPY/creating-callback-functions
- **Method:** `dom_transcript` | **Length:** 6126 chars

Welcome to Creating Callback Functions. After watching this video, you should be able to create a callback function to Intercept Hypertext Transfer Protocol, or HTTP method calls. As an asynchronous framework, Node.js makes extensive use of callback functions to return the result to the calling function. Node.js modules in the Software Development Kit, or SDK, pass an error object as the first parameter in a callback function. Here, the function is defined with an error as the first parameter. With this convention, the callback function checks if the first parameter holds an error object. If error is defined, the callback function handles the error and cleans up any open network or database connections.

If the error is not defined, then the callback function examines the result from the call. If the error is defined, print the error message. Otherwise, the weather.current function call completed successfully. Print the result from the function call. The codes are in the main app, which has a weather object, the Node.js module, that calls the weather's current function. The location is an input parameter, in this example, an airport. To print temp underscore f in the browser, we can use response dot end, the current weather reading is dollar sign temp underscore f degrees.

Now we'll look at an example of passing an error object to the callback function. Recall how callback functions check the first parameter to see if an error condition occurred. Instead of printing the result in the console, you call the resultcallback callback function with the error object. You pass back the error object to the resultcallback callback function of the main application. If no error occurred, you can call the resultcallback function with null as the first parameter. The codes are in the custom Node.js module. The callback handler printed the contents of the HTTP response message body to the console.

What if you wanted it to return the response message to the original calling application? If you use a return function, Node.js might call the callback function after the HTTP dot request call completes. The application calls the exported function. The module that implements the function calls HTTP dot request so that the Node.js framework can make a web service call on its behalf. When that request is sent successfully, the framework returns control to the Node.js module. Then the Node.js module returns control to the application. When the remote server sends back an HTTP response message to the Node.js framework, the framework calls the callback handler that was defined by the Node.js module.

However, there is no connection between the callback function and the main application. So how do you link the callback function to the main application? The pattern is that when one Node.js application calls a module in a non-blocking manner, the application provides a callback function to process the result. If the main application calls HTTP dot request, it must provide a callback handler to process the HTTP response message. If the main application calls a function that calls HTTP dot request, there are two callback functions. The custom module has a callback function that handles the HTTP response message from HTTP dot request. And the main application has a callback function that processes the result captured in the first callback function.

Let us see how this solution works. We will create a callback function to capture the result from the HTTP dot request function call. The application makes a call to the Node.js module. The Node.js module makes an HTTP dot request function call in order to send an HTTP request message to a remote server. Before the remote service returns an HTTP response message, the HTTP dot request function call returns control to the Node.js module as the request message was successfully sent. Then the Node.js module replies with a value to the main application. At a future point, the remote server sends back an HTTP response message.

The Node.js framework calls the callback function defined by the Node.js module. This callback function calls another callback function defined by the main application. Having one callback function invoke another callback function is the only way to pass a message from the Node.js module to the main application when the Node.js module receives a response message. Here, when the main application calls weather dot current, it passes an anonymous callback function to process the result from the call. In this case, the anonymous function takes in one input parameter, temp underscore f. The purpose of this callback function is to take the weather reading in degrees Fahrenheit and print the results in the console log. The resultcallback callback function in the function of the custom Node.js module links to the anonymous callback function, function temp underscore f, of the weather object's current function in the main application.

Now you can see a Node.js module that returns a result to the main application with a callback function. Here, a function is defined for the property named current. This property will be exported as part of the module. The anonymous function takes a parameter named resultcallback from the main application. This is how you pass a reference to the main application's callback function to the Node.js module's callback function. The resultcallback parameter stores the anonymous callback function from the main application. Look at the bottom of the current property.

A response dot on end event handler handles the transmission of the HTTP response message. When the remote server finishes sending back the response message, the code makes a call to resultcallback and passes it to the current weather reading in degrees Fahrenheit. This is how you pass a value from one callback handler to another. In this video, you learned that Node.js makes extensive use of callback functions to return the results to the calling function. Node.js modules in the SDK pass an error object as the first parameter in a callback function. And there is one callback function at each level.

---

### 3. [VIDEO TRANSCRIPT] Expert Viewpoints: Using Anonymous Callback Functions in Node.js Video • 5 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/Yw4Lp/expert-viewpoints-using-anonymous-callback-functions-in-node-js
- **Method:** `dom_transcript` | **Length:** 4231 chars

Welcome to Expert Viewpoints: Using anonymous callback function in Node.js. In this video, we will hear from several application development professionals discussing when they found it useful to know how to use anonymous callback functions in Node.js and how they were key to the solutions they developed. Anything in Node.js that requires you to make a request outside your application, which most likely you will, understanding how callbacks work is very important. So when we say anonymous callbacks, callbacks don't have to be anonymous. In fact, a lot of times I will write named functions and pass that as arguments into my functions that need the callback. I'll give you an example. So let's say you're building a website that displays temperature on the main website, right.

So in order to get the temperature, you're most likely calling another website, most likely another web service, that accepts some JSON as input and gives you back another JSON as output. Now, when the end user comes on your website, they're scrolling up and down. If you block that and make the request to the weather API, then your user will not be able to even scroll up and down, right. So in the browser, it's doing one thing at a time. Node.js is single-threaded, and so everything gets blocked if you're making that request. And if you think about it, if the weather API is not giving your response, for whatever reason, maybe your credentials are incorrect, maybe the server is down, then your users are left waiting. In that case, the callback functions come in handy.

So what you do is you make a request to the weather API, and then you go about your business. And when a response comes back, you can handle that response and show the information to the user. So, understanding callbacks is (a)key to mastering JavaScript. Functions are a first class object in JavaScript and can therefore be passed as parameters to other functions. A callback function specifically follows the callback pattern and involves passing a function as a parameter to another function, and the callback function is invoked once the enclosing function has executed. And so a callback function is a closure in that the callback function has access to the containing function's scope variables. Callback functions can either be anonymous or named, and here we're talking about anonymous callback functions.

Anonymous functions are sometimes more readable and are a good solution when the callback function is not intended to be reused. In other cases, a utility module like Async.js can help cope with asynchronous JavaScript. Anonymous callback functions in JavaScript are great. They are very useful to keep your code clean and define a function just on the fly. So I've used them extensively when dealing with messaging. The idea is that I'm sending messages and receiving messages, and I want to process those messages. I don't always necessarily want to define a full function for how to process it every single time.

I just want to say hey, when I get this message, I'm going to do something really simple. So, oftentimes, it's very easy and very useful to just create a very simple anonymous callback function which gets a message, processes it, does something, and then I never have to worry about it again. If you're planning on using Node.js for web development, the concept of callback functions is one of the first things you'll need to grasp. When you're defining routes in your web server, you'll be relying on a library to provide you with request and response objects. These will be provided as arguments to your callback function which will then read the request and modify the response to make sure the client gets the desired result. While it's possible to use named functions for your callback functions here, anonymous functions are often preferred because each route's logic is unique and not duplicated elsewhere. So using anonymous functions keeps your code clean and readable.

Anonymous callback functions allow you to write a block of scoped code that you can use again at a later time. Anonymous functions combined with the arrow syntax allow us to write clear and concise pipelines in JavaScript to manipulate data inside arrays.

---

### 4. [VIDEO TRANSCRIPT] Issues with Callbacks Video • 5 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/3dHzJ/issues-with-callbacks
- **Method:** `dom_transcript` | **Length:** 4504 chars

Welcome to Issues with Callbacks. After watching this video, you will be able to: Explain why nested callbacks occur, explain the difficulties with nested callbacks, describe inversion of control, explain the difficulties with inversion of control, identify several ways to mitigate nested callbacks and inversion of control. Recall that a callback is a function that is passed as an argument to another function that executes the callback based on the result. They are basically functions that are executed only after a result is produced. Callbacks help us develop asynchronous JavaScript code. Callbacks make sure that a function won’t run before a prerequisite task is completed. In this example, message is an example of a callback function.

When called, it writes, “This message is shown after 3 seconds” to the console. There is a built-in method in JavaScript called “setTimeout”, which waits a specified time in milliseconds before performing an action. In this example, the message gets passed into the setTimeout function. So, after waiting 3 seconds, setTimeout writes “message” to the console. Usually, these asynchronous callbacks, or async for short, are used for accessing values from databases, downloading images, reading files, and so on. Often, these resources are provided by other services outside of the application that needs them. Callback functions wait for a response, and when the response is sent, then they execute.

For example, say you are making a cake. These are the steps: Purchase cake ingredients. Combine ingredients. Bake the cake. Decorate the cake. Serve the cake. These steps cannot be completed at the same time.

In other words, these steps cannot be completed asynchronously. The following step can only be started after the previous step is complete. When using callbacks to make something occur sequentially, functions need to be nested one within another. The pseudocode for our cake example might end up looking something like this, where each subsequent function becomes the argument passed to the next function. Every callback depends on and waits for the previous callback, thereby making a pyramid structure that affects the readability and maintainability of the code. This nesting of callback functions is often referred to as “Callback Hell” and is essentially nested callbacks stacked below one another, forming a pyramid structure. This structure is also sometimes referred to as “The Pyramid of Doom.”

Another issue with callbacks is inversion of control, also called IoC. Inversion of control happens when the flow of control, such as the execution of instructions, is external to your code. Many times, callbacks hand the control over to a third party. But issues and errors with that third-party code can be difficult to catch. You are forced to trust the third-party code, or you must write additional code that ensures the third-party code does not: Get called too many times or too few times, Get called too early or too late, Lose context, or pass back incorrect arguments. For example, say the third-party code has a bug where it gets called multiple times when the user mistakenly clicks a button more than once. You may try to solve this issue with a boolean flag.

When the flag is false, and the button is clicked, the card gets charged and the flag is turned to true. So now, when the flag is true, and the button gets clicked again, the branching logic doesn’t charge the customer’s card another time. But then what if the callback never gets called at all? That flag remains false, and now there is yet another use case you have to account for. To catch these sorts of errors, your code becomes riddled with extraneous code to ensure third-party code doesn’t fail. There are a number of ways to mitigate callback hell and trust issues: You can write comments, split functions into smaller functions, use Promises, or you can use async/await. Promises and async/await will be discussed in upcoming videos.

In this video, you learned that: The need for nested callback functions can occur when several of the callback tasks are dependent on each other and need to be completed sequentially. The term “callback hell” refers to nested callback functions. When using third-party code, you often have inversion of control issues where you cannot trust the third-party code. And ways to mitigate callback hell and trust issues include writing comments, splitting functions into smaller functions, using promises and using async/await.

---

### 5. [VIDEO TRANSCRIPT] Promises Video • 3 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/LiaTV/promises
- **Method:** `dom_transcript` | **Length:** 2683 chars

[Music] Welcome to Promises. After watching this video, you will be able to: Define promises. Explain the different states of a promise and describe how to use promises with asynchronous methods. A promise is an object returned by an asynchronous method. The promise has three states, which are pending, resolved, and rejected. Promises are most useful for application programming interface (API) requests, input/output (I/O) operations, and other operations that are time consuming and can block resources. A method can be defined to return a promise object, if you know it is going to take time for execution and thereby block resources.

When you call a method that returns a promise, a promise object is created. The initial state of the promise is the pending state. It is in this state until the operation is complete or some error has caused the operation to abort. When the operation is complete, the promise is said to be resolved. When there is an error, the promise is said to be rejected. You can also create a promise object if you know that the operations you are going to perform could be blocking. In this example, methCall is a promise which is fulfilled or rejected depending on whether the file is successfully read or not.

You can see on the output screen that the content of the file is read if the filename is valid and displayed. In this case the promise is resolved. If the filename is invalid, the promise is rejected and the error message is displayed. You know that hypertext transfer protocol (HTTP) requests when called synchronously can be blocking. There are many packages in the Node.js ecosystem that wrap promises around HTTP requests. The axios package is one such package to handle HTTP requests. It returns a promise object.

The status of the promise until it hears back from the uniform resource locator (URL) requested is pending. The promise object has a "then" method which is called after the promise is fulfilled. The catch is executed if the promise is rejected. In this example, you first pass a valid URL. It creates a pending promise. Once the promise is fulfilled, then the response is logged on the console. Next, you pass an invalid URL.

This also creates a promise object which is pending. This promise will be rejected. This state is being dealt with in the catch block. You can see the console log for the resolve and reject. In this video you learned that: A promise is an object that is returned by an asynchronous method. The initial state of the promise object is the pending state. The axios package is used in Node.js to handle HTTP requests and you can create a promise if you know that the operations could be blocking.

---

### 6. [VIDEO TRANSCRIPT] Working with JSON Video • 1 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/NGM8J/working-with-json
- **Method:** `dom_transcript` | **Length:** 1280 chars

[Music] Welcome to Working with JSON. After watching this video, you should be able to: Parse JavaScript Object Notation (JSON) data from a hypertext transfer protocol (HTTP) message. JSON is the standard format for application programming interface (API) data exchange. It is the standard representation of native JavaScript objects, and Node.js handles it easily. In this example, the object consists of attribute-value pairs. The first attribute is "Company" and the value is "IBM". The second attribute is "Country" and the value is "USA".

The third attribute is "Headquarters" and the value is "Armonk, New York". To parse a JSON string to a JavaScript object, use method JSON.parse. Method JSON.stringify() converts a JavaScript object to a JSON string. Now that you know what JSON is and two important methods that you can use to parse a string into JSON and also convert JSON into a string. Let us see an example of using a real endpoint that returns JSON. You can use JSON to find out how many astronauts are in the International Space Station (ISS). You have found that the number of astronauts is five.

In this video, you learned that: Node.js handles JSON easily, and you can use two important methods to parse a string into JSON and also convert JSON into a string.

---

### 7. [VIDEO TRANSCRIPT] Expert Viewpoints: Using JSON & JavaScript Video • 3 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/Q7Lr8/expert-viewpoints-using-json-javascript
- **Method:** `dom_transcript` | **Length:** 2779 chars

Welcome to Expert Viewpoints: Using JSON and JavaScript. In this video, we will hear from several application development professionals discussing situations where knowing JSON and JavaScript has helped them and how they think these methods can benefit new cloud application developers. Familiarity with JavaScript and JSON is more or less a requirement for web developers. If you're not working with the front end at all, you might be able to get away without touching any JavaScript, but JSON is the de facto standard for data serialization. You will want to learn how to (3)use JSON so that you can consume APIs written by other people and also, make your own APIs return JSON so other people can easily use them. Another place you'll see JSON a lot is where you have to specify something in a way the computer can easily understand. So you'll probably first see that when specifying requirements for a Node.js project, for instance, but you might see it again when specifying deployments for platform as a service offerings or Kubernetes workloads.

JSON or JavaScript Object Notation is built into JavaScript, right? So when you're working with objects in JavaScript, you're essentially working with JSON. That being said, with RESTful web services, a common format of communication or data is also JSON. So as Node.js developers and as JavaScript developers, you cannot escape from JSON. It's actually a very friendly format to work with. JSON is one of the things, one of those things if you're a JavaScript developer, if you're a Node.js developer, you need to understand and work with JSON objects. So, the sooner you pick it up, the better.

JSON is one of the dominant formats to encode objects in a string. And JSON is a native data type in JavaScript. So serialization converts the JSON object into a byte string and deserialization converts the byte string back to the JSON object. One great benefit of being comfortable with JSON is that the request and response objects in cloud, REST APIs are often in JSON, at least when you're working at the curl level or the shell script level. Another benefit of knowing JavaScript and JSON is working with JSON Oriented document databases. Writing in JavaScript and using JSON helps me all the time, because JavaScript is the language of the Internet. So you see it in a lot of applications.

And being able to just add some code to an existing project or write some JavaScript from scratch is really useful. It's like speaking, a language that's very popular. And JSON is used by many of the modern languages, including Python and Node.js. So I use Python every single day, because it's a really useful way to structure your data and pass it back and forth. And, you know, that's the way you get a response from most APIs.

---

### 8. [VIDEO TRANSCRIPT] Promises, async/await, and axios requests in Node.js and Express Video • 7 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/67RNg/promises-async-await-and-axios-requests-in-node-js-and-express
- **Method:** `dom_transcript` | **Length:** 6301 chars

Welcome to this video that delves into the core concepts of handling asynchronous operations with promises, async/await, and axios in Node.js and Express. After watching this video, you will be able to Explain the fundamental concepts of promises and how they chain operations in JavaScript Use async/await syntax for clearer and more readable asynchronous code Make HTTP requests using the axios library Suppose you use a web application to purchase garden equipment. The application lags in performance and you find the shopping experience disappointing. Would you like to use that application again to make any purchases? A web application with JavaScript's asynchronous programming doesn't face such issues as it is responsive and performant. Mastering asynchronous programming is essential if you're working with Node.js and Express as asynchronous programming improves the performance of your web applications and enhances the user experience. Let's start by exploring promises, a fundamental concept for managing asynchronous operations in JavaScript.

A promise is an object that represents success or failure of an asynchronous operation and its resulting value. It allows you to chain operations in a more readable and manageable way. Now, let's learn about the states of a promise. A promise can be in three states, pending, fulfilled, or rejected. Pending denotes the initial state, which is neither fulfilled nor rejected. Fulfilled state denotes the successful completion of the operation. Rejected state means that the operation has failed.

This allows us to handle asynchronous tasks more gracefully compared to traditional callback methods. Now, it's time to explore how to create a promise. In this code snippet, you can see the creation of a promise. To create a promise, we use the new Promise constructor, which takes a function with resolve and reject as parameters. If your operation is successful, the resolve function is called. Otherwise, the reject function is called. Let's now explore how promises allow you to chain multiple asynchronous operations in sequence.

In this example, the code allows you to handle the resolved value or the error using then and catch methods. These methods also return promises and chain multiple asynchronous operations in sequence. Now, let's explore a practical example where promises are used to read a file. In this code, the promises module performs the following function. It reads the contents of a file. It prints the file content to the console if the file is read successfully, and it throws an error message to the console if the file is not read successfully. Now, it's time to learn how to work with promises using async/await.

Promises complicate the structure and readability of your code. Async and await are syntactic sugar over promises, which makes asynchronous code look more like synchronous code, which makes it easier for you to read and write. As async function returns a promise, you can use await inside an async function. This use of await pauses execution until a promise is resolved or rejected. Let's delve deeper and explore async/await benefits in detail. When you use async and await, asynchronous code appears more linear and easier to understand. It allows you to use the standard try-catch for error handling, which is more familiar to developers.

Also, you can debug easier due to the asynchronous flow of the code. Now that you can recognize the key benefits of async/await, let's use async/await in an example. This code snippet shows how async/await function simplifies asynchronous programming in JavaScript. In this example, the async function performs the following actions. It simulates a conditional operation. It returns a success message if the condition is met. It generates an error when the condition is not met.

It uses await to call async function. It handles the result or any errors using try and catch. It handles promises more easily than chains. Now, it's time to learn about axios and how it is used. Axios is a promise-based HTTP client for the browser and Node.js. Axios makes it easy for you to send asynchronous HTTP requests to REST endpoints and perform CRUD operations. Axios automatically transforms JSON data and provides a clean and simple API.

Now, let's take a look at some key features of axios. axios offers the following features. It uses promises for easy async/await usage. It transforms JSON data automatically. It allows you to intercept requests or responses to modify them. It supports request cancellation. And it provides comprehensive error handling features. Now let's use axios to make a GET request in a practical example.

As you can see in this code snippet, first, you need to install axios. Once installed, you can use axios and see how it simplifies making HTTP GET requests. The axios.get method returns a promise that resolves with the response object. This allows you to access the data. Now it's time to learn how to use axios to make a POST request. Let's look at a code snippet that demonstrates how axios makes HTTP POST requests and handles responses and errors. This code imports axios for HTTP requests and creates user data object for POST request.

By using axios.post function, this code sends data to the server. Finally, it logs response data on success and error message on failure. Now it's time to use async/await and axios together to handle HTTP requests. When you combine async/await with axios, it provides a clean approach to handle HTTP requests. In this example, you can see how the code uses await to pause the function execution until the POST request completes. Finally, the result is handled inside the try block. In this video, you learned that Asynchronous programming in JavaScript can build responsive and performant web applications.

Promises provide you a way to handle asynchronous operations, making code more readable and easier to manage by allowing chaining of operations. The async/await syntax builds on promises and enables you to write asynchronous code that resembles synchronous code, thus simplifying the handling of asynchronous tasks. Axios can be used as an HTTP client to make requests to external APIs and services, simplifying the process of handling HTTP requests in JavaScript applications.

---

### 9. [READING] Promises, Async/Await, and Axios Requests in Node.js and Express Reading • 20 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/kaCOK/promises-async-await-and-axios-requests-in-node-js-and-express
- **Method:** `dom_reading_cml` | **Length:** 9752 chars

### Objectives

In this reading, you will learn about:

- Promises: The core building block for handling asynchronous operations in JavaScript
- Async/Await: A modern and more readable syntax for working with Promises
- Axios: A widely used HTTP client for making network requests

### Introduction

JavaScript's asynchronous programming model is foundational for developing responsive and performant web applications. In Node.js and Express, handling asynchronous operations effectively is essential for tasks such as making API requests, reading files, or querying databases.

### 1. Promises

A Promise is an object that represents the eventual completion (or failure) of an asynchronous operation and its resulting value. It allows you to chain operations in a more readable and manageable way.

#### 1.1 States of a Promise

#### 1.2 Creating a Promise

To create a Promise, you use the new Promise constructor, which takes a function with two parameters: resolve and reject. The resolve function is called when the asynchronous operation completes successfully, and the reject function is called when it fails.

12345678910111213// Creating a new Promise object and assigning it to the variable myPromiseconst myPromise = new Promise((resolve, reject) => { // Simulating a condition with a boolean variable 'success' let success = true;  // If the condition is true, call resolve to mark the promise as fulfilled if (success) {  resolve("The operation was successful!"); } else {  // If the condition is false, call reject to mark the promise as rejected  reject("The operation failed!"); }});Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### 1.3 Using Promises with .then() and .catch()

You can handle the resolved value or the error using .then() and .catch() methods. These methods also return Promises, allowing you to chain multiple asynchronous operations in sequence.

123456789101112// Execute the promise and handle the fulfilled and rejected statesmyPromise // Handle the resolved state of the promise .then((message) => {  // This block will execute if the promise is resolved  console.log(message); // "The operation was successful!" }) // Handle the rejected state of the promise .catch((error) => {  // This block will execute if the promise is rejected  console.error(error); // "The operation failed!" });Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### 1.4 Example: Reading a File

Here's an example using the fs.promises module to read a file. The fs.promises module provides Promise-based methods for file system operations.

123456789101112131415// Import the 'fs' module and use its promise-based methodsconst fs = require('fs').promises; // Read the content of the file 'example.txt' with 'utf8' encodingfs.readFile('example.txt', 'utf8') // Handle the resolved state of the promise .then((data) => {  // This block will execute if the file is read successfully  console.log(data); // Print the file content to the console }) // Handle the rejected state of the promise .catch((err) => {  // This block will execute if there is an error reading the file  console.error('Error reading file:', err); // Print the error message to the console });Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### 2. Async/Await

As you might have already learnt, JavaScript is a single-threaded scripting language. It means the process can happen only sequentially, and no two processes can happen simultaneously. This is a big deterrent to any language, and JS solved this by introducing asynchronous programming through Promises. While Promises solved the issues with synchronous programming, nested then can complicate the structure and readability of the code.

Async and Await are syntactic sugar over Promises, making asynchronous code look more like synchronous code, which is easier to read and write. An async function returns a Promise, and you can use await inside an async function to pause execution until a Promise is resolved or rejected.

#### 2.1 Benefits of Async/Await

#### 2.2 Using async and await

An async function always returns a Promise. Inside the async function, you can use the await keyword to pause execution until a Promise is resolved or rejected.

123456789101112131415161718192021222324252627// Async function that wraps the operationasync function myAsyncFunction() { // Simulating a condition with a boolean variable 'success' let success = true;  // If the condition is true, resolve with a success message if (success) {  return "The operation was successful!"; } else {  // If the condition is false, throw an error to simulate rejection  throw new Error("The operation failed!"); }} // Using async function to handle Promiseasync function executeAsyncFunction() { try {  // Await the async function call to get the result  const result = await myAsyncFunction();  console.log(result); // Output the result if successful } catch (error) {  console.error(error.message); // Handle and output any errors }} // Call the async function to executeexecuteAsyncFunction();Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.This example shows how async and await can simplify asynchronous programming in JavaScript. The async function myAsyncFunction simulates a conditional operation, returning a success message if the condition is met and throwing an error otherwise. The executeAsyncFunction uses await to call myAsyncFunction and handles the result or any errors using try and catch. This approach makes the code easier to read and understand compared to handling promises with .then() and .catch() chains.

### 3. Axios Requests

Axios is a promise-based HTTP client for the browser and Node.js. It makes it easy to send asynchronous HTTP requests to REST endpoints and perform CRUD operations. Axios automatically transforms JSON data and provides a clean and simple API.

#### 3.1 How Axios is Used

- You can install Axios using the following command: npm install axios

#### 3.2 Making a GET Request

- Axios simplifies making HTTP GET requests. Here's how to fetch data from a public API:

12345678910111213141516// Import the axios libraryconst axios = require('axios'); // Using the axios.get method to make a GET request to the specified URL.axios.get('https://api.example.com/data') // If the request is successful, the `.then` block is executed. .then(response => {  // The response object contains the data returned from the server.  // We log the `data` property of the response to the console.  console.log(response.data); }) // If there is an error during the request, the `.catch` block is executed. .catch(error => {  // We log an error message to the console along with the error object.  console.error('Error fetching data:', error); });Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.The axios.get method returns a Promise that resolves with the response object, allowing you to access the data with response.data.

#### 3.3 Making a POST Request

To send data to a server, use a POST request:

1234567891011121314151617// Import the axios library.const axios = require('axios'); // Data to be sent in the POST request.const data = { name: 'John Doe', age: 30}; // Using the axios.post method to make a POST requestaxios.post('https://api.example.com/users', data) .then(response => {  console.log('User created:', response.data); }) .catch(error => {  console.error('Error creating user:', error); });Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.This code snippet demonstrates the basic usage of axios for making HTTP POST requests and handling responses and errors.

### 4. Example: Using Async/Await with Axios

Combining async/await with Axios provides a clean approach to handle HTTP requests:

12345678910111213141516171819202122const axios = require('axios'); // Asynchronous function to post data to an APIasync function postData() { try {  // Await the response from the Axios POST request  let response = await axios.post('https://jsonplaceholder.typicode.com/posts', {   title: 'foo',   body: 'bar',   userId: 1  });   // Log the response data to the console  console.log(response.data); } catch (error) {  // If there is an error, log the error message  console.error('Error posting data:', error); }} // Call the async functionpostData();Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Here, await pauses the function execution until the POST request completes, and the result is handled inside the try block.

### Summary

In this reading, you learned about the fundamental concepts of asynchronous programming in Node.js and Express, focusing on Promises, async/await syntax, and the Axios HTTP client. Promises provide a way to handle asynchronous operations, making code more readable and easier to manage by allowing chaining of operations. The async/await syntax builds on Promises, enabling you to write asynchronous code that resembles synchronous code, thus simplifying the handling of asynchronous tasks. Finally, you explored how to use Axios to make HTTP requests, which is essential for interacting with external APIs and services. By mastering these concepts, you can write more efficient and maintainable asynchronous code, which is crucial for building robust web applications.

### Author(s)

Rajashree Patil 
Sapthashree K S

---

### 10. [READING] Module Summary Reading • 1 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/YoGct/module-summary
- **Method:** `dom_reading_cml` | **Length:** 698 chars

Congratulations! You have completed this module. At this point in the course, you know:

- Asynchronous network operations can be handled using callback functions in order to prevent blocking JavaScript code
- A callback function must invoke another callback function to pass a message from the Node.js module back to the main application after the Node.js module receives a response message
- Nested callbacks can be difficult to read and debug. Inversion of control causes trust issues when dealing with third-party code
- Promise objects are most useful for operations that are time-consuming and can block resources
- JSON.parse() and JSON.stringify() are two methods used to parse JSON objects

---

### 11. [READING] Glossary - Asynchronous I/O with Callback Programming Reading • 5 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/CArzr/glossary-asynchronous-i-o-with-callback-programming
- **Method:** `dom_reading_cml` | **Length:** 778 chars

| Term | Definition |
| --- | --- |
| Async | Short for “asynchronous”. |
| Axios Package | The axios package wraps promises around HTTP requests. It returns a promise object. |
| Callback Hell | Many nested callback functions. |
| Inversion of Control | When the flow of control, such as the execution of instructions, is controlled by a third party. |
| Promise | An object in JavaScript that acts as a placeholder for an asynchronous task that is yet to be completed. It is the object that is returned from an asynchronous method. When you define a promise object in your script, instead of returning a value immediately, it returns a promise. The promise has three states, which are pending, fulfilled, and rejected. |
| Pyramid of Doom | Another term for “callback hell”. |

---

### 12. [READING] Cheatsheet - Asynchronous I/O with Callback Programming Reading • 15 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/Fh953/cheatsheet-asynchronous-i-o-with-callback-programming
- **Method:** `dom_reading_cml` | **Length:** 3687 chars

#### Async-await

Description: We can await promises as long as they are being called inside asynchronous functions.

12345678910const axios = require('axios').default;let url = "some remote url" async function asyncCall() { console.log('calling'); const result = await axios.get(url); console.log(result.data);} asyncCall();Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Callback

Description: Callbacks are methods that are passed as parameters. They are invoked within the method to which they are passed as a parameter, conditionally or unconditionally. We use callbacks with a promise to process the response or errors.

123456//function(res) and function(err) are the anonymous callback functionsaxios.get(url).then(function(res) { console.log(res);}).catch(function(err) { console.log(err)})Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Promise

Description: An object that is returned by some methods, representing eventual completion or failure. The code continues to run without getting blocked until the promise is fulfilled or an exception is thrown.

12345axios.get(url).then(//do something).catch(//do something)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Promise use case

Description: Promises are used when the processing time of the function we invoke takes time like remote URL access, I/O operations file reading, etc.

12345678910111213141516171819let prompt = require('prompt-sync')();let fs = require('fs'); const methCall = new Promise((resolve,reject)=>{ let filename = prompt('What is the name of the file ?'); try {  const data = fs.readFileSync(filename, {encoding:'utf8', flag:'r'});  resolve(data); } catch(err) {  reject(err) }}); console.log(methCall); methCall.then( (data) => console.log(data), (err) => console.log("Error reading file"));Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.object.on()

Description: It defines an event handler that the framework calls when an event occurs

12345678910http.request( options, function(response) {let buffer = ‘’;... response.on('data', function(chunk) { buffer += chunk;}); response.on('end', function() { console.log(buffer);});}).end();Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Callback Hell/The Pyramid of Doom

Description: Nested callbacks stacked below one another and waiting for the previous callback. This creates a pyramid structure that affects the readability and maintainability of the code.

1234567891011const makeCake = nextStep => { buyIngredients(function(shoppingList) { combineIngredients(bowl, mixer, function(ingredients){ bakeCake(oven, pan, function(batter) { decorate(icing, function(cake) { nextStep(cake); }); }); }); });};Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Axios Request

Description: The axios package handles HTTP requests and returns a promise object.

1234567891011121314151617const axios = require('axios').default; const connectToURL=(url)=>{ const req=axios.get(url); console.log(req);  req.then(resp=>{  console.log("Fulfilled");  console.log(resp.data); }) .catch(err=>{  console.log("Rejected"); });} connectToURL('valid-url')connectToURL('invalid-url')Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.

---
