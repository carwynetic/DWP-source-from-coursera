# Module 2: Web API Essentials: REST API and GraphQL

### 1. [VIDEO TRANSCRIPT] What is REST? Video • 3 min
- **URL:** https://www.coursera.org/learn/applications-development-microservices-serverless-openshift/lecture/DyPop/what-is-rest
- **Method:** `dom_transcript` | **Length:** 2715 chars

Welcome to ‘What is REST?’. After watching this video, you will be able to describe RESTful APIs, explain the key characteristics of a REST API, and explain the benefits of using REST APIs. REST stands for Representational State Transfer. REST APIs provide a flexible, lightweight way to integrate applications, and have emerged as the most common method for connecting components in microservices architectures. It is an architectural style that defines how applications should communicate with each other within a network. An API has three characteristics that classify it as RESTful. It manages all requests through HTTP, It provides stateless, client-server communication, and it consists of a uniform interface between components.

REST APIs communicate via HTTP requests to perform standard functions like creating, reading, updating, and deleting records (also known as CRUD) within a resource. For example, a REST API would use a POST request to create a record, a GET request to retrieve a record, a PUT request to update a record, and a DELETE request to delete a record. REST APIs are stateless, meaning that each request contains all the information required to process it. Roy Fielding, the originator of REST, said in his dissertation. “Each request from client to server must contain all of the information necessary to understand the request, and cannot take advantage of any stored context on the server. Session state is therefore kept entirely on the client.” This stateless nature of REST APIs also makes them scalable.

The main benefit of RESTful APIs is the uniform interface, regardless of where the request originates. The REST API should ensure that the same piece of data, such as the product id, belongs to only one uniform resource identifier (or URI). And resources should contain every piece of information that the client may need. For example, the client might require the name and price of the product. Let’s look at an example of REST. The CEX.IO is a cryptocurrency exchange. It provides developers bitcoin, other crypto prices, and market data through REST API.

CEX has documented all API calls in their developer’s section with detailed information on both the request and response parameters, all in a simple JSON format, as well as sample requests and code snippets in JavaScript, Python, C#, and Java. For example, you can request the last price of a currency pair through their public API. In this video, you learned that REST APIs provide flexible but uniform interfaces between components, REST APIs are stateless and scalable, REST APIs communicate using HTTP methods POST, GET, PUT, and DELETE, and REST is an architectural style defining how applications communicate.

---

### 2. [VIDEO TRANSCRIPT] Introduction to API Gateway Video • 4 min
- **URL:** https://www.coursera.org/learn/applications-development-microservices-serverless-openshift/lecture/vJCLd/introduction-to-api-gateway
- **Method:** `dom_transcript` | **Length:** 3907 chars

Welcome to ‘Introduction to API Gateway’. After watching this video, you will be able to explain an API Gateway, explain the benefits of using an API Gateway, explain the drawbacks of using an API Gateway, and describe the available API Gateway products. An API Gateway is an API management tool that sits between a client and a collection of backend services. It aggregates the various services required to fulfill them and returns the appropriate result. So why do you use an API Gateway? An API Gateway can help you to protect your APIs from malicious usage or overuse. Thus, you can use an authentication service with rate limiting.

It also helps to understand how your APIs are used, using an analytics and monitoring service. In addition, you can monetize your APIs using a billing system. A gateway also presents a single point of contact to your various microservices and provides a single response to a request. Finally, you can seamlessly add or remove APIs without the client’s knowledge about the services running at the back end. Since your online store follows microservices architecture; some of those services will be: a product information service that shares basic information about the product such as id, name, and price, an inventory service that reveals what’s available in stock, an order service that enables customers to place an order for a product, and an authentication service to validate users on the platform. So, how does a client access the microservices? This is a problem when you need to interact with multiple APIs.

An API Gateway can remove this complication and allow you to: change hosts and their locations, increase or decrease the number of service instances, and replace your existing service, for example, an ordering service, with a new one. The client’s access to the services remains undisturbed. The benefits of using an API Gateway are as follows: It insulates the clients from how the application is partitioned into microservices. In other words, it simplifies the client side by moving the logic for calling multiple services from the client to the API Gateway. It also provides the optimal API for each client, regardless of who the client is. It reduces the number of requests or round trips. For example, the API Gateway enables clients to retrieve data from multiple services with a single round trip.

And irrespective of how your microservices communicate internally, an API Gateway will provide a standard protocol to communicate with the outside world. Now, although an API Gateway provides many benefits, it also has some drawbacks. It is another component that needs to be developed and maintained. In addition, if not designed carefully, it can become a single point of failure in an application. Also, a Gateway will increase the response time due to this additional network step in the execution of the application. There are plenty of API Gateway products available on the market. You can choose from managed or open-source options.

From IBM, an industry-leading, high-security application gateway called IBM DataPower Gateway. Google has two offerings based on your needs: Apigee or Cloud Endpoints. Microsoft Azure and Amazon AWS also offer gateways on their platforms. And while those are managed products, in the open source world, some famous names are: Kong, being top of the list in popularity, Apache APISIX, Tyk, which also has a managed version, and finally, Gloo, which is also available as an enterprise version. In this video, you learned that: an API Gateway is the door to your backend services, it enables you to plug additional services while providing your client with unified access to your services, it hides the complexity of your backend services from the client, it makes it easier to scale or replace your backend services, and there are many managed and open source API Gateway products available to choose from.

---

### 3. [VIDEO TRANSCRIPT] Creating REST APIs Video • 2 min
- **URL:** https://www.coursera.org/learn/applications-development-microservices-serverless-openshift/lecture/E0Ob5/creating-rest-apis
- **Method:** `dom_transcript` | **Length:** 2159 chars

Welcome to ‘Creating REST APIs’. After watching this video, you will be able to: Create a RESTful API in Python, and use Flask to host your REST API. Python is a programming language that lets you work more quickly and integrate your systems more effectively. Python is used in many application domains. It supports Web development with the help of frameworks such as Flask. Python is widely used in scientific and numeric computing with the help of libraries such as SciPy for mathematics, science, and engineering. Python is also a popular choice among the Artificial Intelligence and machine learning community.

Flask is classified as a micro web framework as it does not require particular tools or libraries. It was built with scalability and simplicity in mind. Flask applications are known for being lightweight compared to other frameworks. Since Flask is not opinionated about what database or template engine to use, it is a good choice for RESTful APIs. For this module, you need Python 3 and pip, which is the Python package manager. Once you verify you have Python and pip, you can then proceed to install Flask with the pip install command. First, you create the hello.py file with the content shown.

You then run the Flask server to host this python file and the output will be displayed. When you open this ‘hello world’ web application in the browser by navigating to 127 dot 0 dot 0 dot 1 and port 5000, you will see the response “Hello World”. You will now create a new python file with the name ‘products.py’ which will provide all endpoints for your products microservice. You start with defining the imports and creating your default list of products. You are not using any database to persist these products, so every time you restart the API, you start with the same list of products. Next, you define the GET method to retrieve all the products. And this method implicitly returns ‘200’, which in HTTP means OK.

In this video, you learned that: Flask is a micro web framework to host Python web applications, you can create your first RESTful API as a microservice using Python, and you can host your first RESTful API using Flask.

---

### 4. [VIDEO TRANSCRIPT] Making API Requests using CURL and Postman Video • 4 min
- **URL:** https://www.coursera.org/learn/applications-development-microservices-serverless-openshift/lecture/9VPp3/making-api-requests-using-curl-and-postman
- **Method:** `dom_transcript` | **Length:** 3626 chars

Welcome to ‘Making API Requests using cURL and Postman.’ After watching this video, you will be able to explain how to use cURL to make HTTP requests, and explain how to use Postman to make HTTP requests. Transferring data to and from a server requires tools that support the necessary network protocols. Linux has multiple tools created for this purpose, the most popular being curl. curl, short for "Client URL” is a command line tool that enables data transfer over various network protocols. Developed in 1998, it has since been used to communicate with web or application servers by specifying a relevant URL and the data that need to be sent or received. curl can either be used at the command line or in scripts to transfer data. You can run a simple curl command, as seen in this example, and then view the output. The most common use cases for curl are: downloading files from the internet, endpoint testing, debugging, and error logging.

Some of the common protocols supported by curl are: HTTP, HTTPS, FTP, and IMAP. If you run this example curl command, you will receive the output as shown. curl accepts a wide array of options, which makes an extremely versatile command. Options start with one or two dashes, and if they do not require additional values, the single-dash options can be written together. So, let’s breakdown the command and output. ‘Hyphen x’ means you are explicitly specifying the HTTP function, which in this case is GET. We then specify the URL to evaluate. ‘Hyphen H’ allows you to define headers, which in our case is telling the web server that we want to work with JSON.

Our output is the list of products returned by the product’s microservice represented in JSON. Now, Postman is an API platform for building and using APIs based on a wide range of extremely user-friendly power tools, enabling the developers to easily create, test, share, and document APIs. Postman simplifies each step of the API lifecycle by allowing to orchestrate multiple requests which can be performed in several repetitions or iterations, and help you streamline collaboration so you can create better APIs—faster. And, due to its simplicity, it is one of the most popular and convenient tools for testing a wide variety of APIs supporting many protocols for example, HTTP requests like GET, POST, PUT, and PATCH--and then convert the API to code for languages like JavaScript and Python. A popular example is the WhatsApp Business Platform Cloud API that has created a streamlined, developer-friendly experience using Postman. With Postman, onboarding time reduces to minutes using automation and pre-filled data, which isn’t the case with alternative methods that require manual setup. Developers can progress from signing up for the WhatsApp Business Platform to testing phone numbers and building message calls in a few minutes.

You can download Postman to your computer or you can use the online version. For this course, we will use the online version which you will need to sign up for, and we will cover the steps in the next lab. Let’s now call the products microservice GET endpoint using Postman. Once in Postman, start with a new tab; the request type is GET, and the URL is the one where your microservice is hosted. Then click on the Send button to analyze the output. You can then save this in your workspace to call your API again in the future. In this video, you learned that: cURL is used for transferring data with URLs, cURL can be used at a command line or in scripts, Postman is an API platform for building and using APIs, and Postman is a simple and popular tool for testing APIs.

---

### 5. [VIDEO TRANSCRIPT] Documenting and Testing REST APIs with Swagger Video • 4 min
- **URL:** https://www.coursera.org/learn/applications-development-microservices-serverless-openshift/lecture/H4L9b/documenting-and-testing-rest-apis-with-swagger
- **Method:** `dom_transcript` | **Length:** 3568 chars

Welcome to ‘Documenting and Testing REST APIs with Swagger’. After watching this video, you will be able to document your REST API using Swagger, and test your REST API using Swagger. APIs specify an interface and connect different systems providing them with consistent communication. And API documentation is like a reference manual containing instructions on effectively using and integrating systems. Swagger saves time writing API documentation by running through the OpenAPI specification to ensure you meet the guidelines. Swagger allows you to describe the structure of your APIs so that machines can read them. With the API’s structure, Swagger automatically builds engaging UI and interactive API documentation.

This structure is defined in a JSON or YAML file that adheres to OpenAPI specifications. Now initially, APIs were not meant for self-service consumption. They were data-driven and solved a few special use cases of connection and communication. Whereas the OpenAPI Specification defines a standard, language-agnostic interface to RESTful APIs. The specification is language agnostic and human and machine-readable. In addition, it allows people and computers to discover and understand the capabilities of a service without requiring access to source code, additional documentation, or inspection of network traffic. It defines all the operations that your API supports, the required parameters and the expected return, and required API authentication.

And it even defines things like terms of service, contact information, and the license information for the exposed API. Now Flask enables exposure to Python functions as APIs. Flask Swagger UI improves upon its capabilities by allowing you to describe and visualize the REST APIs. To introduce the Swagger UI to your application, you need the Flask blueprint ‘Flask-swagger-ui’. The command ‘pip install Flask-swagger-ui’ will add the Swagger UI to your Flask application by using pip. First, you need to import the ‘swagger_ui_blueprint’, which will help you create the Swagger UI using Flask. Then you define the basic configuration, which consists of the path where the Swagger will be available.

You have kept it under the products/docs path in this example. The second argument displays where the swagger file is served. And the name you want to give to this Swagger. You then need to register this blueprint with the app for Flask. Swagger.JSON holds the definition and characteristics of your API in the form of a JSON file. You need to expose this file as well with your API. So, you need a route that will serve your static swagger.JSON file.

Swagger is a JSO file and requires some basic configurations to be present. Here in this example, you are creating the product microservice API swagger and providing the model and path for getting the products list. And defining the properties of the Product object. You now have an API definition and Swagger. You can use the UI to test your API and that is the key benefit of using Swagger. In addition, it allows consumers to get more details about your API, the supported functions, requests, and responses. It also displays content from the product info section.

It displays the only available method, a GET to retrieve all products. You can then execute that endpoint and see the outcome, which, in this case, is the list of products. In this video, you learned that Swagger helps you document your APIs, the OpenAPI specification is a standard way of representing your APIs, and Swagger provides a mechanism for testing your APIs.

---

### 6. [VIDEO TRANSCRIPT] Optional: Basics of GraphQL Video • 3 min
- **URL:** https://www.coursera.org/learn/applications-development-microservices-serverless-openshift/lecture/2smnm/optional-basics-of-graphql
- **Method:** `dom_transcript` | **Length:** 2594 chars

Welcome to ‘Basics of GraphQL’. After watching this video, you will be able to: Describe GraphQL, explain the key characteristics of a GraphQL API, and explain the benefits of using GraphQL APIs. GraphQL is a query language for your API. It provides a standard way to allow clients to request only the data that they need from the API. And it can be developed using any programming language, as it is language agnostic. GraphQL enables you to retrieve exactly what you need from the API. This means you don’t receive the data that you didn’t request.

It also means you receive exactly what you require, even from different resources. Unlike the RESTful API, GraphQL requires just one endpoint to retrieve everything you require. And as can be seen in this product example, you only need the name, and that’s what you receive. With REST, your APIs are the resources that provide endpoints to perform a particular operation using an HTTP method. In GraphQL, the types you define in the schema are the nodes. With REST, you make multiple calls and receive whatever is sent by the server. But in GraphQL, you only request and receive what you require.

Extending your GraphQL API doesn’t need a new version; you add the new fields without breaking the existing clients, as they were only requesting what they required. A Query is used for querying your data, more like a GET request in a RESTful API. At its simplest, GraphQL makes requests for specific fields on objects. A mutation is used for manipulating and modifying your data. And every field in the mutation type can be thought of as a POST, PUT, or DELETE request in a RESTful API. Now Netflix is known for its loosely coupled and highly scalable microservice architecture. Netflix produces original content at an accelerated pace.

From the time a TV show or a movie is pitched to when it’s available on Netflix, a lot happens behind the scenes. Initially, the relationships between entities were disparate and existed in various microservices. To address those challenges, the team started building a curated Graph API called “Studio API”. Its goal is to provide a unified abstraction on top of data and relationships. In this new design, Studio API is responsible for schema and resolving queries. So, the Netflix engineering team did not stop there and went a step ahead with federated architecture, where each team has the ownership of their respective domains. In this video, you learned that: GraphQL is a language-agnostic query language for your API, it provides you with exact data, no more and no less, and it has one endpoint.

---

### 7. [READING] Module 2 Summary Reading • 2 min
- **URL:** https://www.coursera.org/learn/applications-development-microservices-serverless-openshift/supplement/rV0mr/module-2-summary
- **Method:** `dom_reading_cml` | **Length:** 901 chars

Congratulations! You have completed this module. At this point in the course, you know that:

- REST APIs provide flexible but uniform interfaces between components
- REST APIs are stateless and scalable
- REST APIs communicate using HTTP methods POST, GET, PUT and DELETE
- REST is an architectural style defining how applications communicate
- API Gateway is the door to your backend services while also enabling you to plug additional services while providing unified access
- API Gateway makes it easier to scale or replace your backend services
- Flask is a micro web framework to host Python web applications
- cURL is used for transferring data with URLs and can be used at a command line or in scripts
- Postman is a simple and popular tool for building, testing, and using APIs
- Swagger helps you document and test your API
- OpenAPI specification is a standard way of representing your APIs

---
