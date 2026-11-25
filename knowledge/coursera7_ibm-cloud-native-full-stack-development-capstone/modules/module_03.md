# Module 3: Back End Services

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
