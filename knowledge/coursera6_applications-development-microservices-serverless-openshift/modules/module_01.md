# Module 1: Introduction to Microservices

### 1. [VIDEO TRANSCRIPT] Course Introduction
- **URL:** https://www.coursera.org/learn/applications-development-microservices-serverless-openshift/lecture/b6hg7/course-introduction
- **Method:** `dom_transcript` | **Length:** 2830 chars

Welcome to this course: Microservices and Serverless. This course is designed for all software development professionals, including anyone who wants to design, develop, deploy, and manage, solutions using Cloud native technologies like microservices and serverless. Now, do you want to use cloud computing to manage all your business applications? Which solution would you prefer? A Monolithic architecture on the cloud that comprises a single huge application with many complex functions that is difficult to maintain? Or the Microservices architecture containing small applications which simplify maintenance, are easily managed, provide speed and scalability, and are easier to build? These smaller applications work together to perform the function of one large application.

Rather than building large applications, known as monoliths, that perform all the functionality, microservices break down larger applications into smaller pieces that are independently maintainable and scalable, providing a host of benefits. This architecture is used in the largest software organizations in the world because it provides cost benefits, team autonomy, and other advantages. Likewise, serverless has emerged as an increasingly popular computing option in the cloud era. This allows developers and operators to run applications without managing the underlying infrastructure. Serverless applications require only a serverless architecture for the core code. Serverless apps can be deployed quickly, and execute for a brief time, and automatically free up underlying resources when not in use. In this course, you will learn how to create microservices and deploy them on cloud using serverless technologies.

To do so, you will first get an overview of Microservices in Module 1, and understand their benefits. Next, in Module 2 you will learn to create RESTful APIs which are the basic building blocks for microservices based applications. Then, in Module 3, you will understand the benefits of the Serverless framework, and learn about the various serverless platforms. In Module 4, you will work with Code Engine, a serverless environment on IBM Cloud, to deploy, update, and scale microservices. And finally, in Module 5, you will complete a hands-on final project where you will demonstrate what you have learned throughout the course by creating an application based on microservices and deploy it using the serverless framework. So, there is a lot to cover here! To get the most from this course, complete viewing each video, complete all hands-on labs, and check your learning with each quiz.

We're very happy to have you with us as you start your microservices and serverless journey. And if you have any trouble with any of the course material, please don’t hesitate to contact us in the discussion forum. Let's get started!

---

### 2. [READING] Course Overview
- **URL:** https://www.coursera.org/learn/applications-development-microservices-serverless-openshift/supplement/JFxhL/course-overview
- **Method:** `dom_reading_cml` | **Length:** 6181 chars

Welcome to the Application Development Using Microservices and Serverless course. This course is intended for anyone looking to learn how to design, build, deploy, and manage secure, scalable applications using microservices and serverless technologies. This intermediate-level course is part of the IBM Full Stack Software Developer Professional Certificate:-

This course consists of 6 modules, with Module 6 being optional. They guide you through the essential areas of the fundamentals of microservices architecture.

The course contains several hands-on labs, which allow you to practice and apply the content you learn in the course. What makes it even more flexible is that you have two lab options to choose from—allowing you to select the programming language that aligns best with the Professional Certificate track you’re following. More details on this can be found in the next reading:  About the lab learning paths.

### Prerequisites

Before you begin this course, it is recommended to have a basic knowledge of programming concepts, cloud technologies, and containers (Docker/Kubernetes). Additionally, familiarity with the command line, shell, and either Python or JavaScript, depending on your chosen lab path, will be beneficial.

To strengthen your foundation, you may review these courses from the IBM Full Stack Software Developer Professional Certificate:-

- Introduction to Cloud Computing
- Getting Started with Git and GitHub
- Introduction to Containers w/ Docker, Kubernetes & OpenShift

### Course objectives

After completing this course, you will be able to:-

- Explain microservices and serverless concepts, comparing them with monolithic architectures to understand their advantages and trade-offs
- Build and test RESTful APIs and deploy applications using IBM Cloud Code Engine
- Explore OpenShift and service mesh technologies to enhance microservices management and communication
- Apply learned skills through a hands-on microservices project in a real-world context

### Course outline

Module 1: Introduction to Microservices: In this module, you will explore the fundamentals of microservices architecture and how it improves flexibility and scalability compared to monolithic and SOA systems. You will learn best practices for development, deployment, and operations, along with patterns such as SPA, BFF, and Strangler. The module also highlights common pitfalls and anti-patterns to avoid. By the end, you will be able to apply the Twelve-Factor App methodology, design resilient microservices, and evaluate when microservices are the right choice.

Module 2: Web API Essentials: REST API and GraphQL: This module introduces REST architecture and its role in enabling scalable communication between services. You will gain hands-on experience building a RESTful API with Python and Flask, documenting it using Swagger, and testing it with cURL and Postman. You will also learn the importance of API Gateways for abstracting backends and securing services, and explore how GraphQL provides flexible, precise data access. By completing this module, you will develop practical skills in designing, documenting, and testing APIs that are core to microservices communication.

Module 3: Serverless Overview: Here, you will learn what serverless computing is and how it differs from traditional and container-based models. The module covers the Function-as-a-Service (FaaS) model, its benefits, limitations, and best practices for use. You will also explore the Serverless Framework, its components, and real-world use cases across industries. By the end, you will be able to identify when serverless is the right approach, compare it with other models, and design lightweight, event-driven applications with reduced infrastructure management.

Module 4: Create and Deploy Microservices with Serverless: In this module, you will gain hands-on skills using IBM Cloud Code Engine to build and deploy containerized applications. You will learn how Code Engine supports use cases such as application deployment, building from source, and running jobs. Through practical exercises, you will use Dockerfiles to create container images and deploy them using both the IBM Cloud Console and CLI. This module will strengthen your ability to work with container-based microservices and deploy them on a serverless platform that automatically scales.

Module 5: Final Project: This module gives you the opportunity to apply what you have learned across the course. You will build a serverless web application by creating and invoking IBM Cloud Functions, including sequence actions, and deploying the app using OpenShift. You will also create an API to manage your functions and publish your project on GitHub. Finally, you will review your peers’ projects using a structured rubric. By completing this module, you will gain end-to-end experience in designing, deploying, and evaluating real-world cloud-native applications.

Module 6: Optional: OpenShift essentials/Working with OpenShift and Istio: In the final module, you will explore how Red Hat OpenShift builds on Kubernetes to simplify the provisioning, management, and scaling of applications. You will learn about the services OpenShift provides for developers and operators, as well as the challenges of managing distributed microservices. The module introduces service meshes such as Istio, explaining how they improve security, observability, and traffic management between microservices. By the end, you will have the skills to deploy applications on OpenShift, understand its relationship with Kubernetes, and evaluate how service meshes help organizations run microservices at scale.

### Tools/Software

In this course, you will use free versions or trials of several tools:

- Lab environment
- GitHub Account
- Cloud Engine (provided in the lab environment)
- Docker (provided in the lab environment)

By the end of this course, you will have hands-on experience in creating microservices, deploying serverless applications, and using tools to build and manage them efficiently.

Congratulations on taking these steps to further your knowledge and career! Enjoy your learning journey.

---

### 3. [VIDEO TRANSCRIPT] Twelve-Factor App Methodology Video • 8 min
- **URL:** https://www.coursera.org/learn/applications-development-microservices-serverless-openshift/lecture/plf5j/twelve-factor-app-methodology
- **Method:** `dom_transcript` | **Length:** 6878 chars

Welcome to ‘Twelve-Factor App Methodology’. After watching this video, you will be able to: Describe the characteristics of modern software development, describe the goal of twelve-factor apps, and identify the twelve factors and describe how these factors map to three phases of the software delivery lifecycle. In modern software development, the software is often delivered as a service. Software is centrally hosted and accessed through the internet. This software is often called a web app or software-as-a-service, abbreviated to SaaS. You have likely used a variety of web apps within the last day! When you use the internet to book reservations or file your taxes, you are interacting with a web app.

The twelve-factor app methodology is suited for these types of applications. Microservices are not a requirement for twelve-factor apps. However, microservices are often used in conjunction with the twelve-factor application methodology. The twelve factors can be grouped into the code, deploy, and operate phases of the software delivery lifecycle. We’ll start with the three factors that map to the code phase of the software delivery lifecycle. The first is Factor 1, Codebase. You should always track the codebase for an application in a version control system, such as Git.

There is a one-to-one relationship between a codebase and an app. An app should be contained in a --single-- codebase. However, there will be multiple deploys, or instances, of the app. And while the codebase is the same across those deploys, different app versions can be present in each deployment. For example, dev or test environments can have changes that have yet to reach production. Next is Factor 5: Build, release, and run. This phase demonstrates how a codebase becomes a production deployment.

The build stage compiles the code, gathers dependencies, and then transforms the codebase into an executable unit called a build. The release stage combines the build with the deployment’s current configuration so that the code is ready to run. Then, the run stage implements the application. You should strictly separate these three stages. For example, the code should not be changeable at runtime, as that would prevent those changes from being included in the build stage. Factor 10 is dev/prod parity. This factor minimizes the differences between development and production environments, which is necessary to enable continuous delivery to quickly promote changes into production.

This action reduces the chance that code runs appropriately in one environment but not in another. Parity is particularly essential for backend services. If you use MySQL database in production, you should use the same version of MySQL database in your development environments. Parity helps catch failures earlier in the development process. And the last code factor we’ll discuss is Factor 2, Dependencies. An app is only as reliable as its least reliable dependency. As a result, twelve-factor apps do not rely on the implicit existence of any packages, dependencies, or tools.

You must explicitly declare all dependencies. This way, when a new developer grabs the codebase, there is no assumption that any dependencies already exist on their machine. The first deploy factor is Factor 3, Config. The configuration is everything that can differ between deployments. Different databases are likely used in staging and production, so a developer should configure that database’s credentials and location per deployment. You should avoid storing configurations as constants since configurations might differ among environments. Store the config within the environment variables, which are easy to change across deployments without changing the code.

Factor 4 is Backend services. A twelve-factor app should not distinguish between local and third-party services. Both should be accessible via a URL or other location information along with any credentials so that a developer can easily swap out the backend service without changing the code. For example, if a database experiences problems, a new database can be spun up and substituted in without having to change code. Factor 6 is Processes. An app executes in an environment as one or more processes. Processes should be stateless and share nothing.

You should store persistent data in a backend service like a database since memory and filesystems aren’t shared across processes. If another process handles a subsequent transaction, the subsequent transaction won’t have access to data within the prior process. As a result, data needs to be centrally stored. Port binding is Factor 7. When you create a web-facing service, a web server should not be injected into an application at runtime. Instead, the web app should export HTTP by binding to a port and listening to incoming requests on that port. You can use port binding for HTTP and other services.

Binding a port is generally done in the code by declaring a web server library as a dependency. And subsequently, because these apps are accessible via a URL, they can become backend services for other apps. Next are the operate factors. Let’s begin with Factor 8, Concurrency. An application runs concurrent processes to handle the increasing load. And since processes are stateless and share nothing, an application can start additional processes to scale horizontally and handle additional incoming requests without creating interdependencies among processes. Factor 9 is Disposability, and it specifies that application processes require minimal startup time and should end gracefully when terminated.

Quick startup lets you quickly deploy changes to code or config. And you can also easily scale apps because new deploys start quickly. Factor 11 dictates how to handle logs. Logs give visibility into application performance, so an app should not concern itself with storing logs. Instead, an application environment should handle logs as a stream of events written to standard output. The execution environment can capture the log streams for all running apps, aggregate them, and route them to their destination. And this action is especially beneficial when the destination is a log analysis tool.

Finally, the last factor is Factor 12: Admin processes. Admin processes are one-off processes for managing an app, such as database migration. Admin processes run against a release using the same codebase and config. Additionally, the application code should include admin processes so that they remain synchronized with the app. In this video, you learned that: Modern software development often delivers centrally hosted, web-based, software-as-a-service applications, the twelve-factor app methodology enables developers to create more efficient SaaS applications, and the twelve factors map to the code, deploy, and operate stages of the software delivery lifecycle.

---

### 4. [VIDEO TRANSCRIPT] What are Microservices? Video • 3 min
- **URL:** https://www.coursera.org/learn/applications-development-microservices-serverless-openshift/lecture/UcN2s/what-are-microservices
- **Method:** `dom_transcript` | **Length:** 2634 chars

Welcome to ‘What are Microservices?’ After watching this video, you will be able to describe what microservices are, explain the benefits of microservices architecture, and explain how microservices can be scaled. Microservices architecture is an approach in which a single application is composed of many loosely coupled and independently deployable smaller services. These services typically have their own technology stack, inclusive of the database and data management model. Teams can even choose different programming languages for different components as they are dependent on each other via an API endpoint. Microservices components communicate with one another over a combination of REST APIs, event streaming, and message brokers, and they are segregated and organized by business functionality, with the line separating services referred to as a bounded context. Since there is no interdependency between services, you can update code more easily to add new features or functionality without touching the entire application.

Each team can choose its own technology stack which suits its needs and expertise to build components for which the team is responsible. And these components can be scaled independently of one another, reducing the waste and cost associated with having to scale entire applications because a single feature might be facing too much load. So, wherever you see scaling of microservices, it usually involves horizontal scaling. Horizontal scaling means scaling by adding more instances of resources, also described as “scaling out”. With microservices, individual services can be individually deployed and scaled. Done correctly, microservices require less infrastructure because they enable precise scaling of only the components that require it, instead of the entire application in the case of monolithic applications. An API call is often an effective way of initially establishing the state for a given service.

However, it’s not a particularly effective way of staying up to date on progress. This is where event streaming can help broadcast the state change, which helps in scaling the microservice by introducing this message broker. In this video, you learned that: Microservices make each application component its own service, and each service communicates via an API, microservices allow application components to use different technology stacks, microservices enable individual components to scale in response to demand, microservices lessen risks associated with change because components can iterate independently, and failures in one service do not necessarily impact other services.

---

### 5. [VIDEO TRANSCRIPT] Comparison of Monolith vs. SOA vs. Microservices Video • 5 min
- **URL:** https://www.coursera.org/learn/applications-development-microservices-serverless-openshift/lecture/DrpUR/comparison-of-monolith-vs-soa-vs-microservices
- **Method:** `dom_transcript` | **Length:** 4278 chars

Welcome to ‘Comparison of Monolith vs. SOA vs. Microservices’. After watching this video, you will be able to define Monolith implementation, define Service Oriented Architecture (SOA), and define Microservices. A monolithic application has all or most of its functionality within a single process. And the application is managed in internal layers or libraries. These layers could be for security, reporting, analytics, user interface, or data access.

The layers are tightly connected and dependent on each other. And this is where the benefits of a monolithic design lie; in its simplicity and less cross-cutting of features and functionalities since everything is in the same code base. However, over time, most products develop and increase in scope, and the design becomes more complex and difficult to modify. It also becomes a barrier to adapting to new technology which would mean re-writing the whole application. A Windows Forms Application is a typical example of a Monolithic design. Here we embed the user interface, business logic, and data access, all inside one codebase which forms the whole application. And only the database is outside the scope.

A Service Oriented Architecture (SOA) is designed and built with a service provider and consumer approach. The services provided work as a discrete unit of functionality, integrated seamlessly, and are easily reused. Each SOA service consists of three components. The interface defines how a service provider will execute requests from a service consumer, the contract defines how the service provider and service consumer should interact, and the implementation is the service code. The benefits of having these three separate components are that they help increase reliability and support parallel development due to a fixed contract between the services. However, due to these expectations and requirements, an SOA design can become complex and obstruct rapid application development. And the SOA design is an expensive investment, and therefore usually only suits enterprise teams, who can invest the required resources and expertise.

SOA is an enterprise-wide concept. An example would be a banking system. It enables existing applications to be exposed over loosely coupled interfaces, each corresponding to a business function that enables applications, in one part of an extended enterprise, to reuse functionality in other applications. Each interface of the bank provides services to accomplish its responsibility. Like SOA, microservices architectures comprise loosely coupled, reusable, and specialized components that often work independently of one another. And even the data in a microservice is not shared with other services, which helps you to scale individual microservices independently, and being independent also means you have the liberty to select the underlying technology. This architecture provides benefits such as ease of development, where you can define individual work units as a service.

And since each service has a designated responsibility, you have the flexibility to add new technology. But while there is a compelling case for using microservices, there are some challenges associated with it too. The first one is the security aspect. Now that you have so many different services independently hosted, each will need its own security paradigm. For example, a simple requirement, such as transport layer security (or TLS), to secure network communications. And the second is that debugging and isolating issues can also become harder, since each service runs independently, meaning you may find it challenging to locate the root cause. Microservices architecture is an application-scoped concept.

For example, an e-commerce application can have separate microservices to process orders, security, and analytics. A microservices design enables the internals of a single application to be broken up into smaller pieces that can be independently changed, scaled, and administered. However, it does not define how applications talk to one another. In this video, you learned that monolithic design is interconnected and interdependent, SOA design provides seamless integration and reusability, and Microservices architecture gives you targeted scalability and flexibility.

---

### 6. [VIDEO TRANSCRIPT] Microservices Patterns Video • 6 min
- **URL:** https://www.coursera.org/learn/applications-development-microservices-serverless-openshift/lecture/hrqIe/microservices-patterns
- **Method:** `dom_transcript` | **Length:** 5334 chars

Welcome to ‘Microservices Patterns’. After watching this video, you will be able to describe patterns you can use with microservices, and explain the usage of different patterns. Microservices have numerous patterns available that enable some of the more common challenges and opportunities. Examples are the single-page application (or SPA) pattern, the Backend for Frontend (or BFF) pattern, the Strangler pattern, and the service discovery pattern. With the convergence of more powerful browsers, faster networks, and client-side languages, many web interfaces began incorporating all functionality into single-page applications. The user enters through one interface that never reloads the landing page or navigates away from the initial experience. Built using a combination of HTML, CSS, and JavaScript, these applications respond to user input through dynamic service calls to backend REST-based services that update portions of the screen instead of redirecting to an entirely new page.

This application architecture often simplifies the front-end experience, with the tradeoff of more responsibility on the backend services. While a single-page application works well for single-channel user experiences, it delivers poor results across user experiences through different channels, like mobile and web. A Backend for Frontend pattern inserts a layer between the user experience and the resources that the experience calls on. This design allows for customized user experiences between channels. For example, an app used on a desktop will have a different screen size, display, and performance limits than an app used on a mobile device. The BFF pattern allows developers to create and support one backend type per user interface using the best options for that interface rather than trying to support a generic backend that works with any interface but may negatively impact frontend performance. This diagram illustrates a great use case for a Backend for Frontend application architecture.

Suppose a user can access an application via a mobile app or a web application on a desktop. When applying a BFF pattern, you develop one backend specifically for the mobile experience and another backend for the web experience. Each backend knows how to call the correct services and orchestrate code to optimize the requested channel's experience. The mobile app might display a more limited subset of data, and the screen sizes will differ from the web experience. Each backend is a microservice. And instead of having a monolithic app that checks which channel is needed and then contains all the logic to prepare the user experience for that channel, you apply microservice architecture to separate the monolithic backend into distinct services that perform their specific, necessary tasks. The Strangler pattern helps manage the refactoring of a monolithic application in stages.

The pattern gets its metaphorical name from the garden phenomenon of a vine that strangles a tree. Think of a web application built using individual URLs that map functionally to different aspects of a business domain. With the Strangler pattern, you use the structure of a web application to split an application into multiple functional domains and replace those domains with a new microservices-based implementation for one domain at a time. These two aspects form separate applications that exist side-by-side in the same URL space. Over time, the newly refactored application replaces the original application until finally, you can shut off the monolithic application. The Strangler Pattern includes these steps: First, transform. This creates a parallel new site on a cloud platform or within your existing environment.

Next, coexist. This leaves the existing site functional and live for a specified time. It incrementally redirects from the current location to the new site for newly implemented functionality. And finally, eliminate. This removes the outdated functionality from the existing site or stops maintaining that functionality when you redirect traffic from the original site. Now, a service discovery pattern helps applications and services discover each other. This pattern is needed because, in a microservices architecture, service instances change dynamically due to scaling, upgrades, service failure, and even service termination.

A load balancer could also use this pattern to do health checks and rebalance traffic on service failures. Other patterns include the entity and aggregate pattern, which could be used in an e-commerce site, where an order would be an aggregate of products grouped by a buyer. Another is the adapter pattern. Think of it in the way you think of plug adapters when traveling to another country. The purpose of adapter patterns is to help translate relationships between objects that are otherwise incompatible. For example, if you have integrated with a third-party API. In this video, you learned that microservices enable single-page applications that rely on backing services to update the page dynamically, Backend for Frontend patterns use microservices to facilitate different user experiences more easily, you can apply the Strangler pattern to help break up monolithic apps into microservices, and a service discovery pattern helps applications and services discover each other.

---

### 7. [READING] Microservices Anti-Patterns Reading • 10 min
- **URL:** https://www.coursera.org/learn/applications-development-microservices-serverless-openshift/supplement/odDUp/microservices-anti-patterns
- **Method:** `dom_reading_cml` | **Length:** 3150 chars

While there are many patterns for doing microservices well, an equally significant number of patterns exist that can quickly get any development team into trouble. The following are some of the don’ts while developing microservices:

## Don’t build microservices

The first rule of microservices is don’t start with microservices. When you determine that the monolithic application's complexity negatively affects application development and maintenance, consider refactoring that application into smaller services.

When the application becomes too large to update and maintain easily, these microservices will become ideal for breaking down the complexity and making the application more manageable.

However, until you feel that pain, you don’t even have a monolith that needs refactoring.

## Not taking automation seriously

If you have a monolith application, you only need to deploy one piece of software. Once you move to a microservices architecture, you will have more than one application with each having different code, test, and deploy cycles.

Attempting to build microservices without either:

- proper deployment and monitoring automation, or
- managed cloud services to support your now sprawling, heterogenous infrastructure

is asking for a lot of unnecessary trouble.

So, when you are building microservices, always use DevOps or cloud services.

## Don’t build nanoservices

If you go too far with the micro in microservices, you could easily find yourself building nanoservices! The complexity of which will outweigh the overall gains of microservices architecture.

Lean toward creating larger services and create smaller services when:

- Deploying changes becomes difficult
- The common data model becomes overly complex
- Loading and scaling requirements no longer synchronize and affect application performance

## Don’t turn into SOA

The two concepts; microservices and service-oriented architecture (SOA) are often confused with one another because, at their most basic level, both build reusable individual components that can be consumed by other applications.

However, microservices are fine-grained with independent data storage for each, that is, the bounded context.

A microservices project that morphs into an SOA project will likely buckle under its own weight.

## Don’t build a gateway for each service

Instead of implementing end-user authentication, throttle, orchestrate, transform, route, and analytics in each service, you should use an API Gateway.

An API gateway is an API management tool that sits between a client and your collection of backend services.

This will become central to the above-mentioned non-functional concerns and will avoid re-engineering them with each service.

## Conclusion

The aim of microservices is to solve the three most frequent challenges, that is, enhance customer experience, be flexible to new requirements, and reduce costs by providing business functions as fine-grained services.

But while doing so, you should avoid the pitfall of the above-mentioned anti-patterns making microservices a nuisance to your development, delivery, and management requirements.

---

### 8. [READING] Module 1 Summary Reading • 2 min
- **URL:** https://www.coursera.org/learn/applications-development-microservices-serverless-openshift/supplement/eYCi6/module-1-summary
- **Method:** `dom_reading_cml` | **Length:** 897 chars

Congratulations! You have completed this module. At this point in the course, you know that:

- Modern software development often delivers centrally hosted, web-based, software-as-a-service (SaaS) applications
- Twelve factor app methodology enables developers to create more efficient SaaS applications
- The twelve factors map to the code, deploy, and operate stages of the software delivery lifecycle
- Microservices make each application component its own service, and each service communicates via an API
- Microservices allow application components to use different technology stacks
- Microservices enable individual components to scale in response to demand
- Microservices lessen risks associated with change because components can iterate independently
- Failures in one service do not necessarily impact other services
- There are some anti-patterns to avoid when building microservices

---
