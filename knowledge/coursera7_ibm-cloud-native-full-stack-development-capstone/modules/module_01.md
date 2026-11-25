# Module 1: Application - Static Pages

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
