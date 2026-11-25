# Module 1: Python Coding Practices and Packaging Concepts

### 1. [READING] IBM Product Spotlight: IBM Bob Reading • 2 min
- **URL:** https://www.coursera.org/learn/python-project-for-ai-application-development/supplement/iw97f/ibm-product-spotlight-ibm-bob
- **Method:** `dom_reading_cml` | **Length:** 598 chars

Welcome to the course! As you learn to develop AI applications, discover Bob, IBM's AI-powered vibe coding tool that helps you build applications faster using natural language.

Bob is a development tool that turns your ideas into working code. Describe what you want to build, and Bob helps you write, debug, and ship it.

What You Can Do with Bob:

- Generate working code from natural language descriptions
- Accelerate your development workflow with AI
- Debug and refine code through conversation
- Build applications faster without starting from scratch

Try Bob: https://ibm.biz/coursera-bob

---

### 2. [VIDEO TRANSCRIPT] Introduction to the Course Video • 2 min
- **URL:** https://www.coursera.org/learn/python-project-for-ai-application-development/lecture/XE8yU/introduction-to-the-course
- **Method:** `dom_transcript` | **Length:** 2340 chars

[MUSIC] Welcome to this course on developing AI-based applications using Python and Flask. Python is among the top 10 widely used programming languages globally, according to a survey conducted by StackOverFlow. Flask is a Python micro-framework with minimal to no dependence on external libraries. Using Python and Flask, a programmer can develop concise applications, even incorporate components of AI, and can also easily be part of a scalable solution. After completing this course, you will be able to: Describe the steps and processes involved in creating an application. Create Python modules, run unit tests, and package applications. Deploy applications on the web using the Flask framework.

And create and deploy an AI-based application onto a web server using IBM Watson Embedded AI Libraries and Flask. This course is intended for anyone with basic programming knowledge, an elementary understanding of Python, and is interested in building reusable web applications with AI integration. Module 1 will introduce you to the basics of application development, including the lifecycle and best practices for coding. You will also have the opportunity to create modules, run unit tests, and package applications. You will learn the ideal coding practices for Python and learn how to run static code analysis. In Module 2, you will start with an introduction to Flask. Next, you will be introduced to deployment concepts, including routes, request and response objects, error handling, and decorators.

You will also be able to create and deploy an application using Flask. Finally, in Module 3, you will have the opportunity to apply all your knowledge from the previous modules to develop functional web applications and AI-based web applications using Watson Embedded AI Libraries. With one practice project and one graded project, you will be able to demonstrate your proficiency in creating and deploying applications using Flask. You must submit your work for the graded project. There is a lot to cover here. To get the most from this course, make sure to view every video, check your learning with each quiz, and complete all the hands-on labs. If you have any trouble with any of the course material, please don't hesitate to contact us in the discussion forum.

Thank you for being part of our course, and welcome! [MUSIC]

---

### 3. [READING] Helpful Tips for Completing this Course Reading • 3 min
- **URL:** https://www.coursera.org/learn/python-project-for-ai-application-development/supplement/zRLeh/helpful-tips-for-completing-this-course
- **Method:** `dom_reading_cml` | **Length:** 2265 chars

### Helpful tips for course completion

Welcome to Developing AI Applications with Python and Flask. In this three-week class (and an optional fourth week), you can expect to spend approximately 2-3 hours per module. Here are some tips regarding self-paced learning and getting the most out of this class.

1. Familiarize yourself with the course content

Browse the module overviews and objectives to get a feel for the topics presented and the assets associated with the topic of each module. Get accustomed to the order of the content that will be presented. Knowing upcoming topics helps you connect the ideas together to form a cohesive whole. An outline of the modules is presented below.

2. Plan and make a rough timeline for completion

Now that you are familiar with the topics in each module look at the overall completion time estimates for the assets in the modules. Set a reasonable goal for yourself to complete each module. Determine when you would like to finish the course and schedule time each day to study.

3.Actively consume each asset

Dedicate time and a place to study without distractions.

Take notes while watching the instructional videos or download the transcripts and highlight the parts of the narration that you think are most important.

Complete all of the practice quizzes. Read all of the feedback for correct and incorrect responses. Retake the practice quizzes until you get all of the answers correct.

Complete all of the graded quizzes. The incorrect responses will direct you to the video addressing that information. Review the video or the transcript to identify the correct response and ascertain why that answer is correct. Retake graded quizzes until you pass.

Use the cheat sheets to review the terms and code found in each module.

Complete all labs to gain hands-on experience with the ideas taught in the videos.

4.Talk to your friends and family about the course

Keep yourself accountable and commit to the course by talking to your friends and family. Engage them in conversation when you find a topic that piques your interest or where you think another perspective may be beneficial.

5. Follow your plan

Now that you have a plan, keep yourself motivated by rewarding yourself as you achieve your goals.

---

### 4. [READING] Prerequisites and Course Syllabus Reading • 5 min
- **URL:** https://www.coursera.org/learn/python-project-for-ai-application-development/supplement/6aiqr/prerequisites-and-course-syllabus
- **Method:** `dom_reading_cml` | **Length:** 602 chars

## Course Prerequisites

To get the most out of this project course, we suggest completing IBM's Python for Data Science, AI and Development course or building equivalent skills in Python and data work beforehand.

## Course Syllabus

### Module 1: Python Coding Practices and Packaging Concepts

- Lesson 1: Application Development and Packaging using Python

### Module 2: Web App Deployment using Flask

- Lesson 1: Web application deployment using Flask

### Module 3: Creating AI Application and Deploy using Flask

- Lesson 1: Practice Project
- Lesson 2: Final Project
- Lesson 3: Course Wrap-up

---

### 5. [VIDEO TRANSCRIPT] Application Development Lifecycle Video • 6 min
- **URL:** https://www.coursera.org/learn/python-project-for-ai-application-development/lecture/mWKhF/application-development-lifecycle
- **Method:** `dom_transcript` | **Length:** 6376 chars

Welcome to “Application Development Lifecycle.” After watching this video, you will be able to: List the steps in the application development lifecycle Describe the different phases of the application development lifecycle And recognize the importance of writing application codes in multiple files Imagine this. A customer requests you to build an application to help their employees track their daily tasks. Now, consider a scenario where a customer wants you to build a web app to manage hotel reservations, from creation to customer check-out. In either scenario, can you start building the application when the customer makes a request? Not really! You will need to perform certain activities like analyzing requirements, planning, and coding before the application is ready for users.

Regardless of the application type, every application will go through different phases, called the application development lifecycle. You can divide the application development lifecycle into seven phases: Requirement gathering, analysis, design, code and test, user and system test, production, and maintenance. Let’s look at each of the application development phases in detail. Requirement gathering is the first phase in the application development process. In the requirement gathering phase, you will capture the requirements across all aspects of the application, including user requirements, business requirements, and technical requirements. Let’s consider the hotel reservation app. For this app, a user requirement may be that users must be able to view the different rooms and amenities available.

Determining the right charge for different rooms and amenities may be a business requirement. A technical requirement might be that the app must run on all browsers and mobile devices. The goal should be to capture as many requirements as possible, even if it seems redundant or trivial. You must also identify any constraints of design and viability of the business model. For example, for the hotel reservation app, one constraint is that the server needs to keep the status of room availability updated at all times, which has an associated cost. Therefore, to keep the business viable, a minor convenience fee is added to the final payment. After gathering the requirements and constraints, you must analyze each to create a possible solution for the application’s design.

During analysis and design, there might be multiple rounds of verification and revision to create a model solution that meets all the specified requirements. Across the analysis and design phases of application development, you must maintain proper documentation with records of all updates in the design. This documentation should be clear and concise as used during the code and test phase. The final proposed design and the specified requirements are passed on to the code and test phase. During the code and test phase, the team uses the programming requirements specified in the design documentation to code, test, revise, and test the application programs until the code meets all documented requirements. Let’s review the testing phase. The tests you conduct for the unit code is called unit testing.

Conduct the unit testing at the programming level to ensure you meet all required specifications. After the unit testing, you can generate an acceptable application version. The new version of the application is then run through a series of user and system level tests. The user tests verify the functionality from a user’s point of view. In addition, you will need to execute several system-level tests, including integration and performance testing. Integration tests verify that all involved programs continue functioning as expected after integration. Integration testing also verifies that the application functions within a larger framework.

Performance testing helps evaluate the speed, scalability, and stability of the application based on varying workloads. After testing, you can generate a new application version and send it to production. Once in production, end users can access and use it. You must ensure that the application functions accurately and is available to users. When the application is in the production phase, it must remain in a steady state. In a steady state, you should not make any changes to the application. However, this is not always possible.

For example, you might need to make changes to the application in case of an error. These changes are tightly controlled and heavily tested before being implemented into production. The last phase in the application development lifecycle is maintenance. The application might need an upgrade, or you might need to add new features. In this case, the new features must go through all previous phases before being integrated into the application version deployed in production. Let’s briefly review why maintaining multiple files for coding different functionalities is a best practice. Every app usually has multiple functionalities, and the requirements for each functionality might vary.

The best practice is to code each functionality in separate file. You can then create a central program, which runs the application and calls the individual files to perform specific functions. This approach to organizing code makes code maintenance efficient and easy. Having multiple files also helps when you need to add new functionality to an existing application. When you write the code for new functionality in a separate file, only the file will go through the entire design and verification process before being integrated into the running application. In this video, you learned that: The application development lifecycle has seven phases, including: Requirement gathering, where you collect user, business, and technical requirements for the app Analysis, where you analyze the requirements Design, where you design the complete solution Code and test, where you build and test the different components of the app User and system test, where users test the app for usability, and you perform system integration testing and performance testing Production, where the application is available to all end users Maintenance, where you upgrade or fix any user or system issues For efficient coding, always use a central program to call the individual files and functions for performing different actions.

---

### 6. [VIDEO TRANSCRIPT] Introduction to Web Applications and APIs Video • 4 min
- **URL:** https://www.coursera.org/learn/python-project-for-ai-application-development/lecture/KgsLc/introduction-to-web-applications-and-apis
- **Method:** `dom_transcript` | **Length:** 4311 chars

Welcome to “Introduction to Web Applications and APIs.” After watching this video, you will be able to: Describe web applications or web apps Describe an Application Programming Interface (or API) Compare and contrast web apps and APIs Let’s start by defining a web app. A web app, is a program stored on a remote server and delivered over the internet. A user interacts with the app using a browser. Web services like e-commerce sites, webmail, and so on, are all web apps. While some apps may depend on the kind of browser being used, most web apps work on all modern web browsers. A web app requires three components to process a client request: a web server to manage raised requests, an app server to execute the requested task, and a database to store the information needed to complete the task.

When programming web apps, you will write code for the user end or the front-end using JavaScript, HTML, or CSS. You will also code for the server-end or back-end using Python, Java, or Ruby. There are several advantages to using web apps over apps that strictly run locally on a user’s system. The advantages include: Developers can make the same version of the app available to multiple users at the same time. Users have the flexibility of using the app from their platform of choice, such as desktop, laptop, or mobile device. Users can access the app through the browser of their choice. Users do not need to install the app on their local systems.

An API is a software component that enables two apps that are not connected with each other to communicate. APIs help create more flexibility for programmers and enable them to request data from otherwise closed-off apps. As a result, APIs have standardized rules and functions that determine what data can be taken or modified within an app and how that process occurs. For example, the apps on your phone require you to grant permission to different features of your phone, like location, camera, audio, and recorder. An example of an app that uses an API is a weather app. Your weather app does not generate weather data itself. Instead, it simply requests information from a weather API.

The API connects the software that gathers and stores weather data with the app on your mobile device. The device, in turn, provides you with a detailed forecast for the next day. There are several architectures software developers follow to create an API, but the most popular is Representational State Transfer (or REST), or Simple Object Access Protocol (or SOAP). These architectures will be discussed in another video. An API can be beneficial for many reasons, including it: Improves connectivity between apps. Supports traditional create, read, update, delete (or CRUD) actions. Works with HTTP verbs including, PUT, POST, DELETE, and GET.

Is based on HTTP, making it customizable. API is a more generic term given to all forms of apps that create a link between any two parts of a system. Web apps are a form of API that communicate between the front end and the back end. To clarify the distinction between web apps and APIs, let’s consider the example of an e-commerce shopping service. When you access the e-commerce shopping service from a browser, the browser acts as the API that connects you to the web app. When you select a product, the web app checks the availability of the product and, if available, displays its price. If you try to access the e-commerce shopping service using a mobile device, the app in your device acts as the API that connects to the e-commerce shopping service.

The nature of all web apps is to share data with other apps; essentially, all web apps may be considered APIs. However, API is a generic term and includes both “online” or web-based, and “offline” apps. To summarize, all web apps are APIs, but not all APIs are web apps. In this video, you learned that: Web apps are programs stored on a remote server and delivered over the internet through a browser. You can run web apps on different platforms and browsers without having to install new software. An Application Programming Interface, or API, is a software component that enables two unconnected apps to communicate. Web apps are APIs, but not all APIs are web apps.

Both share data between apps, but not all APIs require networks like web apps do.

---

### 7. [VIDEO TRANSCRIPT] Demo: Working with an IDE Video • 5 min
- **URL:** https://www.coursera.org/learn/python-project-for-ai-application-development/lecture/i6zrI/demo-working-with-an-ide
- **Method:** `dom_transcript` | **Length:** 4872 chars

Hello everyone, and welcome to the demo on the Cloud IDE (or Integrated Development Environment) provided by the IBM Skills Network team. Cloud IDE is a programing environment for learning, which you can use for writing, running, debugging, and executing code directly in a browser, without the need to install or configure any software or tools on your personal device. In this demo, you will learn to: Navigate the different components of the Cloud IDE Install the Python packages or libraries Write code Execute code When you open the Cloud IDE, two main panes will be displayed. The left pane is referred to as the instructional pane. It displays the instructions that you need to follow to finish the project. The pane on the right displays a programming interface, where you can write and execute your code. Please note that the right pane is similar to the VS code interface, which is a popular IDE for managing code.

You can resize the instructional and code panes. For example, you can reduce the size of the instructional pane by dragging it from its margin towards the left. Or, you can increase the size by dragging the instructional pane towards the right. You also have the option to modify the fonts and font size based on your preference. If there are multiple pages in the instructional pane, you will see the Next and Previous buttons. These buttons enable you to navigate between the pages. You can also preview an instructional page.

Notice the Table of contents button on the top left corner of the instructional pane. Use this button to navigate through different sections of the instructions. Next, let’s look at an AI-enabled chatbot available on the Cloud IDE. The IBM Skills Network team provides you with a AI enabled Teaching Assistant chatbot called Tai, which provides you with help using the lab environment for coding assignments. The icon for Tai is available on the left side of the instructional pane. To access the chatbot, simply click the icon. Let’s try asking a question, like Please provide me with simple Python code.

As you can see, the code is displayed. You can either copy or execute the code. Next, let’s look at the programming interface of the IDE. The programming interface has several components. However, the two tabs that you will use frequently include the Editor tab, where you write the code, and the Terminal tab, where you execute the code. In the programming pane there is also a Skills Network Toolbox, which enables you to work with various database management environments, big data tools, cloud tools, embedded AI libraries, and launch applications that you build. Before you begin writing the code, you will need to install the required Python libraries or packages in this cloud-based environment.

You will need to perform this task in the Terminal tab. To open a new Terminal, click the Terminal menu. Then, click New Terminal. For the purpose of the demo, let’s copy the code block from the instruction pane and paste it on the terminal. Then, press Enter to execute the command. Notice that the numpy library has been successfully installed. You can now import this library into your code.

Let’s now create a basic Python program. In the programming pane, click File. Then, select New File. The new file opens in the Editor tab. It is a best practice to save the file before starting to add code. Since we are writing a Python code, save the file with a .py extension. From the File menu, click Save (or Ctrl+S).

When prompted, provide the file name. For this example, let’s save the file as Hello.py. The next step is to add the code. You can manually type the code in the Editor tab or copy and paste the code from the instruction pane, if available, to your file. For the purposes of this demo, let’s copy the code from the instruction pane and paste it in the file. Don’t forget to save the file! It’s time to execute the code.

Let’s navigate back to the Terminal tab. Make sure that you are in the folder where the program file is stored. You can execute the file by typing python3 followed by the file name. For this example, that’s python3 Hello.py. Notice that the output is displayed without any errors. This brings us to the end of the demonstration on the Cloud IDE. To summarize: Cloud IDE is a programming environment similar to VS Code [provided by IBM Skills Network for the purposes of learning and developing hands-on skills] The Cloud IDE has 2 panes, instructional and programming.

You can use the Table of contents button on the instructional pane to navigate between instructional pages. The programming pane provides the Editor tab to write code and Terminal tab to execute code. You need to install the required libraries through the Terminal. At any point during the labs, you can copy the code blocks from the instruction pane and paste it in the Editor or Terminal tabs.

---

### 8. [VIDEO TRANSCRIPT] Python Style Guide and Coding Practices Video • 6 min
- **URL:** https://www.coursera.org/learn/python-project-for-ai-application-development/lecture/S1hBj/python-style-guide-and-coding-practices
- **Method:** `dom_transcript` | **Length:** 5723 chars

Welcome to Python Style Guide and Coding Practices. After watching this video, you'll be able to Describe the importance of writing readable code List the Python coding conventions Explain static code analysis When you write code, you need to ensure the team can read and understand it easily. This task requires some coding standards and conventions. Python.org has released a document called Python Enhancement Proposal 8, or PEP-8, that provides conventions and guidelines to make your Python code readable and consistently formatted. Let's start with the key guidelines for improving the readability of the code. PEP-8 recommends the use of spaces instead of tabs for indentation. Wondering why?

Text editors and Integrated Development Environments, or IDEs, interpret the number of spaces in a tab differently. For example, one editor might interpret a tab as three spaces, while another might interpret it as four. Using a tab for indentation can lead to non-uniformity in code, resulting in formatting errors. For example, observe the spacing difference when tab is pressed for statement 1 for the if condition under editor 1 when compared with the space before statement 1 for the if condition under editor 2. To avoid such errors, you should use a consistent number of spaces when indenting your code. For uniformity, the guideline is to use four spaces for every indentation level in a code. Four spaces for an indentation are sufficient for appropriate readability.

Please note that the four dots have been added before statement 1 and statement 2 to depict four spaces. PEP-8 also recommends using blank lines to separate functions and classes in the code. Notice that in the left block, which does not follow PEP-8 guidelines, there is no space between where function 1 ends and where class UserClass, capital U and capital C, no space. However, the right side shows the correct representation with a space before the class definition. The blank lines help establish the beginning and end of different parts of the code. To improve code readability, use spaces around operators and after commas. Using spaces will make the commands look spacious and discreet, improving command readability.

Let's look at some examples. When you write A equals B plus C without any spaces, it can be confusing. However, when you add the spaces, for example, A space equals space B space plus space C, readability improves. Next, let's look at some coding conventions to maintain consistency and manageability. A key coding convention is to create separate functions for functionalities with larger blocks of code. You can then call the functions from the main program. For example, in the code, the if-else syntax does not have a function and will need to be written every time you need the functionality.

However, if you notice function underscore one written as def function underscore one with two parameters A and B, it can be called easily. For example, C equals function one A comma B. This increases the execution speed of the code and supports the reuse of the code block in a much more convenient way. Another coding convention is to name the functions and files using lowercase with underscores. Wondering why? Python uses the naming convention and has many built-in libraries and predefined functions that use the common naming conventions. Therefore, using a lowercase function name, preferably with underscores, is advisable to make the functions unique.

For example, instead of writing function name as comp surface with capital S, radiation with capital R, write comp underscore surface underscore radiation. An exception to the rule is the naming criteria for Python packages, where underscores are generally discouraged. For example, instead of writing my underscore package, write my package. Naming the classes using camel case is also a coding convention. Camel case, or the cap word case, is a naming convention for classes that is well accepted in the coding community. Camel case also helps distinguish between classes and functions in the code. For example, instead of writing class lamb underscore squirrel underscore cage, the best practice is to name the class as lamb squirrel cage with the initial L, S, and C in capital letters.

Use the coding convention of capitalizing all words and separating them with underscores for consistency. The name usually indicates the constant's purpose. For example, max file upload size in capital letters. We discussed the coding convention and guidelines. Software developers commonly use static code analysis to manage compliance with these style guidelines. Static code analysis is a method to evaluate code against a predefined style and standard without executing the code. Static analysis helps find issues such as programming errors, coding standard violations, undefined values, syntax violations, and security vulnerabilities.

You can use the PyLint library to check the compliance of your Python code with PEP 8 guidelines. In this video, you learned that writing consistent code helps all team members read and understand the code easily. The PEP 8 guidelines for better code readability include the following. Four spaces for indentation. Use blank lines to separate functions and classes. And use spaces around operators and after commas. Some coding conventions for code consistency and manageability include add larger blocks of code inside functions.

Name functions and files using lowercase with underscores. Name classes using camel case. And name constants in all capital letters with underscores separating words. Use static code analysis method to evaluate your code against a predefined style and standard without executing the code.

---

### 9. [VIDEO TRANSCRIPT] Unit Testing Video • 6 min
- **URL:** https://www.coursera.org/learn/python-project-for-ai-application-development/lecture/PCCAF/unit-testing
- **Method:** `dom_transcript` | **Length:** 5949 chars

Welcome to Unit Testing. After watching this video, you will be able to Define unit testing Explain the unit test process Build and execute unit tests Review the output of a unit test Unit testing is a method to validate if units of code are operating as designed. A unit is a smaller, testable part of an application. Here is an example of a unit, which has two functions, square and doubler, in the mymodule.py file. The square function is written as def square(number):return number ** 2. Similarly, the code for the doubler function is written as def doubler(number):return number * 2. To develop unit tests, you will use the unit test library, which is an installed Python module providing a framework containing test functionality.

Let's briefly review the end-to-end testing process from unit testing through publishing to the production code base. During code development, you will test each unit. The test is performed in two phases. In the first phase, you will test the unit on your local system. If the test fails, you will determine the reason for the failure and fix the issue. Then, you will again test the unit. After the unit test passes, you will need to test the unit in a server environment, such as the Continuous Integration Continuous Delivery, or CICD, test server.

If the unit fails the server test, you will receive the failure details. You will need to determine and fix the issue. Once the unit passes the server test, the unit is integrated into the final code base. After an overview to the unit test process, let's review some test functions to understand how to build unit tests. Notice the code for the unit and the unit test. Observe that the name of the unit file is mymodule.py. The unit test file has the word test appended or prepended.

This is a good naming convention as it helps to clearly differentiate the unit file from the unit test file. Let's look at the steps to create a unit test file. The first step is to import the unit test Python library. Type import unit test. Next, import the functions to test. For example, to import the square and doubler from the mymodule unit to unit test, type from mymodule import square, doubler. Then, build the unit testing class to call the unit test from a single class object.

For example, to create a class named TestMyModule, enter class test with uppercase T in the first occurrence, my with uppercase M, module with capital M, unit test, dot, test case with T and C in uppercase. Notice how the class name has test prefixed to the unit name in the example. It is a good naming convention to prefix test to the class name to help distinguish between the unit class and the unit test class. Next, make the class inherit the test case class of the unit test library. For example, test case is the test case class of the unit test library. Inheriting the class allows you to leverage the existing methods in the test case class. Then, create functions in the unit testing class corresponding to each function that needs to be tested.

For example, in the TestMyModule class, two functions, test square and test doubler, correspond to the square and doubler functions in the mymodule unit. Note, make sure that the functions are prepended with the test in the unit test module, because only functions that start with test are run. Finally, you can create test cases. When creating the test cases, add one or more assertion methods to ensure that the unit test condition is met. One assertion function is assertEqual. Notice that the method has been added to the test case class in the code. The assertEqual function compares two values or entities and determines if they are equal.

The method is used to check if functions are returning the correct values. One of the parameters that the assertEqual function takes is the actual value. For the actual value, you will call the function that you want to test. The second parameter is the expected value where you will add what the function is expected to return. In the example, the first test is for the square function using the number 2, which should return a value 4 if the function executes correctly. As part of the test, first, the function is evaluated. Then, the two values are compared to see if they are equal.

Depending on the output of the comparison, the test passes or fails. After running the test file, an output is generated. The output displays the test results along with some additional details. For example, if the output displays that two tests were run in 0 seconds, OK indicates that the test passed and the two functions were implemented correctly. But what happens if the function was not implemented correctly? Consider the square function where you wrote the code to calculate the cube of a number instead of square. The function fails and an output is generated.

Let's review the sample output of a failed unit test. The output clearly displays that the unit test failed. For example, the output states Fail:test_square(_main_.TestMyModule). You can also view the function where the unit test failed. For example, in the test_square function, the assertion self.assertEqual(square(2), 4) failed. An assertion error occurred because 8 is not equal to 4.

The detailed output enables you to correct a mistake before the actual deployment of your solution. In this video, you learned that Unit testing is a method to validate if units of code are operating as designed. During code development, each unit is tested. The unit is tested in two phases. Once the unit passes the server test, the unit is merged into the final code base. Make sure that the test files are pre-appended or appended with the word test to clearly differentiate them from the module file. You can use different test functions to build unit tests. assertEqual function is a commonly used assertion method to compare two values.

You can review the unit test output and determine if the test passed or failed.

---

### 10. [VIDEO TRANSCRIPT] Packaging Video • 5 min
- **URL:** https://www.coursera.org/learn/python-project-for-ai-application-development/lecture/0x2h7/packaging
- **Method:** `dom_transcript` | **Length:** 4485 chars

Welcome to Packaging. After watching this video, you will be able to Differentiate between Python module, package, and library Create a Python package Verify a Python package And use a Python package Modules, packages, and libraries are frequently used terms in Python. Let's look at each of the terms in detail. A Python module is a .py file containing Python definitions, statements, functions, and classes. You can import a module to other scripts and notebooks. For example, consider a module named module.py that has two functions. The first function is def square number return number asterisk asterisk two, which squares the input and returns the result as an output.

The second function is def doubler number return number asterisk two, which doubles the input and returns the result as an output. If the function is in the same directory, you can import it and use the functions in that module. Let's consider using the square function with print command. Four caret symbol two square four, the output is displayed as four caret symbol two equals sixteen. Similarly, for the print doubler function with value four, the output is two asterisk four equals eight. A package is a collection of Python modules into a directory with an init.py file, which distinguishes it from just a directory of Python scripts. The example shows the package my project in parent directory with two modules, module one.py and module two.py.

It also contains init.py file. When you import a module or a package, the corresponding object created by Python is always of type module. Note that the distinction between module and package is only at the file system level. A library is a collection of packages or it can be a single package. Examples include NumPy, PyTorch and Pandas. Note that the terms package and library are often used interchangeably. Therefore, NumPy, PyTorch and Pandas are also referred to as packages.

Let's look at the steps to create a Python package. Consider there are two modules. Module one.py has two functions, square and doubler. Module two.py has one function, mean. To make my project folder into a package, you must have init.py as a file in the my project folder. The contents of the init.py file must be from .importmodule1 and from .importmodule2. Typical steps to create a package include.

First, create a folder with the package name. Then create an empty init.py file. Create the required modules. Finally, in the init.py file, add code to reference the modules needed in the package. After creating the package, you need to verify the package. To verify the package, first, open a bash terminal. Make sure the directory is the same as the folder where your package is located.

Open the Python interpreter by running the command python in the shell. Using the Python prompt, type import followed by project name. For example, import my project. If the command runs without errors, it is an indication that the package is successfully loaded. The general structure for testing your package is the package name, .module name, .function name, followed by the parameters without the curly brackets but keeping the round brackets. For example, using my project, myproject.basic.square to, the function will return the value 4. After creating the package, you can use it in the other scripts if the package folder is in the same directory.

In this case, you have the file test.py in the parent directory. You can import the functions in the package. For example, using the Python code from myproject.module1, we import the square and doubler functions. From myproject.module2, we import the mean function. Then, we print the result of square 4. Next, we print the result of doubler 4. Finally, we use the mean function with the values 2, 1, and 3.

You can then run the functions and check if you get the correct results. In this video, you learned that a Python module is a .py file containing Python definitions, statements, functions, and classes. A package is a collection of Python modules into a directory with an init.py file. A library is a collection of packages or it can be a single package. To create a package, create a folder with the package name, create an empty init.py file, create the required modules. In the init.py file, add code to reference the modules needed in the package. You can verify the package via the bash terminal.

After creating the package, you can use it on other scripts if the package folder is in the same directory.

---

### 11. [READING] Module 1 Summary: Python Coding Practices and Packaging Concepts Reading • 2 min
- **URL:** https://www.coursera.org/learn/python-project-for-ai-application-development/supplement/nBXFA/module-1-summary-python-coding-practices-and-packaging-concepts
- **Method:** `dom_reading_cml` | **Length:** 1820 chars

Congratulations! You have completed this module. At this point, you know that:

- The application development lifecycle has seven phases, including:
- Requirement Gathering: You collect user, business, and technical requirements for the app
- Analysis: You analyze the requirements
- Design: You design the complete solution
- Code and test: You build and test the different components of the app
- User and system test: Users test the app for usability, and you perform system integration testing and performance testing
- Production: The application is available to all end users
- Maintenance: You upgrade or fix any user or system issues
- All web apps are APIs, but not all APIs are web apps. Both share data between apps, but not all APIs require networks like web apps do.
- The PEP8 guidelines for code readability include the following:
- Four spaces for indentation
- Blank lines to separate functions and classes
- Spaces around operators and after commas
- The PEP8 coding conventions for consistency and manageability include:
- Add larger blocks of code inside functions
- Name functions and files using lowercase with underscores
- Name classes using CamelCase
- Name constants in capital letters with underscores separating words
- To ensure that your code adheres to the predefined style and standard without executing the code, you can use the Static code analysis method.
- Unit testing is a method to validate if code units are operating as designed. You must test every unit before integration with the final codebase.
- To create a package:
- Create a folder with the package name
- Create an empty __init__.py file
- Create the required modules
- In the __init__.py file, add code to reference the modules needed in the package
- You can verify the package via the bash terminal in a Python shell.

---
