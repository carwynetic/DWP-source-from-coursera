# Full Stack Application Development Capstone Project

- **Course URL:** https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone
- **Crawled at:** 2026-11-24T16:20:34.548750
- **Extracted:** 13/13 items (2 videos, 11 readings) | 28,332 chars

---

## Module 1: Application - Static Pages

### 1. [VIDEO TRANSCRIPT] Course Introduction Video • 4 min
- **URL:** https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/lecture/qZRj5/course-introduction
- **Method:** `dom_transcript` | **Length:** 3846 chars

[MUSIC] Welcome to this course, where you will work on a capstone project as a full stack software developer. Congratulations on making it this far! At this point, you've made it through all the previous courses in the Full Stack Software Developer Professional Certificate. In these courses, you learned about a variety of topics, including cloud computing; HTML, CSS and JavaScript; Git and GitHub; frontends with React; backends with Node.js and Express; Python; web applications using Flask; Django and databases; containers with Docker, Kubernetes, microservices, and serverless. In this capstone project, you now have the opportunity to demonstrate the skills you have acquired throughout the program. After you have successfully completed all the courses, you will receive the Professional Certificate. After completing this course, you will be able to: Create a Full Stack application Develop static and dynamic pages for a website Develop containerized backend services using Express and MongoDB Deploy microservices on Code Engine and use them Work with Django backend and React frontend This course is intended for anyone enrolled in the Full Stack Software Developer Professional Certificate program, and who has completed all the previous courses in the PC.

You should be familiar with HTML, CSS, JavaScript, React, GitHub, Node.js, Express, Python, Flask, Django, containers, microservices, and serverless. The capstone project course is a six-week course with six modules. In this capstone, you will create a car dealerships review portal. The recommendation is for you to spend about two to five hours each week until you complete the project. However, you have the flexibility to complete it in a shorter or longer time frame if needed. The first module will introduce you to the project scenario. You will start by forking the GitHub repository through the link provided and cloning the Django application starter code to build your application.

You will also create a few static webpages using HTML, CSS, and Bootstrap. In Module 2, you will add user management, which includes user registration, login, and logout, along with session management to the Django application with the React front end. In Module 3, you will create backend services in JavaScript that connect with MongoDB. You will containerize MongoDB and Express Server to provide the API endpoints accessing data about the dealership and their reviews. You will also deploy a sentiment analyzer microservice written with Python, Flask, and Natural Language Toolkit (or NLTK) using the IBM Cloud Code Engine. Module 4 is all about adding dynamic React pages to get dealership details, get reviews of the dealership for all end users, and add reviews to the dealership for registered users. You will create user-friendly and aesthetic front-end pages to present these services to the end users.

In Module 5, you will implement Continuous Integration and Continuous Delivery (or CI/CD) with GitHub Workflow for linting. Before moving ahead, you must ensure that your Express-Mongo server is running on Docker, and that the sentiment analyzer microservice is accessible. Then, you will provide your application with the ability to run in a container. You will also add deployment artifacts to the application, so it can be managed by Kubernetes. Finally, in Module 6, you will submit the different artifacts developed in the previous five modules for evaluation. There is a lot to cover here. To get the most from this course, make sure to go through the readings, complete all the hands-on labs, make sure the checklist questionnaire gets a 100% score, and submit your work for evaluation.

If you have any trouble with the course material, please don't hesitate to contact us in the discussion forum. Thank you for being part of our course, and welcome! [MUSIC]

---

### 2. [VIDEO TRANSCRIPT] Project Overview Video • 5 min
- **URL:** https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/lecture/HwaxX/project-overview
- **Method:** `dom_transcript` | **Length:** 4774 chars

[MUSIC] Welcome to the Project Overview. For this Capstone project, you will assume the role of a full stack software developer hired by Best Cars Dealership, a national car dealership with branches all over the US. You will create a website that provides a central database of dealership reviews across the country. You will be provided with a project scenario that requires you to develop the website and the required backend services. Ready to see a demo of the website and the various services it will be using? Let's get started. In this project, you will use the following skills to complete the tasks.

Git, GitHub, and GitHub Actions for version control and continuous integration and continuous delivery or CI/CD. HTML, CSS, and Bootstrap will be used to create a static homepage, About Us page, and Contact Us page for the website. React will be used to create login, registration, dealers view, reviews view and post review components. Python, Django and SQLite for the main application backend for user management and end user views. Python, Flask, and natural language toolkit or NLTK for the sentiment analysis microservice. Node.js, Express, and MongoDB for the dealership and review service. Docker, Kubernetes, Serverless using IBM cloud code engine for deploying various application components and microservices.

Let us give you a sneak peek of what the application should look like. The screenshots in this video are just an example site. Your implementation might differ from this and the site may look quite different than the screenshots you see in the next few slides. When the users come to the website, they should see the homepage from where they can click About Us, to view the details and description of best cars dealership. And Contact Us, to view the company's contact details. The user should be able to view the branches of the dealership by clicking View Dealership. The user does not need to be logged in to view the dealerships.

The homepage should also provide options to log in and register. On the homepage, when the user clicks About Us, it should take them to the About Us page, where they can view the details about the company. Such as its mission and values, as well as introduce key members of its leadership team. When the user clicks Contact Us on the homepage, it should take them to the Contact Us page, where they can see the contact details of Best Car Dealership. Including emails, phone numbers, and website. On the homepage, when the user clicks the Register link, they should be taken to the SignUp page. On the SignUp page, the user should have the provision to provide the necessary details and register.

When the users register, they should automatically get logged in and be taken to the homepage. When the user clicks Login from the homepage, they should see the Login panel. All the registered users should be allowed to login using the Login panel. If the user has not yet registered, they should be allowed to use the link provided to go to the registration page and register. If an unregistered user comes to the homepage and clicks View Dealerships, all the dealerships should be listed, but the Write a review button should not be visible to them. To post a review, the user must be logged in. When the user is logged in, a Write a review option should be available against each dealer to write a review.

The user should be able to filter the dealerships state-wise, by selecting the desired state from the drop down list. The users should also be able to view reviews of a particular dealership by clicking the name of that dealership. The dealership page should show the reviews for the dealership along with the sentiments. The users who are not logged in should not see the button to post a review, but should be allowed to view all the reviews for the selected dealer. Logged in users should be allowed to post a new review by clicking the Write a review button provided. When the logged in user clicks Write a review, they should see the panel to add the details for the review. They can add the review of the dealership, purchase date, car make, and year of manufacture and then post the review.

The review added should be reflected on the dealer's specific page, which can be viewed by users. With this, we come to the end of this exemplar demo. Please follow the instructions to complete each task and take screenshots as necessary for final submission. Let's now get started with the project. Before proceeding with the tasks, read the architecture overview to understand the various components of the process. We hope you enjoyed the demo and are looking forward to this Capstone, where you will get the opportunity to build a creative car dealership's reviews website. All the best.

[MUSIC]

---

### 3. [READING] Overview: Application - Static Pages Reading • 1 min
- **URL:** https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/supplement/WpGLI/overview-application-static-pages
- **Method:** `dom_reading_cml` | **Length:** 843 chars

Congratulations on your new role as the Lead Cloud Application Developer at the "Best Cars" dealership. As a warm-up task, you need to run and test its main Django application.

The Django app will be mainly used for user management and authentication, managing car models and makes, and routing other MongoDB services for dealership and customer reviews. You will build this Django app and related services in a phased manner along the capstone course.

In this module, you are asked to perform the following tasks:

- Fork the GitHub repo containing the project template.
- Clone your forked repository.
- Run the Django app on the development server.
- Add a navigation to the website using Bootstrap.
- Add an "About Us" static page.
- Add a "Contact Us" static page.

Follow the instructional lab to complete the above tasks step by step.

---

## Module 2: Application - User Management

### 1. [READING] User Management Overview Reading • 1 min
- **URL:** https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/supplement/oBZTO/user-management-overview
- **Method:** `dom_reading_cml` | **Length:** 767 chars

Now, you have the initial Django application built and deployed. In the next step, the admins of the dealership will review the app to identify users and manage their accesses based on roles (such as anonymous users or registered users). To accomplish this, you need to add authentication and authorization, that is, user management, to the app. In this lesson, you need to perform the following tasks to add the user management feature:

- Create a superuser for your app.
- Build the Client side and configure it.
- Check the Client configuration.
- Add a Login view to handle login requests.
- Add a Logout view to handle logout requests.
- Add a Registration view to handle Sign-up requests.

Follow the instructional lab to complete the above tasks step by step.

---

## Module 3: Back End Services

### 1. [READING] Node.js Mongo DB dockerized server Overview Reading • 5 min
- **URL:** https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/supplement/WJV2j/node-js-mongo-db-dockerized-server-overview
- **Method:** `dom_reading_cml` | **Length:** 513 chars

The Django application you created in the last module needs to communicate with the database. In this module, you will create a containerized Node.js application that uses MongoDB as the backend to serve API endpoints.

You will write these back-end services in an Express app and containerize it with Docker.

You will view and test the following endpoints:

- /fetchReviews/dealer/29
- /fetchDealers
- /fetchDealer/3
- /fetchDealers/Kansas

Follow the instructional lab to complete the above tasks step by step.

---

### 2. [READING] Django Models Views Reading • 5 min
- **URL:** https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/supplement/vU1wT/django-models-views
- **Method:** `dom_reading_cml` | **Length:** 1004 chars

You have created a dealership and reviews related to CRUD APIs. Next, you need to create data models and services for the dealers' inventory. Each dealer manages a car inventory with different car models and makes, which are, in fact, relatively static data, thus suitable to be stored in Django locally.  To integrate external dealers and review data, you will need to call the APIs from the Django app and process the API results in Django views to be later rendered through REACT pages. Such Django views use proxy services to fetch data from external resources as per users' requests and renders it using REACT components. In this lesson, you need to perform the following tasks to add car model and make related models and views, and proxy services:

- Create CarModel and CarMake Django models
- Register CarModel and CarMake models with the admin site
- Create new car models objects with associated car makes and dealerships

Follow the instructional lab to complete the above tasks step by step.

---

## Module 4: Application - Dynamic Pages

### 1. [READING] Dynamic Pages Overview Reading • 1 min
- **URL:** https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/supplement/wmdOO/dynamic-pages-overview
- **Method:** `dom_reading_cml` | **Length:** 601 chars

You created all necessary backend services (Django views and API endpoints) for managing dealerships, reviews, and cars in the last module. Next, it is time to create some stylized front-end REACT pages to present those service results to the end users. In this learning module, you need to perform the following tasks to add the front-end to the app:

- Create a Dealers component to list all the dealers
- Create a dealer details component that will show the reviews for that particular dealer
- Create a review submission page

Follow the instructional lab to complete the above tasks step by step.

---

## Module 5: CI/CD, Containerize & Deploy to Kubernetes

### 1. [READING] CI/CD Overview Reading • 1 min
- **URL:** https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/supplement/wLvhc/ci-cd-overview
- **Method:** `dom_reading_cml` | **Length:** 739 chars

Congratulations on testing your app after adding static pages and user management. The next step is setting up Continuous Integration and Continuous Delivery for your source code. This is particularly important if you have multiple people working on the project. Continuous Integration provides a way for developers to collaborate, and Continuous Delivery provides a way to deliver your changes to the clients without interruptions.  In this module, you will:

- Understand the workflow present in the provided GitHub workflow template
- Understand the Linting jobs present in the provided GitHub workflow template
- Enable GitHub Actions and run the Linting workflow

Follow the instructional lab to complete the above tasks step by step.

---

### 2. [READING] Overview: Containerize & Deploy to Kubernetes Reading • 10 min
- **URL:** https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/supplement/c4Cgq/overview-containerize-deploy-to-kubernetes
- **Method:** `dom_reading_cml` | **Length:** 1170 chars

In line with the latest trends in technology and to avoid vendor lock-in, your management team is looking to deploy the dealership application to multiple clouds. The application is currently running on Code Engine, but you have been told not all cloud providers have a hosted Code Engine service. You are put in charge to look at containers as a possible way to mitigate this problem as all the big cloud providers have a way to host and manage containers. When containerizing an application, the process includes packaging an application with its relevant environment variables, configuration files, libraries, and software dependencies. The result is a container image that can then be run on a container platform.  You are also asked to use Kubernetes to manage the containerized deployment. Kubernetes is an open-source container orchestration platform that automates the deployment, management, and scaling of applications.

In this module you will:
- Add the ability to your application to run in a container
- Add deployment artifacts for your application so it can be managed by Kubernetes

Follow the instructional lab to complete the above tasks step by step.

---

## Module 6: Share Your Project

### 1. [READING] Complete Documentation and Prepare Your Submission Reading • 10 min
- **URL:** https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/supplement/h9HQr/complete-documentation-and-prepare-your-submission
- **Method:** `dom_reading_cml` | **Length:** 10087 chars

### Final Submission

Estimated time:  10 minutes

Congratulations on finishing the capstone project!

### Option 1: AI-Graded Submission and Evaluation

You will be asked to submit the following artifacts for AI evaluation.

Submit the URL for:

- Your forked GitHub repository with all the code
- cURL command outputs
- Your application deployment (This URL need not be accessible but will be checked against the URL in the messages)
- Screenshots of completed tasks

You will be graded as per the following rubric (50 points):

Task 1: Submit the public GitHub URL of the README.md file that contains the Project name details. (1 point)

Task 2: Copy and paste the terminal output saved in the file named django_server, showing the Django server running. (1 point)

Task 3: Submit the public GitHub URL of the server/frontend/static/About.html file showing the updated “About Us” page with correct CSS links, realistic images, names, roles, brief details, and email IDs. (3 points)

Task 4: Submit the public GitHub URL of the  server/frontend/static/Contact.html file showing the “Contact Us” page of your Django app which you created with updated CSS links, navigation bar (active on Contact Us), images, and all required contact details. (2 points)

Task 5: Copy and paste the cURL command and its output, saved in a file named loginuser, which performs a login operation using any valid username and password. (2 points)

Task 6: Copy and paste the cURL command and its output, saved in a file named logoutuser, which performs the logout operation for the logged-in user. (2 points)

Task 7: Submit the public GitHub URL of the server/frontend/src/components/Register/Register.jsx file showing the “Sign-up” page of your Django/React application with all five input fields (Username, First Name, Last Name, Email, Password) and the Register button. (1 points)

Task 8: Copy and paste the cURL command and its output, saved in a file named getdealerreviews, which displays the review(s) for any dealer ID. (2 points)

Task 9: Copy and paste the cURL command and its output, saved in the file named getalldealers, which displays all dealer(s) retrieved. (2 points)

Task 10: Copy and paste the cURL command and its output, saved in a file named getdealerbyid, which displays the details of any dealer ID.(2 points)

Task 11: Copy and paste the cURL command and its output, saved in the file named getdealersbyState, which displays the dealer(s) located in the state of Kansas. (2 points)

Task 12: Submit the screenshot (admin_login.png or admin_login.jpeg) showing the root user login on the admin page. (2 points)

Task 13: Submit the screenshot (admin_logout.png or admin_logout.jpeg) showing the root user logged out from the admin page. (1 point)

Task 14 and 15: Copy and paste the cURL command and its output, saved in the file named getallcarmakes, which displays all car makes and models retrieved. (4 points)

Task 16: Copy and paste the cURL command and its output, saved in the file named analyzereview, which displays the sentiment analysis result for the review text "Fantastic services". (2 points)

Task 17: Submit the screenshot (get_dealers.png or get_dealers.jpeg) showing the dealers on the home page of the Django application before logging in. (1 point)

Task 18: Submit a screenshot showing the dealers displayed on the home page of the Django application after logging in, with the image name get_dealers_loggedin. The screenshot must clearly show the Review Dealer option, the logged-in username, and the endpoint visible in the browser address bar. (2 points)

Task 19: Submit the screenshot (dealersbystate.png or dealersbystate.jpeg) showing the dealers filtered by the State on the home page of the Django application. Please ensure that the endpoint is visible in the browser address bar. (2 points)

Task 20: Submit a screenshot showing the selected dealer details on the dealer page, along with the reviews, with the image name dealer_id_reviews (saved as .png or .jpeg). The screenshot must clearly display the endpoint visible in the browser address bar. (1 point)

Task 21: Submit a screenshot showing the Post Review page after entering the review details, before submission, with the image name dealership_review_submission. (1 point)

Task 22: Submit a screenshot showing the posted review, with the image name added_review. (2 points)

Task 23: Copy and paste the terminal output saved in the file named CICD that shows your GitHub Actions workflow running successfully. The output should clearly display the steps executed in the workflow. (3 points)

Task 24: Submit the deployment URL for your Django application saved in the file named deploymentURL. (1 points)

Task 25: Submit a screenshot showing the deployed landing page, with the image name deployed_landingpage. (2 points)

Task 26: Submit a screenshot showing the deployed logged-in page, with the image name deployed_loggedin. The screenshot must clearly display the username of the logged-in user. (2 points)

Task 27: Submit a screenshot showing the dealer details page opened through your deployment, with the image name deployed_dealer_detail. (2 points)

Task 28: Submit a screenshot showing the review displayed in your deployed application, with the image name deployed_add_review. (2 points)

### Option 2: Peer-Graded Submission and Evaluation

You need to submit the following artifacts for the peer-reviewed:

URL of:

- Your forked GitHub repo with all the code.
- Your application deployment (This URL need not be accessible but will be checked against the URL in the messages)
- Screenshots of completed tasks

You will be graded as per the following rubric (50 points):

Task 1: Submit the personal GitHub Project repo URL with all code changes. (1 point)

Task 2: Submit the screenshot showing the Django server running. (1 point)

Task 3: Submit the screenshot of the “About Us” page of the Django application. (3 points)

Task 4: Submit the screenshot of the “Contact Us” page of the Django application. (2 points)

Task 5: Submit the screenshot of the “Login” page of the Django application. (2 points)

Task 6: Submit the screenshot of the “Logout alert” of the Django application. (2 points)

Task 7: Submit the screenshot of the “Sign-Up” page of the Django application. (1 point)

Task 8: Submit the screenshot showing dealer reviews through the Express-Mongo application endpoint. The endpoint should be visible on the browser address bar. Please ensure you choose a dealer who has reviews. (2 points)

Task 9: Submit the screenshot showing all dealers through the Express-Mongo application endpoint. The endpoint should be visible on the browser address bar. (2 points)

Task 10: Submit the screenshot showing all dealer details through the Express-Mongo application endpoint. The endpoint should be visible on the browser address bar. (2 points)

Task 11: Submit the screenshot showing all dealers in Kansas through the Express-Mongo application endpoint. The endpoint should be visible on the browser address bar. (2 points)

Task 12: Submit the screenshot showing the root user login on the admin page. (2 points)

Task 13: Submit the screenshot showing the root user logged out from the admin page. (1 point)

Task 14: Submit the screenshot (cars.png or cars.jpg) showing car makes (after adding or populating the car makes), and the endpoint should be visible on the browser address bar.  (2 points)

Task 15: Submit the screenshot showing Car Models (after adding or populating the car models) from the admin page. (2 points)

Task 16: Submit the screenshot showing the sentiment analyzer working through the deployed URL. Please ensure that the endpoint is visible in the browser address bar. (2 points)

Task 17: Submit the screenshot showing the dealers on the home page of the Django application before logging in. Please ensure that the endpoint is visible in the browser address bar. (1 point)

Task 18: Submit the screenshot showing the dealers on the home page of the Django application after logging in. The “Post Review” button and the logged-in username should be visible. Please ensure that the endpoint is visible in the browser address bar. (2 points)

Task 19: Submit the screenshot showing the dealers filtered by state on the homepage of the Django application. Please ensure that the endpoint is visible in the browser address bar. (2 points)

Task 20: Submit the screenshot showing the selected dealer details on the dealer page along with the reviews. Please ensure that the endpoint is visible in the browser address bar. (1 point)

Task 21: Submit the screenshot showing the “Add Review” page after adding the details before you submit. Please ensure that the endpoint is visible in the browser address bar. (1 point)

Task 22: Submit the screenshot showing the “Added Review” after submission. The details should match with the input shown in the previous task. Please ensure that the endpoint is visible in the browser address bar. (2 points)

Task 23: Submit the screenshot of the successful CI/CD implementation on GitHub. (3 points)

Task 24: Submit the deployment URL for your Django application. (1 point)

Task 25: Submit the screenshot of the landing page opened through your deployment. The URL in the address bar of the browser should be visible, and it must match the URL submitted in the previous task. (2 points)

Task 26: Submit the screenshot of the logged-in page opened through your deployment. It should show the username of the logged-in user. The URL in the address bar of the browser should be visible, and it must match the URL submitted in the previous task. (2 points)

Task 27: Submit the screenshot of a dealer details page opened through your deployment. The URL in the address bar of the browser should be visible, and it must match the URL submitted in the previous task. (2 points)

Task 28: Submit the screenshot of a review added through your deployed application. The URL in the address bar of the browser should be visible, and it must match the URL submitted in the previous task. (2 points)

---

### 2. [READING] Congratulations and Next Steps
- **URL:** https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/supplement/UY74W/congratulations-and-next-steps
- **Method:** `dom_reading_cml` | **Length:** 2414 chars

Congratulations on completing this Full Stack Professional Certificate final project! We encourage you to enhance your project by completing the optional (non-graded) labs included as part of the project.  You can also add this project to your portfolio.

In order to receive your certificate for the Full Stack Software Developer Professional Certificate program you must complete one more course, that is, the Full Stack Software Developer Assessment course.

### Career guidance and interview preparation for full stack software developer jobs:

Now that you’ve developed your new skills in full stack software development, you’ll start looking for work in this field to use them. Job-seeking has its own set of skills. However, before you head out into the job market, increase your chance of success by taking the Software Developer Career Guide and Interview Preparation course.

In this course, you’ll learn about becoming an exceptional job candidate, including:

- How to focus your job search to match your goals
- How to write an effective resume
- How to compile a portfolio that shows off your work
- How to find and assess job listings
- Tips for performing at your best in interviews

Information-filled lessons and activities are accompanied by direct advice from experts in the field. You can click this link to access the course.

This course will be offered free for a month if you enroll through this link. Please ensure you complete the course within the time limit if you want to avoid getting charged. It’s a great time to take advantage and give yourself an edge in the competitive world of finding your best next role. So, what are you waiting for? Go ahead and enroll now in the Software Developer Career Guide and Interview Preparation course.

Develop People and Soft Skills:

We also encourage you to build on your people and soft skills by taking our People and Soft Skills for Professional and Personal Success Specialization. This specialization is aimed at helping you develop powerful people and soft skills and behaviors that include:

- Creating and delivering impactful presentations
- Working professionally to deliver quality work and experiences
- Collaborating effectively with teams
- Communicating productively and efficiently
- Dealing with challenges, solving problems, and implementing solutions

You can explore and enroll in the specialization by clicking this link.

---

### 3. [READING] Credits and Acknowledgments
- **URL:** https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/supplement/sdb0Q/credits-and-acknowledgments
- **Method:** `dom_reading_cml` | **Length:** 1197 chars

The entire course team thanks you for taking this course. We hope you enjoyed it and wish you the best in applying your new knowledge and skills.

We encourage you to rate the course and provide a review. Your feedback is much appreciated.

Best regards,

Course Team

Project Lead

- Rav Ahuja

Primary Instructor

- Upkar Lidder
- Lavanya Thiruvali Sunderarajan
- Yan Luo

### Other Contributors and Staff

Instructional Designer

- Priya Kapoor
- Lavanya Thiruvali Sunderarajan

Lab Authors

- Lavanya Thiruvali Sunderarajan
- Upkar Lidder
- Yan Luo
- Sundararajan

### Production Team

Project Coordinator

- Bryan Hayes (Skill-Up Technologies) (April 2021)

Project Manager

- Nancy Varkey (Skill-Up Technologies) (Nov 2023)

Publishing

- Grace Barker (IBM)
- Rachael Jones (Skill-Up Technologies)
- Santosh Kumar Sahu (Skill-Up Technologies)
- Madhumita Pati (Skill-Up Technologies)

QA

- Pradnya B
- Kunal Merchant

Narration

- Bella West (April 2021)
- Sarah Ruth (Nov 2023)

Video Production

- Simer Preet
- Lauren Hall
- Tanya Singh
- Om Singh
- Prayas Gupta (Nov 2023)

Teaching Assistants and Forum Moderators

- Anamika Agarwal
- Lavanya Rajalingam
- K. Sundararajan
- Pallavi Rai

---

## Module 7: Enhancement of Car Dealership Portal

### 1. [READING] Further Your Learning Reading • 2 min
- **URL:** https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/supplement/Ix8O9/further-your-learning
- **Method:** `dom_reading_cml` | **Length:** 377 chars

Put your skills into practice with IBM Cloud Pak for Integration

Ready to take the next step? Explore how IBM Cloud Pak for Integration helps organizations connect applications, APIs, events, messaging systems, and data across hybrid cloud environments. Experience the platform through the approved interactive demo or trial destination.

Explore IBM Cloud Pak for Integration

---
