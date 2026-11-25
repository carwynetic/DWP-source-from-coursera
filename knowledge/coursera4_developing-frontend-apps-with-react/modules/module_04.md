# Module 4: Practice, Final Project, and Submission and Evaluation

### 1. [READING] Practice Project: Conference Expense Planner app Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/supplement/0XTFy/practice-project-conference-expense-planner-app
- **Method:** `dom_reading_cml` | **Length:** 4786 chars

In the Conference Expense Planner app practice project, you will build the front end of an application that allows the user to price out the expenses related to hosting a conference at a convention center. The lab will guide you through the development of the application elements required for this project.

The Conference Expense Planner will have a landing page, a product selection page, and a pop-up summary window. The product selection page allows users to select their rooms, their add-ons, and meals. Based on those selections, it provides pricing. The pop-up window summarizes the expenses in a table based on the user's selections from the product selection page.

We strongly encourage you to complete the practice project prior to starting the final project. It will give you practice developing many of the same elements and functionality you will need to develop in your final project. The practice project lab contains step-by-step instructions for the code required in this application.

Let's discuss the features of the conference expense budgeting app in greater detail. Sample screenshots are provided, though feel free to experiment with the code, components, and layouts.

#### Landing page

The landing page will have the same elements as the final project's landing page.

You will create a landing page like the image below that engages your customers with your product line and provides entry into the main application. See the screenshot at the end of this section for a visual of what this page might look like.

Features on this page should include:

- A paragraph about the company
- A background image
- Your company name and
- A Get Started button linking to the product selection page

You landing page will look something like this:

#### Product selection page

After selecting Get Started, the application should direct the user to the product selection page. This page allows users to select rooms in the venue, add-ons needed for presentations such as microphones and speakers, and meals they would like catered for the participants. This page will have three sections: room selection, add-ons, and meals. Each section should have its own header and also a page header with navigation to each section.

The suggested layout is displayed in an annotated screenshot for each section and an image of the whole page.

Users select from 5 room types:

- Auditorium hall – capacity 200, $5500 ea
- Conference room – capacity 15, $3500 ea
- Presentation room – capacity 50, presentation room, $700 ea
- Large meeting room – capacity 10, $900 ea
- Small meeting room – small meeting room, capacity 5, $1100 ea

You will provide an increment and decrement button for each room type so the user can request the number of each room type they need.

The product selection page should also have a header with a navigation bar. The navigation bar should display a Show Details button, which opens a pop-up window displaying data related to the user's selections.

Users can select their audio/visual equipment in the add-ons section:

- Speakers – $35 ea
- Microphones – $45 ea
- Whiteboards – $80 ea
- Projectors – $200 ea
- Signage – $80 ea

You will provide an increment and decrement button for each type of equipment so the user can request the number of each type of AV equipment they need.

Users can select the following options for meals in the meals section:

- Breakfast – $50 per person
- Lunch – $60 per person
- High tea – $25 per person
- Dinner – $70 per person

You will provide a text entry box where the user can enter the number of people for these meals.

#### Show details pop-up

The users will need to see the details of their selections. For this element, they can access this information through a Show Details button in the header. When the user selects the button, a window pops up displaying a four-column table. Each row of the table contains the selection type, its unit cost, the quantity indicated, and the subtotal for the quantity of that item type. It will also display the total cost for all items.

#### Final project similarities

The final project has many elements in common with the practice project. For your final project, you will create a shopping cart application for purchasing household plants.

Similar functionalities between the two projects include:

- Landing page
- Navigation bar
- Array of product items and associated data
- Array of selected item
- Use of the map() function to iterate through an array
- Subtotal and total cost calculations
- Dynamic pricing displays based on user selections
- Increment and decrement buttons for product quantity selection
- Use of Redux and the Redux toolkit for managing application states with 'slices'
- Function components for presenting interactive UI elements

---

### 2. [VIDEO TRANSCRIPT] Final Project Walkthrough Video • 3 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/lRdEq/final-project-walkthrough
- **Method:** `dom_transcript` | **Length:** 3674 chars

Welcome to the React Final Project Walkthrough. For your final project, you will create the front end of a paradise nursery shopping application. The application interface will allow you to browse a variety of house plants and add them to a shopping cart. The shopping cart feature lets you see all your items and their total cost. Your shopping cart should also allow you to adjust the number of items in the cart before checkout. Your application will have three pages, a landing page, a product listing page, and a shopping cart page. Let's preview the application and tour the user experience.

Here, you see a sample landing page for the Paradise Nursery shopping application. Create a landing page similar to this one that engages your customers with your product line and provides entry into the main application. Elements on this page should include a paragraph about your company, a background image, your company name, and a Get Started button linking to the product listing page. After selecting Get Started, the application should direct you to a product listing page like the one shown here. This page allows you to browse the house plants in your product line. Page elements include a page header and a card for each plant. The page should group the plants by a common feature, such as air purifying or aromatic.

Some sections may have a single plant in multiple groups. The page header should include the company name and logo, which will navigate back to the landing page. It should also include a tagline and a shopping cart icon, displaying the current number of items. The application will navigate to the shopping cart page if you select the cart icon. Each plant should have its own card, similar to what you see here. Each card has a thumbnail, the plant name, its price, a brief description, and an option to add the plant to the cart with the label Add to Cart. If you add the item to the cart, disable this option and change the label to Added to Cart.

Once you select the Add to Cart option, the number on the cart icon should increase by one. Now, take a look at the shopping cart page and its components. You should organize the shopping cart using cards, one for each type of plant added to the cart from the product listing page. Each card should display a thumbnail image, a delete option, and the unit price. You can increase or decrease the number of items using an increase or decrease button, which, when selected, increments or decrements the number on the card. You will also need to update the total number of items in the cart. Also, the card should display the subtotal for the number of that plant type as shown here.

Next, consider the other elements on the shopping cart page. Prominently display the total number of plants in the cart, the sum total costs of all items, and a Checkout button. Use the same page header from the product listing page. You will need to handle the consequences of user events, such as when the number of items in the cart decreases to zero. This affects other elements, such as the disabled Added to Cart option on the product listing page. You need to re-enable that option to select it again when you return to the product listing page. Also, remember to adjust the number of items shown on the cart icon in the header when using the increase and decrease buttons.

We encourage you to complete the practice project before developing this application. Much of the functionality and code you wrote for that project will transfer to this one. After completing these projects, you will feel comfortable applying many of the ideas you learned throughout the course to a single application. Good luck!

---

### 3. [READING] Final Project Overview Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/supplement/o4e2j/final-project-overview
- **Method:** `dom_reading_cml` | **Length:** 6747 chars

For your final project, you will create the front end of a "Paradise Nursery" shopping application. The application interface will allow you to browse a variety of houseplants and add them to a shopping cart. The shopping cart feature lets you see all your items and their total cost. Your shopping cart should also allow you to adjust the number of items in the cart before checkout.

Completing the practice project will help you with the final project. We designed it so that many of the components, code, and skills for that project can be transferred to this final project with some updates.

Your application should have three pages: a landing page, a product listing page, and a shopping cart page. See the lab for details on the specific functionality requirements on each page. The product walkthrough video also demonstrates how your completed project should look and behave.

### Landing page

The landing page should have the following elements:

- A background image
- A paragraph about the company
- The company name
- A Get Started button linking to the product page

The product listing page should have at least six houseplants for sale, organized into three or more categories. Each plant should have the following details about it:

- A thumbnail image
- Plant name
- Price
- An Add to Cart button

### Product listing page

The product listing and shopping cart pages should have a header. The header should have a shopping cart icon with a number that updates dynamically, displaying the total number of items in the cart. The header should also contain navigation to either of the other pages, depending on which page you are on.

### Shopping cart page

The shopping cart page displays all the details about the items in it. It should prominently display the total number of plants in the cart, the total cost of all items in the cart, a continue shopping button, and a checkout button.

On this page, you should be able to see each type of plant in the shopping cart, including its thumbnail and name. You should also display its unit price and the total of all the items in the cart. You should provide an increase or decrease button to change the number of that plant type in the cart, which also updates the shopping cart icon in the header and the total number of items in the cart. Finally, you should also include a delete button for each type of plant in the cart.

You must store your project code in a public GitHub repository. Also, you will use GitHub Pages to deploy your app.

### Evaluation Criteria – 50 Points

You can submit your project deliverables through AI-Graded Submission and Evaluation.  When you do the assessment, you will be redirected to an AI tool where you can upload your deliverables, which may include URLs, terminal outputs, code snippets, or screenshots. You will then receive an AI-generated grade that will automatically reflect on your Coursera progress page.

If you encounter any grading problems, please reach out to the Course Team through the Discussion Forums.

Please find the details of the Grading Criteria below:

Submit the public GitHub URL of the README.md file containing the project name details.(2 points)

Submit the public GitHub URL of AboutUs.jsx, which includes details about the company.(1 point)

Submit the GitHub URL of App.css, which includes the code implementing the background image for the Paradise Nursery landing page.(1 point)

Submit the public GitHub URL of App.jsx, which includes the Paradise Nursery landing page with the company name and a "Get Started" button.(3 points)

Submit the public GitHub URL of CartSlice.jsx, which includes the code implementing the Redux slice for the shopping cart.(4 points)

Submit the public GitHub URL of ProductList.jsx.(16 points)Your implementation must include the following functionalities:

- Display at least six unique houseplants per category, each with a thumbnail, name, and price. (2)
- Group the plants into at least three categories.(2)
- Add the product to the shopping cart (2)
- Disable the button after the product is added (2)
- Update and display the shopping cart quantity (2)
- Include a navbar that appears on both Product Listing and Cart pages (2)
- Navbar provides navigation links to all three pages: Home, Plants, and Cart (2)
- Display a cart icon showing the total number of items dynamically(2)

Submit the public GitHub URL of CartItem.jsx, displaying the Shopping Cart page.(23 points)Your implementation must include the following functionalities:

- Show the total cart amount of the plants(2)
- Show the total cost for each plant in the cart (2)
- Each plant in the cart should display a thumbnail, name, and unit price (6)
- Include button to increase the quantity, updating the cart correctly (4)
- Include button to decrease the quantity, updating the cart correctly (4)
- Include a delete button for each item to remove it from the cart (2)
- Include a checkout button that shows "Coming Soon" or a similar message (1)
- Include a continue shopping button that links back to the product listing page (2)

### GitHub Link (6 points)

- GitHub repository public URL: 2 points
- Redux-related files and code: 4 points

### Deployed app (44 points)

Landing Page (5 points)

- Background image: 1 point
- Paragraph about the company: 1 point
- Company name: 1 point
- Get Started button linking to the product listing page: 2 points

Product Listing Page (9 points)

- Six unique houseplants for sale, each displaying thumbnail, name, and price: 2 points
- Group the plants into at least three categories on the page: 1 point
- After selecting it, the shopping cart icon increases by one.
- After selecting it, the button becomes disabled.
- After selecting it, the appropriate plant gets added to the shopping cart.

Header (7 points)

- Displays on both the product listing page and shopping cart page: 2 points
- A shopping cart icon with a value that displays the total number of items in the cart: 3 points
- Navigation to either of the other pages: 2 points

Shopping Cart Page (23 points)

- The total number of plants in the cart: 2 points
- The total cost of all items in the cart: 2 points
- Each plant type in the cart displays a thumbnail, name, and unit price: 6 points
- Increments the number of items in the cart by one each time it`s clicked and updates all appropriate values.
- Decrease button for each plant type in the cart: 4 points
- Decrements the number of items in the cart by one each time it`s clicked and updates all appropriate values.
- A delete button: 2 points
- A checkout button (displays the message "Coming Soon" or similar):1 point
- A continue shopping button that links to the product listing page: 2 points

### Author

Vandana Pandey

---

### 4. [VIDEO TRANSCRIPT] Course Wrap-Up Video • 5 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/lecture/D1KaN/course-wrap-up
- **Method:** `dom_transcript` | **Length:** 4690 chars

Congratulations on finishing the course. Now that you know the fundamental concepts of using the JavaScript React library, you will find plenty of opportunities to continue your learning and apply your skills. Before discussing those, let's review some of the key aspects of what you learned throughout the course. Components comprise one of the fundamental building blocks behind building client site applications using the React JavaScript library. You use components to render the UI for event management and to update the UI based on the components internal state changes. The ability to develop apps with modular components in React offers several major advantages. Components make React code simple to test and debug.

You can combine components called component composition to create complex UIs, yet still easily read the code. You can choose one of two ways to build React components, with classes or functions. Developing in React requires access to a component state. Prior to React Version 16.8, developers and architects preferred class components because they provided the easiest access to a component's state. Since that version introduced the use of hooks with functional components, those developing with React have steadily moved toward functional components because they perform better and simplify the code, making it easier to read and reason about. The component's properties, or props for short, contain the data for the component. Data can get passed to child components from their parents by passing the props object into the child component as a parameter.

React limits you from passing props from parent to child. You cannot pass data in reverse order. If a child contains data passed from a parent code, you cannot change that data. How you access and manage a component state differs significantly between function based components and class-based components. To access a class component state, you use this.state, and you initialize or update it using the component's this.setState method. When accessing a state with function components, you should use hooks, particularly the useState hook. React uses a virtual DOM that abstracts the actual DOM and allows you to make updates using components, props, and their states.

The virtual DOM updates the actual DOM, affecting only specific elements. React use of a virtual DOM significantly improves the application's performance. When a UI contains a form, you typically store input data from the form in a component state. You will need to validate form data to ensure proper formatting in values. The form validation process includes tasks such as getting input, managing and updating the form state, validating input values, displaying appropriate error messages. You can use the Redux library to help you manage states at the application level. Large applications require application state management to simplify your code.

A high number of components indicates the need for a library, such as Redux, instead of frequently passing props through the component tree. Now that you've reviewed some of the fundamental ideas presented in this course, remember each module's glossaries and cheat sheets. You can use these assets to quickly reference much of what you learned. You can also share the applications you created in the labs and the final projects in GitHub. These projects provide you with examples to showcase your skills to prospective employers. Remember to make these directories public if you wish to make these projects accessible to others. If you are not already enrolled in one of our software developer programs, of which this course is a part, we encourage you to do so.

Depending on your schedule and the number of courses in the program, these programs will take about 2-6 months to complete. The more robust program topics include full-stack development using JavaScript, full-stack development using Python and JavaScript, front-end development, cross-platform mobile app development. If you wish to continue your web and app development journey, but prefer a shorter program, you may wish to consider the following. Cloud application development foundations, client side, server side, and Mongo database, programming with JavaScript. If interested, you can find the links to these programs in the congratulations and next steps reading at the end of this course. Each program contains multiple hands-on labs and a final project. The professional certificate programs also have a capstone course where you synthesize and showcase all of your skills learned throughout the program.

Congratulations on completing this course, and good luck in your web application development journey.

---

### 5. [READING] Congratulations & Next Steps Reading • 2 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/supplement/LKNt0/congratulations-next-steps
- **Method:** `dom_reading_cml` | **Length:** 1041 chars

Congratulations on completing the Developing Front-End Apps with React course! We hope you enjoyed the learning experience and feel confident applying your new skills in the workplace and beyond.

### Continue Your Learning Journey

This course is part of the following programs, designed to equip you with essential skills across front-end, full-stack, and mobile application development:

- Full-Stack JavaScript Developer
- Full-Stack Development using Python and JavaScript
- Front-End Development
- Cross-Platform Mobile App Development (coming soon)
- Cloud Application Development Foundations

### Recommended Next Courses

To further enhance your application development skills, consider exploring:

- Introduction to Containers w/ Docker, Kubernetes & OpenShift
- Application Development using Microservices and Serverless

We’d love to hear from you! Please take a moment to rate this course and share your feedback. Your input helps us improve and create better learning experiences.

Good luck on your continued learning journey!

---

### 6. [READING] A Message from the Course Team Reading • 3 min
- **URL:** https://www.coursera.org/learn/developing-frontend-apps-with-react/supplement/OMzZ7/a-message-from-the-course-team
- **Method:** `dom_reading_cml` | **Length:** 1068 chars

Thank you for taking this course.

On behalf of the entire course team, we hope you enjoyed the learning experience and successfully achieved your goals. We wish you every success as you apply your new knowledge and skills in your career and beyond.

We also encourage you to rate the course and share your feedback—your input helps us continuously improve.

Best regards,

The Course Team

### Course Contributors

This course was made possible through the efforts of many talented contributors:

#### Primary Instructor

- Richa Arora

#### Course Team

- Project Lead: Rav Ahuja
- Instructional Designer: Bethany Hudnutt
- Lab Author: Richa Arora
- Technical Advisor: Richa Arora

#### Production Team

- Publishing: Rachael Jones
- Quality Assurance: Mercedes Schneider, Mary Stenberg, Beth Larsen, Sydney Marsing
- Project Manager: Simranjit Singh
- Narration: Sarah Ruth
- Video Production: Emily Lewis, Tori Sleeper

#### Teaching Assistants and Forum Moderators

- Teaching Assistants: Anamika Agarwal, Nikesh Kumar, Rajashree Patil, Ritika Joshi, Alima Akhter

---
