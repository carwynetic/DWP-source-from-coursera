# Module 3: Full-stack Django Development

### 1. [VIDEO TRANSCRIPT] Django Model-View-Template (MVT) Pattern
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/w3J0e/django-model-view-template-mvt-pattern
- **Method:** `dom_transcript` | **Length:** 2754 chars

​Welcome to Django Model View Template (MVT) pattern, Django’s implementation of the ​standard Model-View-Controller (MVC) pattern After watching this video, you will be able to: ​Describe the Model-View-Controller pattern, and describe the Django Model View Template pattern. ​The MVC design pattern divides application logic into three components. ​Model accesses and manipulates data but does not present data. Model may have database ​interfaces such as SQL or ORM, or it may use business logic to process raw data. ​View presents data in various forms, such as visual elements in a webpage, a mobile ​app user interface, or as JSON/XML format. Controller coordinates between Model and View. ​It routes requests, processes input, requests data CRUD from Model, and updates View.

​When a client application sends a request with inputs to Controller, ​Controller routes the request, validates and processes the input, sends CRUD requests to Model, ​and forwards data to View to be presented. In the Django framework implementation, ​there is no explicit Controller. Instead, the Django server itself performs this function. ​Django Model manages data modelling and database mapping as well as business logic to process data. ​Django View describes which data is presented, but not how it is presented. Typically, ​view delegates to a template, which describes how the data is presented. ​When a client sends a request, the Django server routes the request to the appropriate ​view based on the Django URL configuration. Thus, Django follows a Model-View-Template, ​or MVT, design pattern. As we have learned, ​Django models are classes mapped to database tables.

​Django Model APIs allow developers to perform CRUD on objects and ​developers can also write business logic in Django model classes as functions. ​In Django, a View is essentially a Python function. ​This function takes a Web request and applies the necessary logic to generate a Web response, ​such as the HTML contents of a Web page, a redirect, a 404 error, an XML document, ​an image, or any other Web response. Often, View interacts with Django Model to ​get required data in the form of QuerySet or objects to generate a Web response. ​Django uses a template to generate dynamic Web pages which are sent back ​and rendered in a user’s browser. The Django template contains static HTML elements, ​as well as special Python code describing how the dynamic content of HTML pages will be generated. ​In this video, you learned that: The Django model differs ​from the traditional MVC pattern. In the Django Model-View-Template MVT pattern: ​Django framework acts as Controller. Django View describes which data to present, and ​Django Template describes exactly how data is presented.

---

### 2. [VIDEO TRANSCRIPT] Create a Django App
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/DTrfj/create-a-django-app
- **Method:** `dom_transcript` | **Length:** 5900 chars

​Welcome to Create a Django App! After watching this video, you will be able ​to: Describe the Django web app structure, and ​create and run a simple Django web app. Let’s look at a typical Django development ​process. The order of these steps may vary. First, we create a Django project which is ​a container for Django apps and settings. Then we create and add one or more Django ​apps to the project. In Core Development, we create Django models ​to model the data and create views to determine which data need to be presented to the UI.

​We also map the request URLs to our views so Django can forward requests to corresponding ​views via URLs. Then we can start designing and building the ​UI. Once we are confident of the current version, we can perform unit or system tests. ​After the core development is done, we need to make our Django app production-ready, using ​Add-ons such as an admin site or a 3rd party frontend library. ​Once we have a working Django app, we can deploy it on a web server, either on premise ​or on cloud, and monitor the server status. A Django project is essentially a Python package ​that contains all the settings for an instance of Django app. ​To create a Django project, open a command-line terminal and run `django-admin startproject ​mysite`. This initializes a Django project with related files and folders.

​You need to know the usage for some core files that Django creates. ​manage.py is a command-line interface used to interact with the Django project to start ​the server, migrate models, and so on. settings.py contains the settings and configurations ​for your Django project. urls.py contains the URL and routing definitions ​of your Django app. Once you have created the Django project container, ​you can add your first Django app to it. We’ll call our first app “onlinecourse.” ​From the mysite project directory, run `python manage.py startapp onlinecourse`. Django ​will create a temporary app structure and some important app files. ​admin.py includes everything you need to create and customize an admin site to manage users ​and content. models.py contains the data models and ORM. ​views.py contains view functions and classes to create views. ​urls.py contains the URL declarations and routing for the app. ​app.py contains the application configuration class. ​The migrations folder contains scripts for model migration. ​Now, we add the `onlinecourse` app we just created to our `mysite` Django project.

​Open the settings.py file in the mysite folder, find the INSTALLED_APPS list in the settings ​file, and add a new entry called 'onlinecourse.apps.OnlinecourseConfig` to the list. ​The OnlinecourseConfig is a configuration class that represents the onlinecourse app. ​Now that our app is plugged in, we can optionally set up a database for it. ​The mysite/settings.py file has a DATABASES dictionary to configure the databases for ​our app. We add a database instance by adding its connection information such as engine, ​name, username, and password. Once we have set up our app and database, ​we can define our Django Models as the ORM component between objects and database tables. ​Let’s define a simple Course model here with fields like name and description.

​Next, we tell Django we’ve updated the model by running `python manage.py makemigrations ​onlinecourse`. Django then will create migration scripts under the `migrations` folder. ​To see more details about the SQL statements for the migration, we could run “python, ​manage.py, sqlmigrate, onlinecourse 001.” Here, an onlinecourse_course table will be ​created. Run “python, manage.py, migrate,” to run ​the migration scripts. Next, we create a simple view and a hard-coded ​html template to present the course object. Open the onlinecourse/views.py file to add ​a course_list view function. It accepts an HTTP Request object and returns ​an HttpResponse object. First, we get the course object from the database ​as a course object. Then, we create an html template and dynamically ​insert the course name into the placeholder. Finally, we add the completed html string ​as the content of the HttpResponse and return it to the UI.

​Now we associate the course_list view with a URL so Django will route the request URL ​to the view to be handled. URL routes are defined in a URLConf file for ​each app as well as for the Django project. To create a URLConf file for onlinecourse ​app, we first create a urls.py file under onlinecourse/ folder and then add a path object ​pointing a URL route to the course_list view we created. ​The first argument of the path constructor is the `route`. It defines URL patterns for ​Django to parse and match from the HTTP request to a view. Here we leave it as empty, meaning ​the root URL, host/onlinecourse, will be mapped to our course_list view. ​Next, we point the root URLConf file of onlinecourse app to the project’s root URLConf file.

​We open the project’s URLConf file called mysite/urls.py and add a path object referencing ​the onlinecourse app’s URLConf. So, when Django receives any URLs with the suffix onlinecourse/, ​it will try to match any URLs in the onlinecourse.urls.py file. ​And our Django app is set up. Let’s check the result. ​First, we call the `python manage.py runserver” command-line, which will start a development ​server locally on 127.0.0.1 with default port 8000 for us to host the Django project and ​app we just created. Once the server starts, we go to the root ​URL of the online course app. We should see a web page displaying the sentence: ​“The first course we created is `Cloud Application Development with Database`.”

​This simple html file is generated by the course_list view function we created earlier. ​In this video, you learned: The Django project and app structure and key ​files, A typical Django app development process, ​and how to create and run a simple Django app.

---

### 3. [VIDEO TRANSCRIPT] Django Admin
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/jeS2i/django-admin
- **Method:** `dom_transcript` | **Length:** 5364 chars

​[Music] Welcome to Django Admin. After watching this video, you will be able to ​build an admin site to manage the content of an online course app without using the ​Model APIs in the shell, and customize the admin site. ​Let’s review the models we will be using for our online course app. ​The app has some common entities for an online learning application, ​such as Course, Lessons, Questions, and Choices. For persona, it has User, Learner, and Instructor. ​For actions, it has Course Enrollment and Question submission. ​With so many entities and their relationships, you can imagine how hard it would be for ​developers to build this online course app. Fortunately, Django provides developers with ​a very powerful Django admin site to manage this content with minimal coding efforts.

​Django framework has a clear separation between content publishers and users. Django provides ​a built-in admin site to manage content. For an online course app, instructors or ​site managers can use the admin site to add or edit courses, lessons, questions, and so on. ​Once the course is ready and published, students can enroll in the courses on the public site. ​Let’s start building a Django admin site by first creating an admin user for the admin site. ​First, run a command-line `python, manage.py, createsuperuser`. ​It will ask for credentials like username and password.

​After creating the super user, you can start the django server. ​Go to the admin site and login with the credential you just created. ​You will need to register your models to admin site so you can manage them. ​First, open the onlinecourse/admin.py file and add two lines: admin.site.register(Course) and ​admin.site.register(Instructor) to register Course and Instructor models ​now refresh the admin site. You can see that under the Onlinecourse section, we have added ​Courses and Instructors. Based on the model’s fields, ​Django will create different UI widgets. For instructors, ​Django creates a checkbox for the Boolean field for `Full_time` and numeric input ​for the integer field `total learners`. The Instructor model is inherited from ​User, so User is a related object to Instructor which has some common ​information such as name and date of birth. Here we can just convert a user to an ​instructor and determine if the instructor is full-time or not.

​Notice that although there is a field called Total learners, we probably wouldn’t want to ​manage this field in the admin site, but instead we would calculate it from the number of learners ​that are enrolled in the instructor’s course. Later, we will show you how to choose the fields ​you want to be managed in the admin site. We can create a course by entering its name, ​description, image for the course introduction, publication date, instructors, and so on. ​Developers may only want to include some of the model fields in the admin ​site and to specify a particular order. To select the fields to include, we create a ​model admin class and add a fields list with the field name we want to be included in the model. ​For example, for Course model, we create a CourseAdmin class with a list of fields we ​want to include in the admin site. The order will be pub_date, name, and description.

​Once we have defined CourseAdmin, we modify the admin.site.register method ​to add the CourseAdmin as the second parameter. After refreshing the admin site and trying to ​add a course, only pub date, name, and description are shown and can be edited. ​One course may contain many lessons and questions. Instead of adding each model ​one by one using its own admin form, we can add course and lessons together on one form, ​using admin.StackedInline or admin.TabularInline objects. ​We can create a LessonInLine object by specifying its model to be Lesson and `extra` to be 5, ​which means we want to add at most 5 lessons together with a course at the same time. ​In the CourseAdmin object which defines the course admin form, we add an inlines list to ​include the LessonInline class we defined. After refreshing the page, you can see ​that a Lessons section appears within the Course admin form. You can add the title, ​order, and content of a lesson, which will be added into the course automatically by Django.

​When we display multiple courses or other models in a tabular form, ​we need to determine the fields to appear in the table. For example, for a list of ​courses, we only want to show the name and publication date of the course in the table. ​We do this by adding a list_display with the list of fields we want ​to be shown on the course change table. After refreshing the page, the course change table ​now shows the course name and publication date columns as we defined them in list_display. ​The course change list may be very long, and you may want to be able to search and filter the list. ​To enable search and filter on the course change list, add the search_fields to include the fields ​you want to search and the list_filter to include the fields you want to filter. ​After refreshing the page, a Search box and a Filter menu appear ​on the course change list for you to search and filter the courses on the admin page.

​In this video, you learned that Django Admin site is very powerful and ​easy to use for site managers to manage content. The look and functions can also be customized.

---

### 4. [VIDEO TRANSCRIPT] Django Views
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/d4cVA/django-views
- **Method:** `dom_transcript` | **Length:** 2834 chars

​Welcome to Django Views! After watching this video, you will be able to: ​Understand and create a Django view. A view takes a Web request such as HTTP GET, POST, ​DELETE, or UPDATE and returns a Web response. The web response can be a string, a JSON/XML ​file, an HTML page, or an error status indicating errors on the client or server side. ​Let’s see how to build a function-based view. Like other Django functions, View accepts ​arguments as input and returns something. Normally it needs an HTTP request object as the first ​argument. This object contains read-only metadata such as method, header, parameters, or payload.

​The request method is an HTTP GET method or HTTP POST method, and the view normally needs ​to process using logic. For example, here we query the first course record from the database ​and insert its name into an html template. After processing the http request with ​business logic, an HttpResponse object will be populated and returned to the UI . You can ​typically pass contents such as an HTML page, a string, or a bytestring to the HTTPResponse ​constructor to create and return an HTTPResponse. After creating the view, you map a URL pattern to ​it so that the URL in an HTTPRequest will be mapped to your view function. ​To do this, open the URLConf file - normally called urls.py - in your app’s root folder. ​Then add a path object with the first argument route, which specifies a URL pattern.

​Django will compare the requested URL against each pattern in the urlpatterns list. ​The second argument is the view function we defined in the previous slide. ​The name argument lets you refer to the view from other places in Django, so you ​can change the URL as often as needed and use the reference name to refer to the URL pattern. ​Sometimes you also need to specify an app_name as the prefix or namespace. ​Here, we called our app “onlinecourse” and the name of the view is ‘course’. So, we can refer ​to this URL pattern using onlinecourse:course from anywhere in our Django project. ​Each HTTP response is associated with a status code. In our previous result, ​a default 200 code included in the HTTP response indicates the request was processed successfully.

​However, the response of a view can also be an error. ​For example, when the view cannot find the course in the database, ​it should return a “not found” error to the user. The HTTP error response can be returned by adding ​an error status such as 404 Not Found to the status argument of the HttpResponse constructor, ​along with the content, such as an error message or an error html page ​If the course can be found, a 200 OK status code can be used with a success message or html page. ​In this video, you learned: What Django views are and ​how to create a Django view to receive an HTTP request and send an HTTP response.

---

### 5. [VIDEO TRANSCRIPT] Django Template
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/qPaD9/django-template
- **Method:** `dom_transcript` | **Length:** 4082 chars

​Welcome to Django Template. After watching this video, you will be able ​to: Combine Django views and templates to present ​your data as dynamic HTML pages. You create templates in Django to specify ​how your data will be presented. A Django template combines static HTML elements ​with Django template tags and variables to describe ​how the dynamic parts will be inserted. These work together to ​generate an html page that is rendered in a user’s web browser. ​A Django template is essentially an html file with Django template tags and variables, which ​will be interpreted by the Django template engine. ​To add a template file to our onlinecourse app, we create a folder under the onlinecourse ​root folder called `templates`. Within the `templates` folder we create a second `onlinecourse` ​folder. As such, we could refer to the template file as “onlinecourse/course_list.html.”

​Note that we have two onlinecourse folders in the template path. The main reason is the ​second onlinecourse acts as a name space to distinguish template files with the same name ​in other apps. The best way to ensure that we’re pointing Django at the right template ​is by name spacing the templates by putting them inside another directory named for the ​onlinecourse itself. After a template file is created, it will ​be rendered with a context, which is a dictionary-like object returned by views. ​Rendering replaces variables with their values, which are looked up in the context, and executes ​tags. Everything else is output as is. Here we use an if-else tag to check if the ​course_list list returned by server exists. If it does, then use a “for loop” tag ​to iterate the list. If not, generate an html paragraph tag indicating no courses are available.

​The course and course_list are variables from the context. ​If a variable represents an object, you can use dot notation to look up its attributes. ​Once we have created a template html file, we need to fill the template with data. This ​logic is handled by views. This is an example of an index view which ​first finds all courses in the database. Then, we create a dictionary-like object called ​context and add a `course_list` key with an iterable courses QuerySet. ​Next, instead of returning an HttpResponse object directly, we use a render method here ​to combine a given template with a given context dictionary. As a result, the render method ​returns an HTTPResponse wrapping the rendered text.

​In our index view example, the first argument is the original http request, the second argument ​is a relative path to the template html file, and the third argument is the context which ​will be integrated with the template file. We’ve now created templates and views and ​configured the URL for the view. The view finds a list of courses and calls ​the render method to load the template file and insert the course list. ​In the template file, each course’s name will be displayed as an html header and course ​description will be displayed as an html paragraph. Then we can go to the index view URL. The ​generated web page will display a list of two courses: `Introduction to Python` and ​`Django course.` You have seen how to use Django template to ​present the data provided by Django views as html files.

​To improve an html file by making it more interactive, responsive, and stylized, we ​need to use static resource files such as CSS, media, and JavaScript. Now let’s see ​how to beautify our course index page by adding a simple CSS file. ​To use a CSS stylesheet created in our Django app, we need to first use load static to load ​a static tag set and then use the static tag to generate the absolute URL given a relative ​path. Next, we add the CSS classes to body, paragraph, ​and horizontal line tags, respectively. Here is the updated index page with CSS added. ​Note the absolute path URL has been generated. The background is now light gray, and the ​course descriptions are green and separated by a horizontal line.

​In this video, you learned: how to create Django templates to present ​your data.

---

### 6. [READING] Module 3 Summary: Full-stack Django Development Reading • 2 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/RIzzw/module-3-summary-full-stack-django-development
- **Method:** `dom_reading_cml` | **Length:** 1738 chars

Congratulations! You have completed this module. At this point in the course, you know:

- The Model-View-Controller design pattern divides application logic into three components:
- Model accesses and manipulates data
- View presents data in various forms
- Controller coordinates between Model and View
- The Django Model-View-Template pattern is like MVC, except there is no Controller, and the Django server performs the controller function.
- In Django, a View is a Python function that takes a Web request and applies the necessary logic to generate a Web response.
- Django uses a template containing static HTML elements and special Python code to generate dynamic Web pages.
- When you create a Django project, Django creates some core files.
- manage.py is a command-line interface used to interact with the Django project
- settings.py contains the settings and configurations for your Django project
- urls.py contains the URL and routing definitions of your Django app
- You start building a Django admin site by creating an admin user.
- You can then log in as a superuser and register your models to the admin site so you can manage them.
- You can customize the admin form and add search and filters.
- A Django View takes a Web request such as HTTP GET, POST, DELETE, or UPDATE and returns a Web response. The web response can be a string, JSON/XML file, HTML page, or an error status indicating client or server-side errors.
- You create templates in Django to specify how your data will be presented. A Django template combines static HTML elements with Django template tags and variables to describe how the dynamic parts will be inserted. These work together to generate an HTML page rendered in a user’s web browser.

---

### 7. [READING] Module 3 Cheat Sheet: Full-stack Django Development Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/dqK5n/module-3-cheat-sheet-full-stack-django-development
- **Method:** `dom_reading_cml` | **Length:** 1064 chars

| Package/Method | Description | Code Example |
| --- | --- | --- |
| count() | Counts the number of objects. | MyModel.objects.count() |
| Sum() | Provides the sum of a field. | MyModel.objects.aggregate(Sum('field')) |
| Avg() | Calculates the average of a field. | MyModel.objects.aggregate(Avg('field')) |
| Max() | Provides the maximum value of a field. | MyModel.objects.aggregate(Max('field')) |
| Min() | Provides the minimum value of a field. | MyModel.objects.aggregate(Min('field')) |
| order_by() | Orders objects based on a field. | MyModel.objects.order_by('field') |
| order_by(-) | Order objects based on fields in descending order. | MyModel.objects.order_by('-field') |
| select_related | Performs inner join. | MyModel.objects.select_related('related_model') |
| prefetch_related | Performs left Outer join. | MyModel.objects.prefetch_related('related_model') |
| many_to_many | Performs many-to-many join. | obj.many_to_many_field.all() |
| filter(ForeignKey) | Performs conditional joins. | MyModel.objects.filter(related_model__isnull=True) |

---
