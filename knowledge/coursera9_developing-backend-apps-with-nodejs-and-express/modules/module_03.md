# Module 3: Express Web Application Framework

### 1. [VIDEO TRANSCRIPT] Extending Node.js Video • 4 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/z3XEM/extending-node-js
- **Method:** `dom_transcript` | **Length:** 3611 chars

[Music] Welcome to Extending Node.js. After watching this video, you should be able to: Extend Node.js with third-party packages and define package dependency. You can build a hypertext transfer protocol (HTTP) server using Node.js, but the default Node.js framework is limited. However, there are many aspects of building a web server like routing, parsing incoming files, authentication, connecting to a database, and other aspects. For example, you can parse extensible markup language (XML) with JavaScript string functions, but an XML document object is not efficient in parsing a stream of XML data. Developers rely on external libraries and packages to extend the core Node.js functionality. Say you need to know about the weather data of San Francisco International Airport.

You can send an HTTP request to an external web server. After you receive the weather data, you can parse it manually. Here you parse web service messages as a string. When Node.js receives the final part of the HTTP response message, it calls the response.on('end') event handler. Inside the callback function, the first line with the buffer.match function call locates the part of the XML message that begins and ends with the temp_f XML element tag. This string, including the temp_f start and end tags, is saved in the matches variable. If there is a match, the second call to matches[0].replace strips out the start and end temp_f XML elements.

Consider the disadvantages of treating XML data as a string. String matching ignores the structure of XML data. The message body might contain malformed XML data. Depending on the complexity of the XML data, string matching might be more efficient than building an XML tree of the data. String matching is less tolerant to changes in the XML data structure. And if the message adds or removes any XML elements, you must change the regular expression on the string match function. You can use the xml2js Node.js package to parse a string of XML elements into a JavaScript object.

This is a Node.js package that uses only JavaScript. It does not require an XML parsing library written in another language. Because third-party packages licenses might have their own licenses, confirm that the licensing terms work with your company and your application before installing the xml2js Node.js package. You can use the npm application to manage Node.js packages in your Node.js framework installation. For instance, run the npm install command to retrieve and set up a Node.js package and any package dependencies. In this example, you call npm install xml2js from the command line. The npm application goes out to the Internet and retrieves the Node.js module xml2js and any dependencies that it requires.

Here, you import the package into your application. In the first line, the parseString function calls the callback function when it finishes processing the XML tree in buffer. In the last line, the result JavaScript variable represents the contents of the XML fragment in buffer. In other words, the result JavaScript variable represents the XML element, but in JavaScript form. The property current_observation.temp_f[0] maps to the first child element in the temp_f XML element. The temp_f element is a child of the current_observation element. In this video, you learned that: Developers rely on third-party packages to extend Node.js's features.

String matching ignores the structure of XML data. The xml2js Node.js package parses a string of XML elements into a JavaScript object and the npm application manages Node.js packages in your Node.js framework installation.

---

### 2. [VIDEO TRANSCRIPT] Expert Viewpoints: Working with Third-Party Node.js Extensions Video • 2 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/xvqw1/expert-viewpoints-working-with-third-party-node-js-extensions
- **Method:** `dom_transcript` | **Length:** 2083 chars

Welcome to Expert Viewpoints: Working with 3rd party Node.js Extensions. In this video, several application development professionals will discuss which 3rd party Node.js extensions they commonly use and how these extensions could often benefit application developers. One of the NPM Node.js packages that I've used the most is the serverless framework, because that allows you to deploy serverless microservices in the cloud very easily without writing a lot of the resource and infrastructures code yourself. There's a number of Node.JS extensions I use all the time. For instance, I use Lodash, which is a great package for dealing with collections and arrays, finding the right elements, sorting, so on and so forth. It saves a lot of time. Axios is also very useful for dealing with RESTful APIs. and submitting GETS, PUTS, POSTS, so on and so forth.

Also in my Express applications there's a ton of middlewares, especially middlewares dealing with authentication and JWT tokens. Those are all extremely useful and really help accelerate any cloud developer creating services and other tools in the cloud. When working with Node.js, I'll give you two of my favorite packages that I use on a daily basis. So first is making requests to web services. So my application more likely than not has to request information from another web service. Now, this could be a web service that I've written, or this could be a web service that somebody else has written. Regardless, I need to send a request out with some input parameters, and then wait for the request to come back, or wait for the response to come back and handle that response.

Instead of writing all of this code myself, I use a library like Axios that helps me create these requests with the right headers and also provides me with callback functions and/or promises to be able to handle the responses that come back. My second package would be when I'm working with databases, I'll use NPM packages, more likely than not to talk to an external database, regardless of if it's a relational database or a NoSQL database.

---

### 3. [VIDEO TRANSCRIPT] Introduction to Web Frameworks Video • 7 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/xnVAo/introduction-to-web-frameworks
- **Method:** `dom_transcript` | **Length:** 6457 chars

Welcome to Introduction to Web Frameworks. After watching this video, you will be able to: Explain the difference between Node.js and Node.js-based web frameworks. Explain MVC and REST API architectural styles. And describe prominent features of several Node web frameworks. Sometimes Node.js is incorrectly referred to as a web framework. Node.js is not a framework but a runtime environment that executes JavaScript on a server. Runtime environments are the hardware and software that can execute programs with a particular codebase.

A framework, on the other hand, is like a skeleton on which an application is built for a specific environment. The framework is the fundamental structure that supports the application. So, in order to utilize Node.js, you need to use a web framework that works in conjunction with it. A framework that works with Node.js is called a node web framework or just a node framework. There are a number of different node frameworks. And we will discuss a few later in this video. So, before discussing individual frameworks, let’s first discuss two approaches to building back ends that web frameworks can employ: Model-View-Controller, better known as MVCs, and Representational state transfer application programming interfaces, or REST API for short.

An MVC approach can be used simultaneously with REST APIs. They are not mutually exclusive. MVC stands for “model view controller”. MVC is an architectural pattern that divides an application into three components: model, view, and controller. Let’s discuss what each of these components is. The model layer is responsible for managing the data of the application. It interacts with the database and handles the data logic.

The view is responsible for rendering the presentation of the data that is passed to it by the model. And the controller regulates the flow of the data. It is responsible for processing the data supplied to it by the user and sends that data to the model for manipulation or storage. MVC frameworks are generally used to develop applications that need a separation of data, called the model; the presentation of the data called the view; and the module that manipulates the data, which is the controller. Frameworks that lend themselves to developing the back end with an MVC pattern include Koa, Django, Express, and NestJS. Now let’s discuss REST APIs. REST APIs allow multiple web services to communicate with each other.

RESTful APIs are subject to certain constraints. The code on the client must be completely independent of the server code. Client-side code can be updated without interfering with the server code and vice versa. Secondly, RESTful APIs are also stateless. Stateless means the client does not need to know the state of the server, nor does the server need to know the state of the client for communication between the two. REST APIs communicate via operations on resources, and they do not rely on a particular implementation of the API. When a client requests resources using a REST API using HTTP methods such as GET, POST, PATCH, or DELETE, the server responds with a representation of the state of the resource to the client.

The representation of the data transferred between client and server is usually a JSON payload but can also be HTML, XLT, Python, PHP, or plain text. So, now that we’ve discussed a couple of ways to structure the back-end code, let’s dig deeper and discuss some of the popular frameworks themselves. Express.js, aka Express, is one of the most popular Node Web Frameworks. It is used for routing and middleware. Its straightforward coding using JavaScript means there is a fairly small learning curve. It is easy to implement an MVC architecture pattern with Express. It provides debugging mechanisms to help easily pinpoint the errors in the application.

Express delivers high performance because it handles multiple operation requests concurrently that are independent of each other with asynchronous programming. It has many HTTP helpers that make programs intelligible and reusable for handling HTTP requests. It has great content negotiation that helps the client and server to communicate by efficiently providing HTTP headers to URLs, fetching the exact data needed for the requesting client. Koa is a relatively new web framework designed by the same team who designed Express. It intends is designed to be smaller, more expressive, and provide a more robust foundation for web applications and APIs. Koa uses async functions in such a way that callbacks are not necessary, and it increases the ability to handle errors. Koa is appropriate for applications that are high-performing, demanding, complex, and developed by large, experienced teams.

Socket.io is an excellent choice for developing apps where bidirectional data is exchanged between clients and servers in real-time. You can develop applications that utilize WebSocket rather than HTTP for communication. Its servers push data without the need for that data to be called by the client. It is appropriate for applications such as chat rooms, texting applications, video conferencing, and multiplayer games. Next, Hapi.js is a reliable open source node web framework with lots of security built into it. There are many built-in plugins, so you won’t need to use unofficial middleware. It is most known for developing proxy and API servers, HTTP-proxy applications, REST APIs, and other desktop applications.

And finally, we have, the NestJS framework which is appropriate for building dynamic, scalable enterprise applications in conjunction with its flexibility due to its multitude of libraries. It follows an MVC architecture. NestJS is built on top of Express, so they have similar purposes and provide comparable functions. It is compatible with TypeScript, which is a subset superset of JavaScript. It works in conjunction with the front-end Angular framework. And Nest combines both object-oriented and functional reactive programming, which potentially doubles productivity and application performance. In this video, you learned that: Node.js is a runtime environment, whereas node web frameworks use the Node.js environment in order to run.

The MVC architecture style divides a back-end application into three parts: the model, the view, and the controller. REST API frameworks use HTTP methods to communicate with each other And several popular node web frameworks include Express, Koa, Hapi.js, and NestJS.

---

### 4. [VIDEO TRANSCRIPT] Express Web Application Framework Video • 6 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/Ebcbj/express-web-application-framework
- **Method:** `dom_transcript` | **Length:** 5044 chars

Welcome to Express Web Application Framework. After watching this video, you will be able to describe the Express framework, explain the primary uses of Express, and download Express. Express is a web application framework based on the Node.js runtime environment, however, Express abstracts low-level details. Express helps you organize your application better and develop your application faster. It provides robust mechanisms for integrating middleware packages and handling different hypertext transfer protocol (HTTP) request methods. The Express web application framework is widely used in the field today and forms the basis of other frameworks as well. Express is primarily used for two purposes, one as an API, and the second is to set up templates with server-side rendering, also known as SSR.

Using Express to build APIs means setting up an HTTP interface to interact with the data layer. In the case of APIs, data is sent back to the client in JSON format using a response object, or res for short. The res.json method is used to notify the client of the content type of the data being sent, such as if it's an image or text. It can also be used to Stringify data, in other words, converting JavaScript to JSON format. In Server-side rendering (SSR), Express is used to set up templates. Express is responsible for using the data sent from the client supplied by an HTTP request in conjunction with the template to dynamically write HTML, CSS, and/or JavaScript. The HTML, CSS, and/or JavaScript is sent back to the client as text so that the browser can render the page.

This is accomplished using the Express res.render method. Express implements an app class that you map to a web resource path. In contrast, when using the Node.js core application programming interface (API), the http.createServer function relies on your custom callback function to parse through the web resource path. Here is an overview of how to work with Express. There are five steps. Step one, declare Express as a dependency in the package manifest of a Node.js project. Two, run the npm command to download any missing modules.

Three, import the Express module and create an Express application. Four, create a new route handler. And five, start an HTTP server on a given port number. Next, you will see how to complete steps one and two. First, to declare Express as a dependency in the package.json file, create a package.json file in your project folder. The package.json file stores information about the contents of a Node.js module including five items: name, version, description, main, and dependencies. Name is a name for the Node.js module.

Version is a string that defines the major and minor version number of the module. Description is a sentence that describes the purpose of the module. Main identifies the Node.js script as the entry point into the module. And dependencies is a list of which Node.js modules that the current module requires. To declare Express as a dependency, list the Express module and a version number in the dependencies property. Here, In this package.json dependency file, the name of the module is temperature. Its version is 1.0.0.

Its description is "retrieve current weather conditions in the United States." The main script file, which is the entry point in the module, is set to app.js. It has a dependency on the Express framework, which is version 4.x. In step 2, you run the npm command to download any missing modules. When you run the npm install command inside the Node.js module directory, it resolves any missing dependent Node.js modules. The command downloads and saves any missing Node.js modules into its own node_module directory. This scheme allows you to use different versions of the same Node.js module in different packages.

For example, a custom Node.js module installs a version 4.0 release of the Express framework. Another Node.js module installs version 5.0 in its own Node module repository. To install a Node.js module into the shared node_module directory, run npm install with your module name from the directory with your Node.js installation. To download Express, run npm install in your project folder When you run the command npm install with no parameters, the npm application scans your package.json file. It checks your node_module directory to see if any modules are missing. In this case, the Express web application framework is not in your current installation. The npm application downloads the Express framework and all of its dependent modules.

In this video, you learned that: Express is a third-party module that provides a framework for building web applications. Express serves two purposes: to set up APIs and to implement SSR And to install Express, there are five steps: Declare Express as a dependency in the package manifest of a Node.js project. Run the npm command to download any missing modules. Import the Express module and create an Express application. Create a new route handler. And finally, start an HTTP server on a given port number.

---

### 5. [VIDEO TRANSCRIPT] Your First Express Web Application Video • 3 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/ap2us/your-first-express-web-application
- **Method:** `dom_transcript` | **Length:** 2684 chars

[Music] Welcome to Your First Express Web Application. After watching this video, you will be able to create an application using Express, and identify the five steps to install Express. Follow these five steps to work with Express One, declare Express as a dependency in the package manifest of your Node.js project. Two, run the npm command to download any missing modules. Three, import the Express module and create an Express application. Four, create a new route handler and five, start a Hypertext Transfer Protocol (HTTP) server on a given port number. When you declare Express as a dependency in your Node.js project and download any missing modules, you can create a mynodeserver.js file in your project folder.

Now you can start coding with your first Express program. In this example, you are writing a program to retrieve current weather conditions. When you have imported a copy of the Express web application framework, create an instance of the app JavaScript object from the framework. Next, create a new route handler. In your application, to handle web application requests, map an HTTP method and a web resource path to the JavaScript function. Here, you are listening to incoming HTTP GET requests, which make requests to the temperature resource path. You are also saving the value after the temperature resource path in a variable named location_code.

You can access the variable in the path by using request.params.location_code, and store the value in a location variable named “location.” When you run the weather.current function, you pass the parameter location, which is taken from the resource path. In the last step, you start an HTTP server on a given port number. To create an instance of the server from the app, call app.listen to create a web server object (that is, an instance) that listens to incoming requests on the specified port. The app listens to incoming requests; for example, on port 8080. The second parameter defines an anonymous function that the Express framework calls when it creates an instance of the server object. For the result, enter the uniform resource locator (URL) in your browser.

In this video, you learned that: When you declare Express as a dependency in your Node.js project and download any missing modules, you can create an application and start coding with Express and to install Express, there are five steps: One, declare Express as a dependency in the package manifest of a Node.js project. Two, run the npm command to download any missing modules. Three, import the Express module and create an Express application. Four, create a new route handler, and five, Start an HTTP server on a given port number.

---

### 6. [VIDEO TRANSCRIPT] Expert Viewpoints: Working with Back-end JavaScript Frameworks and Express Video • 3 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/6oW0v/expert-viewpoints-working-with-back-end-javascript-frameworks-and-express
- **Method:** `dom_transcript` | **Length:** 2882 chars

Welcome to Expert Viewpoints: Working with Backend JavaScript frameworks and Express. In this video, we will hear from several cloud-native application development professionals discussing why they use Express.js for building backend web applications. The Express framework for Node.js is a great choice for building back-end web apps. It allows for very high-level expressive declaration of REST API endpoints, which is great for productivity as well as code readability. I believe it's the most popular web framework for Node.js and the Express team. And the community surrounding it have created a bunch of great middleware for things like parsing body content, authentication, handling user sessions, and request logging. There are a number of reasons to use Express nowadays.

It's popular. There's a ton of packages for it. So it will give you the ability to create something with only a few lines of code. Also Express is really great for working with middlewares I find, which lets you pretty much do anything you want with any requests coming in or any responses going out when people are using your service. Also Express can be very, very fast and very, very easy to use, so I find the development life cycle can be very short if you know what you're doing. When it comes to using back-end JavaScript frameworks, I am most familiar with Express.js. It's very prominent.

And you can use it to create applications that live on the Web. So Express.js abstracts a lot of low-level code that you would be writing yourself if you were building your website or web application on Node.js itself. So it makes me a more effective programmer, or software developer. But more than that, Express is built on certain best practices that you would have to follow anyways if you were building all of this from scratch. It's good to rely on this community-driven open source framework that more likely than not will do the right thing for me. By using Express.js for back-end development, we are able to scale applications quickly. We can code both front end and back end with the help of JavaScript easily by using Express.js.

Express.js is supported with the Google V8 engine with the help of which you would be able to get higher performance without any lag or error in the processing. It also supports the caching feature, so you would not have to re-execute the codes again and again. Moreover, it will help web pages to load faster than ever. You can also integrate several third-party applications and services with Express.js. I was taught to use Express when learning backend development. But I ended up not using it that much because I was able to use fully managed services in the cloud to handle a lot of those things for me. So, I could have an API gateway service to handle the API requests for me.

And then I would just need to write the code for what to do in response.

---

### 7. [READING] Introduction to Middleware & Routers Reading • 3 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/RGOT7/introduction-to-middleware-routers
- **Method:** `dom_reading_cml` | **Length:** 2316 chars

In this article, we will discuss the terms middleware and routes.

Middleware is software that sits between applications, databases, or services and allows those different technologies to communicate. It creates seamless interactions for the end user in a distributed system.

Express is a minimal and flexible Node.js web application framework used to build web servers, APIs, and middleware. Express is primarily used on the server side to handle HTTP requests, define routes, and manage middleware. It enables communication between the client (front end) and server (back end) through APIs.

Express applications commonly use JSON for data exchange and implement REST APIs to handle client-server communication. Older messaging frameworks may contain extensible markup language (XML) and simple object access protocols (SOAP) instead of JSON and REST APIs, respectively. The messaging framework provides a standardized way to handle data transfer among different applications.

A web server handles client requests, processes business logic, and interacts with databases. Middleware functions in Express help process requests and responses within this flow. The web server handles the business logic and routes the data from the database based on the request. A route is the part of the code that associates an HTTP request, such as GET, POST, or DELETE, with a URL and the function that gets called that handles that URL. Routing is used in web development to split an application’s user interface based on rules identified by the browser’s URL.

Router functions are called “middleware” collectively. Middleware is responsible for responding to an HTTP request or calling another function in the middleware chain. Express handles router functions through the Router class, such as Router.get(). As the name suggests, Router.get() handles HTTP GET requests. Other Router functions include Router.post(), Router.put(), Router.delete() in mostly the same way. These methods take two arguments, a URL path and a callback function.

In addition to routing, middleware is also responsible for providing secure connections among services by encrypting and decrypting data, managing application loads by distributing traffic to different servers, and sorting or filtering data before the data is returned to the client.

---

### 8. [VIDEO TRANSCRIPT] Routing, Middleware, and Templating Video • 7 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/Dufbu/routing-middleware-and-templating
- **Method:** `dom_transcript` | **Length:** 6285 chars

Welcome to Routing, Middleware, and Templating. After watching this video, you will be able to: Explain routing in Express. Describe middleware and how it is used. And explain template rendering in Express. Routing is an important aspect of server-side scripting. Requests to different routes to the same server must be handled by the server. Requests can be GET, POST, PUT, or DELETE.

The server must handle each request to each of the routes or return appropriate error messages. Routing can be handled at application level or at router level. Here, you are handling each method on each route with separate methods at the application level. This is simple when there are fewer end points or routes. This App.get handles GET queries to end point /user/about/id. This App.post handles POST queries to the same end point. This App.get handles GET queries to end point /item/about/id.

And this App.post also handles POST queries to end point /item/about/id. When there are many routes to handle, code maintenance is better with routers. A router by itself is used for branching query handling and routing each query differently. Here, you are defining two routers. One is for an item and the other is for a user. All the requests that come with the item are handled by the itemRouter. The /item/about and /item/detail routes are handled.

All the requests that come with /user are handled by userRouter. Here, /user/about and /user/detail routes are handled. Depending on the uniform resource locator (URL), the response changes. Middleware includes functions that have access to the request and response objects and the next function. The next parameter determines what is done after the function is executed. An Express application can have more than one middleware and they can be chained to each other. Middleware is categorized based on purpose, use, and source.

Five types of middleware are application level, router level, error handling, built-in, and third party, Middleware is useful for activities like parsing requests, adding authentication, and handling errors. Application-level middleware is bound to the application using app.use. All the client requests to this server application are routed through this middleware. This routing is useful for activities like authentication and checking session information. Here, you are defining middleware that will check the password that is passed. If the password is equal to pwd123, then it will log the time and chain to the next logical action which is processing the request. If it is not, then the response status will be set to 402 and a message will appear saying that the user cannot log in.

Consider application-level middleware as a gatekeeper. No request to the application server can go past it. Router-level middleware is not bound to the application. Instead, it is bound to an instance of express.Router(). You can use a specific middleware for a specific route instead of having all requests going through the same middleware. Here, if the route is /user, then you want the request to go through the user router and if the route is /item, then you want it to go through the item router. You define the two routers, define the middleware function that the routers will use and what happens next, and then you bind the application routes to each router.

The response will vary depending on the request route in the client side. Error-handling middleware can be bound to either the entire application or to specific routers. Error-handling middleware always takes four arguments, which are error, request, response, and the next function that it needs to be chained to. Even if you don’t use the next parameter, you still have to define it in the method signature. This is an example of application-level error-handling middleware. If the user id 1 is accessed, then an error is thrown saying that it is the admin user. This error is handled by the middleware, which returns a response with a 500 status code.

For all other users, the request is seamlessly processed and a Hello User Id message is displayed. Built-in middleware can be bound to either the entire application or to specific routers. Built-in middleware is useful for activities such as rendering hypertext markup language (HTML) pages from the server, parsing JavaScript Object Notation (JSON) input from the front end, and parsing cookies. This is an example of static middleware that is used to render static HTML pages and the images from the server side. Here at application level, you are defining that static files can be rendered from the cad220_staticfiles directory. On the right you see the HTML being rendered from that directory. Notice that the URL has only the server address and the port number followed by the filename.

You can also define your own middleware or use third-party middleware, which can be made available through npm install. Because Node.js is open source, there are plenty available to install and use. Creating middleware is simple. It is a function that takes three parameters, which are request, response, and next. You can define a method that takes these three parameters and then bind it with app.use or router.use. The order in which the middleware is chained depends on the order in which the .use method is used to bind them. Here, you are creating middleware named myLogger and making the application use it.

The output rendered includes the time the request is received. Template rendering is the ability of the server to fill in dynamic content in the HTML template. This example uses express-react-views, which renders React components from the server. You set the view engine property, which is responsible for creating HTML from your views. Views are JSX code. The views are in a directory named myviews. The view engine will look for a JSX file named index in the myviews directory and pass the property name to it.

The output rendered will have the name of the user. This example shows the output for two users. In this video you learned that: Routers are used for branching query handling. Five types of middleware are application level, router level, error handling, built-in, and third party. Template rendering is the ability of the server to fill in dynamic content in the HTML template.

---

### 9. [VIDEO TRANSCRIPT] Authentication and Authorization in Node.js Video • 7 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/s73yk/authentication-and-authorization-in-node-js
- **Method:** `dom_transcript` | **Length:** 6805 chars

Welcome to this video on exploring authentication and authorization in Node.js. After watching this video, you will be able to Describe the need for authentication and how it validates a user's identity in Node.js Explain session-based authentication, including the creation, storage, and destruction of session IDs, and contrast token-based authentication and passwordless authentication, highlighting the use of JWTs and public and private key pairs. Imagine designing an e-commerce platform with Node.js, where users sign up and make purchases. However, you realize that the platform's authentication and authorization mechanisms are not robust enough, as user data may be at risk, making unauthorized access possible. This could lead to severe consequences, such as data breaches and loss of customers' trust. How can you avoid this situation? Learning about the concepts of authentication and authorization in Node.js is essential for securing user authentication, safeguarding sensitive data, and enhancing your app's reliability and user satisfaction.

Let's start by looking at authentication. Authentication refers to verifying who a person claims to be by checking their credentials. This is a fundamental aspect of securing applications, so that only authorized users have access to certain parts of the system. The application's backend is responsible for handling this verification process. Now, let's learn about the three popular authentication methods. Three popular authentication methods in Node.js include session-based, token-based, passwordless. Let's explore each of these in detail.

Session-based authentication is one of the earliest methods. Here's how it works. Log in with your credentials, which are validated against a database that stores the accessible resources based on the session ID. If valid, the server creates a unique encrypted session ID, which is stored in the database and as a browser cookie. When you log out or after a certain period, the session ID is destroyed, logging you out from both the browser and the database. Now let's explore a code snippet demonstrating session-based authentication in an Express application. In this example, the code performs the following functions.

It sets up an Express application and configures session management. Next, the code configures the express-session middleware, with a secret key for encrypting the session data, and other options like resave and save uninitialized. Then, it handles post requests for your login. If the provided username and passwords match, it stores your username in the session. Finally, the code checks if you are authenticated as a user. If authenticated, the application welcomes you, otherwise prompts you to log in. Now that you've learned about session-based authentication, let's move on to token-based security.

Token-based security includes two key concepts, authentication and authorization. Authentication is when you provide credentials and receive a token that validates your user credentials. Authorization is when you use the token to access resources, ensuring the resource server knows which resources you're permitted to access. Tokens, often in the form of JSON Web Tokens, JWT, consist of three parts. Header contains the token type and the algorithm used. Payload includes user attributes, known as claims, such as permissions and expiration times. Signature ensures the token's integrity during transit.

JWT, pronounced jot and written as JWT, is an internet standard for creating signed JSON payload data. In token-based authentication, your browser requests access to a web application. The authentication server responds with an ID token, stored as a secure cookie by the client, which is sent to the web server providing authentication. Now that you understand token-based authentication, let's move on to token-based authorization. Token-based authorization occurs when a web application requests access to a protected resource, such as an API. During this process, the user authenticates with the authorization server, which then generates an access token that is sent back to the client and stored. With each HTTP request, the token is passed to the resource API server, carrying embedded permission details, eliminating the need to query the authorization server.

Even if stolen, the token doesn't expose credentials due to encryption. Next, you'll see a token-based authentication example in an Express application. In this example, the code performs the following functions. First, the code configures an Express application with middleware, like BodyParser, to parse JSON requests. Then, the code handles post requests for user login. If credentials are valid, it generates a JWT or token containing the username, checks for a JWT in the authorization header of incoming requests. If present, the code verifies the token and extracts the username to grant access.

Next, let's look at passwordless authentication. Passwordless authentication eliminates the need for traditional passwords, using methods like biometrics, magic links sent to your email, or one-time passcodes sent to your mobile device. This approach is often used in password recovery systems. It relies on public key and private key encryption. When you register, your device generates a private-public key pair linked to your identity. The public key is used to encrypt data and is accessible to anyone, while the private key, securely stored on your device, decrypts data. During sign-in, the app creates a login challenge, encrypts it with the public key, and decrypts it with your private key to authorize access.

Next, you'll see how passwordless authentication is implemented in an Express application. In this example, the code performs the following functions. The code sets up an Express application with middleware to parse JSON requests or body parser. Then, it handles post requests, where users provide their email to request access. And then the code generates a six-digit verification code and stores it in an in-memory object. Next, the code handles post requests to verify the received code against the stored code. If matched, the code grants access to the user.

Otherwise, it denies access. In this video, you learned that authentication confirms your identity using credentials, by validating who you claim to be. Session-based authentication uses credentials to create a session ID stored in a database and the client's browser. When you log out, the session ID is destroyed. Token-based authentication uses access tokens, often JWTs, that get passed between server and client with the data that is passed between the two. Passwordless authentication uses public-private key pairs to encrypt and decrypt data passed between client and server without any password.

---

### 10. [READING] Welcome to Authentication and Authorization in Node.js Reading • 20 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/SlCK9/welcome-to-authentication-and-authorization-in-node-js
- **Method:** `dom_reading_cml` | **Length:** 11925 chars

### Objectives

In this reading, you will be able to:

- Define authentication
- Explain session-based, token-based, and passwordless authentication
- Compare and contrast different types of authentications, including session-based, token-based, and passwordless

### Authentication

The authentication process confirms a user's identity using credentials by validating who they claim to be. Authentication assures an application's security by guaranteeing that only those with valid credentials can access the system. Authentication is the responsibility of an application's backend.

Three popular authentication methods in Node.js include:

- Session-based
- Token-based
- Passwordless

Let's explain a little bit about each of these methods and compare them.

### Session-based

Session-based authentication is the oldest form of authentication technology. Typically, the flow of a session is as follows:

- The user uses their credentials to log in.
- The login credentials are verified against the credentials in a database. The database is responsible for storing which resources can be accessed based on the session ID.
- The server creates a session with a session ID that is a unique encrypted string. The session ID is stored in the database.
- The session ID is also stored in the browser as a cookie.
- When the user logs out or a specified amount of time has passed, the session ID is destroyed on both the browser and the database.

Below is a code snippet demonstrating session-based authentication in an Express application:

123456789101112131415161718192021222324252627282930313233343536const express = require('express');const session = require('express-session');const app = express(); // Middleware to set up session managementapp.use(session({ secret: 'secret-key', // Replace with a strong secret key resave: false, // Whether to save the session data if there were no modifications saveUninitialized: true, // Whether to save new but not modified sessions cookie: { secure: false } // Set to true in production with HTTPS})); // POST endpoint for handling loginapp.post('/login', (req, res) => { const { username, password } = req.body;  // Simulated user authentication (replace with actual logic) if (username === 'user' && password === 'password') {  req.session.user = username; // Store user information in session  res.send('Logged in successfully'); } else {  res.send('Invalid credentials'); }}); // GET endpoint for accessing dashboardapp.get('/dashboard', (req, res) => { if (req.session.user) {  res.send(`Welcome ${req.session.user}`); // Display welcome message with user's name } else {  res.send('Please log in first'); }}); // Start the server on port 3000app.listen(3000, () => console.log('Server running on port 3000'));Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Explanation:

Express Setup: This code sets up an Express application and configures session management using express-session. Session Configuration: Express-session middleware is configured with a secret key (secret: 'secret-key') for encrypting the session data, and other options like resave and saveUninitialized. Login Endpoint (/login): Handles POST requests for user login. If the provided username and password match, it stores the username (req.session.user) in the session. Dashboard Endpoint (/dashboard): Checks if the user is authenticated (req.session.user exists). If authenticated, it welcomes the user; otherwise, it prompts them to log in.

### Token-based

Token-based security entails two parts: authentication and authorization. Authentication is the process of providing credentials and obtaining a token that proves the user's credentials. Authorization refers to the process of using that token so the resource server knows which resources the user should have access to.

#### Token-based authentication

Token-based authentication uses access tokens to validate users. An access token is a small piece of code that contains information about the user, their permissions, groups, and expirations that get passed from a server to the client. An ID token is an artifact that proves that the user has been authenticated.

The token contains three parts: the header, the payload, and the signature. The header contains information about the type of token and the algorithm used to create it. The payload contains user attributes, called claims, such as permissions, groups, and expirations. The signature verifies the token's integrity, meaning that the token hasn't changed during transit. A JSON web token, pronounced "jot" but spelled JWT, is an internet standard for creating encrypted payload data in JSON format.

A user's browser makes a call to an authentication server and gets access to a web application. The authentication server then passes back an ID token, which is stored by the client as an encrypted cookie. The ID token is then passed to the app on the web server as proof that the user has been authenticated.

#### Token-based authorization

This flowchart shows the workflow of a token through the authorization process.

The authorization process gets executed when the web application wants to access a resource, for example, an API that is protected from unauthorized access. The user authenticates against the Authorization server. The Authorization server creates an access token (note that the ID token and access token are two separate objects) and sends the access token back to the client, where the access token is stored. Then, when the user makes requests or resources, the token is passed to the resource, also called an API server. The token gets passed with every HTTP request. The token contains embedded information about the user's permissions without the need to access those permissions from the authorization server. Even if the token is stolen, the hacker doesn't have access to the user's credentials because the token is encrypted.

Below is a code snippet demonstrating Token-based Authentication in an Express application:

12345678910111213141516171819202122232425262728293031323334353637383940const express = require('express');const jwt = require('jsonwebtoken');const bodyParser = require('body-parser'); const app = express();app.use(bodyParser.json()); const secretKey = 'your-secret-key'; // Replace with a strong secret key // POST endpoint for user login and JWT generationapp.post('/login', (req, res) => { const { username, password } = req.body;  // Simulated user authentication if (username === 'user' && password === 'password') {   // Generate JWT with username payload  const token = jwt.sign({ username }, secretKey, { expiresIn: '1h' });  res.json({ token }); // Send token as JSON response  } else {  res.send('Invalid credentials'); }}); // GET endpoint to access protected resource (dashboard)app.get('/dashboard', (req, res) => {  // Get token from Authorization header const token = req.headers['authorization'];  if (token) {   // Verify JWT token  jwt.verify(token, secretKey, (err, decoded) => {   if (err) {    res.send('Invalid token');   } else {    // Token is valid, send welcome message with username    res.send(`Welcome ${decoded.username}`);Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Explanation:

Express Setup: Configures an Express application with middleware like body-parser to parse JSON requests. JWT Generation (/login): Handles POST requests for user login. If credentials are valid, it generates a JWT (token) containing the username (jwt.sign({ username }, secretKey, { expiresIn: '1h' })). JWT Verification (/dashboard): Checks for a JWT in the Authorization header of incoming requests (const token = req.headers['authorization']). If present, it verifies the token (jwt.verify(token, secretKey)) and extracts the username (decoded.username) to grant access.

### Passwordless

With passwordless authentication, the user does not need login credentials, but rather, they gain access to the system by demonstrating they possess a factor that proves their identity. Common factors include biometrics such as a fingerprint, a "magic link" sent to their email address, or a one-time passcode sent to a mobile device. Password recovery systems now commonly use passwordless authentication.

Passwordless authentication is achieved using Public Key and Private Key Encryption. In this method, when a user registers for the app, the user's device generates a private key/public key pair that utilizes a factor that proves their identity, as noted above.

The public key is used to encrypt messages, and the private key is used to decrypt them. The private key is stored on the user's device, and the public key is stored with the application and registered with a registration service.

Anyone may access the public key, but the private key is only known to the client. When the user signs into the application, the application generates a login challenge, such as requesting biometrics, sending a "magic link," or sending a special code via SMS, encrypting it with the public key. The private key allows the message to be decrypted. The app then verifies the sign-in challenge and accepts the response to authorize the user.

Below is a code snippet demonstrating Passwordless-based Authentication in an Express application:

12345678910111213141516171819202122232425262728293031323334353637383940const express = require('express');const bodyParser = require('body-parser');const nodemailer = require('nodemailer'); const app = express();app.use(bodyParser.json()); const users = {}; // In-memory storage for demo purposes // Endpoint to request access and send verification code via emailapp.post('/request-access', (req, res) => { const { email } = req.body;  // Generate a 6-digit verification code const code = Math.floor(100000 + Math.random() * 900000).toString();  // Store the code in memory (users object) users[email] = code;  // Simulated email sending (for demonstration) console.log(`Sending code ${code} to ${email}`); res.send('Code sent to your email');}); // Endpoint to verify the received codeapp.post('/verify-code', (req, res) => { const { email, code } = req.body;  // Compare the received code with stored code for the email if (users[email] === code) {  // Code matches, access granted  res.send('Access granted'); } else {  // Code does not match, access denied  res.send('Invalid code'); }}); // Start the Express serverapp.listen(3000, () => console.log('Server running on port 3000'));Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Explanation:

Express Setup: Sets up an Express application with middleware to parse JSON requests (body-parser). Request Access (/request-access): Handles POST requests where users provide their email to request access. Generates a 6-digit verification code (code) and stores it in an in-memory object (users[email] = code). Verify Code (/verify-code): Handles POST requests to verify the received code against the stored code (if (users[email] === code)). If matched, it grants access; otherwise, it denies access.

### Summary

In this reading, you learned that:

- Authentication is the process of confirming a user's identity using credentials by validating who they claim to be.
- Session-based authentication uses credentials to create a session ID stored in a database and the client's browser. When the user logs out, the session ID is destroyed.
- Token-based authentication uses access tokens, often JWTs, that get passed between server and client with the data that is passed between the two.
- Passwordless authentication uses public/private key pairs to encrypt and decrypt data passed between client and server without the need for a password.

### Author(s)

Rajashree Patil 
Sapthashree K S

---

### 11. [VIDEO TRANSCRIPT] Authentication in Node.js Video • 7 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/7SDmH/authentication-in-node-js
- **Method:** `dom_transcript` | **Length:** 6399 chars

Welcome to Authentication in Node.js. After watching this video, you will be able to Discuss advantages of token-based authentication in Node.js And implement token-based authentication and authorization in Node.js So, authentication is the process of confirming a user's identity by obtaining credentials And using those credentials to validate their identity. Authentication is meant to identify users and provide access rights and contents depending on their ID. As discussed in another video, authentication can be achieved using the following approaches Session-based authentication, token-based authentication, and password-less authentication. Token-based authentication is the most popular approach to implementing authentication in Node.js And the following are some of the advantages of using token-based authentication. Token-based authentication is more scalable as the token only needs to be stored on the client side. Also, since the server only needs to verify the token along with the user information, it is easier to handle multiple users.

Token-based authentication offers flexibility as they can be used across multiple servers And they can offer authentication for diverse websites and applications at once. And JWT used in token-based authentication can be signed and encrypted Which means they cannot be tampered with and also cannot be read without the private encryption key. Now let's set up an ExpressJS API server that provides access to employee information based on their usage rights. The application will have two APIs, each with its own endpoints. We will first use a POST API for logging in that returns a web token to sign in by sending the username and password in the request body. The call to this API endpoint should be made from the web server that hosts the application's front end. And a second GET API will be the resource endpoint to get employee information that only authenticated users can access.

Let's consider what this code might look like. This code creates a web server module by calling the express function and assigning it to the constant myApp. The myapp.get function creates a GET API endpoint for the employee's API And any call to this endpoint currently returns an HTTP status code of 401. And 401 means not authorized. With the message, please log in to access this resource. The server also listens on port 5000 for any HTTP calls to the server and logs the message API server is localhost colon 5000 to the console. To execute the API first, save the file and name it apiServer.js.

Now run the command node apiServer.js. To verify that the secure endpoint cannot be accessed unless the user is authorized, run this curl command on the screen. In the output, you should see the message, please log in to access this resource per your code. In the next part of the code, we allow users to sign in and send back a verified generated token as long as the username and password are correct. Generally, usernames and passwords are stored in the database. However, since setting up a database connection is out of the scope of this code demo, we will hard code user and password as the username and password in this code example. Now, to generate the verified JWT, use the jsonwebtoken npm package.

Install it using the command npm install option save jsonwebtoken. At the start, you will need to require the module jsonwebtoken from the jsonwebtoken package. This module is used to generate the JWT using the JWT secret. A constant is then declared to store the JWT secret. The myapp.use method enables returning a JSON response by the API methods. To display the code in this video, we are hard coding the username and password. Please note, however, that the JWT secret should always be generated using a password generator and stored in the config file as an environment variable and not hard coded in the API as shown here.

The username and password from the request body is then compared with the values fetched from the database. And once the username and password match, the JWT is generated using the jsonwebtoken.sign function by including the username and the JWT secret as parameters and is returned as a JSON response from the sign-in API. Now, if the username and password match fails, then an HTTP status code of 401 is returned with the message, invalid username and or password. Next, we define the getAPI method with the employees endpoint. The token fetched from the call to the sign-in API is passed in the authorization header. The getAPI employees is updated to read the authorization header from the incoming API request using the request.header function. And if no header is found within the request, then a status code of 401 is sent back by the getAPI with the message, no token.

The authorization header always starts with the string, bearer, at the start of the header, and therefore, this token is also known as bearer token. The fetched JWT is verified using the function jsonwebtoken.verify by passing the fetched token and the JWT secret. And the value returned by this function is then used to verify if the user property matches with the username fetched from the database. And if that match happens, then the user is authenticated and is provided access to the employees API. The API then returns the 200 success status code with the message, access successful to employee endpoint. Now, if the verification fails, then the 401 unauthorized status code is sent back to the client with the message, please log in to access this resource. Lastly, write a listener function that listens for the response on port 5000, then log the phrase, API server is localhost 5000 to the console log.

Recall that the code you just wrote has a sign-in API endpoint that reads the username and password from the request body and then validates it against the username and password stored in the database. If there is a match, it then uses the jsonwebtoken.sign method to generate the token and send it back in the response. In this video, you learned that The advantages of token-based authentication include scalability, flexibility, and security. The POST API is used during authentication to log a user into an application. The GET API is used in authorization to determine which resources a user can access. And a JSON web token is used to authenticate a user and authorize which resources they have access to use.

---

### 12. [READING] HTTP Methods and Rest APIs Reading • 20 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/eihSy/http-methods-and-rest-apis
- **Method:** `dom_reading_cml` | **Length:** 13485 chars

### Objectives

After reading this document, you should be able to:

- Define terms related to HTTP methods
- Explain guidelines and best practices for writing REST APIs

The internet relies on a client-server architecture. The end-user interfaces with the client, while the servers house the services that operate the applications, the business logic, and the data. Clients communicate with the servers to achieve desired functionality for the end user. Data is transferred between client and server using hypertext transfer protocol, more commonly known as HTTP. This communication usually happens via APIs. In 2000, a set of guidelines for writing these APIs for a client-server architecture was developed called REST APIs.

The acronym "REST" stands for REpresentational State Transfer. Before explaining this term in more detail, let's discuss HTTP methods and some terminology first.

In a client/server architecture, the applications are composed of one or more services that reside on the servers. These services contain resources. The client makes a request for a resource via a request object using a route that has an endpoint within the service. The application sends a response object back in response to the client to honor that request.

A request object contains three parts, a URL, a request header, and a request body. The server uses the URL to identify the service and the endpoint within the service being acted upon. The URL contains four parts: a protocol, a hostname, a path, and a query string. The request header contains metadata about the resource of the requesting client, such as the user agent, host, content type, content length, and what type of data the client should expect in the response.

The server responds with a response object consisting of a header, a body, and a status code. The response object body often contains a JSON payload to provide the data back to the client.

There are a number of HTTP methods that can be used in the REST API that allow interaction between the client and a service. The most common methods are GET, POST, PUT, DELETE, and PATCH.

The name of the method describes what happens to the resource when the method is applied. PUT and DELETE methods result in idempotent data if the same API method is called multiple times.

HTTP has three ways to pass parameters: the URL path parameter, the URL query parameter, and the header parameter. The path and query parameters are passed as part of the URL, but the header parameter is passed by the browser directly to the service.

When the service completes a request, it returns a response. An HTTP status code should be part of that response. The HTTP status code indicates whether the response has been completed or not. Response code categories are shown in the following table.

#### Status Code Categories

| Status Code Range | Meaning |
| --- | --- |
| 200-299 | Everything is OK |
| 300-399 | Resource has moved |
| 400-499 | Client-side error |
| 500-599 | Server-side error |

As mentioned earlier, REST is a set of guidelines. There are five requirements for an API to be considered RESTful, plus one optional criterion:

- The API leverages a client-server architecture made up of resources that are managed and delivered via HTTP.
- Communication between client and server is stateless.
- Data is cacheable to improve performance on the client side.
- The interface is transferred in a standard format such that the requested resources stored on the server are separated from the representation sent to the client. The representation sent to the client contains sufficient data so that the client can manipulate the representation.
- Requests and responses communicate through different layers, such as middleware. The client and server often do not communicate directly with each other.
- (Optional) Resources are usually static but can also contain executable code. The code should only be executed when the client requests it.

When the client makes a request, it also must pass information about its state to the server. Every communication between the client and server should contain all the information needed to perform the request. The client, not the service, maintains the state. Each request must contain the requisite information so the server understands the request. So, for example, if the user is viewing a database record and that record needs to be updated, the client must also send which record needs updating. The server doesn't know which record is currently being viewed.

An @app.route() method is used when defining a RESTful service. This method takes two parameters: the route from the URL to the service being acted upon and an optional HTTP method parameter such as POST, GET, etc. The route parameter can include variables, such as <username>. The root of a route is represented by '/'. For example, if you want the route to be www.mywebsite.com/accounts, you only need to specify '/accounts' as the route parameter in the @app.route() function.

REST APIs have the following characteristics:

- Resource-based; that is, they describe sets of resources
- Only contain nouns, not verbs
- Use singular nouns when referring to a singular resource or plural nouns when referring to a collection of resources
- Always identified by URLs

#### NOT RESTful APIs vs RESTful equivalents

| NOT RESTful APIs | RESTful equivalents |
| --- | --- |
| GET http://api.myapp.com/getUser/123 | GET http://api.myapp.com/users/123 |
| POST http://api.myapp.com/addUser | POST http://api.myapp.com/users |
| GET http://api.myapp.com/removeUser/123 | DELETE http://api.myapp.com/users/123 |

#### URL format guidelines

- Should use a slash '/' to denote a hierarchical relationship in the directory structure
- Should avoid using a trailing slash, e.g., /resource/
- Should use hyphens, not camel case, e.g., /my-resource, not /myResource
- Should not use an underscore '_' in the URL, e.g., /my-resource, not /my_resource
- Should use lowercase
- Should not use a period '.' in a URL
- May contain multiple subordinate resources and IDs in the URL, e.g., GET /resource/{id}/subordinate/{id}

#### Terms and Definitions

| Term | Description |
| --- | --- |
| 1.Service | A software component that makes up part of an application and serves a specific purpose. Generally, a service takes input from a client or another service and produces an output. |
| 2.HTTP | The protocol used by a client-server architecture on the internet for fetching or exchanging resources data. |
| 3.API | An Application Programming Interface is a set of definitions and protocols that allow two services to communicate with each other. The API requests data that can be exchanged between a resource and the results that are returned from that resource. |
| 4.REST | A set of architectural guidelines that describe how to write an interface (API) between two components, usually a client and server, that describe how these components communicate with each other. REST stands for REpresentational State Transfer. REST describes a standard way to identify and manipulate resources. REST ensures the messages passed between the client and server are self-descriptive and define how the client interacts with the server to access resources on the server. |
| 5.Resource | A resource is the fundamental concept of a RESTful API. It is an object that has a defined type, associated data, relationships to other resources, and a set of methods that can operate on it. A resource is commonly defined in JSON format but can also be XML. |
| 6.Request | A request is made by a client to a host on a server to access a resource. The client uses parts of a URL to determine the information needed from the resource. Most common request methods include GET, POST, PUT, PATCH, and DELETE but also include HEAD, CONNECT, OPTIONS, TRACE, and PATCH. |
| 7.Request Object | Contains the HTTP request data. It contains three parts: a URL, a header, and a body. |
| 8.Route | The combination of an HTTP method and the path to the resource from the root of the path. |
| 9.Endpoint | The location of the resource specified by a REST API that is being accessed on the server. It is usually identified through the URL in the HTTP method of the API. |
| 10.Response Object | Contains the HTTP response data in response to a request. It contains a header, a body, and a status. |
| 11.Response | A response is made by a server and sent to a client to either provide the client with the requested resource, tell the client the requested action has been completed, or let the client know there has been an error processing the request. |
| 12.URL | A "Uniform Resource Identifier" is used interchangeably with the term URL. They are part of a RESTful API that locates the endpoint of the requested resource and contains the data about how that endpoint should be manipulated. The client issues an HTTP request using the URI/URL to manipulate the resource. They should consist of four parts: the hostname, the path, the header, and a query string. |
| 13.Request Header | Information passed to the server about the retrieved resource or the requesting client. Examples include: Method with endpoint: POST /car-reviews User-agent: The type of browser the client is using. Host: A computer on a network that communicates with other hosts. ContentType: The media type of a resource such as text, audio, or an image. Content length: The number of bytes of data being sent in a response. Accept-Encoding: Expected return data format, e.g., application/json Connection information |
| 14.Request Body | Provides the data being passed to the server. |
| 15.Protocol | Tells the service how the data is to be transferred between the server and the client. |
| 16.Hostname | The name of a device on a network, also often called the site name. |
| 17.Path | The path identifies the location of the resource in the service and its endpoint. For example: https://www.customerservice/customers/{customer_id} |
| 18.Query String | The part of a URL that contains the query. |
| 19.User-agent | The type of browser the client is using. |
| 20.Host | A computer on a network that communicates with other hosts. |
| 21.Content type | The media type of a resource such as text, audio, or an image. |
| 22.Content length | The number of bytes of data being sent in a response. |
| 23.Response Header | Contains metadata about the response, such as a time stamp, caching control, security info, content type, and the number of bytes in the response body. |
| 24.Response Body | The data from the requested resource is sent back to the client. |
| 25.Response Status | The return code that communicates the result of the request’s status to the client. |
| 26.JSON | "JavaScript Object Notation" is a format for storing and transporting data, usually as a way to send data from a service on a server to the client. It consists of key-value pairs and is self-describing. The format of JSON data is the same as the code for creating JavaScript objects, making it easy to convert this data into JavaScript objects but can be written in any programming language. JSON has three data types: scalars (numbers, strings, Booleans, null), arrays, and objects. |
| 27.Payload | The payload is the data in the body of a response being transported from a server to the client due to an API request. |
| 28.GET | The GET method is used as a request that retrieves a representation of a resource. GET() should never modify a resource and only return a representation of the requested resource. |
| 29.POST | HTTP method that sends data to the server to create a resource and should return 201_CREATED status code. |
| 30.PUT | HTTP method that updates a resource or replaces an existing one. Calling PUT multiple times in a row does not have side effects, whereas POST does. It should return a 200_OK code if the resource exists and can be updated or return a 404_NOT_FOUND code if the resource doesn't exist. |
| 31.DELETE | HTTP method that deletes a resource and returns 204_NO_CONTENT if the resource exists and can be deleted by the server or if the resource cannot be found, which means it has already been deleted. |
| 32.PATCH | HTTP method that applies partial modifications to a resource. |
| 33.Idempotent | Describes an element of a set that remains unchanged when making multiple identical requests. PUT and DELETE methods result in idempotent data if the same API method is called multiple times. |
| 34.URL Path Parameter | Passed into the operation by the client as a variable in the URL's path. |
| 35.URL Query Parameter | Contains key-value pairs, usually in JSON format, and are separated from the path by a '?'. If there are multiple key-value pairs, they should be separated by an '&'. The query can be used to pass in a filter to be applied to the results that are returned by the operation. |
| 36.Header Parameter | Contains additional metadata about the query, such as identifying the client that is calling the operation. |
| 37.Stateless | All requests from a client to a server for resources happen in isolation from each other. The server is unaware of the application's state on the client, so this information needs to be passed with every request. |
| 38.Cacheable | The ability to store data on the client so that data can be used in a future request. |
| 39.Middleware | Software that sits between applications, databases, or services and allows those different technologies to communicate. |

---

### 13. [VIDEO TRANSCRIPT] Express Best Practices Video • 7 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/VNpHP/express-best-practices
- **Method:** `dom_transcript` | **Length:** 6104 chars

Welcome to Express Best Practices. After watching this video, you will be able to describe the folder structure conventions for building an Express application and APIs, and identify commonly followed best practices for building Express applications and APIs Web frameworks such as Ruby on Rails, .NET, and Django have required directory structures for storing files. Express does not require a pre-defined directory structure for its applications. However, defining a directory structure in advance is usually a good idea because as the size of the application grows, it can be difficult to maintain otherwise. The following folders are conventionally used to store files. Within the project folder it is suggested you use the following directories: Node modules, config, models, routes, views, and public.

Let’s describe the contents of each of these folders next. The node modules folder contains the application’s modules and packages. It is automatically created after running the “npm install” command. Node package manager, or npm, is discussed in another video. The “config” folder should contain configuration files such as database connection configuration, an environment variables file, and a credentials file containing the API keys for external services used by the application under development. The “models” folder contains the data models for the application. The files specify the type of datastore, such as relational or non-relational, and are defined by an object-relational mapping, or ORM, library.

The routes folder is used to specify all of the routes for the different entities in different files. It should have one file for each logical set of routes, such as one file for one type of resource. The views folder contains template files. A template dynamically writes HTML, CSS, and JavaScript to send back to the client. This approach makes it easier to generate user-specific user interfaces. The public folder will contain all static content such as images, CSS, and JavaScript. It is often helpful to have a sub-folder for each type of content.

The project folder should also contain a few files: app.js, routes.js, and package.json. The app.js file is the main configuration file for your application. A routes.js file is a central location to access all the routes in the application. This file requires or imports all the files in the routes folder and then exports them as a single module which is imported into the app.js file. This helps create a single point of entry for all the routes in the application. The package.json file contains the metadata used to manage the project’s dependencies. When building the folder structure for an API, it is quite similar to the project folder.

It does not need the views or the public folders. So, the folders should look something like this. Node modules, config, models, and routes. And then the following files app.js, routes.js, and package.json. When naming an API route, be sure to use a noun as a resource identifier. This table provides examples of HTTP routes for post, get, patch, and delete using the word employee in the route. These routes are examples if you are writing HTTP methods and API routes to modify employee data.

Be sure to use HTTP status codes correctly. A 200s code means everything is ok, a 300s code means the resource has been moved, a code in the 400s means there has been a client-side error, and a number in the 500s means something went wrong on the side of the API. Another best practice is to black-box test your node.js REST APIs. Black-box testing means you test the code without looking at its internal structure. The system is tested as a whole without mocked or stubbed dependencies. Mocha, which is a JavaScript test framework that runs on Node.js, contains a simple module called “supertest.” SuperTest provides you with a way to test HTTP requests, which is exactly what you need when you want to black-box test REST APIs.

And when your API needs to authenticate, it is best practice to use JSON Web Token, or JWT based stateless authentication. Since the REST APIs must be stateless, your authentication will need to be as well. Stateless authentication verifies users by supplying most of the session information, such as user properties, on the client side. The last best API practice we will emphasize here is creating proper API documentation. The whole purpose of an API is so that someone else can use them, so you want to provide appropriate documentation for your Node.js REST API. Two open-source projects that you might find useful to create documentation for your APIs are API Blueprint which can be found at api blueprint dot org, and Swagger, which can be found at swagger dot I O. There are a number of other helpful tips that are widely followed when building an express node.js application.

Regarding the use of node package manager, or NPM, use the npm init command when initializing a node.js project. When using the npm install command to install dependencies, use the dash save or the dash save dash dev attribute. This makes sure that if the application is moved to a different platform, the correct dependencies will be installed with it. Never push a node modules repository. And always use npm to install. Stick with the following capitalization conventions. Use all lowercase for file names, use camel case for variables, and npm modules are named in lowercase, separated by dashes.

And when using the “require” method for npm modules, use camel case. In this video, you learned that use a directory structure in both an Express.js application and an API that includes node modules config, models, and routes folders. Best practices when developing RESTful APIs include: Use a noun as a resource identifier, use HTTP status codes correctly, black-box test REST APIs using SuperTest, and use JWT-based stateless authentication. and include good documentation. Finally, other tips include: Following capitalization conventions, using npm as recommended, and using config files for variables and group similar functioning routes into their own files.

---

### 14. [READING] Module Summary Reading • 1 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/yaUdy/module-summary
- **Method:** `dom_reading_cml` | **Length:** 849 chars

Congratulations! You have completed this module. At this point in the course, you know:

- Developers rely on third-party packages to extend Node.js.
- You can use the npm application to manage Node.js packages in your Node.js framework installation.
- The MVC architecture style divides a back-end application into three parts: the model, the view, and the controller.
- REST API frameworks use HTTP methods to communicate with each other.
- Express abstracts low-level details.
- Routing can be handled at the application level or at the router level.
- Five types of middleware are application level, router level, error handling, built-in middleware, and third party.
- Template rendering is the ability of the server to fill in dynamic content.
- The npm jsonwebtoken package should be required in an Express application to authenticate a user.

---

### 15. [READING] Glossary: Express Web Application Framework Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/zELb9/glossary-express-web-application-framework
- **Method:** `dom_reading_cml` | **Length:** 6076 chars

Module 3 Glossary: Express Web Application Framework

| Term | Definition |
| --- | --- |
| Access Token | A small piece of code that contains information about the user, their permissions, groups, and expirations that get passed from a server to the client. |
| API Endpoint | The touchpoint where the API connects to the application it is communicating with. |
| Application-Level Middleware | Acts as a gatekeeper and is bound to the application. No request to the application server can go past it. |
| Authentication | The process of confirming a user’s identity using credentials by validating who they claim to be. Authentication assures an application’s security by guaranteeing that only those with valid credentials can access the system. |
| Authorization | In token-based authentication, it is the process that gets executed when a web application wants to access a protected resource. A user authenticates against an authorization server. |
| Built-In Middleware | Can be bound to either the entire application or to specific routers. Useful for activities such as rendering HTML pages from the server, parsing JSON input from the front end, and parsing cookies. |
| Controller | The layer in an MVC application regulates the flow of the data. It is responsible for processing the data supplied to it by the user and sends that data to the model for manipulation or storage. |
| Error-Handling Middleware | Can be bound to either the entire application or to specific routers. Error-handling middleware always takes four arguments: error, request, response, and the next function that it needs to be chained to. Even if you don’t use the next parameter, you still define it in the method signature. |
| Express.js | A web application framework based on the Node.js runtime environment, however, Express abstracts low-level details. |
| Framework | A framework is a skeleton on which an application is built for a specific environment. The framework is the fundamental structure that supports the application. |
| HTTP Headers | Additional information about and contained in an HTTP response or request. |
| HTTP Request | A method called by a client and sent to a server requesting access to a resource on the server. |
| HTTP Response | A method called by a server and sent to a client in response to an HTTP request. |
| ID Token | An artifact that proves that a user has been authenticated and contains information about authorized API routes. |
| JSON Payload | Data that is transferred in JSON format between the client and server in the header of an HTTP method. |
| JWT | A JSON Web token. An internet standard for creating encrypted payload data in JSON format. |
| Middleware | Includes functions that have access to the request and response objects and the next() function. |
| Model | The layer in an MVC application responsible for managing the data of the application. It interacts with the database and handles the data logic. |
| MVC | Short for “Model-View-Controller”. It is an architectural pattern that divides an application into three components: model, view, and controller. |
| Node Framework | A framework that works in conjunction with Node.js. A framework is a skeleton on which an application is built for a specific environment. The framework is the fundamental structure that supports the application. |
| npm | An application that manages Node.js packages in your Node.js framework installation. |
| Passwordless Authentication | A type of authentication that uses public/private key pairs to encrypt and decrypt data passed between client and server without the need for a password. |
| Private Key | In cryptography, it is a key that is known only to a specific client used to decrypt messages. Used in conjunction with a public key. |
| Public Key | In cryptography, it is a key that can be used by anyone to encrypt messages for a specific client. Used in conjunction with a private key. |
| REST | “Representational state transfer” is a set of guidelines for creating stateless client/server interfaces using HTTP methods. |
| REST API | An API used for communicating between clients and servers that conforms to REST architecture principles. |
| Route | The code that associates an HTTP request method and a URL. |
| Router-Level Middleware | Bound to a router and not bound to an application. You can use specific middleware for a specific route instead of having all requests go through the same middleware. Then you bind the application routes to each router. |
| Session-based Authentication | A type of authentication where a user provides login credentials that are verified against stored credentials in a database on a server. A session ID is provided to the client and stored in the browser as a cookie. |
| Statelessness | Implies that each HTTP request happens in isolation in relation to other requests. The state of the client is not stored on the server; the state is passed to the server by the client for each request. |
| Template Rendering | The ability of the server to fill in dynamic content in an HTML template. |
| Token | Contains three parts, the header, the payload, and the signature. The header contains information about the type of token and the algorithm used to create it. The payload contains user attributes, called claims, such as permissions, groups, and expirations. The signature verifies the token’s integrity, meaning that the token hasn’t changed during transit. |
| Token-based Authentication | A type of authentication that uses access tokens, often JWTs, which get passed between server and client with the data that is passed between the two. |
| TypeScript | A language that builds on top of JavaScript and provides type safety which assists with the development of large-scale applications by reducing the complexity of component development in JavaScript. |
| View | The layer in an MVC application responsible for rendering the presentation of the data that is passed to it by the model. |
| xml2js | Node.js package to parse a string of XML elements into a JavaScript object. |

---

### 16. [READING] Cheatsheet - Express Web Application Framework Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/GNwvB/cheatsheet-express-web-application-framework
- **Method:** `dom_reading_cml` | **Length:** 5208 chars

Module 3 Cheat Sheet: Express Web Application Framework

| Package/Method | Description | Code Example |
| --- | --- | --- |
| Dependencies in package.json | A dependency of express version between 4.0 to 5.0 will be declared as: | plaintext<br>"dependencies":{"express":"4.x"}<br> |
| new express() | Creates an express object which acts as a server application. | javascript<br>const express = require("express");<br>const app = new express();<br> |
| express.listen() | The listen method is invoked on the express object with the port number on which the server listens. The function is executed when the server starts listening. | javascript<br>app.listen(3333, () => {<br> console.log("Listening at http://localhost:3333")<br>})<br> |
| express.get(); | This method is meant to serve the retrieve requests to the server. The get() method is to be implemented with two parameters; the first parameter defining the endpoint and the second parameter is a function taking the request-handler and response-handler. | javascript<br>// handles GET queries to end point /user/about/id.<br>app.get("user/about/:id", (req,res)=>{<br> res.send("Response about user " +req.params.id)<br>})<br> |
| express.post(); | This method is meant to serve the create requests to the server. The post() method is to be implemented with two parameters: the first parameter defines the end-point and the second parameter is a function taking the request-handler and response-handler. | javascript<br>// handles POST queries to the same end point.<br>app.post("user/about/:id", (req,res)=>{<br> res.send("Response about user " +req.params.id)<br>})<br> |
| express.use() | This method takes middleware as a parameter. Middleware acts as a gatekeeper in the same order that it is used, before the request reaches the get() and post() handlers. The order in which the middleware is chained depends on the order in which the .use() method is used to bind them. The middleware myLogger() function takes three parameters, which are request, response, and next. You can define a method that takes these three parameters and then bind it with express.use() or router.use(). Here, you are creating middleware named myLogger and making the application use it. The output rendered includes the time the request is received. | javascript<br>const express = require("express");<br>const app = new express();<br><br>function myLogger(req, res, next){<br> req.timeReceived = Date();<br> next();<br>}<br><br>app.use(myLogger);<br><br>app.get("/", (req, res)=>{<br> res.send("Request received at "+req.timeReceived+" is a success!")<br>})<br> |
| express.Router() | Router-level middleware is not bound to the application. Instead, it is bound to an instance of express.Router(). You can use specific middleware for a specific route instead of having all requests going through the same middleware. Here, the route is /user and you want the request to go through the user router. Define the router, define the middleware function that the router will use and what happens next, and then you bind the application route to the router. | javascript<br>const express = require("express");<br>const app = new express();<br><br>let userRouter = express.Router();<br>let itemRouter = express.Router();<br><br>userRouter.use(function (req, res, next){<br> console.log("User query time:", Date());<br> next();<br>})<br><br>userRouter.get("/:id", function (req, res, next) {<br> res.send("User "+req.params.id+ " last successful login "+Date())<br>})<br><br>app.use("/user", userRouter);<br><br>app.listen(3333, () => {<br> console.log("Listening at http://localhost:3333")<br>})<br> |
| express.static() | This is an example of static middleware that is used to render static HTML pages and the images from the server side. At the application level, the static files can be rendered from the cad220_staticfiles directory. Notice that the URL has only the server address and the port number followed by the filename. | javascript<br>const express = require("express");<br>const app = new express();<br><br>app.use(express.static("cad220_staticfiles"))<br><br>app.listen(3333, () => {<br> console.log("Listening at http://localhost:3333")<br>})<br> |
| jsonwebtoken.sign() | Used for signing-in based on a generated JWT (JSON Web token) | javascript<br>if (uname === "user" && pwd === "password") {<br> return res.json({<br> token: jsonwebtoken.sign({ user: "user" }, JWT_SECRET),<br> });<br>}<br> |
| jsonwebtoken.verify() | Verifies a JWT by passing the token value & the JWT secret as arguments. | javascript<br>const verificationStatus = jsonwebtoken.verify(tokenValue, "aVeryVerySecretString");<br> |
| Project folder strucure | A fairly established project structure for API's built using Express.js is: | plaintext<br>test-project/<br> node_modules/<br> config/<br> db.js //Database connection and configuration<br> credentials.js //Passwords/API keys for external services used by your app<br> models/ //For mongoose schemas<br> items.js<br> prices.js<br> routes/ //All routes for different entities in different files<br> items.js<br> prices.js<br> app.js<br> routes.js //Require all routes in this and then require this file in package.json<br> |

---
