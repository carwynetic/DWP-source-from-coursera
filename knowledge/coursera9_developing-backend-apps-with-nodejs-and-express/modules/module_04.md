# Module 4: Final Project

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
