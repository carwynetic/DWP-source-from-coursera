# Developing Back-End Apps with Node.js and Express

- **Course URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express
- **Crawled at:** 2026-11-25T21:57:09.496457
- **Extracted:** 52/52 items (27 videos, 25 readings) | 204,380 chars

---

## Module 1: Introduction to Server-Side JavaScript

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

## Module 2: Asynchronous I/O with callback programming

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

## Module 3: Express Web Application Framework

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

## Module 4: Final Project

### 1. [READING] Project Overview: Scenario and Review Criteria Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/HCpsy/project-overview-scenario-and-review-criteria
- **Method:** `dom_reading_cml` | **Length:** 5421 chars

### Project Overview

You will have the chance to practice and put your skills, knowledge, and abilities to use Node.JS & Express.JS by developing an Online Book review application in your final project.

### Final Project Scenario

In this project, you will assume the role of a back-end developer working for an online retailer selling books. You have been tasked with developing a server-side application that stores, retrieves, and manages book ratings and reviews.

Your server-side application is required to provide the following features and capabilities to allow users to:

- Retrieve a list of all books available in the bookshop
- Search for specific books and retrieve their details based on the book’s ISBN code, author names, and titles
- Retrieve reviews/comments for specified books
- Register as a new user of the application
- Login to the application
- Add a new review for a book (logged in users only)
- Modify a book review (logged in users can modify only their own reviews)
- Delete a book review (logged in users can delete only their own reviews)
- (Multiple users) Access the application at the same time to view and manage different book reviews simultaneously

As is the case with most software development projects, different people in the team work on different parts of the application. Another front-end developer in your team is working on the web-based client-side application that will communicate with your server-side application using REST. Therefore, your job is to implement your server-side application as a RESTful web service. A software architect on your team has written the skeleton code for your server-side application using Node.js and Express.js.

To complete the project, you will fork the skeleton code into your own repo, clone it locally into your development environment, and develop the code further to implement the CRUD capabilities listed above as HTTP methods in your Express server and test them using cURL/Postman. You will also implement Session and JWT authentication to allow only logged in users to perform certain operations. For your reference, this application comes preloaded with all of the book information.

Furthermore, you will need to enhance your code using Promises, Callbacks, or Async/Await functions to allow multiple users to interact with the application simultaneously and not have to wait for each other’s operations to complete.

### Evaluation Criteria – 30 marks total

You can submit your project deliverables in the following way:

#### AI-Graded Submission and Evaluation

You will be redirected to an AI tool where you can upload your deliverables, which may include URLs, terminal outputs, code snippets, or screenshots. You will then receive an AI-generated grade that will automatically reflect on your progress page.

If you encounter any grading problems, please reach out to the Course Team through the Discussion Forums.

Please find the details of the Grading Criteria below:

AI-Graded Submission and Evaluation:
Please save the specified text (cURL command and its output) for each task in your final assignment, as mentioned in the lab instructions. This project carries 30 points towards your final grade and is weighted as follows:

Note: The repository's JSON file containing the book details will be used for evaluation.

#### General users:

Task 1: Copy and paste the cURL command and its output, saved as getallbooks, which displays all book(s) retrieved.- 2 Points

Task 2: Copy and paste the cURL command and its output, saved as getbooksbyISBN, which displays all book(s) retrieved based on the specified ISBN.- 2 Points

Task 3: Copy and paste the cURL command and its output, saved as getbooksbyauthor, which displays all books retrieved based on the specified author.- 2 Points

Task 4: Copy and paste the cURL command and its output, saved as getbooksbytitle, which displays all books retrieved based on the specified title.- 2 Points

Task 5: Copy and paste the cURL command and its output, saved as getbookreview, which displays the initial book review. - 2 Points

Task 6: Copy and paste the cURL command and its output, saved as register, which displays a message confirming the successful registration of a new user. – 3 Points

Task 7: Copy and paste the cURL command and its output, saved as login, which displays the result of logging in as a registered user.- 3 Points

#### Registered Users:

Task 8: Copy and paste the cURL command and its output, saved as reviewadded, which displays a message and reviews after adding or modifying a book review.- 2 Points

Task 9: Copy and paste the cURL command and its output, saved as deletereview, which displays a delete message after deleting a book review.- 2 Points

#### Node.JS program with 4 methods:

Use Async/Await or Promises with Axios in Node.js for all the four methods.

Task 10: Submit the GitHub URL of the general.js file, which contains the code implementation to retrieve all books and their details based on author, title, and ISBN, using promise callbacks or async/await with Axios.- 8 Points

Task 11: Copy and paste the cURL command and its output, saved as githubrepo, which shows that your GitHub repository is forked from ibm-developer-skills-network/expressBookReview.- 2 Points

### Next Steps

Be sure to read the Overview before starting the step-by-step instructions.

### Author(s)

Lavanya T S 
Sapthashree K S 
Sameep

---

### 2. [READING] Project Breakdown Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/R5QVN/project-breakdown
- **Method:** `dom_reading_cml` | **Length:** 2591 chars

This final project for this course has several steps that you must complete. To give you an overview of the project, all the high-level steps are listed below. The project is then divided into several tasks that give the detailed instructions for each step. You must complete all the task to successfully complete the project.

### Prerequisite

You need to complete the following two labs before starting the final project.

- Hands-on Lab - CRUD operations with Node.js.
- Practice Project - CRUD operations on Express server with JWT & Session Authentication.

### Part A: Fork the Git repository to have the server side book review application code you need to start

- Create your own copy of the git repository which has the code you need to start the project.
- Clone the repository into the theia environment.

### Part B: npm install the necessary packages

- Change to the express JS server directory and install all the packages required in your local environment for the server to run.
- Depending on the submission type, you may either use cURL to test the required API endpoints or use your Google Mail credentials to register or log in to Postman and test the same endpoints.

### Part C: Implementing Authentication for using the Book Review application

- You will create access restrictions to some endpoints using JWT and session level authentication.

### Part D: Access the book review application as general purpose user and register user

- General user can access all the books available in the shop and get all books based on ISBN, Author, Title, Review.
- Once a user register with the app, they are able to add or modify and delete book reviews.

### Part E: Use Async/Await or Promises with Axios in Node.js for each of the four CRUD Operations

- Using the async, callback function, retrieve all books. Using Promises, search for the book by ISBN and then search by author or title.
- Depending on the submission type, you may either use cURL to test the required API endpoints or use your Google Mail credentials to register or log in to Postman and test the same endpoints.

### Submit your project for Grading

#### AI-Graded Submission and Evaluation:

- To receive a grade, submit the cURL command and its output for your Book Review application, along with a link to the public GitHub repository as mentioned in the final project.
- In this lab, you will be asked to save the cURL command text and its output for evaluation.

### Next Steps

To complete the lab, follow the step-by-step instructions.

### Author(s)

Sapthashree K S 
K Sundararajan 
Sameep

---

### 3. [READING] Module Summary Reading • 1 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/Aqtb5/module-summary
- **Method:** `dom_reading_cml` | **Length:** 462 chars

Congratulations! You have completed this lesson. At this point in the course, you know:

- How to write code that implements session and JWT authentication that only allows logged-in users to perform specified operations.
- How to write a RESTful web service given skeleton code using the Express framework.
- How to generate code that uses promises, callbacks, and/or Async/Await functions to allow multiple users to interact with an application simultaneously.

---

### 4. [READING] Thanks from the Course Team Reading • 1 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/yWG0p/thanks-from-the-course-team
- **Method:** `dom_reading_cml` | **Length:** 769 chars

The Course Team below would like to thank you for completing the Developing Back-end Applications with Node.js and Express!

#### Primary Instructors

- Upkar Lidder
- Sachin Jambur

#### Other Contributors & Staff

- Project Lead: Rav Ahuja
- Instructional Designer: Bethany Hudnutt, Marianne Siedler
- Labs and Projects Authors, Technical Advisor: Lavanya T S, Sapthashree K, K Sundararajan
- Subject Matter Expert: Sachin Jambur
- Editor: Steve Hord, Jarrod Renfro

#### Production Team

- Publishing: Grace Barker, Rachael Jones
- Project Coordinator: Kanika Ralhan, Bryan Hayes
- Narration: Bella West
- Video Production: Sohini Biswas, Sachin Kumar, Simer Preet

#### Teaching Assistants and Forum Moderators

- Anamika Agarwal
- Lavanya Rajalingam
- Ritika Joshi

---

### 5. [READING] Congrats & Next Steps Reading • 2 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/SHzcm/congrats-next-steps
- **Method:** `dom_reading_cml` | **Length:** 913 chars

Congratulations on completing this course. We hope you enjoyed it.

Back-end professionals are expected to have skills with multiple tools and programming languages. In addition to this course, you may consider further developing your Python skills to add to your resume. As a next step, you can take Python for Data Science, AI, and Development and its follow-up course Python Project for Data Science.

If you would like to learn how to implement SQL databases, you may consider the course Databases and SQL for Data Science with Python.

If you would like to explore full-stack development further, you may wish to consider the IBM Full Stack Developer Professional Certificate program.

Coming soon! IBM will soon offer a professional certificate program specifically for back-end developers.

We encourage you to leave your feedback and rate this course so that we can continue to improve the course content.

---

### 6. [READING] Further Your Learning Reading • 2 min
- **URL:** https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express/supplement/Qq5pS/further-your-learning
- **Method:** `dom_reading_cml` | **Length:** 377 chars

Put your skills into practice with IBM Cloud Pak for Integration

Ready to take the next step? Explore how IBM Cloud Pak for Integration helps organizations connect applications, APIs, events, messaging systems, and data across hybrid cloud environments. Experience the platform through the approved interactive demo or trial destination.

Explore IBM Cloud Pak for Integration

---
