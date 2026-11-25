# Module 1: Introduction to Server-Side JavaScript

### 1. [VIDEO TRANSCRIPT] Course Introduction: Welcome to Developing Back-End Apps with Node.js & Express Video • 3 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/hhwg1/course-introduction-welcome-to-developing-back-end-apps-with-node-js-express
- **Method:** `dom_transcript` | **Length:** 2624 chars

Welcome to this course, Developing Backend Applications with Node.js and Express. Now, you may wonder about the relevance of developing backend applications with Node.js and Express. In Stack Overflow's 2022 survey, Node.js was used by about 50% of the developers who answered the survey, making it the number one most used server-side technology, whereas Express ranked as the popular web technology overall, so making it the most popular server-side web framework. Node.js is a runtime environment that can run server-side JavaScript applications, while Express is a server-side JavaScript web framework that runs on top of Node.js in which to write your applications. This course is designed to help you succeed as a backend or full-stack developer. You may be in IT looking to step up in your career, or a new graduate seeking to further establish your server-side skills, an IT decision maker who needs to manage more cloud-centric projects, or someone in another field who wants to be able to talk about server-side computing more knowledgeably. In the course instructional videos and labs, you will learn about server-side development using JavaScript, code your first web server, and use Node Package Manager to manage your application modules and dependencies.

You'll explore how to make applications run in a non-blocking manner by using asynchronous callbacks and promises, learn how REST APIs are used in conjunction with HTTP requests and responses with the Express.js framework, and then practice using Express by building a web server and creating dynamic content with middleware, routing, and templating. Additionally, hear directly from experts about their experiences with these server-side technologies in the expert viewpoint videos. Let's hear these experts introduce themselves. My name is James Reeve, and I'm a full-stack software engineer at IBM. Hi, my name is Rupinder, and I work as a chief solutions architect at Skillab Technologies. I'm Dennis Harvey. I work at Coursera as a content strategy manager for cloud technology.

Hello there, my name is Bradley Steinfeld. I'm a software architect, and I work for IBM Cloud and Cognitive Software. Hello everyone, my name is Subkaru Leder, and I'm a developer advocate with IBM. Hi, I'm Jan Stoneman. I'm a solution architect at Smartronics. Now, there's a lot to cover here, so to get the most from this course, view each video, check your learning with each quiz, and build a winning portfolio by completing the hands-on labs and final project. Take the next step along this exciting journey that leads to a world of possibilities, and good luck!

---

### 2. [READING] Welcome to Developing Back-end Apps with Node.js and Express Reading • 2 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/IuApY/welcome-to-developing-back-end-apps-with-node-js-and-express
- **Method:** `dom_reading_cml` | **Length:** 967 chars

In this four-week class, expect to spend approximately 3–4 hours per week on the course.

In the first week, you will be introduced to Node.js and server-side JavaScript. The second week focuses on asynchronous programming using callback functions. In the third week, you will explore the Express web application framework. During the fourth week, you will develop a book review application project, which you will submit for final evaluation.

Throughout the course, you will have ample time to practice and hone your skills with hands-on labs.

To be successful in this course and become proficient with Node.js and Express, you should:

- Watch all videos
- Complete the practice and graded quizzes
- Finish the hands-on labs
- Complete the final project
- Submit your work for evaluation
- Periodically review the discussion forums

Please use the discussion forum if you get stuck or want to discuss content further.

Have fun learning about Node.js and Express!

---

### 3. [READING] Course Overview Reading • 2 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/OXB5b/course-overview
- **Method:** `dom_reading_cml` | **Length:** 1647 chars

In a recent Stack Overflow survey, Node.js was used by about 50% of the developers who answered the survey, making it the most used server-side technology. Express ranked as the fourth most popular web technology overall, making it the most popular server-side web framework.

In this course, you will focus on Node.js and Express. Specifically, you will:

- Develop applications using asynchronous callbacks and promises
- Create REST APIs and perform CRUD operations
- Implement authentication and session management

Throughout the course, you will complete numerous hands-on labs to gain practical experience. At the end of the course, you will demonstrate your Node.js skills with a final project to build your portfolio.

This course will help you succeed as a back-end or full-stack developer. It suits those in IT looking to step up in their careers or new graduates seeking to establish their server-side skills. It also suits those who need to manage cloud-centric projects.

Note: This course requires knowledge of JavaScript and Git.

### Prerequisites

- Basic HTML5 and JavaScript skills
- Basic understanding of Cloud Native Development concepts
- Basic understanding of Cloud DevOps and Git concepts

### Audience

#### Who is this course intended for?

Anyone who wants to start building cloud applications—whether you are starting a career as a Cloud Application Developer (e.g., developers, systems/cloud architects, technical leads, data engineers, security engineers, consultants, technical sellers, etc.) or you are looking to learn more about the technologies used in building, deploying, and maintaining cloud applications.

---

### 4. [VIDEO TRANSCRIPT] What is Back End Development? Video • 7 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/1Z7QS/what-is-back-end-development
- **Method:** `dom_transcript` | **Length:** 5605 chars

Welcome to “What is backend development?” After watching this video, you will be able to: Define backend development Differentiate between frontend and backend technologies Explain the components of the backend of a web application Describe the importance of a robust, scalable backend Client-server applications such as cloud-based and web applications generally consist of a “frontend” and a “backend.” The frontend runs on the client machine, and the backend runs on a server. The client machine runs the web browser and the web browser’s engine. The browser’s engine is what communicates with the backend. Backend developers work on the technologies that ensure a website performs correctly, part of which includes writing the code that communicates with the browser’s engine and the backend server. Furthermore, backend development refers to the development of the server-side logic, including the code that pertains to databases, servers, and applications.

Backend technologies include servers, databases, web APIs, programming languages, frameworks, and runtimes. Servers consist of hardware, software, or both that communicate with and provide functionality to a client. Servers may also communicate with and provide functionality to each other. There are many types of servers. Web applications often use many types of servers, including database servers, application servers, and web servers. Let’s briefly discuss each of these types of servers. The database server is the machine and the application that houses, retrieves, and delivers data.

The terms “database server” and “database” are often used interchangeably. Web servers ensure client requests are responded to, often using hypertext transfer protocol or HTTP for short. An HTTP server is part of the software running on a web server. The software part of a web server is what controls how a user accesses files hosted on the server. Application servers host and deliver a business application through HTTP. They sit between a database server and a web server. Application servers transform data into dynamic content and run the business logic, which is the data storage and transfer rules.

Servers must communicate with each other as well as the frontend in a client-server architecture. APIs, which stands for “application programming interface,” allow two pieces of software to communicate with each other. A web service is a type of web API. A web service communicates using HTTP requests. In other words, the web service is the programming interface that sends and receives requests using HTTP among web servers and the client. Backend programming languages are the languages that developers use to make the servers function. These languages include JavaScript, PHP, Python, Ruby, Java, and C-sharp.

Frameworks provide structure for the code. An application can be built and deployed using a framework. The framework often generates code that cannot be altered to perform common tasks. Some common backend frameworks include Django, a Python framework, Ruby on Rails, a Ruby framework, and Express.js a JavaScript framework. Express.js is a framework running on top of node.js that handles HTTP requests made to a web server. Let’s discuss runtime environments. A runtime behaves similarly to a mini operating system that provides the resources necessary for an application to run.

The runtime is the infrastructure that supports the execution of a codebase. It is the hardware and software environment in which an application gets executed. Node.js is an example of a backend runtime environment. The reason Node.js has become so popular as a backend technology is because it runs on Google Chrome’s open-source V8 engine, the same engine that runs the browser on the frontend. Moreover, most modern browsers such as Microsoft Edge and Opera also run on the V8 engine. Node.js makes it very easy for the frontend to communicate with the backend. Node.js executes JavaScript.

Recall from a previous course that JavaScript is widely used on the frontend. This makes JavaScript a handy language for web developers to learn because of its use both on the frontend and the backend. Another issue backend developers need to be concerned with is scalability. Scalability is essential for enterprise software success and is the responsibility of the backend which is affected by the load on an application. Load refers to the number of concurrent users, the number of transactions, and the amount of data transferred back and forth between the clients and servers. Web applications should be scalable. Scalability is the application’s ability to dynamically handle the load as it grows or shrinks without it affecting the application’s performance.

Scalability is essential for the success of a client-server application. Lastly, other backend responsibilities include security, authentication, and prevention of malware attacks. The backend is also mainly responsible for performance because it retrieves and transfers data between machines, delivers content to the front end, and supplies the business logic of the application. In this video, you learned that Backend development refers to the development of the server-side logic, including the code that pertains to databases, servers, and applications. Frontend technologies are those that pertain to the client, such as the interface and the web browser. Backend technologies include various types of servers and supporting infrastructures such as programming languages, frameworks, and other hardware. The backend is responsible for scalability, security, and performance.

---

### 5. [READING] Back-end and Front-end Development Overview Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/In5Si/back-end-and-front-end-development-overview
- **Method:** `dom_reading_cml` | **Length:** 3276 chars

#### Back-end Development

Back-end development, also known as server-side development, involves creating the part of a website or application that users do not see. It manages the server, database, and application logic, ensuring that the front end has access to the necessary data and functionality.

#### Key Components of Back-end Development

Server: The hardware or software that provides resources, data, services, or programs to clients over a network.

Database: A structured collection of data that can be easily accessed, managed, and updated.

- SQL Databases: Relational databases like MySQL, PostgreSQL, and SQLite.
- NoSQL Databases: Non-relational databases like MongoDB, Cassandra, and Redis.

Server-Side Languages: Programming languages used to build the back-end logic.

- Node.js: A JavaScript runtime built on Chrome's V8 JavaScript engine.
- Python: A high-level programming language known for its readability and efficiency.
- Ruby: A dynamic, open-source programming language with a focus on simplicity.
- Java: A versatile and powerful programming language used for large-scale applications.

Frameworks and Libraries:

- Express: A minimal and flexible Node.js web application framework.
- Django: A high-level Python web framework that encourages rapid development.
- Ruby on Rails: A server-side web application framework written in Ruby.
- Spring: A comprehensive framework for enterprise Java development.

Responsibilities of a Back-end Developer:

#### Importance of a Robust, Scalable Back-end

A robust back end ensures data security, performance, scalability, and smooth application logic. It supports user interactions, handles business logic, and integrates with front-end systems.

#### Front-end Development

Front-end development, also known as client-side development, involves creating the part of a website or application that users interact with directly. This includes everything the user experiences visually and through interactions.

#### Key Components of Front-end Development

HTML (HyperText Markup Language): The structure of web pages, defining elements such as headings, paragraphs, images, and links.

CSS (Cascading Style Sheets): The styling of web pages, including layout, colors, fonts, and responsiveness.

JavaScript: The behavior of web pages, enabling interactive features such as forms, animations, and dynamic content updates.

Frameworks and Libraries:

- React: A JavaScript library for building user interfaces.
- Angular: A TypeScript-based framework for building web applications.
- Vue.js: A progressive JavaScript framework for building user interfaces.

Responsibilities of a Front-end Developer:

#### Conclusion

Back-end and front-end development are essential for creating functional and user-friendly web applications. Front-end development involves technologies like HTML, CSS, and JavaScript to build interactive user interfaces. Back-end development manages servers, databases, and application logic using languages such as Node.js, Python, and Java. A robust back end ensures data security, performance, and scalability, supporting seamless integration with the front end for a smooth user experience. Both are crucial for the success of any web application.

#### Author

Ritika Aditya Joshi

---

### 6. [READING] Getting Started with Node.js Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/UcDvK/getting-started-with-node-js
- **Method:** `dom_reading_cml` | **Length:** 3363 chars

#### Full-stack Application

A full-stack application includes the following components:

The Client Side: The website and the mobile application that are user-facing.

The Server Side: Processes any requests from the client side and sends responses back to the client. In today’s world, the cloud hosts the web server, application server, and database.

#### Open Source and Cross-Platform

JavaScript is an ideal choice for client-side validation of HTML pages due to its versatility and cross-platform compatibility. Recognizing its ease of use, JavaScript was further adapted for server-side coding, resulting in Node.js.

Node.js functions as a runtime environment and requires no special licenses for use. Additionally, a wide range of packages and libraries have been developed for use with Node.js due to its open-source nature. Furthermore, Node.js code can seamlessly run across various operating systems such as Linux, Windows, and macOS.

#### V8 Engine

Every piece of code you write needs to be processed and converted into a machine-readable form. In Node.js, JavaScript code is executed using the Google V8 engine.

V8 is a high-performance, open-source engine developed by Google and integrated into all Google Chrome browsers. Modern browsers such as Microsoft Edge also use the V8 engine for JavaScript, while Node.js uses V8 on the server side.

#### Event-Driven, Asynchronous, Non-Blocking, Single-Threaded

Server processes can be categorized as either single-threaded or multi-threaded. In a single-threaded environment, only one command is processed at a time, whereas in a multi-threaded environment, multiple commands can be processed simultaneously.

Despite being single-threaded, Node.js performs efficiently due to its asynchronous and non-blocking nature. This means that while a process is being executed, the program does not need to wait for it to finish.

Node.js is event-driven, meaning that when it performs an input/output (I/O) operation—such as reading from a network, database, or file system—an event is triggered. Instead of blocking the thread and consuming processor time while waiting, Node.js resumes operations when the response is received or when the corresponding event occurs.

This non-blocking behavior enables the server to remain responsive and handle multiple tasks concurrently, similar to a multi-threaded environment.

#### JSON Payload

JSON stands for JavaScript Object Notation and is formatted as key-value pairs. The payload represents the data transmitted between the client and the server.

When the client needs to send data to the server, it does so in the form of a JSON object, as shown below:

{ 
"name": "John", 
"age": "24", 
"email": "johnparker@gmail.com"
}

The above object is a JSON. When this data is sent as part of the request, its values can be extracted using request.name and so on.

Similarly, the response is also sent as JSON. An example is shown below:

{ 
"status": "ok", 
"message": "Successfully added"
}

Express Framework

While Node.js provides packages to create a server, the Express framework simplifies the process of creating APIs and endpoints.

An API endpoint is a specific point of entry for a request from the client to the server.

#### Next Steps

In this course, you will learn how to perform server-side coding with Node.js using the Express framework.

---

### 7. [VIDEO TRANSCRIPT] Introduction to Node.js Video • 3 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/8ffyS/introduction-to-node-js
- **Method:** `dom_transcript` | **Length:** 2667 chars

Welcome to Introduction to Node.js. After watching this video, you will be able to describe the role of Node.js for server-side scripting, list the differences between JavaScript and Node.js, describe ExpressJS, and explain how ExpressJS helps developers build Node.js apps. Node.js is an open-source language that runs on V8. V8 is an open-source engine that was developed by Google for the Google Chrome browser. Developers often use JavaScript for client-side functionality. Node.js is the server component in the same language. Node.js is event-driven and uses asynchronous non-blocking I.O.

With server-side JavaScript, node applications process and route web service requests from the client. In Step 1, the user selects an option in the user interface written in HTML and CSS. In Step 2, this action by the user triggers JavaScript code that implements the business logic on the client-side, for example, input validation. In Step 3, the JavaScript application makes a web service call over HTTP with a JSON data payload. The REST web service, which is part of a Node.js application running on the Node server, receives the HTTP request. In Step 4, the REST web service processes the request and returns the result to the client as a JSON payload over HTTP. Although developers can still use JavaScript for browser functionality in frameworks, such as AngularJS, Dojo, and jQuery, they can now use Node.js in the same components of the architecture where they use Java, Perl, C++, Python, and Ruby.

Node.js is used in production by companies such as Uber, Yahoo, LinkedIn, GoDaddy, eBay, and PayPal. It is event-driven and uses asynchronous, non-blocking I.O. Express.js is a highly configurable framework for building applications on Node.js. It abstracts lower-level APIs in Node.js by using HTTP utility methods and middleware. Before you build your first Node.js app, let's get familiar with the IDE and some key Node.js concepts. Express.js simplifies application development on Node.js. The following features enable you to develop your application quickly.

Public – public assets like image, CSS, and Java. Templates or Views – server-rendered HTML that is sent back to the client in response to requests. Routes – defines endpoints that accept and process client requests. Server.js – a file which contains the main application code. Package.json – contains metadata information about the project including dependencies, scripts, and so on. In this video, you learned that Node.js is the server-side component of JavaScript. Using Node.js can improve application performance.

And Express.js is a framework that helps you build Node.js applications.

---

### 8. [VIDEO TRANSCRIPT] Expert Viewpoints: Introductory Thoughts on Server-Side JavaScript and Node.js Video • 5 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/LHIi1/expert-viewpoints-introductory-thoughts-on-server-side-javascript-and-node-js
- **Method:** `dom_transcript` | **Length:** 4179 chars

Welcome to Expert Viewpoints: Introductory thoughts on Sever-side JavaScript and Node.js. In this video, we will hear from several application development professionals discussing working with server-side JavaScript and Node.js. The wonderful thing about using Node.js as your back-end language is it's the same as your front-end language. So it makes it easier (kind of) to context switch between writing for the front end and then writing for the back end. You can have the same developers basically writing both. I mean a lot of developers know multiple languages. But this way, if you've got someone very strong at JavaScript, all that knowledge will pay off in both the front end and the back end.

And you can also use the same code scanning and code testing for the front-end JavaScript as for the back-end JavaScript. So that and like the dependency security scanning and all of that, both the front end and the back end are going to be using NPM, the node package management, for the dependencies. And that way, you've got kind of a unified approach to dependencies and packages. I think the most obvious appeal of using Node.js, at least for full-stack developers, is that you get to use the same language client side and server side. So if you're a new developer, that's one less language you have to learn. And even if you're not, it can be nice to minimize the differences when context-switching between front-end and back-end development. Another benefit is actually the community surrounding Node.js. I think on the most recent Stack Overflow survey it was being used by over 50% of professional developers.

And that's really reflected in the wealth of learning resources and support that are available to you. If you are a front-end developer, if you understand JavaScript, then picking up back end using a framework like Node.js is not that much of a stretch. I actually started building static websites, and then slowly learned how to put in dynamic content using JavaScript. And then I had to use Java or PHP to build my back-end systems on the server. There's a little bit of a context switch when you're doing that, but Node.js, the cool thing is, you're using JavaScript on the front end, and you're using JavaScript on the back end as well. So there's a little bit less of a context switch. It's easy to switch between working with services on the back end and then going to your website and putting in some JavaScript.

The one thing that I did find a little bit odd at first was the single-threaded nature of Node.js in everything relying on callbacks. So asynchronous programming using callbacks is a little bit of a twist with Node.js. But it's a matter of getting used to that. The one thing I did like was the abundance of packages in registries like NPM for you to be able to use in your applications. Key benefit of using Node.js is faster processing. It can handle concurrent requests faster than any other server-side languages. Node.js is a popular choice for online gaming, chats, video conferences, or any solution that requires constantly updated data.

It is easier to learn Node.js if one already has a good grasp on JavaScript. Developers can write both front end and back end in Javascript using a runtime environment. There is no need for separate front-end and back-end developers in this case. JavaScript is obviously the de facto standard for client-side web development. And so it quite naturally makes sense to allow JavaScript developers to leverage those skills on the server side. And that's where Node.js fits in nicely. The big deal with Node.js is its architecture as it offers a rather unique single-threaded, asynchronous, event-oriented architecture that enables it to handle a very large number of concurrent connections.

Think hundreds of thousands of concurrent connections. Node.js is built on top of Google's Chrome JavaScript V8 engine. Parsing JSON is blazingly fast because JSON is a native data type in JavaScript. And Node.js also fits very nicely into the adoption of microservices since each microservice is dedicated to one or a small number of cohesive services and is inherently therefore limited in scope.

---

### 9. [VIDEO TRANSCRIPT] Import and Require Video • 5 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/NJJTn/import-and-require
- **Method:** `dom_transcript` | **Length:** 4452 chars

Welcome to import and require. After watching this video, you will be able to explain what a module is, explain what a module specification is, explain the purpose of import and require statements, and differentiate between import and require statements. In Node.js, modules are files containing related, encapsulated JavaScript code that serve a specific purpose. Modules can be a single file or a collection of multiple files and folders. Developers rely heavily on modules because of their reusability as well as their ability to break down complex code into manageable chunks. When an external application needs to use the code contained in a module the application needs to call that module. When the external application calls a module, the module is called using an import() or a require() statement.

Which statement is needed depends on the specification. Let’s talk about specifications next. A directory with one or more modules bundled together is called a package. Module specifications are the conventions and standards used to create packages in JavaScript code for Node.js applications. The most commonly used module specifications for Node.js applications are CommonJS and ES modules. Some of the differences between CommonJS and ES modules will be discussed in a moment. By default, Node.js treats JavaScript code as a CommonJS module.

Library authors can easily enable ES modules in a Node.js package by simply changing the package file extension from dot j-s to dot m-j-s. CommonJS modules use the require() statement to import modules whereas ES modules use the import() function. When a module is needed outside of its own file it must be exported first. The module.exports statement should be used with CommonJS. Modules can be exported to an ES specification using the “export” keyword. Next, we’ll take a closer look at the differences between require and import. Let’s look at the differences in calling require and import within the application code.

The require statement can be called anywhere in the file whereas the import statement must be called at the beginning of the file. Since the require statement can be called from anywhere, this means that it can be called within conditional statements and functions, but import cannot. This may sound like an advantage of require but note that the require statement is bound dynamically whereas import is bound statically. This means errors that occur when linking the function definition to the function call will not be identified until run-time. For Import, binding errors are identified at Compile time. Require modules are synchronous in nature and modules imported with import are asynchronous. Synchronous means the modules will be loaded and processed in a linear fashion, one at a time.

Asynchronous means the modules can be processed simultaneously. Import runs faster compared to require functions in large-scale applications which involve loading hundreds of modules. Let’s take a look at some sample code that shows how to export and import using require and import. Recall that the require statement is used with CommonJS applications. This code snippet will show how to export from a file named message dot j-s. We use module dot exports to export the string “Hello programmers” from the message dot j-s module. Next, to import the message dot j-s module into the main application, we use the require statement.

In this code the result of require is assigned to the let m-s-g, then the variable is logged in the console. Now, let’s look at code that exports an ES module from a file named module dot m-j-s. This code names a constant ‘a’ and sets the constant equal to 1. Next, the export statement is used. Note the use of the curly brackets. A is renamed to my value. Finally, we look at code to import an ES module using import.

Simply use the import keyword. We are importing my value from the module.mjs file. In this video, you learned that a module is a file containing related JavaScript functions that serves a specific purpose. Module specifications are conventions and standards used to create packages in JavaScript code. import and require statements are used to call a module or a package into an external application. The require statement can be called from anywhere in the app code, is bound dynamically, and is synchronous, and the import statement can only be called at the beginning of a file, is bound statically, and is asynchronous.

---

### 10. [VIDEO TRANSCRIPT] Introduction to Server-Side JavaScript Video • 3 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/GEfdA/introduction-to-server-side-javascript
- **Method:** `dom_transcript` | **Length:** 2975 chars

[Music] Welcome to Introduction to server-side JavaScript. After watching this video, you will be able to: Explain the purpose of the Node.js JavaScript framework and explain the differences between client-side JavaScript and server-side JavaScript. JavaScript is one of the main languages used in the World Wide Web. It was originally built to add dynamic behavior to static websites on clients where there were primarily browsers. JavaScript is an interpreted language. You do not need to compile JavaScript applications before running them. Although the language syntax resembles Java, it is not derived from the Java programming language.

JavaScript can now be run on different servers and embedded systems and all modern web browsers support JavaScript. Developers build responsive, interactive web applications with hypertext markup language (HTML), cascading style sheets (CSS), and JavaScript. With a text editor and a web browser, you can quickly write, test, and debug JavaScript applications. With client-side JavaScript, developers create rich, interactive web applications in the web browser. In step 1, the user interface is rendered using HTML and CSS. When the user selects an option in the web page, it triggers business logic written as a JavaScript application. The JavaScript application sends a web service request using JavaScript Object Notation (JSON) over hypertext transfer protocol (HTTP).

On the server, a Representational State Transfer (REST) web service intercepts the call. This service traditionally would be written in Java, PHP: Hypertext Preprocessor (PHP), or another backend language. In the last step, the application server processes the web service request using a server-side application such as Enterprise Java components and returns to the client. With server-side JavaScript, Node.js applications process, and route web service requests from the client. Compare the following diagram with the one in the previous slide. Most of the steps are identical. In step 1, the user selects an option in the user interface, which is written in HTML and CSS.

In step 2, the option triggers a JavaScript application that implements the business logic on the client-side. In step 3, the JavaScript application makes a web service call over HTTP with a data payload written in JSON. In step 4, a REST web service intercepts the HTTP request and in the final step, instead of invoking an Enterprise Java application, the Node.js server hosts an application written in the JavaScript language. This code written in JavaScript runs on the server, and not in the client's web browser. In this video, you learned that: Node.js is a server-side programming framework that uses JavaScript as its programming language. With server-side JavaScript, Node.js applications process and route web service requests from the client and Node.js is for developers who want to build scalable, concurrent server applications quickly with a minimal set of tools.

---

### 11. [VIDEO TRANSCRIPT] Creating a Web Server with Node.js Video • 2 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/t480f/creating-a-web-server-with-node-js
- **Method:** `dom_transcript` | **Length:** 2215 chars

Welcome to Creating a Web Server with Node.js. After watching this video, you will be able to: Describe the characteristics of Node.js and write a simple web server with Node.js. Node.js is a server-side programming framework that uses JavaScript as its programming language. Many developers are already familiar with the JavaScript language. It is built with a heavy emphasis on concurrent programming with a lightweight language. Node.js is a single-threaded application environment that handles input/output (I/O) operations through events. Instead of blocking on asynchronous I/O operations, you write callback functions to handle results when they complete.

Node.js is suited for developers who want to build scalable and concurrent server applications by using features like callback functions and the Node.JS runtime event loop. These features of the JavaScript language and the Node.js runtime enable quick development with a minimal set of tools. Every JavaScript file is a module in Node.js. A module corresponds to a script file. A package can contain one or more nodes. The Node.js runtime is packaged with many utility modules that you can use to create and extend your applications. With the HTTP Node.js module, you can develop an application that listens to HTTP requests and returns HTTP response messages.

To create an instance of a web server, use the HTTP.createServer function. The web server is stored in a variable called "server." The createServer function takes in an optional callback function as a parameter. This callback function handles the incoming request message and provides an appropriate response message. The callback function shown here is anonymous. After you create an instance of the server object, you can set the server to listen to a specific port; for example, call the HTTP.listen function with a parameter of 8080 as the port to set the server to listen on 8080. In this video, you learned that: Node.js is a single-threaded application environment that handles I/O operations through events.

Every JavaScript file is a module in Node.js. With the HTTP Node.js module, you can develop an application that listens to HTTP requests and returns HTTP response messages.

---

### 12. [VIDEO TRANSCRIPT] Working with Node.js Modules Video • 4 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/ZDQVK/working-with-node-js-modules
- **Method:** `dom_transcript` | **Length:** 3377 chars

[Music] Welcome to Working with Node.js Modules. After watching this video, you will be able to: Describe Node.js packages. Import Node.js modules into your script. Export functions and properties from a module, and access exported properties from a module. A package consists of one or more modules. The package.json file describes details about a Node.js module. If a package does not have a package.json file, Node.js assumes that the main file is named index.js.

To specify a different main script for your module, specify a relative path to the Node.js script from the module directory. This is an example of a package.json file. The name and version fields form a unique identifier for the module; for example, today-1.0.0. The main field lists a path to the main Node.js script; in this example, the today.js script in the lib subdirectory. Package.json defines many other fields. For example, license states the module's usage rights. You can use the require function to import a Node.js module.

The require statement assumes that scripts have a file extension of .js. The require function creates an object that represents the imported Node.js module. In this example, a Node,js script file that is named today.js is in the same directory as your application. When you call require with the name of a subdirectory, Node.js looks for a script file with the same name as the subdirectory. If the script file does not exist, the function assumes that the name is the name of a directory and looks for a script named index.js within that directory. To import a Node.js module that consists of a single script, use the require function with a relative path to the script file. In this example, the main application is in the Node.js script file.

Hello.js makes a require function call to the today.js script file. This example uses the same hello.js Node.js file. The Node.js module is saved in a directory named mod_today. The actual script file is saved in index.js. When hello.js makes a call to the require function in the mod_today directory, the script file checks whether there is a file named index.js. This is the default name for a script in a Node.js module. Each Node.js module has an implicit exports object.

To make a function or a value available to Node.js applications that import your module, add a property to exports. In this example, the dayOfWeek property is added to the exports object. Then, dayOfWeek is assigned an anonymous function that returns the day of the week. For example, if the dayOfWeek function returns 1, this value maps to Monday. When you import a Node.js module, the require function returns a JavaScript object that represents an instance of the module. For example, the today variable is an instance of the today Node.js module that is called "today." To access the properties of the module, retrieve the property from the variable.

In the same example, today.dayOfWeek represents the current exported property from the today Node.js module. In this video, you learned that: Every package has a package.json file that describes details about a Node.js module. To make a function or a value available to Node.js applications that import your module, add a property to the implicit exports object and when you import a Node.js module, the require function returns a JavaScript object that represents an instance of the module.

---

### 13. [READING] Advanced Node.js Modules Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/wd117/advanced-node-js-modules
- **Method:** `dom_reading_cml` | **Length:** 4528 chars

After completing this reading, you will be able to describe the three types of Node.js modules. You will also be able to explain what several prominent core modules can be used for.

In Node.js, reusable code is organized into modules. There are three types of modules: core, local, and third-party.

Core Node.js modules are built-in modules that provide essential functionality for developing Node.js applications.

Local modules are the next type of Node.js module. Local modules are the modules written by you and the development team as part of creating your Node.js application.

Third-party modules are created by external developers and are typically available through package registries such as npm. These modules are distributed under different licenses, and developers should review license terms before use

Commonly used core modules include http, path, fs, os, util, url, and querystring. Let's briefly discuss each of these and provide code examples.

The http module provides methods to transfer data over HTTP. To include the http module in your application, you should require it.

Here is a sample code snippet that creates a server using the http module. This code makes use of the http.createServer() method to create the server instance.

let http = require('http');

http.createServer(function (req, res) {

res.write('hello from server');//write a response to the client

res.end();//end of response from server

}).listen(6000);//the server instance listens for http requests on port 6000

The fs module is used to interact with a file system. It does not need to be installed because it is part of the Node.js core and can simply be required. The following code sample reads a local file asynchronously using the fs module and prints the file contents to the console.

const fs = require('fs');

// Asynchronously read the file 'sample.txt'

fs.readFile('sample.txt', 'utf8', (err, data) => {

if (err) {

console.error(err);

return;

}

// Print the contents of 'sample.txt' to the console

console.log(data);

});

The fs module can also be used for input and output, known as I/O. The fs module methods can be used to retrieve information from or write data to an external file.

const fs = require('fs');

// Read the contents of the file '/content.md' synchronously and store them in 'data'

const data = fs.readFileSync('/content.md', 'utf8');

// Print the contents of 'content.md' to the console

console.log(data);

The OS module provides methods to retrieve information from the operating system that the application is running on and interact with it. This is sample code from the OS module that gets the computer's platform and architecture.

let os = require('os');

console.log("Computer OS Platform Info : " + os.platform());

console.log("Computer OS Architecture Info: " + os.arch());

The path module allows you to retrieve and manipulate directory and file paths.The following code retrieves the last portion of a given file path and prints that value to the console:

const path = require('path');

let result = path.basename('/content/index/home.html');

console.log(result); //outputs home.html to the console

The Node.js util module is intended for internal use for accomplishing such tasks as debugging and deprecating functions. Say you want to debug a program to count the number of iterations in a loop. You could use util.format() method as follows:

let util = require('util');

let str = 'The loop has executed %d time(s).';

for (let i = 1; i <= 10; i++) {

console.log(util.format(str, i)); //outputs 'The loop has executed i time(s)'

}

The URL module is used to divide up a web address into readable parts. Here is a sample code that returns the value of the "firstName" query object from the given URL.

const url = require('url');

let webAddress = 'http://localhost:2000/index.html?lastName=Kent&firstName=Clark';

let qry = url.parse(webAddress, true);

let qrydata = qry.query; //returns an object: {lastName: 'Kent', firstName: 'Clark'}

console.log(qrydata.firstName); //outputs Clark

The querystring module provides methods to parse query strings from a URL. Modern applications often use URL and URLSearchParams.For example:

let qry = require('querystring');

let qryParams = qry.parse('lastName=Kent&firstName=Clark');

console.log(qryParams.firstName); //returns Clark

There are also a number of useful third-party packages for use with Node.js. Some of those include AsyncJS, Axios, and Express. These libraries will be discussed later in the course.

---

### 14. [VIDEO TRANSCRIPT] Overview of Node Package Manager Video • 5 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/lecture/LA0wl/overview-of-node-package-manager
- **Method:** `dom_transcript` | **Length:** 4313 chars

Welcome to overview of node package manager. After watching this video, you will be able to explain the purpose of a package manager, describe the two main aspects of node package manager (NPM), describe the purpose of a package.json file, and compare and contrast a local NPM install to a global NPM install When dealing with languages that use modules and packages, such as JavaScript, a tool called a package manager is usually needed. A package manager is a set of tools used to deal with modules and packages containing dependencies. Sometimes it is also referred to as a package-management system. Dependencies are code, usually in the form of libraries and packages, that are called and reused in a program. So, for example, say you are developing a new module, and you call a function contained in another module written by you, which calls another module written by someone else, which calls yet another module, written by that 3rd-party. The module you are writing is “dependent” on all of those other modules.

A library of code usually contains many dependencies, but the library is self-contained and isn’t dependent on code outside of the library itself. Packages work the same. A package manager automates the process of finding, installing, upgrading, configuring, maintaining, and removing packages for a computer program. Package managers usually are connected to and maintain a database of dependencies and versioning information for the packages in a repository. The package manager ensures that a piece of software has the dependencies to run correctly and eliminates the need to do this work manually. Node Package Manager, usually abbreviated as NPM, is the default package manager for the Node.js runtime engine. NPM has two functions.

First, it provides a command line interface that allows users to publish and download packages. Second, it behaves as an online repository of binary JavaScript packages. The repository is a database of packages that tracks versions of packages referenced in applications. All NPM packages require a file named “package.json” that should be located in the project’s root directory. NPM uses the metadata in the package.json file to determine all of the dependencies in a package. This file contains the project’s identifying metadata in the form of key-value pairs that, at a minimum, identify the name of the project and the project’s version number. The code shown here displays an example of those two key-value pairs.

There are two ways in which NPM can install packages: locally or globally. You will want to use the local install if you are installing a package you want to use within your application. Run the local install command from the directory you want the package installed in. The local install is npm’s default behavior. To install the node_modules package locally, use the NPM command line interface to enter: npm install <package_name> This command creates a directory named node_modules with the package and its dependencies in your current working directory. Packages can also be installed globally. A global install means that all applications on the machine in which the package is installed can use that code.

Global installs should be used judiciously because all projects on that computer will make use of that package and its dependencies. If you have different versions of a project on your machine, they will all use the globally installed package, which might break compatibility with other dependencies. To install node_modules so the package can be accessed by any application on the machine, which means they are installed globally, use the command “npm install minus g package_name” in the command line interface. It is the same command as the local install command but adds the minus g option. In this video, you learned that: The package manager ensures a piece of software has the dependencies it needs to run correctly. NPM provides a command line interface tool and also functions as an online database of JavaScript packages. NPM uses the metadata in a package.json file to determine a package’s dependencies.

And, a local install means only the application within the directory of the installed can access the package, whereas a global install means that any application on the machine can access the package.

---

### 15. [READING] Module Summary Reading • 2 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/alBQz/module-summary
- **Method:** `dom_reading_cml` | **Length:** 1345 chars

Congratulations! You have completed this module. At this point in the course, you know:

- Backend technologies include various types of servers and supporting infrastructure, such as programming languages and frameworks.
- Node.js is a JavaScript runtime environment used for server-side development.
- The require statement can be called from anywhere in the application code, is bound dynamically, and loads modules synchronously.
- The import statement must be called at the beginning of a file and is bound statically. Module loading with import is asynchronous.
- Client-side JavaScript is used to process front-end user interface elements, while server-side JavaScript enables access to different kinds of servers and web applications.
- With server-side JavaScript, Node.js applications process and route web service requests from the client.
- To make a function or a value available to Node.js applications that import your module, add a property to the exports object.
- Core modules provide essential functionality, local modules are those that you create for your application, and third-party modules are created by the Node.js community.
- A local install means only the application within the installation directory can access the package, whereas a global install means that any application on the machine can access the package.

---

### 16. [READING] Module 1 Glossary: Introduction to Server-Side JavaScript Reading • 5 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/gRusF/module-1-glossary-introduction-to-server-side-javascript
- **Method:** `dom_reading_cml` | **Length:** 3211 chars

Developing Back-End Apps with Node.js and Express

| Term | Definition |
| --- | --- |
| Anonymous Function | A function that is not named. An anonymous function is often passed into another function as a parameter. |
| Application Server | Transforms data into dynamic content and runs the business logic, which is the data storage and transfer rules. |
| Asynchronous | A process that runs independently of other processes. |
| Callback Function | A function passed into another function as a parameter, which is then invoked inside the outer function to complete an action. Instead of blocking on asynchronous I/O operations, callback functions are used to handle results when the operations complete. |
| Database Server | A server dedicated to providing database services. |
| Dependencies | Code, usually in the form of libraries and packages, that are called from other modules and reused in a program. |
| Event-Driven | Where the flow of a program is determined by particular events such as user input. |
| Express.js | A highly configurable web framework for building applications on Node.js. |
| Framework | Generates code that cannot be altered to perform common tasks. Examples include Django, Ruby on Rails, and Express.js. |
| HTTP Server | A type of software-based server that understands URLs and hypertext transfer protocol. |
| Load | Refers to the number of concurrent users, the number of transactions, and the amount of data transferred back and forth between the clients and servers. |
| Module | Files containing related, encapsulated JavaScript code that serve a specific purpose. |
| Multi-Threaded | Where multiple tasks are executed simultaneously. |
| Node.js | A JavaScript runtime environment that runs on Google Chrome’s V8 engine. |
| Non-Blocking | Failure of a given thread does not cause failure in another, and the execution of a task is not blocked until execution of another task is completed. |
| Npm | Stands for node package manager. It is the default package manager for the Node.js runtime environment. |
| Package | A directory with one or more modules bundled together. |
| Package.json | Contains metadata information about the project, including dependencies and scripts. |
| Payload | The data transmitted between client and server. |
| Runtime Environment | Behaves similarly to a mini operating system that provides the resources necessary for an application to run. It is the infrastructure that supports the execution of a codebase. It is the hardware and software environment in which an application gets executed. Node.js is an example of a backend runtime environment. |
| Scalability | The application’s ability to dynamically handle the load as is or shrinks without it affecting the application’s performance. |
| Server.js | A file that contains the code that handles server creation. |
| Single-Threaded | Where only one command is processed at a given point of time. |
| Web Server | Ensures client requests are responded to, often using HTTP. |
| Web Service | A type of web API that communicates using HTTP requests. It is the web service in the programming interface that sends and receives requests using HTTP among web servers and the client. |

---

### 17. [READING] Module 1 Cheat Sheet: Introduction to Server-Side JavaScript Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/0EykK/module-1-cheat-sheet-introduction-to-server-side-javascript
- **Method:** `dom_reading_cml` | **Length:** 1682 chars

### Developing Back-End Apps with Node.js and Express

| Package/Method | Description | Code Example |
| --- | --- | --- |
| http/createServer | http package is used for establishing remote connections to a server or to create a server which listens to client. createServer - Takes a requestListener, a function which takes request and response parameters, where request is the handle to the request from the client and response is the handle to be sent to the client. | const http = require('http');const requestListener = function(req, res) { res.writeHead(200); res.end('Hello, World!');}const port = 8080;const server = http.createServer(requestListener);console.log('server listening on port: '+ port);server.listen(port); |
| new Date() | new Date() method returns the current date as an object. You can invoke methods on the date object to format it or change the timezone. | module.exports.getDate = function getDate() { let aestTime = new Date().toLocaleString("en-US", {timeZone: "Australia/Brisbane"}); return aestTime;} |
| import() | The import statement is used to import modules that some other module has exported. A file that includes reusable code is known as a module. | // addTwoNos.mjsfunction addTwo(num) { return num + 4;}export { addTwo };// app.jsimport { addTwo } from './addTwoNos.mjs';// Prints: 8console.log(addTwo(4)); |
| require() | The built-in NodeJS method require() is used to incorporate external modules that are included in different files. The require() statement essentially reads and executes a JavaScript file before returning the export object. | module.exports = 'Hello Programmers';let msg = require('./messages.js');console.log(msg); |

---

### 18. [READING] Basic JavaScript Concepts Reading • 20 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/dvzZX/basic-javascript-concepts
- **Method:** `dom_reading_cml` | **Length:** 4953 chars

#### Learning Objectives

- Describe variable declaration and data types in JavaScript
- Apply control structures for logic flow
- Define and use functions, including arrow functions
- Explain the working of array methods (map, filter, reduce) for data transformation
- Implement basic object-oriented programming with classes
- Describe parse and stringify JSON data
- Demonstrate how to set up a simple Express.js server and define basic routes
- Explain how to use req.params, req.query, and req.body in Express

#### Prerequisite

As highlighted in the Course Overview, basic knowledge of JavaScript is a prerequisite for this course. This reading includes additional JavaScript concepts to support and enhance your understanding.

#### Variables and Data Types

JavaScript uses let, const, and var to declare variables. Variables declared with let and var default to undefined if not initialized. Variables declared with const must be initialized at the time of declaration and cannot be reassigned.

let name = "Book Review"; // string

const rating = 4.5; // number (immutable binding)

var isPublished = true; // boolean (function-scoped)

let book = { title: "JS Guide", author: "MDN" }; // object

let tags = ["JavaScript", "Express"]; // array

#### Control Structures

Control structures manage the flow of logic in programs.

// Conditional

if (rating > 4) {

console.log("Highly rated!"); // executes if condition is true

} else {

console.log("Needs improvement."); // executes otherwise

}

// Loop

for (let tag of tags) {

console.log(tag); // prints each tag

}

#### Functions

Functions encapsulate reusable logic.

// Function Declaration

function greet(user) {

return `Hello, ${user}`;  // returns a greeting

}

// Arrow Function

const add = (a, b) => a + b;  // concise syntax for function

console.log(greet("Dev")); // Hello, Dev

#### Array Methods

Used to process data collections.

const books = [

{ title: "JS Basics", rating: 5 },

{ title: "Node Intro", rating: 3 }

];

// Filter: Get books with rating > 4

const topBooks = books.filter(book => book.rating > 4);

// Map: Get an array of book titles

const titles = books.map(book => book.title);

// Reduce: Calculate average rating

const averageRating = books.reduce((sum, book) => sum + book.rating, 0) / books.length; // 0 is initial value

console.log(topBooks); // [{ title: "JS Basics", rating: 5 }]

console.log(titles); // ["JS Basics", "Node Intro"]

console.log(averageRating); // 4

#### Object-Oriented JavaScript

Organizes code using classes and objects.

class Book {

constructor(title, rating) {

this.title = title;

this.rating = rating;

}

describe() {

return `${this.title} has a rating of ${this.rating}`;

}

}

const b1 = new Book("Node Basics", 4.2);

console.log(b1.describe());

Working with JSON

JSON is commonly used in APIs for data exchange.

let jsonData = '{"title":"Express 101","rating":5}';

const bookObj = JSON.parse(jsonData); // convert JSON to JS object

const newJson = JSON.stringify(bookObj); // convert JS object to JSON

#### Simple Node.js + Express Example

Create a minimal Node.js server using Express that responds with JSON data.

// app.js

const express = require("express");

const app = express();

app.use(express.json()); // middleware to parse JSON request bodies

app.get("/books", (req, res) => {

res.json([{ title: "Learn Node", rating: 4 }]); // return JSON response

});

app.listen(3000, () => console.log("Server running on port 3000"));

HTTP Methods Overview (REST API)

Used for CRUD operations in web services.

| Method | Purpose |
| --- | --- |
| GET | Read data |
| POST | Create data |
| PUT | Update data |
| DELETE | Remove data |

#### Understanding req.params, req.query, and req.body

These are ways to access incoming request data in Express.

#### 1. req.params

Visiting /users/123 sets req.params.id to "123"

app.get('/users/:id', (req, res) => {

const userId = req.params.id;  // extract dynamic part from URL

res.send(`User ID is ${userId}`);

});

#### 2. req.query

Visiting /books?author=JohnDoe sets req.query.author to "JohnDoe"

app.get('/books', (req, res) => {

const author = req.query.author; // extract ?author= value from query string

res.send(`Filter by author: ${author}`);

});

#### 3. req.body

For JSON { "username": "aname", "password": "pwd123" }, req.body.username returns "aname"

app.post('/register', (req, res) => {

const username = req.body.username;  // get value from request body

res.send(`Username received: ${username}`);

});

#### Summary

In this reading, you explored the core JavaScript concepts essential for server-side development with Node.js and Express. These included variables, functions, array methods, classes, and working with JSON. You also gained an understanding of how a basic Express server operates and how to handle incoming request data using req.params, req.query, and req.body.

#### Author(s)

Ritika Joshi

---
