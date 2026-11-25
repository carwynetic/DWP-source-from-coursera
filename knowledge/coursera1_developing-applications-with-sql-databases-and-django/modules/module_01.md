# Module 1: Getting Started with SQL & Relational Databases

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
