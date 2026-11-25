# Module 5: APIs and Data Collection

### 1. [VIDEO TRANSCRIPT] Application Program Interface Video • 5 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/rLaLi/application-program-interface
- **Method:** `dom_transcript` | **Length:** 4441 chars

In this video we will discuss Application Program Interfaces (APIs for short). Specifically, we will discuss what an API is, API libraries, and REST APIs, including Request and Response and an example with PyCoinGecko. An API lets two pieces of software talk to each other. For example, you have your program, you have some data, you have other software components. You use the API to communicate with other software via inputs and outputs. Just like a function, you don’t have to know how the API works, just its inputs and outputs. Pandas is actually a set of software components, much of which are not even written in Python.

You have some data. You have a set of software components. We use the pandas API to process the data by communicating with the other software components. Let’s clean up the diagram. When you create a dictionary, and then create a pandas object with the DataFrame constructor, in API lingo, this is an “instance.” The data in the dictionary is passed along to the pandas API. You then use the dataframe to communicate with the API.

When you call the method head, the dataframe communicates with the API displaying the first few rows of the dataframe. When you call the method mean the API will calculate the mean and return the values. REST APIs are another popular type of API; they allow you to communicate through the internet allowing you to take advantage of resources like storage, access more data, artificial intelligence algorithms, and much more. The RE stands for Representational, the S for State, and T for Transfer. In REST APIs your program is called the client. The API communicates with a web service you call through the internet. There is a set of rules regarding communication, input or request, and output or response. Here are some common terms.

You or your code can be thought of as a client. The web service is referred to as a resource. The client finds the service via an endpoint. We will review this more in the next section. The client sends requests to the resource and the response to the client. HTTP methods are a way of transmitting data over the internet. We tell the REST APIs what to do by sending a request. The request is usually communicated via an HTTP message. The HTTP message usually contains a JSON file.

This contains instructions for what operation we would like the service to perform. This operation is transmitted to the web service via the internet. The service performs the operation. In a similar manner, the web service returns a response via an HTTP message, where the information is usually returned via a JSON file. This information is transmitted back to the client. Cryptocurrency data is excellent to be used in an API because it is constantly updated and it is vital to cryptocurrency trading. We will use the PyCoinGecko Python client/wrapper for the CoinGecko API, updated every minute by CoinGecko.

We use the wrapper/client because it is easy to use so you can focus on the task of collecting data, we will also introduce pandas time series functions for dealing with time series data. Using PyCoinGecko to collect data is simple. All we need is to install and import the library, then create a client object, and finally use a function to request our data. In this function we are getting data on bitcoin, in US dollars, for the past 30 days. In this case our response is a JSON expressed as a Python dictionary of nested lists including price, market cap, and total volumes, which contain the UNIX timestamp and the price at that time. We are only interested in price so that is what we will select using the key price. To make things simple, we can convert our nested list to a DataFrame, with the columns timestamp and price it's difficult to understand the column timestamp.

We will convert it to a more readable format using the pandas function to_datetime. Using the to_datetime function, we create readable time data, the input is the timestamp column, unit of time is set to milliseconds. We append the output to the new column, date. Now we want to create a candlestick plot. To get the data for the daily candlesticks we will group by the date to find the minimum, maximum, first, and last price of each day. Finally we will use plotly to create the candlestick chart and plot it. Now we can view the candlestick chart by opening the HTML file and clicking Trust HTML in the top left of the tab. It should look something like this.

---

### 2. [READING] Some Context on APIs Reading • 5 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/M083f/some-context-on-apis
- **Method:** `dom_reading_cml` | **Length:** 3184 chars

## What are APIs?

APIs, or Application Programming Interfaces, are a crucial part of software development. They allow developers to create new applications by leveraging existing functionality from other systems. APIs define how software components should interact and facilitate communication between various products and services without requiring direct implementation.

## Importance of APIs

APIs are essential for any engineer because they provide a way to access data and functionality from other systems, which can save time and resources. For instance, APIs can be used to integrate applications into the existing architecture of a server or application, allowing developers to communicate between various products and services without requiring direct implementation.

APIs are also important because they enable developers to create new applications by leveraging existing functionality from other systems. This can help developers throughout the engineering and development process of apps.

APIs are used in a wide range of applications, from social media platforms to e-commerce websites. They are also used in mobile applications, web applications, and desktop applications.

## Applications of APIs

APIs have a wide range of applications, some of which are:

- Social media platforms: Social media platforms like Facebook, Twitter, and Instagram use APIs to allow developers to access their data and functionality. This allows developers to create applications that can interact with these platforms and provide additional functionality to users.
- E-commerce websites: E-commerce websites like Amazon and eBay use APIs to allow developers to access their product catalogs and other data. This allows developers to create applications that can interact with these platforms and provide additional functionality to users.
- Weather applications: Weather applications like AccuWeather and The Weather Channel use APIs to access weather data from various sources. This allows developers to create applications that can provide users with up-to-date weather information.
- Maps and navigation applications: Maps and navigation applications like Google Maps and Waze use APIs to access location data and other information. This allows developers to create applications that can provide users with directions, traffic updates, and other location-based information.
- Payment gateways: Payment gateways like PayPal and Stripe use APIs to allow developers to access their payment processing functionality. This allows developers to create applications that can process payments securely and efficiently.
- Messaging applications: Messaging applications like WhatsApp and Facebook Messenger use APIs to allow developers to access their messaging functionality. This allows developers to create applications that can interact with these platforms and provide additional functionality to users.

## Conclusion

In summary, APIs are an essential part of software development, and they provide a way to access data and functionality from other systems. They are used in a wide range of applications and can help developers save time and resources while creating new applications.

---

### 3. [VIDEO TRANSCRIPT] REST APIs & HTTP Requests - Part 1 Video • 4 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/W6xwd/rest-apis-http-requests-part-1
- **Method:** `dom_transcript` | **Length:** 3170 chars

In this video, we will discuss the HTTP protocol. Specifically, we will discuss: Uniform Resource Locator: URL Request and Response We touched on REST APIs in the last section. The HTTP protocol can be thought of as a general protocol of transferring information through the web. This includes many types of REST APIs. Recall that REST APIs function by sending a request, and the request is communicated via HTTP message. The HTTP message usually contains a JSON file. When you, the client, use a web page your browser sends an HTTP request to the server where the page is hosted. The server tries to find the desired resource by default "index.html".

If your request is successful, the server will send the object to the client in an HTTP response; this includes information like the type of the resource, the length of the resource, and other information. The table under the Web server represents a list of resources stored in the web server. In this case, an HTML file, png image, and txt file. When the request is made for the information, the web servers sends the the requested information, that is, one of the files. A uniform resource locator (URL) is the most popular way to find resources on the web. We can break the URL into three parts. First we have the scheme: this is the protocol, and for this lab it will always be http:// The internet address or Base URL: this will be used to find the location; some examples include www.ibm.com and www.gitlab.com And finaly, the route: this is the location on the web server, for example: /images/IDSNlogo.png Let's review the request and Response process.

The following is an example of the request message for the get request method. There are other HTTP methods we can use. In the start line we have the GET method. This is an HTTP method. In this case, it’s requesting the file index.html The Request header passes additional information with an HTTP request. In the GET method the Request header is empty. Some Requests have a body; we will have an example of a request body later.

The following table represents the response. The response start line contains the version number followed by a descriptive phrase. In this case, HTTP/1.0 a status code (200) meaning success, and the descriptive phrase, OK. We have more on status codes later. The response header contains information. Finally, we have the response body containing the requested file, in this case an HTML document. Lets look at other status codes.

Some status code examples are shown in the table below. The prefix indicates the class; for example, the 100s are informational responses; 100 indicates that everything is OK so far. The 200s are Successful responses: For example, 200 The request has succeeded. Anything in the 400s is bad news. 401 means the request is unauthorized. 500’s stands for server errors, like 501 for not Implemented. When an HTTP request is made, an HTTP method is sent. This tells the server what action to perform. A list of several HTTP methods is shown here.

In the next video, we will use Python to apply the GET method that retrieves data from the server and the post method that sends data to the server.

---

### 4. [VIDEO TRANSCRIPT] REST APIs & HTTP Requests - Part 2 Video • 4 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/h9CR3/rest-apis-http-requests-part-2
- **Method:** `dom_transcript` | **Length:** 3887 chars

In this video, we will discuss the HTTP protocol using the requests library, a popular method for dealing with the HTTP protocol in Python. We will review Python library requests for working with the HTTP protocols, and we will provide an overview of Get requests and Post requests. Let us review the request module in Python. This is one of several libraries, including HTTPlib and urllib, that can work with the HTTP protocol. Requests is a Python library that allows you to send HTTP/1.1 requests easily. We can import the library as follows. You can make a GET request via the method GET to www.ibm.com.

We have the response object R. This has information about the request, like the status of the request. We can view the status code using the attribute status underscore code, which is 200 for OK. You can view the request headers. You can view the request body in the following line. As there is no body for a GET request, we get a none. You can view the HTTP response header using the attribute headers.

This returns a Python dictionary of HTTP response headers. We can look at the dictionary values. We can obtain the date the request was sent by using the key date. The key content type indicates the type of data. Using the response object R, we can also check the encoding. As the content type is text or HTML, we can use the attribute text to display the HTML in the body. We can review the first 100 characters.

You can also download other content. See the lab for more. You can use the GET method to modify the results of your query, for example, retrieving data from an API. In the lab, we will use httpbin.org, a simple HTTP request and response service. We send a GET request to the server. Like before, we have the base URL in the route. We append /get.

This indicates we would like to perform a GET request. This is demonstrated in the following table. After GET is requested, we have the query string. This is part of a uniform resource locator or URL, and this sends other information to the web server. The start of the query is a question mark, followed by a series of parameter and value pairs as shown in the table below. The first parameter name is name, and the value is Joseph. The second parameter name is ID, and the value is 123.

Each pair parameter and value is separated by an equal sign. The series of pairs is separated by the ampersand. Let us complete an example in Python. We have the base URL with GET appended to the end. To create a query string, we use the dictionary payload. The keys are the parameter names, and the values are the value of the query string. Then we pass the dictionary payload to the params parameter of the GET function.

We can print out the URL and see the name and values. We can see the request body. As the info is sent in the URL, the body has a value of none. We can print out the status code. We can view the response as text, and we can look at the key content type to look at the content type. As the content content type is in the JSON, we format it using the method JSON. It returns a Python dict.

The key args has the name and values for the query string. Like a GET request, a POST request is used to send data to a server, but the POST request sends the data in a request body, not the URL. In order to send the POST request in the URL, we change the route to POST. This endpoint will expect data, and it is a convenient way to configure an HTTP request to send data to a server. We have the payload dictionary. To make a POST request, we use the POST function. The variable payload is passed to the parameter data.

Comparing the URL using the attribute URL from the response object of the GET and POST We see the POST request has no name or value pairs in its URL. We can compare the POST and GET request body. We see only the POST request has a body. And we can view the key form to get the payload.

---

### 5. [READING] Web Scraping and HTML Basics Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/IUWHA/web-scraping-and-html-basics
- **Method:** `dom_reading_cml` | **Length:** 7266 chars

## Objectives

After completing this reading, you'll learn about:

- Explain key concepts related to HTML structure and HTML tag composition.
- Explore the concept of HTML document trees.
- Familiarize yourself with HTML tables.
- Gain insight into the basics of web scraping using Python and BeautifulSoup.

## Introduction to web scraping

Web scraping, also known as web harvesting or web data extraction, is the process of extracting information from websites or web pages. It involves automated retrieval of data from web sources. People use it for various applications such as data analysis, mining, price comparison, content aggregation, and more.

## How web scraping works

### HTTP request

The process typically begins with an HTTP request. A web scraper sends an HTTP request to a specific URL, similar to how a web browser would when you visit a website. The request is usually an HTTP GET request, which retrieves the web page's content.

### Web page retrieval

The web server hosting the website responds to the request by returning the requested web page's HTML content. This content includes the visible text and media elements and the underlying HTML structure that defines the page's layout.

### HTML parsing

Once the HTML content is received, you need to parse the content. Parsing involves breaking down the HTML structure into components, such as tags, attributes, and text content. You can use BeautifulSoup in Python. It creates a structured representation of the HTML content that can be easily navigated and manipulated.

### Data extraction

With the HTML content parsed, web scrapers can now identify and extract the specific data they need. This data can include text, links, images, tables, product prices, news articles, and more. Scrapers locate the data by searching for relevant HTML tags, attributes, and patterns in the HTML structure.

### Data transformation

Extracted data may need further processing and transformation. For instance, you can remove HTML tags from text, convert data formats, or clean up messy data. This step ensures the data is ready for analysis or other use cases.

### Storage

After extraction and transformation, you can store the scraped data in various formats, such as databases, spreadsheets, JSON, or CSV files. The choice of storage format depends on the specific project's requirements.

### Automation

In many cases, scripts or programs automate web scraping. These automation tools allow recurring data extraction from multiple web pages or websites. Automated scraping is especially useful for collecting data from dynamic websites that regularly update their content.

## HTML structure

Hypertext markup language (HTML) serves as the foundation of web pages. Understanding its structure is crucial for web scraping.

- <html> is the root element of an HTML page.
- <head> contains meta-information about the HTML page.
- <body> displays the content on the web page, often the data of interest.
- <h3> tags are type 3 headings, making text larger and bold, typically used for player names.
- <p> tags represent paragraphs and contain player salary information.

## Composition of an HTML tag

HTML tags define the structure of web content and can contain attributes.

- An HTML tag consists of an opening (start) tag and a closing (end) tag.
- Tags have names (<a> for an anchor tag).
- Tags may contain attributes with an attribute name and value, providing additional information to the tag.

## HTML document tree

You can visualize HTML documents as trees with tags as nodes.

- Tags can contain strings and other tags, making them the tag's children.
- Tags within the same parent tag are considered siblings.
- For example, the <html> tag contains both <head> and <body> tags, making them descendants of <html but children of <html>. <head> and <body> are siblings.

## HTML tables

HTML tables are essential for presenting structured data.

- Define an HTML table using the <table> tag.
- Each table row is defined with a <tr> tag.
- The first row often uses the table header tag, typically <th>.
- The table cell is represented by <td> tags, defining individual cells in a row.

## Web scraping

Web scraping involves extracting information from web pages using Python. It can save time and automate data collection.

### Required tools

Web scraping requires Python code and two essential modules: Requests and Beautiful Soup. Ensure you have both modules installed in your Python environment.

12# Import Beautiful Soup to parse the web page contentfrom bs4 import BeautifulSoupInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Fetching and parsing HTML

To start web scraping, you need to fetch the HTML content of a webpage and parse it using Beautiful Soup. Here's a step-by-step example:

1234567891011121314151617import requestsfrom bs4 import BeautifulSoup # Specify the URL of the webpage you want to scrapeurl = 'https://en.wikipedia.org/wiki/IBM' # Send an HTTP GET request to the webpageresponse = requests.get(url) # Store the HTML content in a variablehtml_content = response.text # Create a BeautifulSoup object to parse the HTMLsoup = BeautifulSoup(html_content, 'html.parser') # Display a snippet of the HTML contentprint(html_content[:500])Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Navigating the HTML structure

BeautifulSoup represents HTML content as a tree-like structure, allowing for easy navigation. You can use methods like find_all to filter and extract specific HTML elements. For example, to find all anchor tags () and print their text:

123456# Find all <a> tags (anchor tags) in the HTMLlinks = soup.find_all('a') # Iterate through the list of links and print their textfor link in links:    print(link.text)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Custom data extraction

Web scraping allows you to navigate the HTML structure and extract specific information based on your requirements. This process may involve finding specific tags, attributes, or text content within the HTML document.

#### Using BeautifulSoup for HTML parsing

Beautiful Soup is a powerful tool for navigating and extracting specific web page parts. It allows you to find elements based on their tags, attributes, or text, making extracting the information you're interested in easier.

#### Using pandas read_html for table extraction

Pandas, a Python library, provides a function called read_html, which can automatically extract data from websites' tables and present it in a format suitable for analysis. It’s similar to taking a table from a webpage and importing it into a spreadsheet for further analysis.

### Conclusion

In this reading, you learned about web scraping with BeautifulSoup and Pandas with emphasis on extracting elements and tables. BeautifulSoup facilitates HTML parsing, while Pandas' read_html streamlines table extraction. The reading also highlighted responsible web scraping, ensuring adherence to website terms. Armed with this knowledge, you can confidently engage in precise data extraction.

---

### 6. [VIDEO TRANSCRIPT] (Optional) HTML for Web Scraping Video • 4 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/nUuvs/optional-html-for-web-scraping
- **Method:** `dom_transcript` | **Length:** 4024 chars

In this video we will review Hypertext Markup Language or HTML for Web Scraping. Lots of useful data is available on web pages, such as real estate prices and solutions to coding questions. The website Wikipedia is a repository of the world's information. If you have an understanding of HTML, you can use Python to extract this information. In this video, you will: review the HTML of a basic web page; understand the Composition of an HTML Tag; understand HTML Trees; and understand HTML Tables. Let’s say you were asked to find the name and salary of players in a National Basketball League from the following page. The web page is comprised of HTML. It consists of text surrounded by a series of blue text elements enclosed in angle brackets called tags. The tags tells the browser how to display the content. The data we require is in this text.

The first portion contains the "DOCTYPE html” which declares this document is an HTML document. The "html" element is the root element of an HTML page, and "head" element contains meta information about the HTML page. Next, we have the body, this is what's displayed on the web page. This is usually the data we are interested in, we see the elements with an “h3”, this means type 3 heading, makes the text larger and bold. These tags have the names of the players, notice the data is enclosed in the elements. It starts with a h3 in brackets and ends in a slash h3 in brackets. There is also a different tag “p”, this means paragraph, each p tag contains a player's salary.

Let’s take a closer look at the composition of an HTML tag. Here is an example of an HTML Anchor tag. It will display IBM and when you click it, it will send you to IBM.com. We have the tag name, in this case “a”. This tag defines a hyperlink, which is used to link from one page to another. It’s helpful to think of each tag name as a class in Python and each individual tag as an instance. We have the opening or start tag and we have the end tag.

This has the tag name preceded by a slash. These tags contain the content, in this case what’s displayed on the web page. We have the attribute, this is composed of the Attribute Name and Attribute Value. In this case it the url to the destination web page. Real web pages are more complex, depending on your browser you can select the HTML element, then click Inspect. The result will give you the ability to inspect the HTML. There is also other types of content such as CSS and JavaScript that we will not go over in this course.

The actual element is shown here. Each HTML document can actually be referred to as a document tree. Let's go over a simple example. Tags may contain strings and other tags. These elements are the tag’s children. We can represent this as a family tree. Each nested tag is a level in the tree.

The tag HTML tag contains the head and body tag. The Head and body tag are the descendants of the html tag. In particular they are the children of the HTML tag. HTML tag is their parent. The head and body tag are siblings as they are on the same level. Title tag is the child of the head tag and its parent is the head tag. The title tag is a descendant of the HTML tag but not its child.

The heading and paragraph tags are the children of the body tag; and as they are all children of the body tag they are siblings of each other. The bold tag is a child of the heading tag, the content of the tag is also part of the tree but this can get unwieldy to draw. Next, let’s review HTML tables. To define an HTML table we have the table tag. Each table row is defined with a "tr" tag, you can also use a table header tag for the first row. The table row cell contains a set of "td" tags, each defines a table cell. For the first row first cell we have; for the first row second cell we have; and so on.

For the second row we have; and for the second row first cell we have; for the second row second cell we have; and so on. We now have some basic knowledge of HTML. Now let's try and extract some data from a web page.

---

### 7. [VIDEO TRANSCRIPT] (Optional) Web Scraping Video • 4 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/GHf2O/optional-web-scraping
- **Method:** `dom_transcript` | **Length:** 4171 chars

In this video we will cover Web Scraping. After watching this video you will be able to: define web scraping; understand the role of BeautifulSoup Objects; apply the find_all method; and web scrape a website. What would you do if you wanted to analyze hundreds of points of data to find the best players of a sports team? Would you start manually copying and pasting information from different websites into a spreadsheet? Spending hours trying to find the right data, and eventually giving up because the task was too overwhelming? That’s where web scraping can help. Web scraping is a process that can be used to automatically extract information from a website, and can easily be accomplished within a matter of minutes and not hours. To get started, we just need a little Python code and the help of two modules named Requests and Beautiful Soup.

Let’s say you were asked to find the name and salary of players in a National Basketball League, from the following webpage. First we import BeautifulSoup. We can store the webpage HTML as a string in the variable HTML. To parse a document, pass it into the Beautiful Soup constructor. We get the Beautiful Soup object, soup, which represents the document as a nested data structure. Beautiful Soup represents HTML as a set of Tree like objects with methods used to parse the HTML. We will review the Beautiful Soup object using the Beautiful Soup object, soup, we created.

The tag object corresponds to an HTML tag in the original document. For example, the tag “title.” Consider the tag h3. If there is more than one tag with the same name, the first element with that tag is selected. In this case with Lebron James, we see the name is Enclosed in the bold attribute "b". To extract it, use the Tree representation. Let’s use the Tree representation.

The variable tag-object is located here. We can access the child of the tag or navigate down the branch as follows: You can navigate up the tree by using the parent attribute. The variable tag child is located here. We can access the parent. This is the original tag object. We can find the sibling of “tag object.” We simply use the next-sibling attribute.

We can find the sibling of sibling one. We simply use the next sibling attribute. Consider the tag child object. You can access the attribute name and value as a key value pair in a dictionary as follows. You can return the content as a Navigable string, this is like a Python string that supports Beautiful Soup functionality. Let's review the method find_all. This is a filter, you can use filters to filter based on a tag’s name, its attributes, the text of a string, or on some combination of these.

Consider the list of pizza places. Like before, create a BeautifulSoup object. But this time, name it table. The find_all () method looks through a tag’s descendants and retrieves all descendants that match your filters. Apply it to the table with the tag tr. The result is a Python iterable just like a list, each element is a tag object for tr. This corresponds to each row in the list- including the table header.

Each element is a tag object. Consider the first row. For example, we can extract the first table cell. We can also iterate through each table cell. First, we iterate through the list “table rows,” via the variable row. Each element corresponds to a row in the table. We can apply the method find_all to find all the table cells, then we can iterate through the variable cells for each row.

For each iteration, the variable cell corresponds to an element in the table for that particular row. We continue to iterate through each element and repeat the process for each row. Let’s see how to apply Beautiful Soup to a webpage. To scrape a webpage we also need the Requests library. The first step is to import the modules that are needed. Use the get method from the requests library to download the webpage. The input is the URL. Use the text attribute to get the text and assign it to the variable page.

Then, create a BeautifulSoup object ‘soup’ from the variable page. It will allow you to parse through the HTML page. You can now scrape the Page. Check out the labs for more.

---

### 8. [READING] Web Scraping - A Key Tool in Data Science Reading • 5 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/up3H7/web-scraping-a-key-tool-in-data-science
- **Method:** `dom_reading_cml` | **Length:** 3207 chars

## Introduction

Web scraping, also known as web harvesting or web data extraction, is a technique used to extract large amounts of data from websites. The data on websites is unstructured, and web scraping enables us to convert it into a structured form.

## Importance of Web Scraping in Data Science

In the field of data science, web scraping plays an integral role. It is used for various purposes such as:

- Data Collection: Web scraping is a primary method of collecting data from the internet. This data can be used for analysis, research, etc.
- Real-time Application: Web scraping is used for real-time applications like weather updates, price comparison, etc.
- Machine Learning: Web scraping provides the data needed to train machine learning models.

## Web Scraping with Python

Python provides several libraries for web scraping. Here are some of them:

### BeautifulSoup

BeautifulSoup is a Python library used for web scraping purposes to pull the data out of HTML and XML files. It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner.

12345from bs4 import BeautifulSoupimport requestsURL = "http://www.example.com"page = requests.get(URL)soup = BeautifulSoup(page.content, "html.parser")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Scrapy

Scrapy is an open-source and collaborative web crawling framework for Python. It is used to extract the data from the website.

1234567import scrapyclass QuotesSpider(scrapy.Spider):    name = "quotes"    start_urls = ['http://quotes.toscrape.com/tag/humor/',]    def parse(self, response):        for quote in response.css('div.quote'):            yield {'quote': quote.css('span.text::text').get()}Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Selenium

Selenium is a tool used for controlling web browsers through programs and automating browser tasks.

123from selenium import webdriverdriver = webdriver.Firefox()driver.get("http://www.example.com")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Applications of Web Scraping

Web scraping is used in various fields and has many applications:

- Price Comparison: Services such as ParseHub use web scraping to collect data from online shopping websites and use it to compare the prices of products.
- Email address gathering: Many companies that use email as a medium for marketing, use web scraping to collect email ID and then send bulk emails.
- Social Media Scraping: Web scraping is used to collect data from Social Media websites such as Twitter to find out what's trending.

## Conclusion

Web scraping is an essential skill in the fast-growing world of data science. It provides the ability to turn the web into a source of data that can be analyzed, processed, and used for a variety of applications. However, it's important to remember that one should use web scraping responsibly and ethically, respecting the terms of use or robots.txt files of the websites being scraped.

---

### 9. [READING] Web Scraping Tables using Pandas Reading • 7 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/VdUUL/web-scraping-tables-using-pandas
- **Method:** `dom_reading_cml` | **Length:** 3004 chars

The Pandas library in Python contains a function read_html() that can be used to extract tabular information from any web page.

Consider the following example:

Let us assume we want to extract the list of the largest banks in the world by market capitalization, from the following link:

1URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.We may use pandas.read_html() function in python to extract all the tables in the web page directly.

A snapshot of the webpage is shown below.

We can see that the required table is the first one in the web page.

Note: This is a live web page and it may get updated over time. The image shown above has been captured in November 2023. The process of data extraction remains the same.

We may execute the following lines of code to extract the required table from the web page.

12345import pandas as pdURL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'tables = pd.read_html(URL)df = tables[0]print(df)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.This will extract the required table as a dataframe df. The output of the print statement would look as shown below.

Although convenient, this method comes with its own set of limitations.Firstly, web pages may have content saved in them as tables but they may not appear as tables on the web page.

For instance, consider the following URL showing the list of countries by GDP (nominal).

1URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.The images on the web page are also saved in tabular format. A snapshot of the web page is shared below.

Secondly, the contents of the tables in the web pages may contain elements such as hyperlink text and other denoters, which are also scraped directly using the pandas method. This may lead to a requirement of further cleaning of data.A closer look at table 3 in the image shown above indicates that there are many hyperlink texts which are also going to be treated as information by the pandas function.

We can extract the table using the code shown below.

12345import pandas as pdURL = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'tables = pd.read_html(URL)df = tables[2] # the required table will have index 2print(df)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.The output of the print statement is shown below.

Note that the hyperlink texts have also been retained in the code output.

It is further prudent to point out, that this method exclusively operates only on tabular data extraction. BeautifulSoup library still remains the default method of extracting any kind of information from web pages.

---

### 10. [VIDEO TRANSCRIPT] Working with Different File Formats Video • 4 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/EPUdg/working-with-different-file-formats
- **Method:** `dom_transcript` | **Length:** 3453 chars

Hello. Welcome to Working With Different File Formats. After watching this video, you will be able to: Define different file formats such as csv, xml, and json. Write simple programs to read and output data. List what Python libraries are needed to extract data. When collecting data you will find there are many different file formats that need to be collected or read in order to complete a data driven story or analysis. When gathering the data Python can make the process simpler with its predefined libraries, but before we explore Python let’s first check out some of the various file formats. When looking at a file name you will notice an extension at the end of the title. These extensions let you know what type of file it is and what it needed to open it. For instance if you see a title like “FileExample.csv” you will know this is a “csv” file. This is only one example of different file types as there are many more such as “json” or “xml”. When coming across these different file formats and trying to access their data we need to utilize Python libraries to make this process easier. The first Python library to become familiar with is called Pandas. By importing this library in the beginning of the code we are then be able to easily read the different file types.

Since we have now imported the Panda library let’s use it to read the first “csv” file. In this instance we have come across the “FileExample.csv” file. The first step is to assign the file to a variable. Then create another variable to read the file with the help of the Panda library. We can then call read_csv function output the data to the screen. With this example there were no headers for the data so it added the first line as the header. Since we don’t want the first line of data as the header let’s find out how to correct this issue.

Now that we have learned how to read and output the data from a “csv” file let’s make it look a little more organized. From the last example we were able to print out the data but because the file had no headers it printed the first line of data as a header. We easily solve this by adding a dataframe attribute. We use the variable “df” to call the file and then add the “columns” attribute. By adding this one line to our program we can then neatly organize the data output into the specified headers for each column. The next file format we will explore is the “json” file format. In this type of file the text is written in a language independent data format and is similar to a Python dictionary. The first step in reading this type of file is to import json. After importing “json” we can add a line to open the file call the “load” attribute of “json” to begin and read the file and lastly we can then print the file. The next file format is “xml”. This type of file is also known as Extensible Markup Language. While the Pandas library does not have an attribute to read this type of file let’s explore how to parse this type of file. The first step to read this type of file is to import xml. By importing this library we can then use the “etree” attribute to parse the “xml” file.

We then add the column headers and assign then to the dataframe. Then create a loop to go through the document to collect the necessary data and append the data to a dataframe. In this video, you learned: How to recognize different file types How to use Python libraries to extract data How to use dataframes when collecting data

---

### 11. [READING] Module 5 Summary: APIs and Data Collection Reading • 5 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/0dLP3/module-5-summary-apis-and-data-collection
- **Method:** `dom_reading_cml` | **Length:** 4529 chars

Congratulations! You have completed this module. At this point, you know that:

- Simple APIs in Python are application programming interfaces that provide straightforward and easy-to-use methods for interacting with services, libraries, or data, often with minimal configuration or complexity. - An API lets two pieces of software talk to each other. - Using an API library in Python entails importing the library, calling its functions or methods to make HTTP requests, and parsing the responses to access data or services provided by the API. - Pandas API processes the data by communicating with the other software components. - An Instance forms when you create a dictionary and then use the DataFrames constructor to create a Pandas object. - Method “head()” will display the mentioned number of rows from the top (default 5) of DataFrames, while method “mean()” will calculate the mean and return the values
- Rest APIs allow you to communicate through the internet, taking advantage of resources like storage, access more data, AI algorithms, and so on. - HTTP methods transmit data over the internet. - An HTTP message typically includes a JSON file with instructions for operations. - HTTP messages containing JSON files are returned to the client as a response from web services. - Dealing with time series data involves using the Pandas time series function. - You can get data for daily candlesticks and plot the chart using Plotly with the candlestick plot.
- The HTTP (HyperText Transfer Protocol) transfers data, including web pages and resources, between a client (a web browser) and a server on the World Wide Web. - The HTTP protocol is commonly used for implementing various types of REST APIs. - An HTTP response includes information like the type of resource, length of resource, and so on - Uniform resource locator (URL) is the most popular way to find resources on the web. - URL is divided into three parts: scheme, internet address or base URL, and route - The GET method is one of the popular methods of requesting information. Some other methods may also include the body. - Response method contains the version and body of the response. - POST submits data to the server, PUT updates data already on the server, DELETE deletes data from the server
- Requests is a Python library that allows you to send HTTP/1.1 requests easily - You can modify the results of your query with the GET method. - You can obtain multiple requests from a URL like name, ID, and so on with a Query string.
- Web scraping in Python involves extracting and parsing data from websites to gather information for various applications, using libraries like Beautiful Soup and requests. - HTML comprises text surrounded by blue text elements enclosed in angular brackets called tags. - You can select an HTML element on a web page to inspect the webpage. - Web pages may also contain CSS and JavaScript along with HTML elements. - Each HTML document is like an HTML Tree, which may contain strings and other tags. - Each HTML table is comprised of table tags and is structured with elements such as rows, headers, body and so on.
- Tabular data can also be extracted from web pages using the `read_html` method in Pandas.
- Beautiful Soup in Python is a library for parsing and navigating HTML and XML documents, making extracting, and manipulating data from web pages more accessible.
- To parse a document, pass it through the Beautiful Soup constructor to get a beautiful soup object representing the document as a nested data structure.
- Beautiful soup represents HTML as a set of tree-like objects with methods to parse the HTML.
- Navigable string is like a Python string that supports beautiful soup functionality.
- find_all is a method used to extract content based on the tag’s name, its attributes, the text of a string, or some combination of these.
- The find_all method looks through a tag’s descendants and retrieves all descendants that match your filters.
- The result is a Python iterable like a list.
- File formats refer to the specific structure and encoding rules used to store and represent data in files, such as .txt for plain text or .csv for comma-separated values.
- Python works with different file formats such as CSV, XML, JSON, xlsx, and so on
- The extension of a file name will let you know what type of file it is and what it needs to open with.
- To access data from CSV files, we can use Python libraries such as Pandas.
- Similarly, different methods help parse JSON, XML, and other files.

---

### 12. [READING] Cheat Sheet: APIs and Data Collection Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/xbkcN/cheat-sheet-apis-and-data-collection
- **Method:** `dom_reading_cml` | **Length:** 9478 chars

Use this cheat sheet for various packages/methods, their descriptions, and examples.

### Accessing element attribute

Access the value of a specific attribute of an HTML element.

Syntax:

1attribute = element[(attribute)]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1href = link_element[(href)]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### BeautifulSoup()

Parse the HTML content of a web page using BeautifulSoup. The parser type can vary based on the project.

Syntax:

1soup = BeautifulSoup(html, (html.parser))Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1html = (https://api.example.com/data) soup = BeautifulSoup(html, (html.parser))Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### delete()

Send a DELETE request to remove data or a resource from the server. DELETE requests delete a specified resource on the server.

Syntax:

1response = requests.delete(url)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1response = requests.delete((https://api.example.com/delete))Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### find()

Find the first HTML element that matches the specified tag and attributes.

Syntax:

1element = soup.find(tag, attrs)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1first_link = soup.find((a), {(class): (link)})Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### find_all()

Find all HTML elements that match the specified tag and attributes.

Syntax:

1elements = soup.find_all(tag, attrs)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1all_links = soup.find_all((a), {(class): (link)})</td>Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### findChildren()

Find all child elements of an HTML element.

Syntax:

1children = element.findChildren()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1child_elements = parent_div.findChildren()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### get()

Perform a GET request to retrieve data from a specified URL. GET requests are typically used for reading data from an API. The response variable will contain the server's response, which you can process further.

Syntax:

1response = requests.get(url)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1response = requests.get((https://api.example.com/data))Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Headers

Include custom headers in the request. Headers can provide additional information to the server, such as authentication tokens or content types.

Syntax:

1headers = {(HeaderName): (Value)}Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1base_url = (https://api.example.com/data) headers = {(Authorization): (Bearer YOUR_TOKEN)} response = requests.get(base_url, headers=headers)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Import Libraries

Import the necessary Python libraries for web scraping.

Syntax:

1from bs4 import BeautifulSoupInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### json()

Parse JSON data from the response. This extracts and works with the data returned by the API. The response.json() method converts the JSON response into a Python data structure, usually a dictionary or list.

Syntax:

1data = response.json()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

12response = requests.get((https://api.example.com/data)) data = response.json()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### next_sibling()

Find the next sibling element in the DOM.

Syntax:

1sibling = element.find_next_sibling()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1next_sibling = current_element.find_next_sibling()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### parent

Access the parent element in the Document Object Model (DOM).

Syntax:

1parent = element.parentInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1parent_div = paragraph.parentInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### post()

Send a POST request to a specified URL with data. Create or update POST requests using resources on the server. The data parameter contains the data to send to the server, often in JSON format.

Syntax:

1response = requests.post(url, data)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1response = requests.post((https://api.example.com/submit), data={(key): (value)})Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### put()

Send a PUT request to update data on the server. PUT requests are used to update an existing resource on the server with the data provided in the data parameter, typically in JSON format.

Syntax:

1response = requests.put(url, data)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1response = requests.put((https://api.example.com/update), data={(key): (value)})Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Query parameters

Pass query parameters in the URL to filter or customize the request. Query parameters specify conditions or limits for the requested data.

Syntax:

1params = {(param_name): (value)}Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

123base_url = "https://api.example.com/data"params = {"page": 1, "per_page": 10}response = requests.get(base_url, params=params)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### select()

Select HTML elements from the parsed HTML using a CSS selector.

Syntax:

1element = soup.select(selector)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1titles = soup.select((h1))Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### status_code

Check the HTTP status code of the response. The HTTP status code indicates the result of the request (success, error, redirection). It can be used for error handling and decision-making in your code.

Syntax:

1response.status_codeInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

123url = "https://api.example.com/data"response = requests.get(url)status_code = response.status_codeInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### tags for find() and find_all()

Specify any valid HTML tag as the tag parameter to search for elements of that type. Here are some common HTML tags that you can use with the tag parameter.

Tag examples:

12345678910- (a): Find anchor () tags.- (p): Find paragraph ((p)) tags.- (h1), (h2), (h3), (h4), (h5), (h6): Find heading tags from level 1 to 6 ( (h1),n (h2)).- (table): Find table () tags.- (tr): Find table row () tags.- (td): Find table cell ((td)) tags.- (th): Find table header cell ((td))tags.- (img): Find image ((img)) tags.- (form): Find form ((form)) tags.- (button): Find button ((button)) tags.Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### text

Retrieve the text content of an HTML element.

Syntax:

1text = element.textInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1title_text = title_element.textInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.

---

### 13. [READING] Module 5 Glossary: APIs and Data Collection Reading • 5 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/Btu33/module-5-glossary-apis-and-data-collection
- **Method:** `dom_reading_cml` | **Length:** 9175 chars

Welcome! This alphabetized glossary contains many of the terms you'll find within this course. This comprehensive glossary also includes additional industry-recognized terms not used in course videos. These terms are important for you to recognize when working in the industry, participating in user groups, and participating in other certificate programs.

| Term | Definition |
| --- | --- |
| API Key | An API key in Python is a secure access token or code used to authenticate and authorize access to an API or web service, enabling the user to make authenticated requests. |
| APIs | APIs (Application Programming Interfaces) are a set of rules and protocols that enable different software applications to communicate and interact, facilitating the exchange of data and functionality. |
| Audio file | An audio file is a digital recording or representation of sound, often stored in formats like MP3, WAV, or FLAC, allowing playback and storage of audio content. |
| Authorize | In Python, "authorize" often means granting permission or access to a user or system to perform specific actions or access particular resources, often related to authentication and authorization mechanisms. |
| Beautiful Soup Objects | Beautiful Soup objects in Python are representations of parsed HTML or XML documents, allowing easy navigation, searching, and manipulation of the document’s elements and data. |
| Bitcoin currency | Bitcoin is a decentralized digital currency that operates without a central authority, allowing peer-to-peer transactions on a blockchain network. |
| Browser | A browser is a software application that enables users to access and interact with web content, displaying websites and web applications. |
| Candlestick plot | A candlestick plot in Python visually represents stock price movements over time, using rectangles to illustrate the open, close, high, and low prices for a given period. |
| Client/Wrapper | A client or wrapper in Python is a software component that simplifies interaction with external services or APIs, encapsulating communication and providing higher-level functionality for developers. |
| CoinGecko API | The CoinGecko API is a web service that provides cryptocurrency market data and information, allowing developers to access real-time and historical data for various cryptocurrencies. |
| DELETE Method | The DELETE method in Python is an HTTP request method used to request the removal or deletion of a resource on a web server. |
| Endpoint | In Python, an "endpoint" refers to a specific URL or URI that a web service or API exposes to perform a particular function or access a resource. |
| File extension | A file extension is a suffix added to a filename to indicate the file's format or type, often used by operating systems and applications to determine how to handle the file. |
| find_all | In Python, find_all is a Beautiful Soup method used to search and extract all occurrences of a specified HTML or XML element, returning a list of matching elements. |
| GET method | The GET method in Python is an HTTP request method used to retrieve data from a web server by appending parameters to the URL. |
| HTML | HTML (Hypertext Markup Language) is the standard language for creating and structuring content on web pages, using tags to define the structure and presentation of documents. |
| HTML Anchor tags | HTML anchor tags in Python are used to create hyperlinks within web pages, linking to other web pages or resources using the <a> element with the href attribute. |
| HTML Tables | HTML tables in Python are used to organize and display data in a structured grid format on a web page, constructed with <table>, <tr>, <th>, and <td> elements. |
| HTML Tag | An HTML tag in Python is a specific code enclosed in angle brackets used to define elements within an HTML document, specifying how content should be presented or structured. |
| HTML Trees | HTML trees in Python refer to the hierarchical structure created when parsing an HTML document, representing its elements and their relationships, typically used for manipulation or extraction of data. |
| HTTP | HTTP (HyperText Transfer Protocol) is the foundation of data communication on the World Wide Web, used for transmitting and retrieving web content between clients and servers. |
| httplib | A library that provides a set of functions and classes to send and handle HTTP and HTTPS requests. |
| Identify | In Python, "identify" usually means determining if two variables or objects refer to the same memory location, which can be checked using the is operator. |
| Instance | In Python, an "instance" typically refers to a specific occurrence of an object or class, created from a class blueprint, with its own unique set of data and attributes. |
| JSON file | A JSON (JavaScript Object Notation) file is a lightweight data interchange format that stores structured data in a human-readable text format, commonly used for configuration, data exchange, and web APIs. |
| Mean value | The mean value in Python is the average of a set of numerical values, calculated by adding all values and dividing by the total number of values. |
| Navigable string | In Python, a Navigable String is a Beautiful Soup object representing a string within an HTML or XML document, allowing for navigation and manipulation of the text content. |
| Plotly | Plotly is a Python library for creating interactive and visually appealing web-based data visualizations and dashboards. |
| PNG file | A PNG (Portable Network Graphics) file is a lossless image format in Python that is commonly used for high-quality graphics with support for transparency and compression. |
| POST method | The POST method in Python is an HTTP request method used to send data to a web server, often used for submitting form data and creating or updating resources. |
| Post request | A POST request in Python is an HTTP method used to send data to a web server for the purpose of creating or updating a resource, typically used in web applications and APIs. |
| PUT method | The PUT method in Python is an HTTP request method used to update an existing resource on a web server by replacing or modifying it. |
| Py-Coin-Gecko | Py-Coin-Gecko is a Python library that provides a convenient interface for accessing cryptocurrency data and information from the CoinGecko API. |
| Python iterable | A Python iterable is an object that can be looped over, typically used in for loops, and includes data structures like lists, tuples, and dictionaries. |
| Query string | A query string in Python is a part of a URL that contains data or parameters to be sent to a web server, typically used in HTTP GET requests to retrieve specific information. |
| rb mode | In Python, "rb" mode is used when opening a file to read it in binary mode, allowing you to read and manipulate non-text files like images or binary data. |
| Resource | In Python, a "resource" typically refers to an external entity such as a file, database connection, or network object that can be managed and manipulated within a program. |
| Rest API | A REST API in Python is a web-based interface that follows the principles of Representational State Transfer (REST), allowing communication and data exchange over HTTP using standard HTTP methods and data formats. |
| Service instance | In Python, a "service instance" typically refers to an instantiated object or entity representing a service, enabling interaction with that service in a program or application. |
| Timestamp | A timestamp is a representation of a specific moment in time, often expressed as a combination of date and time, used for record-keeping and data tracking. |
| Transcribe | "Transcribe" typically means converting spoken language or audio into written text, often using automatic speech recognition (ASR) technology. |
| Unix timestamp | A UNIX timestamp is a numerical value representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC, used for time-keeping in Unix-based systems and programming. |
| url (Uniform Resource Locator) | In Python, a URL (Uniform Resource Locator) is a web address that specifies the location of a resource on the internet, typically consisting of a protocol, domain, and path. |
| urllib | The "urllib" library in Python is used for working with URLs and making HTTP requests, including functions for fetching web content, handling cookies, and more. |
| Web service | Web services in Python are software components that allow applications to communicate over the internet by sending and receiving data in a standardized format, typically using protocols like HTTP or XML. |
| Web scraping | Web scraping in Python is the process of extracting data from websites by parsing and analyzing their HTML structure, often done with libraries like BeautifulSoup or Scrapy. |
| xlsx | An XLSX file is a file format used for storing spreadsheet data in Excel, containing worksheets, cells, and formulas in a structured manner. |
| xml | XML (Extensible Markup Language) is a text-based format for storing and structuring data using tags, often used for data interchange and configuration files. |

---

### 14. [READING] Congratulations and Next Steps Reading • 2 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/ipX1s/congratulations-and-next-steps
- **Method:** `dom_reading_cml` | **Length:** 1449 chars

Congratulations on completing this course. We hope you enjoyed it.

As a next step, you can take the appropriate follow-on Python Project from the list below to apply your new found skills in a real-world scenario.

- Python Project for Data Science
- Python Project for Data Engineering
- Developing AI Applications with Python and Flask

Note: Successful completion of this course is a pre-requisite for these Python Project courses.

You can explore the courses below to further hone and develop your skills for working with Data and Python:

- Databases and SQL for Data Science with Python

If you are looking to start a career in Data Science, Data Engineering or AI & Application Development, note that this course is part of the following Professional Certificates which are designed to empower you with the skills to become job-ready in these fields.

- IBM Applied AI Professional Certificate
- IBM Data Analyst Professional Certificate
- IBM Data Science Professional Certificate
- IBM Data Engineering Professional Certificate
- IBM Full Stack Software Developer Professional Certificate
- IBM DevOps and Software Engineering Professional Certificate
- IBM Back-End Development Professional Certificate
- Applied Software Engineering Fundamentals Specialization
- Data Science Fundamentals with Python and SQL Specialization
- Applied Data Science Specialization

We encourage you to leave your feedback and rate this course.

Good luck!

---

### 15. [READING] Python Cheat Sheet: The Basics Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/BpYo7/python-cheat-sheet-the-basics
- **Method:** `dom_reading_cml` | **Length:** 161 chars

Congratulations on finishing the course, here is a cheat sheet you can download summarizing everything you have learned over this course.

Click here to download

---
