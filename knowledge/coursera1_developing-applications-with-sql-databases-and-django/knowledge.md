# Django Application Development with SQL and Databases

- **Course URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django
- **Crawled at:** 2026-11-24T15:06:45.767647
- **Extracted:** 46/46 items (29 videos, 17 readings) | 150,882 chars

---

## Module 1: Getting Started with SQL & Relational Databases

### 1. [VIDEO TRANSCRIPT] Course Introduction
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/glShv/course-introduction
- **Method:** `dom_transcript` | **Length:** 2632 chars

​Welcome to this introductory course on developing database-powered applications using Django. ​In this course, you will learn about the fundamentals of working with databases and SQL. ​You will also hone the skills to develop web applications that store ​and manage data in relational databases using the Django framework in Python. ​This course is suitable for aspiring and existing software developers. ​To benefit from this course, ​you should have a working knowledge of GitHub, Python, HTML, and CSS. ​These skills are taught in the previous courses in IBM Full Stack Software ​Developer Professional Certificate and the IBM Back-End Development Professional Certificate. ​Module one introduces fundamental database concepts and the basics ​of SQL, a simple and powerful programming language for querying and managing data.

​You will learn about relational and non-relational databases and complete ​several hands-on labs to perform the Create, Read, Update, and Delete or CRUD operations using SQL. ​In Module two, you will learn about Django, Object-oriented programming ​and be introduced to object-relational mapping or ORM framework and tools. ​You will get hands-on experience deploying your first Django Web app. ​Module three explores how the Django Model-View-Template pattern works ​together to present data on a website. You will discover how to combine Django ​views and templates to present your data as dynamic web pages and build ​an admin site with user interface (or UI) features such as Search and Filter. ​Building a class-based view in module four will add to your Django skills. ​You will also learn about authentication and authorization in Django and how to add Bootstrap, ​an open-source web front-end framework, to your Django template to build interactive web pages.

​You will create a Django web app with login, log-out, and user registration capabilities. ​In module five, you will complete a final project to apply your skills by adding new ​features to a Django online course app. In the final project, you will: ​Learn project requirements and download the MVP app. ​Build models and templates. Develop new app functionalities to submit, ​display, and evaluate results, And run and test your app. ​To get the most from this course, watch every video and check your learning with each quiz. ​Complete the hands-on labs to practice your new skills and ​continue building a portfolio demonstrating your abilities.

​And feel free to converse with the course staff and your peers in the Course Discussion Forums. ​Congratulations on beginning the next step on this exciting journey. And good luck.

---

### 2. [READING] Helpful Tips for Course Completion
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/6c4fW/helpful-tips-for-course-completion
- **Method:** `dom_reading_cml` | **Length:** 76 chars

## Helpful Tips for Course Completion

#### Loading audio...

#### Completed

---

### 3. [READING] Syllabus and Prerequisites
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/aoASD/syllabus-and-prerequisites
- **Method:** `dom_reading_cml` | **Length:** 1196 chars

Welcome to Developing Applications with SQL, Databases, and Django. In this 5-week class, you can expect to spend approximately 2-3 hours per module.

Prerequisites

This course assumes you’re familiar with GitHub, HTML, CSS, and Python.

Course Outline

Module 1: Getting Started with SQL & Relational Databases

- Lesson 0: Welcome
- Lesson 1: Introduction to Databases
- Lesson 2: Basic SQL Statements
- Lesson 3: (Optional) Creating Tables, Sorting Results, and Join
- Lesson 4: Module 1 Summary

Module 2: ORM: Bridging the Gap Between the Real World and Relational Model

- Lesson 1: ORM: Bridging the Gap Between the Real World and Relational Model
- Lesson 2: Module 2 Summary and Graded Quiz

Module 3: Full-stack Django Development

- Lesson 1: Full-stack Django Development
- Lesson 2: Module 3 Summary and Graded Quiz

Module 4: Consolidate and Deploy your Django App

- Lesson 1: Consolidate and Deploy your Django App
- Lesson 2: Module 4 Summary and Graded Quiz

Module 5: Final Project: Enhance Online Course App with New Features

- Lesson 1: Practice Project: Customer360
- Lesson 2: Final Project: Add a New Assessment Feature to an Online Course App
- Lesson 3: Course Wrap Up

---

### 4. [VIDEO TRANSCRIPT] Introduction to Data and Databases Video • 2 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/O4x2p/introduction-to-data-and-databases
- **Method:** `dom_transcript` | **Length:** 2488 chars

​Data is a collection of facts in the form of words, numbers, or even pictures, ​data is one of the most critical assets of any business, it is used and ​collected practically everywhere. ​Your bank stores data about you, your name, address, phone number, ​account numbers, etcetera. ​Your credit card company and your PayPal accounts also store data about you. ​Data is important, so it needs to be secure and it needs to be stored and ​accessed quickly, the answer is a database, so what is a database? ​A database is a collection of data or information designed for the input, ​storage, search and retrieval and modification of data. ​And a database management system, or DBMS, ​is a set of programs that creates and maintains the database. ​It allows you to store, modify and ​extract information from the database using a function called querying.

​For example, if you want to find customers who have been inactive for six months or ​more using the querying function. ​The database management system will retrieve data of all customers from ​the database that have been inactive for six months or more. ​Even though a database and DBMS mean different things, ​the terms are often used interchangeably. ​There are different types of databases. ​Several factors influence the choice of database, such as the data type and ​structure, querying mechanisms, latency requirements, ​transaction speeds, and intended use of the data. ​It's important to mention two main types of databases here relational and ​non-relational databases. ​Relational databases, also referred to as RDBMSs, ​build on the organizational principles of flat files, ​with data organized into a tabular format with rows and columns.

​Following a well-defined structure and schema, however, ​unlike flat files, RDBMSs are optimized for data operations and ​querying involving many tables and much larger data volumes. ​Structured query language, or SQL, ​is the standard querying language for relational databases. ​Then we have non-relational databases, also known as NoSQL, or not only SQL. ​Non-relational databases emerged in response to the volume, diversity and ​speed at which data is being generated today. ​Mainly influenced by advances in cloud computing, the internet of things, and ​social media proliferation. ​Built for speed, flexibility and scale, ​non-relational databases made it possible to store data in a schema-less or ​free form fashion, NoSQL is widely used for processing big data. ​[MUSIC]

---

### 5. [VIDEO TRANSCRIPT] Relational Databases Video • 7 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/Q2mXQ/relational-databases
- **Method:** `dom_transcript` | **Length:** 6232 chars

​[MUSIC] ​A relational database is a collection of data organized into a table structure ​where the tables can be linked or related, based on data common to each. ​Tables are made of rows and columns, where rows are the records and ​the columns the attributes. ​Let's take the example of a Customer Table that maintains data about each ​customer in a company. ​The columns or attributes in the Customer Table are the Customer ID, ​Customer Name, Customer Address, and Customer Primary Phone. ​And each row is a customer record. ​Now let's understand what we mean by tables being linked or ​related based on data common to each. ​Along with the Customer Table, ​the company also maintains transaction tables that contain data describing ​multiple individual transactions pertaining to each customer.

​The columns for the transaction table might include the Transaction Date, ​Customer ID, Transaction Amount, and Payment Method. ​The Customer Table and ​transaction tables can be related based on the common Customer ID field. ​You can query the Customer Table to produce reports, such as a customer ​statement that consolidates all transactions in a given period. ​This capability of relating tables based on common data enables you to retrieve ​an entirely new table from data in one or more tables with a single query. ​It also allows you to understand the relationships among all available data and ​gain new insights for making better decisions. ​Relational databases use structured query language or SQL for querying data. ​We'll learn more about SQL later in this course.

​Relational databases build on the organizational principles of flat ​files such as spreadsheets, with data organized into rows and ​columns following a well defined structure and schema. ​But this is where the similarity ends. ​Relational databases, by design, are ideal for the optimized storage, ​retrieval and processing of data for large volumes of data. ​Unlike spreadsheets that have a limited number of rows and columns, ​each table in a relational database has a unique set of rows and columns, ​and relationships can be defined between tables which minimizes data redundancy. ​Moreover, you can restrict database fields to specific data types and values, ​which minimizes irregularities and leads to greater consistency and data integrity. ​Relational databases use SQL for querying data, ​which gives you the advantage of processing millions of records and ​retrieving large amounts of data in a matter of seconds. ​Moreover, the security architecture of relational databases provides ​controlled access to data and also ensures that the standards and ​policies for governing data can be enforced.

​Relational databases range from small desktop systems to massive ​cloudbased systems. ​They can be either open source and internally supported open source with ​commercial support or commercial closed source systems. ​IBM DB 2, Microsoft SQL Server, MySQL, Oracle database, and ​PostgreSQL are some of the popular relational databases. ​Cloud-Based Relational Databases, also referred to as Database-as-a-Service, ​are gaining wide use as they have access to the limitless compute and ​storage capabilities offered by the cloud. ​Some of the popular Cloud Relational Databases include ​Amazon Relational Database Service or RDS, Google Cloud ​SQL, IBM DB 2 on Cloud, Oracle Cloud, and SQL Azure. ​RDBMS is a mature and well documented technology, ​making it easy to learn and find qualified talent. ​One of the most significant advantages of the Relational Database Approach is ​its ability to create meaningful information by joining tables.

​Some of its other advantages include flexibility. ​Using SQL, you can add new columns, add new tables, rename relations, ​and make other changes while the database is running and queries are happening. ​Reduced redundancy. ​Relational databases minimize data redundancy. ​For example, the information of a customer appears in a single entry in ​the Customer Table, and the Transaction Table pertaining to ​the customer stores a link to the Customer Table. ​Ease of backup and disaster recovery. ​Relational databases offer easy export and import options, ​making backup and restore easy.

​Exports can happen while the database is running, making restore on failure easy. ​Cloud-Based Relational Databases do continuous mirroring, ​which means the loss of data on restore can be measured in seconds or less. ​ACID compliance. ​ACID stands for atomicity consistency, isolation and durability. ​ACID compliance implies that the data in the database remains accurate and ​consistent despite failures and database transactions are processed reliably. ​Now we'll look at some use cases for relational databases. ​Online Transaction Processing OLTP applications are focused on ​transaction oriented tasks that run at high rates.

​Relational databases are well suited for ​OLTP applications because they can accommodate a large number of users. ​They support the ability to insert, update or delete small amounts of data, ​and they also support frequent queries and updates as well as fast response times. ​Data Warehouses. ​In a data warehousing environment, ​relational databases can be optimized for online analytical processing or ​OLAP, where historical data is analyzed for business intelligence. ​IoT Solutions Internet of Things, or ​IoT solutions require speed as well as the ability to collect and ​process data from edge devices, which need a lightweight database solution. ​This brings us to the limitations of RDBMS. ​RDBMS does not work well with semi structured or unstructured data and ​is therefore not suitable for extensive analytics on such data.

​For migration between two RDBMS, schemas and type of data need ​to be identical between the source and destination tables. ​Relational databases have a limit on the length of data fields, which means if ​you try to enter more information into a field than it can accommodate, ​the information will not be stored. ​Despite the limitations and the evolution of data, in these times of big ​data cloud computing, IoT devices, and social media, RDBMS continues ​to be the predominant technology for working with structured data. ​[MUSIC]

---

### 6. [VIDEO TRANSCRIPT] Non-relational Databases Video • 7 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/MRgZ7/non-relational-databases
- **Method:** `dom_transcript` | **Length:** 5840 chars

​NoSQL, which stands for not only SQL or ​sometimes Non SQL is a non-relational database design that ​provides flexible schemas for the storage and retrieval of data. ​NoSQL databases have existed for many years but have only recently become more ​popular in the era of cloud, big data, and high volume web and mobile applications. ​They are chosen today for their attributes around scale, ​performance, and ease of use. ​It's important to emphasize that the no in NoSQL is ​an abbreviation for not only and not the actual word no. ​NoSQL databases are built for specific data models and have flexible ​schemas that allow programmers to create and manage modern applications. ​They do not use a traditional row, column, table database design with fixed schemas, ​and typically, not use the structured query language or SQL to query data. ​Although some may support SQL or SQL like interfaces.

​NoSQL allows data to be stored in a schema less or free form fashion. ​Any data, be it structured, semi structured, or ​unstructured can be stored in any record. ​Based on the model being used for storing data, ​there are four common types of NoSQL databases. ​Key value store, document based, column based, and graph based. ​Key value store, ​data in a key value database is stored as a collection of key value pairs. ​The key represents an attribute of the data and is a unique identifier. ​Both keys and values can be anything from simple integers or ​strings to complex JSON documents.

​Key value stores are great for storing user session data and ​user preferences, making real time recommendations and ​targeted advertising, and in-memory data caching. ​However, if you want to be able to query the data on specific data value, ​need relationships between data values, or ​need to have multiple unique keys, a key value store may not be the best fit. ​Redis, Memcached and DynamoDB are some well ​known examples in this category. ​Document based, document databases store each record and ​its associated data within a single document. ​They enable flexible indexing, powerful ad hoc queries, and ​analytics over collections of documents. ​Document databases are preferable for ecommerce platforms, ​medical records, storage, CRM platforms, and analytics platforms. ​However, if you're looking to run complex search queries and ​multi operation transactions, ​a document based database may not be the best option for you.

​MongoDB, DocumentDB, CouchDB, and ​Cloudant are some of the popular document based databases. ​Column based, column based models store data in cells grouped ​as columns of data instead of rows. ​A logical grouping of columns, ​that is columns that are usually accessed together is called a column family. ​For example, a customer's name and profile information will most likely ​be accessed together, but not their purchase history, so customer name and ​profile information data can be grouped into a column family. ​Since column databases store all cells corresponding to a column ​as a continuous disk entry, accessing and searching the data becomes very fast. ​Column databases can be great for systems that require heavy write requests, ​storing time series data, weather data, and IoT data. ​But if you need to use complex queries or change your querying patterns frequently, ​this may not be the best option for you.

​The most popular column databases are Cassandra and HBase. ​Graph based, ​graph based databases use a graphical model to represent and store data. ​They are particularly useful for visualizing, analyzing, and ​finding connections between different pieces of data. ​The circles are nodes and they contain the data, the arrows represent relationships. ​Graph databases are an excellent choice for working with connected data, ​which is data that contains lots of interconnected relationships. ​Graph databases are great for social networks, ​real time product recommendations, network diagrams, ​fraud detection, and access management. ​But if you want to process high volumes of transactions, ​it may not be the best choice for you because graph databases ​are not optimized for large volume analytics queries.

​Neo4J and CosmosDB are some of the more popular graph databases. ​NoSQL was created in response to the limitations of traditional ​relational database technology. ​The primary advantage of NoSQL is its ability to handle large volumes ​of structured, semi structured, and unstructured data. ​Some of its other advantages include the ability to run as distributed systems ​scaled across multiple data centers, ​which enables them to take advantage of cloud computing infrastructure. ​An efficient and cost effective scale-out architecture that provides ​additional capacity and performance with the addition of new nodes and ​simpler design, better control over availability and improved scalability ​that enables you to be more agile, more flexible, and to iterate more quickly. ​To summarize the key differences between relational and ​non-relational databases, RDBMS schemas rigidly define how ​all data inserted into the database must be typed and composed, ​whereas NoSQL databases can be schema agnostic, allowing unstructured and ​semi-structured data to be stored and manipulated. ​Maintaining high-end commercial relational database management systems is expensive, ​whereas NoSQL databases are specifically designed for low-cost commodity hardware.

​Relational databases, unlike most NoSQL, support ACID compliance, ​which ensures reliability of transactions and crash recovery. ​RDBMS is a mature and well documented technology, ​which means the risks are more or less perceivable as compared to NoSQL, ​which is a relatively newer technology. ​Nonetheless, NoSQL databases are here to stay and ​are increasingly being used for mission critical applications. ​[MUSIC]

---

### 7. [VIDEO TRANSCRIPT] Relational Data Concepts Video • 5 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/wYg5I/relational-data-concepts
- **Method:** `dom_transcript` | **Length:** 4394 chars

​Hello and welcome to Database Concepts. ​In this video, we will learn about different types of models, how we use models to map ​data to tables, and define relationships between tables. ​At the end of this lesson, you will be able to explain the advantage of the relational ​model, explain how the entity name and attributes map to a relational database table, describe ​the difference between an entity and an attribute, identify some commonly used data types, and ​describe the function of primary keys. ​The relational model is the most used data model for databases because this model allows ​for data independence. ​Data is stored in a simple data structure. ​Tables: this provides logical data independence, physical data independence, and physical storage ​independence. ​An entity relationship data model, or ER data model, is an alternative to a relational data ​model.

​Using a simplified library database as an example, this figure shows an entity relationship ​diagram or ERD that represents entities called tables and their relationships. ​In the library example, we have books. ​A book can be written by one or many authors. ​The library can have one or many copies of a book. ​Each copy can be borrowed by only one borrower at a time. ​An entity relationship model proposes thinking of a database as a collection of entities ​rather than being used as a model on its own. ​The ER model is used as a tool to design relational databases.

​In the ER model, entities are objects that exist independently of any other entities ​in the database. ​The building blocks of an ER diagram are entities and attributes. ​An entity can be a noun: person, place, or thing. ​In an ER diagram, an entity is drawn as a rectangle. ​Entities have attributes which are the data elements that characterize the entity. ​Attributes tell us more about the entity. ​In an ER diagram, attributes are drawn as ovals.

​Using a simplified library as an example, the book is an example of an entity. ​Attributes are certain properties or characteristics of an entity and tell us more about the entity. ​The entity book has attributes such as book title, the edition of the book, the year the ​book was written, etc. Attributes are connected to exactly one entity. ​The entity book becomes a table in the database and the attributes become the columns in a ​table. ​A table is a combination of rows and columns. ​While mapping, the entity becomes the table.

​Having said that, the table has not yet taken the form of rows and columns. ​The attributes get translated into columns in a table providing the actual table form ​of rows and columns. ​Later, we add some data values to each of the columns, which completes the table form. ​Each attribute stores data values of different formats, characters, numbers, dates, currency, ​and many more besides. ​In the book table example, the title is made up of characters. ​As book titles vary in length, we can set the variable character data type for the title ​column: Varchar. ​For character columns that do not vary in length, we use character or Char.

​The edition and year columns would be numeric. ​The ISBN column would be Char because it contains dashes as well as numbers and so ​on. ​Using the book entity mapping as an example, we can create the tables for the remainder ​of our simplified library example using entity names, like author, author list, borrower, ​loan, and copy. ​The entity attributes will be the columns of the tables. ​Each table is assigned a primary key. ​The primary key of a relational table uniquely identifies each tuple or row in a table, preventing ​duplication of data and providing a way of defining relationships between tables. ​Tables can also contain foreign keys which are primary keys defined in other tables, ​creating a link between the tables.

​Now you know that the key advantage of the relational model is logical and physical data ​independence and storage independence. ​Entities are independent objects which can have multiple characteristics called attributes. ​When mapping to a relational database, entities are represented as tables and attributes map ​to columns. ​Common data types include characters such as Char and Varchar, numbers such as integer ​and decimal, and timestamps including date and time. ​A primary key uniquely identifies a specific row in a table and prevents duplication of ​data.

---

### 8. [READING] Module 1 Lesson 1 Summary Reading • 2 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/fSyZz/module-1-lesson-1-summary
- **Method:** `dom_reading_cml` | **Length:** 1103 chars

Congratulations! You have completed this lesson. At this point in the course, you know:

- Structured Query Language, or SQL, was designed to manage data in relational databases and is useful for handling structured data.
- Data is a collection of facts in words, numbers, and pictures.
- A database is a repository of data that provides functionality for adding, modifying, and querying data.
- Relational databases store tabular data as collections of related items, with columns containing item properties.
- The basic SQL statements are CREATE TABLE, INSERT, SELECT, UPDATE, and DELETE.
- Non-relational databases provide a flexible and scalable approach to storing and retrieving data.
- Relational databases are ideal for the optimized storage, retrieval, and processing of large volumes of data.
- RDBMS is a mature and well-documented technology, providing flexibility, reduced redundancy, ease of backup and disaster recovery, and ACID compliance.
- An Entity-Relationship model is a tool for designing relational databases. Entities become tables, and attributes are translated into columns. .

---

### 9. [VIDEO TRANSCRIPT] SELECT Statement Video • 3 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/qVQ5W/select-statement
- **Method:** `dom_transcript` | **Length:** 3320 chars

​Hello and welcome to retrieving data with a SELECT statement. ​In this video, we will learn about retrieving data from ​a relational database table by selecting columns of a table. ​At the end of this lesson, ​you will be able to retrieve data from a relational database table, ​to find the use of a predicate, ​identify the syntax of the SELECT statement using the WHERE clause, and ​list the comparison operators supported by a relational database management system. ​The main purpose of a database management system, ​is not just to store the data but also facilitate retrieval of the data. ​So, after creating a relational database table and inserting data into the table, ​we want to see the data. ​To see the data, we use the SELECT statement. ​The SELECT statement is a data manipulation language statement.

​Data Manipulation Language statements or DML statements are used to read and modify data. ​The SELECT statement is called a query, ​and the output we get from executing this query is called a result set or a result table. ​In its simplest form, a SELECT statement is select star from table name. ​Based on the book entity example, ​we would create the table using ​the entity name book and the entity attributes as the columns of the table. ​The data would be added to the book table by adding ​rows to the table using the insert statement. ​In the book entity example, select star from book gives the result set of four rows. ​All the data rows for all columns in the table book are displayed.

​In addition, you can also retrieve all the rows for all columns by ​specifying the column names individually in the SELECT statement. ​You don't always have to retrieve all the columns in a table. ​You can retrieve just a subset of columns. ​If you want, you can retrieve just two columns from the table book. ​For example book_id and title. ​In this case, the select statement is select book_id, title from book. ​In this case, only the two columns display for each of the four rows.

​Also notice that the order of the columns displayed ​always matches the order in the SELECT statement. ​However, what if we want to know the title of the book whose book_id is B1. ​Relational operation helps us in restricting ​the result set by allowing us to use the clause WHERE. ​The WHERE clause always requires a predicate. ​A predicate is conditioned evaluates to true, false or unknown. ​Predicates are used in the search condition of the WHERE clause. ​So, if we need to know the title of the book whose book_id is B1, ​we use the WHERE clause with the predicate book_id equals B1.

​Select book_id title from book where book_id equals B1. ​Notice the result set is now restricted to ​just one row whose condition evaluates to true. ​The previous example used comparison operator equal to in the WHERE clause. ​There are other comparison operators supported by ​a relational database management system: equal to, ​greater than, less than, ​greater than or equal to, ​less than or equal to, and not equal to. ​Now you can retrieve data and select columns from a relational database table, ​define the use of a predicate, ​identify the syntax of the SELECT statement using the WHERE clause, and ​list the comparison operators supported by a relational database management system. ​Thanks for watching this video.

---

### 10. [VIDEO TRANSCRIPT] COUNT, DISTINCT, LIMIT Video • 2 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/tiudn/count-distinct-limit
- **Method:** `dom_transcript` | **Length:** 1775 chars

​[MUSIC] ​Hello and welcome. ​In this video, we'll briefly present a few useful expressions that ​are used with select statements. ​The first one is COUNT, COUNT is a built-in database function that ​retrieves the number of rows that match the query criteria. ​For example, get the total number of rows in a given table, ​select COUNT(*) from tablename. ​Let's say you create a table called MEDALS which has a column called COUNTRY, and ​you want to retrieve the number of rows where the medal recipient is from Canada. ​You can issue a query like this: ​Select COUNT(COUNTRY) from MEDALS where COUNTRY='CANADA.' ​The second expression is DISTINCT.

​DISTINCT is used to remove duplicate values from a result set. ​Example, to retrieve unique values in a column, ​select DISTINCT columnname from tablename. ​In the MEDALS table mentioned earlier, ​a country may have received a gold medal multiple times. ​Example, retrieve the list of unique countries that received gold medals. ​That is, removing all duplicate values of the same country. ​Select DISTINCT COUNTRY from MEDALS where MEDALTYPE = 'GOLD'. ​The third expression is LIMIT, LIMIT is used for ​restricting the number of rows retrieved from the database.

​Example, retrieve just the first 10 rows in a table. ​Select * from tablename LIMIT 10. ​This can be very useful to examine the results set by looking at just a few ​rows instead of retrieving the entire result set which may be very large. ​Example, retrieve just a few rows in the MEDALS table for a particular year. ​Select * from MEDALS where YEAR = 2018 LIMIT 5. ​In this video we looked at some useful expressions that are used with select ​statements, namely the COUNT, DISTINCT, and LIMIT built-in functions. ​Thanks for watching this video.

​[MUSIC]

---

### 11. [VIDEO TRANSCRIPT] INSERT Statement Video • 2 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/Nmcg3/insert-statement
- **Method:** `dom_transcript` | **Length:** 2313 chars

​Hello, and welcome to the Insert Statement. In this video, we will learn about populating ​a relational database table. At the end of this video, you will be able to identify the ​syntax of the Insert Statement, and explain two methods to add rows to a table. ​After a table is created, the table needs to be populated with data. To insert data ​into a table, we use the Insert Statement. The Insert Statement is used to add new rows ​to a table. The Insert Statement is one of the Data Manipulation Language Statements.

​Data Manipulation Language Statements, or DML Statements, are used to read and modify ​data. Based on the Author entity example, we created the table using the entity name, ​Author, and the entity attributes as the columns of the table. ​Now we will add the data to the Author table by adding rows to the table. To add the data ​to the Author table, we use the Insert Statement. The syntax of the Insert Statement looks like ​this. Insert into TableName, ColumnName, Values. In this statement, TableName identifies the ​table. The ColumnName list identifies each column in the table. And the Values clause ​specifies the data values to be added to the columns in the table.

​To add a row with the data for Raul Chong, we insert a row with an Author underscore ​ID of A1, the last name as Chong, the first name as Raul, the email as rfc at ibm.com, ​the city as Toronto, and the country as CA, for Canada. The Author table has six columns, ​so the Insert Statement lists the six column names, separated by commas, followed by a ​value for each of the columns, also separated by commas. It is important that the number ​of values provided in the Values clause is equal to the number of column names specified ​in the ColumnName list. This ensures that each column has a value. ​Some databases allow inserting multiple rows in a single Insert Into statement by separating ​rows with commas in the Values clause. For example, in the Insert Statement, we are inserting ​two rows, one for Raul Chong and one for Rav Ahuja. However, SQLite does not support ​this feature, so row insertion must be done individually.

​Now you can identify the syntax of the Insert Statement and explain the two methods to add ​rows to a table, one row at a time or multiple rows. ​Thanks for watching this video.

---

### 12. [VIDEO TRANSCRIPT] UPDATE and DELETE Statements Video • 3 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/oX5Yh/update-and-delete-statements
- **Method:** `dom_transcript` | **Length:** 2926 chars

​Hello and welcome to the UPDATE Statement and the DELETE Statement. ​In this video, we will learn about altering and deleting data in a relational ​database table. ​At the end of this lesson, you will be able to identify the syntax of the UPDATE statement ​and DELETE statement, and explain the importance of the WHERE clause in these statements. ​After a table is created and populated with data, ​the data in a table can be altered with the UPDATE statement. ​The UPDATE statement is one of the data manipulation language or DML statements. ​DML statements are used to read and modify data. ​Based on the author entity example, we created the table using the entity name author ​and the entity attributes as the columns of the table.

​Rows were added to the author table to populate the table. ​Sometime later, you want to alter the data in the table. ​To alter or modify the data in the author table, we use the UPDATE statement. ​The syntax of the UPDATE statement looks like this: ​UPDATE [TableName] SET [[ColumnName]=[Value]] ​In this statement, table name identifies the table, ​the column name identifies the column value to be changed as specified in the WHERE condition. ​Let's look at an example. ​In this example, you want to update the first name and last name of the author ​with Author_Id A2 from Rav Ahuja to Lakshmi Katta. ​In this example, to see the update statement in action, ​we start by selecting all rows from the author table to see the values.

​To change the first name and last name to Lakshmi Katta, ​where the author ID is equal to A2, enter the UPDATE statement as follows: ​UPDATE AUTHOR SET LASTNAME='KATTA' FIRSTNAME='LAKSHMI' ​WHERE AUTHOR_ID='A2' ​Now, to see the result of the update, select all rows again from the author ​table and you will see that in row two the name changed from Rav Ahuja to Lakshmi Katta. ​Note that if you do not specify the WHERE clause, all the rows in the table will be updated. ​In this example, without specifying the WHERE clause, ​all rows in the table would have changed the first and last names to Lakshmi Kata. ​Sometime later, there might be a need to remove one or more rows from a table. ​The rows are removed with the DELETE statement. ​The DELETE statement is one of the data manipulation language ​statements used to read and modify data. ​The syntax of the DELETE statement looks like this: DELETE FROM [TableName] <WHERE [Condition]> ​The rows to be removed are specified in the WHERE condition.

​Based on the author entity example, we want to delete the rows for author ID A2 and A3. ​Let's look at an example. ​DELETE FROM AUTHOR WHERE AUTHOR_ID ID IN ('A2', 'A3') Note that if you do not ​specify the WHERE clause, all the rows in the table will be removed. ​Now, you can identify the syntax of the UPDATE statement and DELETE statement, and explain ​the importance of the WHERE clause in these statements. ​Thanks for watching this video.

---

### 13. [READING] Module 1 Lesson 2 Summary Reading • 2 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/ISlQa/module-1-lesson-2-summary
- **Method:** `dom_reading_cml` | **Length:** 1367 chars

Congratulations! You have completed this lesson. At this point in the course, you know:

- Structured Query Language, or SQL, is used for querying and managing data.
- SQL is useful for handling structured data or data incorporating relations among entities and variables.
- The SQL SELECT statement retrieves data from a relational database table.
- The SELECT statement is a query, and the output we get from executing this query is a Result Set or a Result Table.
- In its simplest form, the syntax for a SELECT statement is: SELECT * from TableName
- The SQL INSERT statement inserts data into a relational database table by adding rows.
- The syntax of the INSERT statement is: INSERT INTO TableNameColumnName VALUES (values)
- For the INSERT statement, the values provided in the Values clause must equal the number of column names specified in the Column Name list. This ensures that each column has a value.
- The SQL UPDATE statement is used to read and modify data.
- The syntax of the UPDATE statement is as follows: UPDATE [TableName] SET [[ColumnName]=[Value]] <WHERE [Condition]>
- The SQL DELETE statement is used to remove data from a table.
- The syntax of the DELETE statement is: DELETE FROM [TableName] <Where [Condition]>
- The WHERE clause specifies the rows in a table that will be acted on by a SQL statement such as SELECT, DELETE, or UPDATE.

---

### 14. [READING] Module 1 Cheat Sheet: Getting Started with SQL & Relational Databases Reading • 5 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/T7c7e/module-1-cheat-sheet-getting-started-with-sql-relational-databases
- **Method:** `dom_reading_cml` | **Length:** 2626 chars

| Package/Method | Description | Code Example |
| --- | --- | --- |
| SELECT | Retrieves data from one or more tables based on specified columns. | SELECT column1, column2 FROM table_name; |
| FROM | Specifies the table from which data is retrieved. | SELECT column1, column2 FROM table_name; |
| WHERE | Filters data based on specified conditions. | SELECT column1, column2 FROM table_name WHERE condition; |
| ORDER BY | Sorts the result set based on specified columns in ascending or descending order. | SELECT column1, column2 FROM table_name ORDER BY column1 ASC; |
| GROUP BY | Groups rows based on a specified column. | SELECT column1, COUNT(*) FROM table_name GROUP BY column1; |
| HAVING | Filters grouped data based on specified conditions. | SELECT column1, COUNT(*) FROM table_name GROUP BY column1 HAVING COUNT(*) > 1; |
| INSERT INTO | Inserts data into a table. | INSERT INTO table_name (column1, column2) VALUES (value1, value2); |
| UPDATE | Modifies data in a table based on specified conditions. | UPDATE table_name SET column1 = value1 WHERE condition; |
| DELETE FROM | Deletes data from a table based on specified conditions. | DELETE FROM table_name WHERE condition; |
| JOIN | Combines rows from multiple tables based on related columns. | SELECT column1, column2 FROM table1 JOIN table2 ON table1.column = table2.column; |
| INNER JOIN | Returns only matching rows from both tables. | SELECT column1, column2 FROM table1 INNER JOIN table2 ON table1.column = table2.column; |
| LEFT JOIN | Returns all rows from the left table and matching rows from the right table. | SELECT column1, column2 FROM table1 LEFT JOIN table2 ON table1.column = table2.column; |
| RIGHT JOIN | Returns all rows from the right table and matching rows from the left table. | SELECT column1, column2 FROM table1 RIGHT JOIN table2 ON table1.column = table2.column; |
| FULL JOIN | Returns all rows from both tables, regardless of the match. | SELECT column1, column2 FROM table1 FULL JOIN table2 ON table1.column = table2.column; |
| DISTINCT | Returns unique values from a column. | SELECT DISTINCT column1 FROM table_name; |
| COUNT | Counts the number of rows or non-null values in a column. | SELECT COUNT(*) FROM table_name; or SELECT COUNT(column1) FROM table_name; |
| SUM | Calculates the sum of values in a column. | SELECT SUM(column1) FROM table_name; |
| AVG | Calculates the average value of a column. | SELECT AVG(column1) FROM table_name; |
| MAX | Finds the maximum value in a column. | SELECT MAX(column1) FROM table_name; |
| MIN | Finds the minimum value in a column. | SELECT MIN(column1) FROM table_name; |

---

### 15. [READING] Bonus Lesson Overview Reading • 2 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/yCjIm/bonus-lesson-overview
- **Method:** `dom_reading_cml` | **Length:** 985 chars

There are many ways that you can use SQL to help analyze your data and present it in a way that supports your data story. In this bonus lesson, you will learn some SQL techniques beyond the basics, that will help you do more with data. You’ll learn how to use SQL commands to create tables. You’ll also learn how to refine your query results, as well as sort and organize your results, making your query results easier to take useful insights from.

This bonus lesson is provided for informational purposes only and does not contain any graded content. While useful to know these things about SQL, those developing applications will typically employ other mechanisms to perform these tasks, some of which will be taught in later modules of this course.

If you want to learn more about SQL beyond what is covered in this course, the following course will be of interest, especially for those in Data Engineering, Data Science or Data Analyst tracks:

- SQL for Data Science with Python

---

### 16. [VIDEO TRANSCRIPT] CREATE Table Statement Video • 3 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/oPrhc/create-table-statement
- **Method:** `dom_transcript` | **Length:** 2687 chars

​[Music] In this video, we will learn how to create a relational database table. ​CREATE ​The syntax of the CREATE table is shown here: ​You start with “CREATE TABLE” followed by the name of the table you want to create. ​Then enclose rest of the statement inside a pair of parenthesis or round brackets. ​Each row inside the parenthesis specifies the name of a column followed by its datatype ​and possibly some additional optional values that we will see later. ​Each attribute or column definition is separated by a comma. ​For example, if we want to create a table for provinces in Canada you would specify: ​CREATE TABLE provinces (id char(2) Primary key not null comma name varchar(24) close ​parenthesis. ​In this example, the data types used are: CHAR which is a character string of a fixed ​length, in this case 2.

​And VARCHAR, which is a character string of a variable length. ​In this case, this variable character field can be up to 24 characters long. ​Issuing this statement would create a table in the database with 2 columns. ​The first column id for storing the abbreviated 2 letter province short codes such as AB , BC, ​etc. ​And the second column called name for storing the full name of the province, such as ALBERTA, ​BRITISH COLUMBIA, etc. ​Now, let’s look at a more elaborate example based on the Library database. ​This database includes several entities such as AUTHOR, BOOK, BORROWER, etc.

​Let’s start by creating the table for the AUTHOR entity. ​The name of the table will be AUTHOR, and its attributes ​such as AUTHOR_ID, FIRSTNAME, LASTNAME, etc. will be the columns of the table. ​In this table, we will also assign the Author_ID attribute as the Primary Key, ​so that no duplicate values can exist. ​Recall, the Primary Key of a relational table uniquely identifies each tuple (or row) in ​a table. ​To create the Author table, issue the following command: ​CREATE TABLE author ( author_id CHAR(2) PRIMARY KEY NOT NULL, lastname VARCHAR(15) NOT NULL, ​firstname VARCHAR(15) NOT NULL, email VARCHAR(40), city VARCHAR(15), ​country CHAR(2) ) ​Note that the Author_ID is the Primary Key. ​This constraint prevents duplicate values in the table. ​Also note that Last Name and First Name have the constraint NOT NULL.

​This ensures that these fields cannot contain a NULL value, since an author must have a ​name. ​Now you know that: ​CREATE is a DDL statement for creating Entities or tables in a database. ​The CREATE TABLE statement includes definition of attributes of columns in the table, including ​Names of columns, ​Datatypes of columns, ​and other Optional values if required such as the Primary Key constraint. ​Thanks for watching this video.

---

### 17. [VIDEO TRANSCRIPT] ALTER, DROP, and Truncate Tables Video • 4 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/sEbau/alter-drop-and-truncate-tables
- **Method:** `dom_transcript` | **Length:** 3491 chars

​[Music] Hello, and welcome to ALTER, DROP, and TRUNCATE tables. ​After watching this video, you will be able to: ​Describe the ALTER TABLE, DROP TABLE, and TRUNCATE statements. ​Explain the syntax ​and use the statements in queries. ​You use the ALTER TABLE statement to add or remove columns from a table, to modify the ​data type of columns, to add or remove keys, and to add or remove constraints. ​The syntax of the ALTER TABLE statement is shown here. ​You start with ALTER TABLE followed by the name of the table that you want to alter. ​Differently to the CREATE TABLE statement though, you do not use parentheses to enclose ​the parameters for the ALTER TABLE statement.

​Each row in the ALTER TABLE statement specifies one change that you want to make to the table. ​For example, to add a telephone number column to the AUTHOR table in the Library database ​to store the author’s telephone number, use the following statement: ​ALTER TABLE author ADD COLUMN telephone_number BIGINT; ​In this example, the data type for the column is BIGINT which can hold a number up to 19 ​digits long. ​You also use the ALTER TABLE statement to modify the data type of a column. ​To do this, use the ALTER COLUMN clause specifying the new data type for the column. ​For example, using a numeric data type for telephone number means that you cannot include ​parentheses, plus signs, or dashes as part of the number. ​You can change the column to use the CHAR data type to overcome this. ​This code shows how to alter the author table: ​ALTER TABLE author ALTER COLUMN telephone_number SET DATA TYPE CHAR(20 ); ​Altering the data type of a column containing existing data can cause problems though if ​the existing data is not compatible with the new data type.

​For example, changing a column from the CHAR data type to a numeric data type will not ​work if the column already contains non-numeric data. ​If you try to do this, you will see an error message in the notification log and the statement ​will not run. ​If your spec changes and you no longer need this extra column, you can again use the ALTER ​TABLE statement, this time with the DROP COLUMN clause, to remove the column as shown: ​ALTER TABLE author DROP COLUMN telephone_number; ​Similar to using DROP COLUMN to delete a column from a table, you use the DROP TABLE statement ​to delete a table from a database. ​If you delete a table that contains data, by default the data will be deleted alongside ​the table. ​The syntax for the DROP TABLE statement is: ​DROP TABLE table_name ; ​So, you use this statement: ​DROP TABLE author; ​to remove the table from the database. ​Sometimes you might want to just delete the data in a table rather than deleting the table ​itself. ​While you can use the DELETE statement without a WHERE clause to do this, it is generally ​quicker and more efficient to truncate the table instead.

​You use the TRUNCATE TABLE statement to delete all of the rows in a table. ​The syntax of the statement is: ​TRUNCATE TABLE table_name IMMEDIATE; ​The IMMEDIATE specifies to process the statement immediately and that it cannot be undone. ​So, to truncate the author table, you use this statement: ​TRUNCATE TABLE author IMMEDIATE; ​In this video, you learned that: ​The ALTER TABLE statement changes the structure of an existing table, for example, to add, ​modify, or drop columns. ​The DROP TABLE statement deletes an existing table ​and the TRUNCATE TABLE statement deletes all rows of data in a table.

---

### 18. [VIDEO TRANSCRIPT] Sorting Result Sets Video • 2 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/56Zm2/sorting-result-sets
- **Method:** `dom_transcript` | **Length:** 2615 chars

​Hello, and welcome to sorting select statement result sets. ​In this video, we will learn about some advanced techniques in retrieving data ​from a relational database table and sorting how the result set displays. ​At the end of this lesson, you will be able to describe how to sort the result ​set by either ascending or descending order. ​And explain how to indicate which column to use for the sorting order. ​The main purpose of a database management system is not just to store the data, ​but also facilitate retrieval of the data. ​In its simplest form, a select statement is select* from Table Name. ​Based on our simplified library database model and the Table Book, ​select* from Book gives a result set of four rows.

​All the data rows for all columns in the Table Book are displayed. ​We could choose to list the book titles only, as shown in this example, ​select Title from Book. ​However, the order does not seem to be in any order. ​Displaying the result set in alphabetical order would make the result set more ​convenient. ​To do this, we use the order by clause. ​To display the result set in alphabetical order, ​we add the order by clause to the select statement. ​The order by clause is used in a query to sort the result set by a specified column.

​In this example, we have used order by on the column title to sort the result set. ​By default, the result set is sorted in ascending order. ​In this example, the result set is sorted in alphabetical order by book title. ​To sort in descending order, use the keyword DESC. ​The result set is now sorted according to the column specified, which is Title, ​and is sorted in descending order. ​Notice the order of the first three rows, ​the first three words of the title are the same. ​So the sorting starts from the point where the characters differ.

​Another way of specifying the sort column is to indicate the column sequence number. ​In this example, select title, pages from Book ORDER BY 2 indicates ​the column sequence number in the query for the sorting order. ​Instead of specifying the column name pages, the number two is used. ​In the select statement, the second column specified in the column list is Pages. ​So the sort order Is based on the values in the Pages column. ​In this case, the Pages column indicates the number of pages in the book. ​As you can see, the result set is in ascending order by number of pages.

​Now you can describe how to sort the result set by either ascending or ​descending order. ​And explain how to indicate which column to use for the sorting order, thanks for ​watching this video. ​[MUSIC]

---

### 19. [VIDEO TRANSCRIPT] Join Overview Video • 4 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/6p3gD/join-overview
- **Method:** `dom_transcript` | **Length:** 3613 chars

​Hello and welcome to Join Overview. ​After watching this video, you will be able to: ​Define the join operator ​Explain the role of primary keys and foreign keys in a join operation ​List different types of join operators ​A simple Select statement retrieves data from one or more columns from a single table. ​The next level of complexity is retrieving data from two or more tables. ​This leads to multiple possibilities of how the result set can be generated. ​To combine data from two tables, you use the JOIN operator. ​A JOIN combines the rows from two or more tables based on a relationship between certain ​columns in these tables. ​In this simplified library database example, author and book are entities.

​This entity relationship diagram represents the relational data model for the author and ​book entity as well as other entities such as borrower, loan, copy, and author list. ​The information is split into different tables. ​If you wanted to know which borrower has which copy of a book out on loan, you need to gather ​data from three tables: the borrower, loan, and copy tables. ​This is when you need to use the JOIN operator. ​First you need to identify the relationship between these tables. ​That is, the column or columns in each table to use as a link between the tables. ​In this entity relationship diagram, notice the author ID, book ID, borrower ID, and copy ​ID have the primary key icon.

​A primary key uniquely identifies each row in a table. ​Notice also the entities on the lower half of the screen some attributes have FK in brackets ​next to them. ​This identifies a foreign key, which is a set of columns referring to a primary key ​of another entity. ​For example, the loan entity has the borrower ID attribute with the FK in brackets. ​In this example, the borrower ID attribute is the Foreign Key in the loan entity, which ​refers to the Primary Key for the borrower entity. ​So, if you wanted to know which borrower has a book out on loan, you need to gather data ​from the borrower and loan tables. ​You will need the borrower ID from both tables.

​So far, you have seen an example of combining two tables. ​But what if you need to combine data from three or more different tables? ​You simply add new tables to the joins. ​For example, if you want to know which borrowers have a book on loan, and which copy of the ​book they have on loan, first you join the information from the borrower table and the ​loan table by matching borrower IDs. ​Then, you join the information from the loan table and the copy table by matching the copy ​IDs. ​SQL offers you several different types of JOINs. ​You can extract a data set corresponding to the intersection of the two tables involved, ​or you can choose a bigger data set.

​You can go up to the point of selecting the combination of all the data from these two ​tables. ​The most common type of join is an inner join, which displays only the rows from two tables ​that have matching value in a common column, usually the primary key of one table that ​exists as a foreign key in the second table. ​There are also outer joins, which return matching rows, and even the rows from one or the other ​table that don’t match. ​There are many varieties of outer join that you can use to refine your result set. ​In this video, you learned that: ​You can use the JOIN operator to combine rows from two or more tables, ​The tables being joined are related by a common column, which is usually the primary key of ​one table, and appears as a foreign key in the other table, ​There are two types of joins; inner joins and outer joins.

---

### 20. [READING] Module 1 Bonus Lesson 3 Summary Reading • 2 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/E0jl2/module-1-bonus-lesson-3-summary
- **Method:** `dom_reading_cml` | **Length:** 1685 chars

Congratulations! You have completed this lesson. At this point in the course, you know:

- CREATE, ALTER, TRUNCATE, and DROP define, change, or drop database objects such as tables.
- The CREATE TABLE statement includes the definition of attributes of columns in the table, including:
- Names of columns
- Datatypes of columns
- Optional values, if required, such as the Primary Key constraint
- The ORDER BY clause is used in a SQL query to sort the result set by a specified column. For example, “ORDER BY title” sorts the result set by the column named “title.”
- You can also specify the sort of column by indicating the column sequence number. For example, “select title, pages from book ORDER BY 2” indicates that the sort order is based on the values in the second column.
- The JOIN operator combines rows from two or more tables based on a relationship between certain columns in these tables.
- The tables being joined are related by a common column, which is usually the primary key of one table and appears as a foreign key in the other table.
- The Primary Key of a relational table uniquely identifies each row in a table.
- A Foreign Key is a set of columns referring to a primary key of another entity.
- If you need to combine data from three or more different tables, add new tables to the joins. First, you combine table A and table B information by matching their shared attributes. Then, you join the information from table B and table C by matching their shared attributes.
- SQL offers several types of JOINs - such as INNER JOIN and OUTER JOIN. You can extract a data set corresponding to the intersection of the two tables involved or choose a bigger data set.

---

### 21. [READING] Module 1 Summary: Getting Started with SQL & Relational Databases
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/amL39/module-1-summary-getting-started-with-sql-relational-databases
- **Method:** `dom_reading_cml` | **Length:** 2699 chars

Congratulations! You have completed this module. At this point in the course, you know:

- Structured Query Language, or SQL, was designed to manage data in relational databases and is useful for handling structured data.
- Data is a collection of facts in words, numbers, and pictures.
- A database is a repository of data that provides functionality for adding, modifying, and querying data.
- Relational databases store tabular data as collections of related items, with columns containing item properties.
- The basic SQL statements are CREATE TABLE, INSERT, SELECT, UPDATE, and DELETE.
- Non-relational databases provide a flexible and scalable approach to storing and retrieving data.
- Relational databases are ideal for the optimized storage, retrieval, and processing of large volumes of data.
- RDBMS is a mature and well-documented technology, providing flexibility, reduced redundancy, ease of backup and disaster recovery, and ACID compliance.
- An Entity-Relationship model is a tool for designing relational databases. Entities become tables, and attributes are translated into columns.
- CREATE, ALTER, TRUNCATE, and DROP define, change, or drop database objects such as tables.
- The CREATE TABLE statement includes the definition of attributes of columns in the table, including: - Names of columns - Datatypes of columns - Optional values, if required, such as the Primary Key constraint
- The ORDER BY clause is used in an SQL query to sort the result set by a specified column. For example, “ORDER BY title” sorts the result set by the column named “title.”
- You can also specify the sort of column by indicating the column sequence number. For example, “select title, pages from book ORDER BY 2” indicates that the sort order is based on the values in the second column.
- The JOIN operator combines rows from two or more tables based on a relationship between certain columns in these tables.
- The tables being joined are related by a common column, which is usually the primary key of one table and appears as a foreign key in the other table.
- The Primary Key of a relational table uniquely identifies each row in a table.
- A Foreign Key is a set of columns referring to a primary key of another entity.
- If you need to combine data from three or more different tables, add new tables to the joins. First, you combine table A and table B information by matching their shared attributes. Then, you join the information from table B and table C by matching their shared attributes.
- SQL offers several types of JOINs - such as INNER JOIN and OUTER JOIN. You can extract a data set corresponding to the intersection of the two tables involved or choose a bigger data set.

---

## Module 2: ORM: Bridging the Gap Between the Real World and Relational Model

### 1. [VIDEO TRANSCRIPT] Introduction to Django
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/tPlLl/introduction-to-django
- **Method:** `dom_transcript` | **Length:** 6219 chars

​Welcome to introduction to Django. ​After watching this video, ​you will be able to describe the key features and nature of the Django ​web framework and identify the types of web applications that can be built using Django. ​Django is a high-level accessible and open source python web framework. ​It follows the model view controller MVC pattern ​which helps developers build web applications quickly, ​and efficiently Django was created to enable rapid development and code reusability. ​Users can build almost any web application with ​Django including a Content management system or CMS, ​social media platforms, business applications and new websites. ​A common phrase to describe Django is batteries included due to Django's ​comprehensive nature of the Django web framework. ​Django provides a wide range of features and functionalities ​out-of-the-box. Django provides an object relational ​mapping or orm layer that allows you to define your data models ​Using python classes. This makes it easier to work with databases and perform operations.

​Such as querying, inserting, updating, and deleting records ​Django has a built-in template engine that enables developers ​to separate the business logic from the presentation logic of your application. ​Django also provides an administration interface that ​is automatically generated based on the models in your application. ​It provides a user-friendly interface for managing site ​content and can be customized to fit specific requirements. ​Django provides robust security features ​including protection against common web vulnerabilities ​such as cross-site scripting or xss, cross-site request forgery or CSRF, and SQL injection. ​It also provides mechanisms for password hashing and user session management. ​Django has built-in authentication and authorization mechanisms, ​allowing you to manage user accounts, including ​registration login and password management. ​It also provides fine-grained authorization ​controls to define user permissions and access restrictions.

​Django is expandable with the help of modules, also known as Django apps or packages. ​These modules are reusable components that you can integrate ​into your Django projects to add specific functionality or features. ​For example, Django supports language localization, using the gettext module ​Django offers third party packages like Django Simple Captcha for captcha integration, ​which helps prevent automated bot submissions in forms and Django's built-in forms module, ​includes robust form. ​Validation logic to ensure the form data meets the criteria. ​Django promotes an architecture where each web server instance ​operates independently known as the share nothing or stateless. ​Architecture each web server, ​instance handles requests and responses autonomously without relying ​on shared resources or maintains any server-side state between requests. ​Django web framework make scaling easy because the ​Django app is stateless it manages your user sessions.

​This allows developers to add more instances of an application and ​transfer the user's experience across the models without losing data. ​Django support, all kinds of tests, including unit, integration, and functional test. ​Django's testing framework includes a test runner, ​that allows developers to run tests quickly and provides detailed test ​reports. It offers various testing utilities, assertions, ​and fixtures to facilitate writing and executing tests. ​Due to Django being built on python it's platform agnostic meaning ​it could be run on many platforms. ​This platform independence is due to python's ​portability and wide availability on different operating systems. ​This allows developers to choose the hosting ​platform that best suits their needs and infrastructure.

​A Django application can run on almost all Cloud providers. ​Django's platform-agnostic nature ​allows you to deploy your application on various cloud ​platforms depending on your specific requirements and preferences. ​For example, ​if you have a Blog platform and you prefer the ​Simplicity and user-friendliness of Microsoft Azure's cloud services, ​you can deploy your blog application to Azure without any hassle. ​The Django web framework owes much of its success to its dedicated community of users. ​This community includes developers, designers, ​and enthusiasts worldwide, who share a common passion for creating exceptional, ​web applications. One of the core strengths of the Django Community lies in ​its commitment to continuously enhancing and advancing the framework. ​The open-source nature of Django and able to developers ​to contribute their expertise and improvements to the framework's ​codebase. This collective effort results ​in regular updates and releases introducing new features, ​optimizing performances, and addressing security concerns. Several famous, ​web applications have been built using Django. Instagram, ​a popular social media platform for sharing photos ​and videos was initially built using Django. Spotify, ​a leading music ​streaming platform has also used Django and its infrastructure ​The popular video-sharing platform ​YouTube has incorporated Django into its architecture.

​And the Washington Post, ​a renowned news publication has adopted Django for its content management system or CNS. ​In this video, you learn that Django is a high-level ​accessible and open source python web framework. Using Django, ​users can build content Management systems, ​or CMS's, social media platforms, business applications, and websites. ​Django's object relational mapping or orm layer, ​lets you define your data modules using python classes. ​Built in Django features include templates an administration ​interface, security, authentication and authorization, ​mechanisms, user-friendly scaling, and test support. ​Django is expandable with modules or Django apps ​or packages which add functions and features. ​Django promotes a shared nothing or stateless architecture ​allowing for the autonomous handling of requests and ​responses without relying on shared resources. And Django is platform agnostic, ​meaning it can run on any platform and almost any cloud server.

---

### 2. [VIDEO TRANSCRIPT] Object-Oriented Analysis and Design
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/xKwOC/object-oriented-analysis-and-design
- **Method:** `dom_transcript` | **Length:** 3731 chars

​Welcome to object oriented analysis and design. ​After watching this video, ​you will be able to ​explain what are objects and classes are. ​Describe the purpose of a class diagram and explain ​object-oriented design in ​relation to software architecture. ​Object oriented analysis and design, ​or OOAD for short, ​is an approach for analyzing and ​designing a software system when ​the system will use object ​oriented programming languages to develop it. ​Before we discuss OOAD, ​let's learn a little more about ​object oriented programming in ​languages like Java or C plus plus or Python. ​At the heart of OOAD are objects. ​Objects contain data and they also have ​behaviors that prescribe the actions the object can take.

​I could create an object, ​for example, that represents a patient. ​Let's say that patient's name is Nia Patel ​and Nia needs to cancel an appointment she made. ​Before creating Nia, however, ​we must first create ​a generic version of a patient object. ​The generic version of an object is called a class. ​Let's discuss classes next ​before we discuss more about Nia. ​Specific objects, also called instances, ​are created from classes which are ​blueprints or templates for an object. ​From our previous example, ​considering Nia Patel, Nia ​would be an instance of the patient class.

​The class contains the objects, ​generic and attributes, the properties and methods, ​but it is only when the object is created, ​which is called instantiation inside the code that ​these generic attributes are set to particular values. ​The patient class might have a variable called LastName, ​which is a property but does not ​specify what that LastName is. ​Lastname is a placeholder until ​the object is created and assigned a name. ​Once the object has been instantiated, ​its methods can be called to ​make the object perform some action, ​such as making or canceling and appointment. ​OOAD is used for a system that can be ​broken down into objects that interact with each other. ​In this way, multiple developers can work on ​different aspects of the application at the same time. ​As noted earlier, visual UML diagrams can be created ​that show both the static structure ​and dynamic behavior of a system.

​We've seen a couple of examples of ​behavioral UML diagrams all ready. ​Let's look at a structural UML diagram ​called a class diagram next. ​Now that we know what classes are. ​This is an example of a class diagram. ​Class diagrams are commonly used to communicate ​a software system structure in OOAD. ​The class diagram shows how the class is in ​an object oriented design relate to one another. ​Each box represents a class and shows its attributes.

​Recall that an object's attributes ​are both its properties ​or its data and it's available actions called methods. ​A class diagram also shows ​the relationships between classes. ​A subclass is said to ​inherit its parent class attributes, ​meaning it has the same properties ​and methods as the parent class, ​but also may add additional properties and methods. ​In this diagram, the nurse, ​doctor and technician classes are sub-classes of ​medical personnel and the specialist class ​is a subclass of the doctor class. ​This means that doctors can do ​anything medical personnel can do, ​and specialists can do anything a doctor can do. ​In this video, you learned ​that object oriented analysis and design is ​the process of planning a software system ​based on the behaviors of interacting objects. ​Objects contain data, and they also have ​behaviors that prescribe the actions the object can take.

​Classes are blueprints for objects. ​A class diagram is ​a structural UML diagram that ​shows the relationship between objects.

---

### 3. [VIDEO TRANSCRIPT] Object-Relational Mapping (ORM)
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/FSyaq/object-relational-mapping-orm
- **Method:** `dom_transcript` | **Length:** 6488 chars

​[Music] Welcome to Object-Relational Mapping, or ORM. ​In this video, we will explain how ORM can simplify application development with databases ​After watching this video, you will be able to: ​Describe the difference between the SQL paradigm and the object-oriented programming, or OOP, ​paradigm. ​Explain the core concepts of ORM ​and list the pros and cons of ORM. ​Software developers often use a database as the main data repository for their application, ​so they need to integrate SQL into their application code. ​SQL statements must be assembled in application code and executed in the database system using ​database APIs. ​The retrieved database rows are returned to application code as Cursor, a special control ​data structure for iterating over rows in a database. ​This online course database contains only two entities, Course and Learner.

​The relationship between them is Many-To-Many. ​One course can have many learners enrolled and one learner can enroll in many courses. ​This relationship is persisted in an associative table. ​Let’s see an example of executing SQL in Python code. ​First, we create a connection to an embedded SQLite database. ​This is the empty online course database. ​Next, we create a Cursor object from the connection context.

​Then we can send and execute SQL. ​We start with an Insert statement to create and insert a learner record. ​Once the Insert statement is assembled, we call Cursor to execute methods to run the ​SQL. ​Lastly, we create another SELECT statement to query the learner record we just inserted, ​and we use Cursor-Fetch-One to retrieve the first row. ​The output shows the learner row we just inserted. ​In the modern application development environment, OOP is the mainstream, and it is quite different ​from SQL. ​Unlike SQL, which models entities using tables, rows, and columns, an object-oriented language ​models entities using classes and objects.

​In OOP, Course entity would be defined as a class with two primitive attributes: name ​and description; and one reference attribute, the list of learners. ​Methods for data manipulation also need to be defined along with class attributes. ​Here we define a simple method: get Learners. ​Learner entity would also be defined as a class with four attributes: first name, last ​name, date of birth, and occupation. ​A simple print profile method would also be defined. ​Let’s create a Learner object from a database using both the SQL and OOP paradigms. ​First, we execute a SQL select statement and get the first Learn row.

​To load the data into the Learn object, we create an object by calling its default constructor. ​Then we update the object with attribute values queried from cursor. ​We need to manually map each column to each class primitive attribute. ​This can become complicated if we have complex data relationships. ​Finally, we call the print profile method to print the object. ​We have seen that the OOP and SQL paradigms model data differently. ​OOP models entities using classes, objects, and attributes, whereas ​SQL models entities using tables, rows, and columns.

​Also, OOP models relationships using class patterns like inheritance, association, and ​aggregation, whereas SQL models relationships using JOIN and FOREIGN KEY. ​Lastly, OOP performs CRUD on data using methods, whereas SQL performs CRUD on data using data ​manipulation language, like the SQL statements insert, delete, and update. ​Since we generally build modern applications using OOP, can we also access databases using ​OOP instead of SQL? ​That way, we can stick to one programming paradigm for our development. ​The main reason people invented object-relational mapping was to bridge the gap between OOP ​and SQL and make it possible to use OOP languages to access databases. ​ORM libraries or tools can map and transfer data stored in a relational database as rows ​into objects or objects into rows. ​Suppose we have a learner object model created by a developer using OOP.

​ORM can help transfer the Learner object into a Learner row in a Learner table and read ​it back into a Learner object. ​This reduces developers’ workload because they only need to focus on object operations. ​Here’s how ORM can transfer a three-table-join SQL query as a single line of code. ​Suppose we want to get all learners who are enrolled in the `Introduction to Python` course. ​In SQL, we would have to join Course, Learner, and their lookup tables to get all the information. ​We would also need to mix both the OOP and SQL paradigms. ​But with the help of ORM, we just need to first call the get method in Course class ​to find the course by name, and then retrieve all its learners.

​DONE! ​Now that you’ve learned how convenient ORM is, you may want to use it in your application. ​There are ORM libraries for almost all popular languages. ​For Python, you can use Django Model and SQLAlchemy. ​For Java, you can use Hibernate and OpenJPA ​and for JavaScript, you can use Sequelize and TypeORM. ​These are just a few examples. ​In this course, we’ll focus on Django Model.

​Like all third-party software libraries, ORM has its pros and cons. ​On the positive side: With ORM, your class designs define the databases. ​For OOP application development, you just need to define classes and create objects. ​You can use databases without writing SQL. ​Also, you can use a single ORM interface to manage multiple database systems without worrying ​about differences in SQL syntax. ​All these benefits will speed up your application delivery. ​On the negative side: SQL and OOP are still two different languages ​with different modeling concepts, and ORM may fail to perform the mapping of objects ​into database tables.

​Also, since ORM combines data access logic with application code, any database change ​will require changes to both the application logic and the data access logic. ​Because ORM hides the implementation details, debugging can be challenging. ​Finally, ORM may reduce application performance. ​ORM adds an extra translation layer, but it cannot guarantee that the translated SQL statements ​are optimized. ​In this video, you learned that: SQL and OOP model data differently. ​ORM bridges the gap between SQL and OOP. ​ORM allows application developers to use databases without writing Sequel code.

​ORM can speed up application development ​and he disadvantages of ORM include imperfect mapping, increased code coupling, and difficulty ​in debugging.

---

### 4. [VIDEO TRANSCRIPT] Django Model
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/tzoj3/django-model
- **Method:** `dom_transcript` | **Length:** 6304 chars

​Welcome to Django Model, a popular object-relational mapping, or ORM, library for Python. ​After watching this video, you will be able to explain the core concepts of Django ORM ​and convert your entity relationship diagrams into Django models. ​Recall that ORM can make the developer's life easier by abstracting databases and automatically ​mapping objects and methods to tables and SQL queries. ​Now you will learn how Django ORM, a Python ORM component that belongs to the Django Web ​Application Framework, can help speed up your application development with databases. ​In Django ORM, each Django model maps to a database table. ​When you create a class object, it represents a table row. ​Each field represents a table column.

​Schema and tables are automatically generated once model classes are defined. ​For example, you can define a user class, which is a subclass of the Django model. ​Django will then create a corresponding user table in the database by generating table ​create statements and creating columns based on the class fields. ​In our example, a FirstName column will be created based on the FirstName field. ​Each field in the model should be defined as a field class. ​Django maps each field to a column type. ​Here, FirstName is defined as a character field and will be transferred into VARCHAR, ​and DateOfBirth is a date field and will be transferred into Date.

​For each column, we define its metadata, such as type and constraints, by specifying parameters ​in a Django field class. ​For example, for the FirstName field, we use the MaxLength parameter to specify the length ​for VARCHAR. ​Once we have defined models and fields, Django ORM will generate schema and table create ​statements. ​FirstName, LastName, and DateOfBirth fields are converted into columns. ​Each field has customization parameters, such as null, blank, default, or primary key. ​Next, we model the relationships between entities. ​Django ORM supports common relationships, such as one-to-one, many-to-one, and many-to-many.

​We will start with a one-to-one relationship. ​Suppose we have an Instructor and User ER diagram. ​User class holds some common fields, such as Name or DateOfBirth. ​An Instructor class has some special fields like IsFull or TotalNumberOfLearners the Instructor ​has. ​One Instructor can only have basic information stored in one User class, and one User can ​only have one role, such as Instructor or Learner. ​Now let's convert the ER diagram into two Django models. ​First, we define the models, Instructor and User, and their fields.

​To define the relationship, we define an extra one-to-one field to act as a foreign key pointing ​to User. ​Django ORM will create Instructor and User tables with a foreign key in the Instructor ​table pointing to the User table. ​We'll use a Project and Course ER diagram to illustrate a many-to-one relationship. ​The Project class represents a course project with fields such as ProjectName and Grade. ​The Course class represents an online course entity. ​It has atom fields such as Name and Description. ​More importantly, it has a collective field called Projects, which represents a set of ​course project objects.

​Thus, one course would have many course projects, and one course project would only belong to ​one course. ​This is a typical many-to-one relationship. ​To create models in Django, we add an extra course field as a foreign key. ​Note that this is not a one-to-one field because multiple projects may have the same course ​field. ​For a many-to-many relationship, let's look at a Course and Learner ER diagram. ​One course may have many learners enrolled, and one learner may enroll in many courses. ​To model this relationship, we add a many-to-many field to one of the models.

​Normally, the many-to-many field should go in the model which will be edited most often. ​For instance, Course will likely be edited on an hourly basis as learners are added or ​removed, but each learner may only enroll in a new course on a weekly or monthly basis. ​Sometimes you need extra information about the relationship between the models. ​For example, you may want information about the enrollment that occurred between learners ​and courses, such as the date enrolled. ​Django allows you to specify the model that will be used to govern the many-to-many relationship. ​In our case, the intermediate model is the enrollment table. ​It is associated with the many-to-many field using the through argument.

​Model inheritance in Django is like inheritance in Python. ​You need to determine if the parents are just holders of common information that will only ​be visible through the child models, or if parents should have their own tables. ​There are three scenarios for model inheritance. ​Use multi-table mode when you're subclassing an existing model and want each model to have ​its own database table. ​Use abstract base classes if the parent class will just hold information. ​Use proxy models to model the Python-level behavior of a model without changing fields. ​Multi-table inheritance is like a one-to-one relationship.

​The only difference is you need to subclass instructor from the model. ​Django will create a new instructor table and a one-to-one field in the instructor class. ​As such, inheritance for multi-table classes is an implicit one-to-one relationship. ​We have defined entities and relationships for our online course database. ​Now Django will create these database tables and foreign keys automatically. ​User table is the base table which has ID as the primary key and contains atom columns ​such as name. ​Learner table is inherited from user and has a many-to-many relationship with course through ​an intermediate enrollment table.

​Instructor and course also have a many-to-many relationship. ​Lastly, the project and course tables have a many-to-one relationship. ​Now that Django has created these tables, we can perform read, update, and delete operations ​on the data. ​In this video, you learned that in Django ORM, each Django model maps to a database ​table. ​Each field maps to a column type such as INT, VARCHAR, or DATE. ​Each field has customization parameters. ​And Django ORM supports common relationship patterns such as one-to-one, many-to-one, ​and many-to-many.

---

### 5. [VIDEO TRANSCRIPT] Django Models CRUD
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/GKL93/django-models-crud
- **Method:** `dom_transcript` | **Length:** 6015 chars

​Welcome to Django Models CRUD. ​After watching this video, you will be able to: Use Django Model APIs to perform CRUD ​operations on objects. The most common operations on data are: ​Create Read ​Update, and Delete. ​Django Model provides comprehensive CRUD APIs to manipulate objects without writing SQL queries. ​Let’s review the online course models we will use for our examples. ​The base User model contains common information about our Instructor and Learner models. ​Instructor is inherited from the user model and has fields like “is full time” or ​total number of learners. Learner is also inherited.

​It has fields like occupation and social link. The Course model has Many-To-Many relationships ​with both the Instructor and Learner models. Course model also has a Many-To-One relationship ​with the Project model. In a Django model, you create ​an object and call the model’s save method to insert it into the database as a record. ​Here, we have created and saved the object `course_cloud_app`. ​If the object you create contains a reference to another model, such as a Foreign Key or ​Many-to-Many field, you use the related model reference to create a relationship. ​We have created a Project object and referred its Course foreign key to the ​cloud app course we just created. Once we have inserted objects and ​their relationships into the database, we can query them.

​First, let’s see how to read all objects for a model. This is equivalent to using SELECT * from ​a table to get all table rows in SQL. In general, to read objects using Django Model ​API, you need to construct a QuerySet using a Manager on your model class. ​A QuerySet represents a collection of records in a database. ​After you have defined your model by subclassing a Django Model - such as Course in our example – ​you can use its model Manager as an interface to access database records. ​By default, the name of the model manager is `objects`. You can only access the objects manager ​using the model class, not the model instance, to enforce a separation between table-level ​operations and record-level operations. To get all course records, use the Manager’s “all” ​method that will return you a QuerySet object. In the output, you can see that all courses were ​returned and included in the QuerySet object. Usually, you’ll just need a subset of ​records instead of the entire table. To create a subset of part-time instructors, ​you refine the initial QuerySet by calling a filter method.

​The filter method can have many lookup parameters, such as greater than, ​less than, contains, or is null. This is like the condition usage in the SQL WHERE clause. ​Lookup parameters contain the field name and the query expression, ​which can be empty for an equal check or separated by an underscore for other checks. ​In this example, we are checking that the Boolean field “is_full_time” is False, ​to create a subset of only part-time instructors. The Course model manager will return all part-time ​instructor objects contained in a QuerySet object. The exclude method returns a new QuerySet that ​does not match the given lookup parameters. Since both the exclude and filter methods return ​a QuerySet, we could further append exclude and filter methods to form ​a filter chain. This is like adding multiple conditions using `and` in a SQL Where clause.

​We can find a subset of Instructors using both exclude and filter. ​First, we use the exclude method to remove all part time instructors. Then we apply two ​filters to find instructors with more than 30,000 learners and a first name that starts with J. ​Another way to apply multiple filters is by adding multiple lookup parameters in one filter method. ​And we can see the target QuerySet has been returned. ​If there is only one object that matches your query, ​you can use the Get method to return the object. ​For example, if we know there’s only one instructor with the first name `John`, ​we can use the Get method with a first_name lookup parameter to get the instructor.

​In our previous model design, many models were related using relational field references. ​For example, the Course model had a Many-To-Many field reference to the Instructor model. ​From an object point of view, these composite fields are references to related models. ​From a SQL perspective, these fields are foreign keys pointing to related tables and ​could be joined to obtain related information. When querying related records in a database, ​Django handles SQL JOIN automatically, so you can read related objects using references. ​You can also create lookup parameters on the related fields in other objects. ​For example, to find all courses with an instructor whose first name equals `John`, ​we can create a lookup parameter with the related field called `instructors`, ​followed by a double underscore, then followed by an Instructor's field called `first_name`.

​We have seen how to insert records into a database and how to read data using Django models. ​Now let’s see how to update database records by updating objects. ​One way is by updating the primitive fields of an object. ​For our learner object, we can change the “date of birth” field to March 16th, ​1985 and use the “save” method to update the change to the database. ​The Django model will create and execute the corresponding SQL Update statements. ​We can also update the related fields, such as the Foreign Key Field or the Many-To-Many Field. ​For example, we can update a course foreign key field, so it points to a different course.

​We can also use the Add method to add another learner to a course. ​To delete records in a database, you call the Delete method on a model object or a Query Set. ​Django ORM supports different “on delete” options. You will ​learn more about these later. In this video, you learned that: ​With Django APIs, you can perform actions on data in databases without writing SQL queries ​and you can use Django Model APIs to create, read, update, and delete objects.

---

### 6. [VIDEO TRANSCRIPT] Related Objects
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/2Sg8g/related-objects
- **Method:** `dom_transcript` | **Length:** 4708 chars

​Welcome to Related Objects. ​After watching this video, ​you will be able to use ​Django model APIs to access and delete related objects. ​All our online course models are related. ​User has a one-to-one relationship ​with instructor and learner. ​Course has a many-to-many relationship ​with instructor and learner, ​and a many-to-one relationship with project. ​We'll show you how to handle these related models ​using Django model APIs. ​Django only requires you to define a model relationship ​on one side.

​For example, you only need to define the learner model ​as having a one-to-one field reference to the user model. ​This explicit reference is called forward access. ​Under the hood, ​Django will create a backward relationship ​from user to learner, ​so you can also access learner from the user model. ​This is an implicit reference or backward access. ​To access the common information about a learner, ​such as first or last name, ​we need to get its user object. ​Since we already defined a user reference ​in the learner model, ​we can easily get the user from learner explicitly. ​We can also get a learner from the user object ​because Django creates the backward relationship ​automatically.

​An inheritance relationship ​is like a one-to-one relationship. ​The learner class inherits from the user class. ​We can access learner's parent user reference ​with user underscore PTR, ​which is created by Django with the model name user ​plus a PTR suffix separated by an underscore. ​Meanwhile, Django creates a backward relationship ​from user to learner. ​A one-to-many or many-to-one relationship ​is defined using a foreign key field. ​Here we have defined a forward reference ​from project to course. ​Now we can access the course for a project explicitly.

​Meanwhile, Django creates a backward reference ​from course to project ​with an implicit project set field ​so we can access projects that belong to a course. ​Handling many-to-many related objects ​works like other relationships. ​In this example, course model has a many-to-many field ​pointing to instructor as an explicit reference. ​We can access the instructors of a course ​via this forward access ​and we can also access the instructors ​who are currently teaching courses ​via the implicit reference created by Django. ​We previously explained that you delete an isolated object ​by simply calling the delete method. ​However, what if the objects are related? ​For example, one course may have many course projects ​via the foreign key field ​and one course project belongs to one course.

​If we delete a course, ​what will happen to those course projects belonging to it? ​Will Django keep the projects or delete them also? ​In fact, Django supports different deletion behaviors ​based on how you set the onDelete options. ​We can put the onDelete option ​in the foreign key field as a parameter. ​Let us see how each option works ​when delete a course object with related project objects. ​The default option is cascade. ​It will delete all course projects ​if the course object is deleted.

​The protect option protects a course object from deletion ​if it has any associated course projects. ​The set null option keeps the course projects ​for future use. ​Set null is only available ​if we allow the foreign key to be null. ​The set default or set option ​assigns the projects to a default course ​or a different course ​when the related course has been deleted. ​The do nothing option does nothing to related projects ​when the course has been deleted. ​This option is discouraged ​because the projects will be orphan objects. ​They still point to a non-existent course object.

​There are some additional Django methods ​to handle related objects. ​To add an object to the related object set, ​use the add method with the object reference. ​To create a new object with related objects, ​use the create method with keyword parameters ​such as primitive or relational field values. ​To remove certain objects, ​use the remove method with the related object references. ​To clear all related objects, ​use the clear method without any parameters. ​And to replace related objects, ​use the set method with the new object set. ​In this video, ​you learned the Django model provides convenient APIs ​to read or manipulate related objects.

​Django only requires you to define the relationship ​on one side called a forward or explicit relationship. ​When you define a forward relationship, ​Django will automatically create a backward ​or implicit relationship ​based on the type of forward relationship you have defined. ​And on delete options, ​specify what happens to related objects ​when an object is deleted.

---

### 7. [READING] Module 2 Summary: ORM: Bridging the Gap Between the Real World and Relational Model Reading • 2 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/KOMya/module-2-summary-orm-bridging-the-gap-between-the-real-world-and-relational
- **Method:** `dom_reading_cml` | **Length:** 1334 chars

Congratulations! You have completed this lesson. At this point in the course, you know:

- The Object-Oriented Programming (OOP) and SQL paradigm model data differently.
- Object Relational Mapping, or ORM bridges the gap between OOP and SQL.
- ORM libraries or tools can map and transfer data stored in a relational database as rows into objects or objects into rows.
- ORM allows developers to use OOP to query and manipulate data because it transfers objects into rows and rows into objects.
- Django ORM is a Python ORM component that belongs to the Django web application framework.
- Django ORM can help speed up database development because you define maps to a database table for each Django model.
- Each Django field maps to a column type.
- Django automatically creates tables once models and fields are defined.
- Django APIs can perform Create, Read, Update, and Delete (CRUD) operations on database objects.
- In a Django model, you create an object and call the model’s save method to insert it into the database as a record.
- You must construct a QuerySet using a Manager on your model class to read objects using Django Model API.
- There are several ways to update database records in Django by updating objects.
- To delete records in a database, you call Django ORM’s Delete method on a model object or query set.

---

### 8. [READING] Module 2 Cheat Sheet: ORM: Bridging the Gap Between the Real World and Relational Model Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/VrAFH/module-2-cheat-sheet-orm-bridging-the-gap-between-the-real-world-and-relational
- **Method:** `dom_reading_cml` | **Length:** 2903 chars

| Package/Method | Description | Code Example |
| --- | --- | --- |
| django.db.models.Model | Define a model. | from django.db import models class MyModel(models.Model): field1 = models.CharField(max_length=100) field2 = models.IntegerField() |
| makemigrations/migrate | Create database tables based on models. | python manage.py makemigrations python manage.py migrate |
| all() | Retrieves all instances of the ‘MyModel’ model from the database. | MyModel.objects.all() |
| filter() | Filter objects using conditions. | MyModel.objects.filter(field1="value") MyModel.objects.filter(field2__gt=5) |
| get() | Retrieves a single instance of the ‘MyModel’ model from the database where the value of ‘field1’ is "value". | MyModel.objects.get(field1="value") |
| obj = MyModel(field1="value", field2=5) obj.save() | Creates a new instance of the ‘MyModel’ model with the values "value" for ‘field1’ and 5 for ‘field2’, and then saves the instance to the database. | obj = MyModel(field1="value", field2=5) obj.save() |
| obj.field1 = "new value" obj.save() | Updates the value of ‘field1’ for the ‘obj’ instance to "new value" and saves the changes to the database. | obj.field1 = "new value" obj.save() |
| delete() | Deletes an object. | obj.delete() |
| obj.related_model | Retrieves the related model associated with the ‘obj’ instance. Access related objects (Foreign Key or OneToOneField) | obj.related_model |
| obj.model_set.all() | Fetches all related objects associated with the ‘obj’ instance. Access related objects in reverse (ForeignKey) | obj.model_set.all() |
| field | Performs a filtering operation on the ‘MyModel’ model instances based on a related model's field value. | MyModel.objects.filter(related_model__field="value") |
| exact | Retrieves instances of the ‘MyModel’ model from the database where the value of the ‘field’ attribute is exactly equal to "value". | MyModel.objects.filter(field__exact="value") |
| iexact | The iexact lookup is case-insensitive, meaning it will match values regardless of whether they are uppercase or lowercase and provide a case-insensitive match. | MyModel.objects.filter(field__iexact="value") |
| contains | Checks if the value is a substring within the field. | MyModel.objects.filter(field__contains="value") |
| startswith | Determines whether a string begins with the characters of a specified string. | MyModel.objects.filter(field__startswith="value") |
| endswith | Determines whether a string ends with the specified suffix. | MyModel.objects.filter(field__endswith="value") |
| in | Checks if the value of the field is present in the given list of values. | MyModel.objects.filter(field__in=["value1", "value2"]) |
| gt | Checks if the value of ‘field’ is numerically greater than 5. | MyModel.objects.filter(field__gt=5) |
| lt | Checks if the value of ‘field’ is numerically less than 10. | MyModel.objects.filter(field__lt=10) |

---

## Module 3: Full-stack Django Development

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

## Module 4: Consolidate and Deploy Your Django App

### 1. [VIDEO TRANSCRIPT] Class-based and Generic Class Views
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/VM3LJ/class-based-and-generic-class-views
- **Method:** `dom_transcript` | **Length:** 4735 chars

​Welcome to Django class-based views. After watching this video, you will be able ​to: Create class-based and generic class-based ​views, and Compare the pros and cons of function-based ​views and class-based views. The function-based view was the original view ​implementation in Django. It was created to solve a specific problem with a request parameter ​and explicit logic for how to generate a response. The class-based view was added to Django to ​improve the extensibility and reusability of views. ​Whether a view is built using function-based views or class-based views, a view is essentially ​a Python function or callable. The main issue with the function-based view ​is it is normally very hard to extend or customize. To address these issues, the class-based view ​was created. Let’s see how to build a class-based view to return an HTTP Response.

​Instead of creating a function, you define a class subclassing the Django View base class. ​Then, you can access some common methods abstracted by the View base class, such as Get or Post ​to handle an HTTP Get or Post request. Next, implement your own logic to handle http ​requests. For example, to handle the HTTP Get method ​from a URL, we implement a simple Get method by first querying the course record from the ​database, inserting the course name into an html template, and populating HttpResponse. ​We also need to map a URL pattern to a class-based view class. This is like configuring the URL ​for the function-based view. The only difference is that for the view argument ​you need to specify the as_view function or the CourseView class we defined. The as_view ​function is inherited from the View base class. The Django View class is the base class for ​all class-based views. The Django View class defines an as_view method, which also defines ​an inner_view method and will be returned as a callable.

​So, when we add them to the URLconf using the view.as_view class method, it returns ​a function. After being called, the view callable passes ​the request to the dispatch method, which will execute the http method accordingly, ​such as GET or POST. So, even a class-based view is essentially ​a function to handle a certain http method. Thus, both function-based and class-based ​views are functions. In web app development, we need to perform ​common tasks such as displaying a list or showing the details of an object in drill-down. ​To speed up development and solve those common tasks, Django provides some built-in view ​classes called generic-based views for developers to reuse and extend with minimal code changes. ​Let’s see an example of a generic class-based view to display a course detail like we have ​done before. First, we need to define a CourseView that ​extends the generic DetailView. Then we specify the model to be Course and ​provide an html template file path. The methods provided by the DetailView know how to get ​the object and populate the html page. So, developers only need to write two lines ​of code to display a course object in a browser based on an html template, without writing ​any code to handle the http request. Let’s look at a few examples of generic ​class-based views. ListView represents a list of objects.

​DetailView represents the details of an object. FormView represents a form, and ​A group of Date views handles date-based data. So far, you’ve learned about the function-based, ​class-based, and generic class-based views. Let’s summarize the pros and cons to help ​you decide which one to use in your application. For the function-based view, the main pros ​are that it’s simple to write code and easy to understand. You can explicitly write your ​logic without following any extra structure or designs such as the methods defined in ​View base class. If you have a very specific function that’s ​not likely to be reused, the function-based view could be your choice.

​The main cons are that function-based views are difficult to extend or reuse. And they ​handle http request methods using conditional statements, which may increase the code complexity. ​For Class-based views, the pros include reusability and extendibility. ​Also, you can handle requests using class methods. And you can leverage the generic ​class-based views to solve common tasks. The main cons for class-based views are that ​adding the extra View base class inheritance makes the code harder to read. Implicit code ​is hidden, and developers must check the source code to understand exactly how the views are ​implemented. In this video, you learned: ​How to implement class-based views. How to use Django built-in generic class views ​to solve common tasks and the pros and cons of function-based and class-based ​views.

---

### 2. [VIDEO TRANSCRIPT] Django Authentication System
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/5NlAw/django-authentication-system
- **Method:** `dom_transcript` | **Length:** 5470 chars

​Welcome to Django Authentication System. After watching this video, you will be able ​to: Define authentication and authorization and ​use Django User objects to perform authentication and authorization. ​Authentication is the process of validating the identities of users, using credentials ​such as username and password. Modern authentication systems such as one-time passcode via SMS/email ​and single sign-on (SSO), or biometrics such as face recognition and fingerprints, do not ​even require users to enter passwords directly. After users are authenticated, authorization ​will check the users’ access permissions for resources such as databases. System admins ​usually need to define different roles or groups with specific access permissions, such ​as permission to view a course’s content. Admins assign roles or add users to specific ​groups in order to grant access. The User model provides basic user information ​such as username, password, and email. In Django, a User model is created to handle ​authentication and to work with other models such as groups and permissions to handle authorization.

​Developers can extend the User model to define application-specific users such as instructors ​or learners inherited from the User model. To authenticate or login a user with username ​and password, we first create a webpage template to receive the credentials. Let’s see how ​to authenticate a user in a typical web login page. ​Note that this is not a complete html template; we only show the “import form” element. ​For this simple login form, we created a text input for receiving username and a password ​input for receiving password with a password mask. ​Once we submit the form, we will send a POST request to the onlinecourse login view to ​authenticate the user. Here is a preview of the login page we just ​created. Username and password can be entered and sent to a login view in the backend.

​For the login view, we first obtain the username and password from the POST attribute of the ​request object. We use the authenticate method provided by ​Django authentication framework, which returns a valid user if the username and password ​match the database records. It returns “None” if the provided credentials do not match. ​Finally, we can use the login method to login the user and redirect to an index view. ​Once a user is logged in, Django creates a unique session with a session ID. Then it ​queries the user information and appends it to the session so that the server will know ​which user is being identified by the unique session id. ​The web session stores stateful data for users visiting a web site, so that site and user ​can perform a series of actions with server without a login for each action.

​The browser side also stores the session ID in its COOKIE for identifications within the ​site. We can use the COOKIES attribute to get the ​session id and session attribute to get the dictionary-like session data. ​If the user is authenticated, we should be able to see a valid session id and the session ​dictionary data should contain information about the user such as user id. ​If the user is not authenticated, we receive session id as “None” and an empty session ​dictionary. Logging out a user is simple. We just call ​the logout method with the http request object. Creating a registration form is similar to ​creating a login form. We can point the action url of the form to ​a registration view with post method, and add two input elements to receive the ​username and password from users. The registration page is similar to a login ​page. It receives username and password and sends them to a registration view.

​The registration view receives username and password from the POST attribute, ​and calls User model manager’s create_user method to create a new user. ​User can then be logged in and redirected to the onlinecourse index page. ​User authorization in Django is managed mainly by three models: User, Permission, and Group. ​We explained the User model in authentication. The Permission model has many-to-many relationships ​with User to store the types of objects and how users can access them. ​The Group model provides a convenient way to manage users with the same permissions. ​The easiest way to manage permissions and groups is with Django admin site, but you ​can also choose to manage them programmatically using APIs.

​In Django, you can create and assign permissions to each model you have defined. ​The four default permissions are: View, Add, Change, and Delete. ​For example, we have Can add, Can change, Can delete, and Can view permissions for our ​course model. Sometimes we want to group users with the ​same permissions together. With Django Group model, you can create user ​groups and assign permissions to groups. For example, we can create an Instructors ​group with Course add, change, delete, and view permissions. ​We can create another group, Learners, who can only view the course content and ​we can easily add a new instructor user to the Instructors group to grant the user all ​the instructor permissions automatically. In this video, you learned ​The definition of authentication and authorization, and ​How to use Django to Register and authenticate users, ​add permissions to users using admin site, and ​manage users as groups. In the authentication and authorization lab, ​you will get more coding practice adding authentication and authorization to a Django app.

---

### 3. [VIDEO TRANSCRIPT] Bootstrap
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/XOsL2/bootstrap
- **Method:** `dom_transcript` | **Length:** 4656 chars

​Welcome to bootstrap! ​Bootstrap is a free, web front-end framework, designed to facilitate web app development, ​it provides many well-designed, ​and commonly used HTML and CSS templates to simplify Django ​template development. With the help of bootstrap, ​developers can easily build stylized and interactive web pages. ​Let us look at how to quickly add bootstrap framework into our Django templates. ​Integrating bootstrap is simple. ​If you want to use bootstrap CSS style classes without downloading bootstrap, ​you can simply add a link to the latest bootstrap version hosted by content ​delivery networks like max cdn into the head element of your HTML template. And that's it, ​the simplest way to add bootstrap.

​Now, you can start using the CSS classes provided by bootstrap. Web page development ​normally starts with layout design. ​Let us design a simple course index layout to represent the courses in an online course app. ​Like many other web pages, ​our course index page has a navigation bar at the ​top which contains links and items for navigating the site. ​Our navigation bar also has a forum where users can submit authentication related data, ​such as sign in or sign up. ​Next is the main content of the web page which includes its main elements such as a list, ​a table or a picture gallery. ​Here, we will use a container to wrap content elements. We plan to present each course, ​as a card, a card is a bordered box with padding around its content.

​They can have a header, footer, content, images, colors, ​and so on. To manage multiple course cards, we will wrap them into a card deck, ​which creates a grid of cards, which will have equal height and width. ​In bootstrap, we create a navigation bar with navbar class with additional classes, ​such as background color, and how to extend or collapse ​the navigation bar, to adapt to screen size. To add items, ​such as a link or button to the navigation bar, ​we use the UL element with class navbar dash nav ​then add li items with nav dash item. ​Here we added a simple home link with class nav dash link to the navigation bar. ​Let us preview the result. ​You see that a navigation bar with a light background theme is created.

​It only has one link item. ​Next, we add a form to the navigation bar for submitting authentication related data. ​We need to create an inline form in which all elements will be in line and left ​aligned. Within the inline form, ​we can add two input elements for receiving username and password. ​Here, we use form dash control class which is ​a standard Django class for styling textual elements. ​Then we add a submission button stylized by btn ​and btn dash primary classes which create a standard bootstrap blue button. ​Finally, ​we add a sign-up link that jumps to the ​registration page stylized by btn and btn dash link classes.

​In the result, you can see a sign-in form that has been added to the navigation bar. ​We have now finished the header part of our course index page. ​Next, we will start building the main content of the page. ​We want to include the page in a div element styled by container class. ​There are two types of containers in bootstrap. ​The first container class has a fixed width, the other one is container fluid, ​which spans the entire width of the parent element. Within the ​container class, we create a div styled by card dash deck class ​The card dash deck class creates a card grid to arrange our course cards.

​Then we create a card div to represent a course card. ​Each course card has an image element to display a course image, ​a card body which includes a card title to display the course name, and card ​dash text to display the course description. ​The result is a nice course ​card deck, that is rendered with each course, presented as a card. ​Another commonly used content template is table which displays ​tabular data such as a student list. To create a bootstrap table, ​we create a table element styled by a table class. ​Then we create a table head with a t dash head ​element to define table headers such as first name, ​last name, and email. ​Next, we add a table body to display user objects for a course with each table row, ​or tr representing a user in each table column ​or td representing a user attribute such as first name, ​last name or email.

​The result is a student table showing a list of students enrolled in a course. ​In this video, you learned what bootstrap ​is and how to integrate bootstrap into your Django ​template. You also learned about some common bootstrap, ​templates: navigation bar with a sign in form, container, card, and card deck and table.

---

### 4. [VIDEO TRANSCRIPT] Django Static Files
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/QGe9i/django-static-files
- **Method:** `dom_transcript` | **Length:** 3597 chars

​[Music] Welcome to Django Static Files. After watching this video, you will be able ​to: Explain how Django manages static files such ​as CSS and media files and combine Django views, templates, and static ​files to present your data as dynamic HTML pages. ​To add static files to your apps, you need to first create folders for different static ​files such as html templates, images, or CSS files. ​Next, under each folder to hold static files, you will need to create a subfolder using ​the same app name, such as app `onlinecourse`. The main reason you need this extra level ​is to create name spacing for static files because you may have static files using the ​same name across multiple apps in a Django project. ​Django uses the name space to uniquely refer to static files across multiple apps. ​In Django, you create different apps within the project container. Each app may have its ​own set of static files, normally stored in a folder named `static` in the app’s root ​folder. In addition to these app-specific static files, ​you may have to use some external static files. You can define the directories for these additional ​static files in the STATICFILES_DIRS list in Django project’s settings.py file.

​Django provides a set of STATICFILES_FINDERS such as AppDirectoriesFinder for locating ​the static files in an app and FileSystemFinder for locating other static file directories. ​These finders will generate the absolute path references and serve those files for you. ​Note that these static folders are where you store your static files in your development ​environment. They may be stored in multiple places in your local file system, especially ​if you have multiple apps. This is not convenient for deploying the app on a remote server. ​When you deploy your app to a production web server, you may want to move all your static ​files to a single location. Django provides a staticfiles app, which is ​installed by default, to collect all static files into a single directory.

​First, you specify the STATIC_ROOT, an absolute path that acts as the root location for your ​static files and creates a file structure for them. ​Then, specify the STATIC_URL, a prefix for your static files’ URL. ​Next, call the collectstatic command line provided by the staticfiles app, which will ​collect the static files to the STATIC_ROOT folder with a file structure created for you. ​Alternatively, you could also use the findstatic command line to search for more relative paths ​containing static files. Here is an example file structure under STATIC_ROOT ​after the collectstatic command line has been executed. ​Folder names at the first child level are the app name as the naming space. ​Under the app folders are different types of static file folders such as CSS, font, ​and images. When you deploy your Django app on a remote ​web server, the web server will know all files are collected under the STATIC ROOT folder.

​This will make it easier for the server to locate all necessary files. ​The files under the STATIC ROOT folder need to be served to your apps or other external ​users. They can be served either locally by a development Django server or remotely by ​a dedicated web server. You can find these files via URL with host ​and domain name, followed by the STATIC_URL you defined, such as `/static/`, which is ​essentially a URL prefix for your static files, then followed by the same file path in the ​STATIC ROOT folder, such as /onlinecourse/course.css. ​In this video, you learned: How Django manages static files in development ​and deployment environments

---

### 5. [VIDEO TRANSCRIPT] Deploy Your Django Apps
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/g52t0/deploy-your-django-apps
- **Method:** `dom_transcript` | **Length:** 5301 chars

​Welcome to deploy your Django apps! ​After watching this video, ​you will be able to explain how to deploy Django apps on web servers, ​explain how to deploy Django apps on the cloud, and list ​best practices to make a Django app production ready for the cloud. ​Running the runserver command line in Django development starts ​a minimal development web server for you to develop and test ​Django apps quickly. To deploy Dependable scalable and maintainable Django apps, ​you need to deploy them on web servers ​Since most web servers such as Apache, ​HTTP and Nginx are not written in Python, Django apps ​need extra interfaces to talk to web servers supporting those interfaces. ​The web server Gateway Interface, or WSGI, ​is the main python standard for communicating between web servers and applications. ​It supports synchronous code only. ​The start project command line will create a wsgi.py file, ​declaring an application callable, by default to make Django at work with wsgi, ​WSGI servers will try to find this application callable and use ​it as an entry point to communicate with your Django app.

​Some popular wsgi web servers are available for Django apps. ​Such as Gunicorn, uWSGI, Apache, and mod_wsgi. ​The Django app supports the asynchronous server Gateway Interface, ​another web server interface. ​The main difference from wsgi is it supports asynchronous code. ​The start project command line, creates a asgi.py file, declaring an application. ​callable to work with the asgi web server. ​Popular asgi web servers are Daphne, Hypercorn, and Uvicorn. Deploying Django apps ​or any other web apps in a production ​environment is non-trivial as you need to carefully build ​and configure platforms and infrastructure such as run times, ​operating systems, networks, databases, and servers to meet your deployment requirements.

​Thankfully, ​nowadays what the help of infrastructure-as-a-service and ​platform-as-a-service, you can deploy apps on provisioning platforms with minimal effort. ​Imagine you've just completed your website ​or reached a stage where it's ready for public testing, ​you'll require a hosting solution that offers greater accessibility and availability, ​than your personal development computer. ​One option would be to deploy it on cloud. To run a Django app ​on the cloud, you need a mechanism to host the web application ​and the database. First, you will need to consider hosting. ​There are several options to choose from. ​The first option is to use a virtual machine or VM from the cloud provider ​of your choice and install the minimal operating system or OS and software needed, ​such as Ubuntu, Python and Apache.

​Then you will manually configure the environment, ​install dependencies and deploy your Django app. ​Another choice is to use platform-as-a-service or PaaS deployment. ​Platforms like Heroku provide a more streamlined deployment process. With this method, ​you push your code to their Git repository and ​they handled the deployment process automatically. ​A third option is containerization deployment with this method, ​you can use Docker containers to package your Django app and its ​dependencies and deploy them using container orchestration tools ​like Kubernetes or K8s. ​The IBM Cloud code engine abstracts ​the operational burden of building deploying and managing workloads, ​so developers can focus on co-development. ​You may choose to use the Django database. Django officially supports PostgreSQL.

​MariaDB, MySQL, Oracle and SQLite. ​These databases can be deployed as self-managed ​or database-as-a-service from your cloud provider. ​To make your Django app production-ready on the cloud. ​Follow the following best practices and Implement various configurations ​to ensure scalability security and reliability, ​use the production database. In production, ​It's recommended to use a robust and scalable database. ​Like PostgreSQL, MySQL, or another suitable, ​relational database. Avoid using SQLite in production ​as it's not designed for high concurrency or heavy traffic. Secure ​database credentials.

​Store your database credentials and other sensitive information and environment variables, ​and never hard code them. ​Use HTTPS for secure communication between the server, your hosted ​Django app, and clients - your users accessing it in the browser. Static and media files. ​Use a cloud storage service or content delivery network, ​or CDN to efficiently serve static files like CSS or JavaScript and ​user-uploaded media files to reduce server load. Load balancing. ​With Django being stateless, ​make the most of it and consider using a load balancer to distribute, ​incoming traffic across multiple instances of your ​Django app ensuring that our performance and high availability. ​Horizontal scaling. Design your app to scale horizontally, adding more ​instances or containers as traffic increases. Monitoring and logging.

​Setup error monitoring and logging services to track and diagnose issues. ​In this video you learned how to deploy the Django apps on WSGI and ASGI ​web servers, how a VM, PaaS, containerization deployment, ​IBM, Cloud code engine and the Django database can facilitate your app ​deployment, and best practices for making your Django app production ready for the cloud.

---

### 6. [READING] Module 4 Summary: Consolidate and Deploy Your Django App Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/VBcU2/module-4-summary-consolidate-and-deploy-your-django-app
- **Method:** `dom_reading_cml` | **Length:** 2534 chars

Congratulations! You have completed this module. At this point in the course, you know:

- Both function-based and class-based views are Python functions.
- When you build a class-based view, you define a class subclassing the Django View base class. Then you access some standard methods such as Get or Post. Next, you implement your logic to handle HTTP requests.
- To speed up development and solve common tasks, Django provides some built-in view classes called generic-based views for developers to reuse.
- Authentication is validating users’ identities using credentials such as username and password.
- After users are authenticated, authorization will check the users’ access permissions for resources such as databases.
- In Django, a user model is created to handle authentication and to work with other models, such as groups and permissions, to handle authorization.
- Developers can extend the User model to define application-specific users, such as instructors or learners inherited from the User model.
- Bootstrap, a free web front-end framework, facilitates web app development.
- Bootstrap provides many HTML and CSS templates to simplify Django template development.
- If you want to use Bootstrap CSS style classes without downloading Bootstrap, add a link to the latest Bootstrap version into the head element of your HTML template.
- To add static files to your apps, you first create folders for different static files, such as HTML templates, images, or CSS files.
- Under each folder to hold static files, you create a subfolder using the same app name. This creates namespacing to uniquely refer to static files that use the same name across multiple apps in a Django project.
- Django provides a set of STATICFILES_FINDERS for locating the static files in an app. It also provides a staticfiles app to collect all static files in a single directory when an app is deployed.
- To deploy reliable, scalable, and maintainable Django apps, you need to deploy them on web servers.
- Since most web servers are not written in Python, Django apps need extra interfaces to talk to web servers.
- The Web Server Gateway Interface, or WSGI, is the main Python standard for communicating between Web servers and applications.
- The Django app supports the Asynchronous Server Gateway Interface, another web server interface.
- Infrastructure as a Service and Platform as a Service offering allows you to focus on your app development and deploy apps without worrying about the underlying Infrastructure and platform.

---

### 7. [READING] Module 4 Cheat Sheet: Consolidate and Deploy Your Django App Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/hYFvf/module-4-cheat-sheet-consolidate-and-deploy-your-django-app
- **Method:** `dom_reading_cml` | **Length:** 4635 chars

| Package/ Method | Description | Code Example |
| --- | --- | --- |
| ListView: | Displays a list of objects. | class MyListView(ListView): model = MyModel template_name = 'my_template.html' context_object_name = 'object_list' # default: object_list |
| DetailView | Displays details of a single object. | class MyDetailView(DetailView): model = MyModel template_name = 'my_template.html' context_object_name = 'object' # default: object pk_url_kwarg = 'my_model_id' # default: pk |
| CreateView | Displays a form to create a new object. | class MyCreateView(CreateView): model = MyModel template_name = 'my_template.html' fields = '__all__' # or specify a list of fields |
| UpdateView | Displays a form to update an existing object. | class MyUpdateView(UpdateView): model = MyModel template_name = 'my_template.html' fields = '__all__' # or specify a list of fields pk_url_kwarg = 'my_model_id' # default: pk |
| DeleteView | Displays a confirmation page to delete an object. | class MyDeleteView(DeleteView): model = MyModel template_name = 'my_template.html' success_url = '/success-url/' pk_url_kwarg = 'my_model_id' # default: pk |
| Basic View Function | Function-based view that returns “Hello, World!” From Django.http import HttpResponse | def my_view(request): # Your view logic here return HttpResponse("Hello, World!") |
| Render a Template | Function-based view to render a template with context. From django.shortcuts import render | def my_template_view(request): context = {'variable': value} return render(request, 'my_template.html', context) |
| Redirect to a URL | Function-based view to redirect to a specific URL. From django.shortcuts import redirect | def my_redirect_view(request): return redirect('url_name_or_path') |
| Handle a Form Submission | Function-based view to handle form submission. From django.shortcuts import render | def my_form_view(request): if request.method == 'POST': # Process the form data here else: # Display the form return render(request, 'my_form_template.html', context) |
| Handle URL Parameters | Function-based view that accesses URL parameters. | def my_param_view(request, param): # Access the 'param' value from the URL |
| Protecting Views (Restrict Access) using @login_required Decorator | Function-based view protected with login_required decorator. From django.contrib.auth.decorators import login_required | @login_required def my_protected_view(request): # Your view logic here |
| Bootstrap CSS | Link to include Bootstrap CSS in the base template. | Add the following link to the <head> section of your base template (usually base.html): <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"> |
| Bootstrap JavaScript | Script tag to include Bootstrap JavaScript library. | Include the Bootstrap JavaScript library at the end of the <body> section to enable certain features (for example, dropdowns, modals): <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js"></script> |
| Bootstrap classes and components | Create visually appealing and responsive web pages without having to write CSS styles manually. | <a href="#" class="btn btn-primary">Click Me</a> |
| Configuration – Static files | Django settings for static files configuration. | In your Django settings (settings.py), define the following settings: STATIC_URL = '/static/studio/edx.org-next/' # URL to access static files STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] # Directory to look for static files |
| Configuration – Installed apps | Defines a list of all the applications installed in the project. | Add 'django.contrib.staticfiles' to your INSTALLED_APPS in settings.py: INSTALLED_APPS = [ # ... 'django.contrib.staticfiles', # ... ] |
| Configuration – App Dirs | A configuration option used within the TEMPLATES setting. When set to TRUE, Django will look for template files within the app directories. | Make sure the APP_DIRS setting is set to True in the TEMPLATES list. This allows Django to look for static files within the apps' directories. TEMPLATES = [ { # ... 'APP_DIRS': True, # ... }, ] |
| Usage – Static content | Code to style the HTML templates and provide interactivity to web pages. | <link href="{% static 'your_app/css/style.css' %}" rel="stylesheet"> <script src="{% static 'your_app/js/script.js' %}"></script> <img src="{% static 'your_app/img/logo.png' %}" alt="Logo"> |
| Collecting static files | When deploying your project, you need to collect all static files into a single location. | python manage.py collectstatic STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') |

---

## Module 5: Final Project: Enhance Online Course App with New Features

### 1. [READING] Congratulations and Next Steps Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/v0AE0/congratulations-and-next-steps
- **Method:** `dom_reading_cml` | **Length:** 1172 chars

Congratulations on completing this Developing Applications with SQL, Databases & Django course! We hope you enjoyed it and find great satisfaction using your new skills in the workplace or elsewhere.

This course is part of the IBM Back-End Development Professional Certificate and the IBM Full Stack Software Developer Professional Certificate.

These Professional Certificates will equip learners with all the key skills and technical know-how to launch a career as an entry level back-end or full stack developer. Guided by experts, they will learn the latest tools and technologies used by professional developers, including Linux scripting, Git and GitHub, Python, SQL, Databases, Django, Containers with Docker, Kubernetes, and OpenShift, Microservices, Serverless, as well as Application Security, and Monitoring.

To continue to develop skills as a back-end developer, you should consider these related programs:

- Introduction to Containers w/ Docker, Kubernetes & OpenShift
- Application Development using Microservices and Serverless

We also encourage you to leave your feedback and rate this course so that we can continue to improve our content.

Good luck!

---

### 2. [READING] Thanks from the Course Team Reading • 2 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/DMWKC/thanks-from-the-course-team
- **Method:** `dom_reading_cml` | **Length:** 1015 chars

The course team expresses their gratitude for your participation in this course. We sincerely hope that you found it enjoyable and wish you all the best as you apply your newly acquired knowledge and skills. We encourage you to rate the course and share your feedback through a review. Your input is highly valued.

Best regards,

Course Team

- - -

This course has been made possible through the contributions of the following team members:

#### Primary Instructors:

- Yan Luo

#### Other Contributors and Staff

Project Lead: Rav Ahuja

Subject Matter Expert: Muhammad Yahya

Instructional Designer: Claire Baddeley, Misty Taylor, Pooja Bhardwaj

Lab Author: Yan Luo, Muhammad Yahya 

Production Team

Publishing: Jada Harrison, Deyanira Mares, Grace Barker

QA: Steve Hord, Mary Stenberg, Mercedes Schneider

Project Manager: Zahira Omar

Narration: Bella West, Sarah Ruth

Video Production: Simer Preet, Alex Jones 

Teaching Assistants and Forum Moderators

Teaching Assistants: Pallavi Rai, Anamika Agarwal

---

### 3. [READING] Further Your Learing Reading • 10 min
- **URL:** https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/JtuC8/further-your-learing
- **Method:** `dom_reading_cml` | **Length:** 266 chars

Put your skills into practice with IBM Db2

Ready to take the next step? Explore how IBM Db2 helps you work with data using SQL and build, manage, and query enterprise databases. Experience IBM Db2 for yourself with the confirmed no-cost experience.

Explore IBM Db2

---
