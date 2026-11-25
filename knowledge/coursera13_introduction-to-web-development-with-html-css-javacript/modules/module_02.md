# Module 2: HTML Overview

### 1. [VIDEO TRANSCRIPT] Introduction to HTML Video • 4 min
- **URL:** https://www.coursera.org/learn/introduction-to-web-development-with-html-css-javacript/lecture/Ph2f7/introduction-to-html
- **Method:** `dom_transcript` | **Length:** 2876 chars

Welcome to Introduction to HTML. After watching this video, you will be able to explain what Hyper Text Markup Language (HTML) and HTML5 is, and  list the objectives of HTML5. The core HTML specification includes this background information. HTML stands for Hypertext Markup Language, which can be thought of as “the language of the Internet.” It is a markup language that was originally designed for sharing scientific documents. Adaptations to HTML over the years made it suitable to describe a number of other types of documents that can be displayed as web pages on the Internet. HTML Elements are the building blocks of an HTML page.

The pieces of content that form the page are assigned labels such as “paragraph,” “list,” and “table”. They are represented by tags. Browsers do not display the tags but use them to render the content. HTML has been in continuous evolution since it was introduced to the Internet in the early 1990s by CERN: The European Organization for Nuclear Research and the IETF: Internet Engineering Task Force. The World Wide Web Consortium (W3C) made a number of recommendations to the HTML standards over the years. New features were continually added, and specifications changed over time. Initially, the Web Hypertext Application Technology Working Group (WHATWG) worked on recommendations independently.

Then, in 2007, W3C formed a working group chartered to work with the WHATWG on the development of the HTML5 specification. The W3C published the specification under the W3C copyright, while a version with a less restrictive license was kept on the WHATWG site. Since 2007, both the W3C and WHATWG groups worked together on the development of the HTML5 standard. The HTML5 specification, as drafted by W3C, includes the following objectives: The HTML5 specification defines a single language called HTML5 that can be written in HTML or XML syntax. The HTML5 specification defines a processing model that can interoperate with earlier HTML implementations. HTML5 improves the markup for documents. HTML5 includes markup and APIs for idioms, such as web storage, video, and audio content.

When speaking about about creating web pages, developers may use the terms HTML and HTML5 interchangeably. In general, the term HTML implies HTML5. Use the full term HTML5 if you need to differentiate between versions, such as when discussing features new to HTML5. In this course, HTML refers to HTML5, unless specified otherwise. In this video, you learned: HTML stands for HyperText Markup Language, a markup language that enables documents to be displayed as web pages on the Internet. Tags represent the elements of an HTML page like paragraphs, lists, and tables. HTML5, the latest version, supports pages written in HTML or XML syntax, interoperation with earlier HTML versions, and markup and APIs for web storage, video, and audio content.

---

### 2. [VIDEO TRANSCRIPT] HTML Features Video • 6 min
- **URL:** https://www.coursera.org/learn/introduction-to-web-development-with-html-css-javacript/lecture/BqDxO/html-features
- **Method:** `dom_transcript` | **Length:** 4408 chars

(Music) Hello and welcome to HTML Features. After watching this video, you will be able to list some of the features of HTML5, describe the Document Object Model or DOM tree, explain when you would use XML and when you would use HTML. So, what are some HTML5 features? It provides the means to categorize web pages into different sections, and includes tools for effective data management, drawing, video, and audio. Facilitates the development of cross-browser applications for the web and portable devices. Allows greater flexibility, permitting the development of exciting and interactive websites. Helps to create a more engaging user experience. Pages that are designed by using HTML5 can provide an experience similar to desktop applications.

Allows for enhanced, multiple-platform development by combining the capability of an application programming interface (API). By using HTML5, developers can create a modern application experience that is uniform across platforms and devices. Here is an example of a document that conforms to the syntax of HTML5. Documents that have the text or html media type are parsed using HTML rules. If a document is transmitted with an HTML content type, such as text or html, it is processed as an HTML document by web browsers. This example uses the following elements: The !DOCTYPE is a declaration tag that represents the document type.

The !DOCTYPE declaration is not an HTML tag; it is an instruction to the web browser about what version of HTML the page is written in. Although this declaration is not required, it should be the first line of the HTML code if the developer decides to include it. The html tag is the root element of this tree. It contains all of the other HTML elements, except the !doctype tag. This example, contains two elements: head and body.

The head tag contains a title tag, which contains the text “Sample page” in the example. The head element can contain the following tags: title, scripts, style, style sheet links, meta information, browser support information and other initialization functions. Finally, the body tag contains all content that is displayed on the webpage. HTML user agents, commonly known as browsers, parse the markup, turning it into a DOM (Document Object Model) tree. A DOM tree is an in-memory representation of a document. DOM trees contain several kinds of nodes, which include a DOCTYPE node, elements such as headers and paragraphs, text nodes, and comment nodes. Here is an example of a document that conforms to the XML syntax of HTML5.

Extensible Markup Language (XML) documents look similar to HTML documents, except they have an XML tag on the first line. In addition, with XML documents, the Content-type must be specified as an XML media type such as application or xml. When a document is transmitted with an XML content type, it is treated as an XML document by a web browser and an XML processor parses the document. How do you decide whether to use HTML or XHTML for developing web pages? Which of the two options you choose is related to how you intend to use the application. For instance, are you using XSLT (Extensible Style Sheet Language Transformations) to create other documents and resources from your web pages? People are equally divided about whether to use XHTML or HTML.

Both HTML and XHTML use the same semantic or tags. However, XHTML tags all need to be in lowercase, while the case used does not matter in HTML. In addition, XHTML must be well-formed. Every element must have an end tag. All attributes must have a value and double or single quotation marks must surround all attribute values. If an XML parser encounters a situation where the syntax is not well-formed, it stops processing. In HTML, different case, unmatched quotation marks, and non-terminated and uncontained elements are allowed and commonplace.

In this regard, HTML syntax is less rigorous than XHTML syntax. In this video, you learned that HTML5 includes features for categorizing sections of web pages, and managing data, video and audio tools. Enables you to develop a single, cross-browser application for the web and portable devices. and helps you to create a more engaging user experience. The DOM tree is an in-memory representation of a document. DOM trees contain nodes, which define the type of document and its structure, such as headers and paragraphs, text nodes, and comment nodes.

---

### 3. [VIDEO TRANSCRIPT] HTML Management and Support Video • 3 min
- **URL:** https://www.coursera.org/learn/introduction-to-web-development-with-html-css-javacript/lecture/WkGyH/html-management-and-support
- **Method:** `dom_transcript` | **Length:** 2942 chars

Hello and welcome to HTML Management and Support! After watching this video, you will be able to list some HTML document API properties and methods, describe how scripting is enabled in browsers, describe browser support for HTML5 features. So, let’s examine some of the key themes of the HTML5 specification. The syntax it defines is compatible with HTML4 and XHTML1 documents. HTML5 is defined in a way that it is compatible with earlier versions in the way browsers handle deployed content. It separates conformance requirements for user agents and authors. In other words, how browsers treat HTML5 code and how page authors treat HTML5 code is different.

For user agents, HTML5 is defined in a way that supports elements and attributes of the earlier specifications. For authors, several elements and attributes have been removed in order to simplify the language. HTML5 includes some elements and application programming interfaces that help in the creation of web applications. Examples include video and audio elements, and an API that supports the creation of offline applications. What do you think makes HTML suitable for creating web applications? There are a number of possible reasons: The range of devices that all have built-in browsers that support HTML5 features. The number of APIs that enhance the user experience, such as the advanced animation, drawings, audio, and video elements.

The efficient use of HTML and CSS, while reducing the number of images, can lead to faster load times for rendering web pages. Search engine optimizations can use keywords that are taken from HTML attributes to improve the visibility of a website when search results are displayed. The meta tags shown are used to provide information to search engines. Here are some examples of elements in HTML5. New structural elements are part of the HTML5 specification. These markup elements help you to logically define the page structure. New APIs such as canvas, audio, and video help with graphics and embedded content.

New attributes were added to the input element attributes. Examples include the email, datetime, and number types. The browser automatically validates the input field according to the input attribute, without the need for custom validation scripts. By using web storage APIs, you can store data in the browser. The web workers feature can be used for non-interactive processing. Web workers provide a way to run processing-intensive tasks without blocking the user interactions to the current page. In this video, you learned about HTML5 Themes, which provide: Syntax compatible with HTML4 and XHTML1, and new and refined APIs for video and audio elements, offline web apps, and drag and drop.

About HTML5 Web Applications, which have: Improved search indexing with meta tags, better page load times, enhanced user experience, and about HTML5 Elements, which enable you to define and manage web page structure and content.

---

### 4. [VIDEO TRANSCRIPT] HTML Scripting Video • 5 min
- **URL:** https://www.coursera.org/learn/introduction-to-web-development-with-html-css-javacript/lecture/MN10o/html-scripting
- **Method:** `dom_transcript` | **Length:** 4005 chars

Welcome to HTML Scripting. After watching this video, you will be able to define scripting, explain how browsers enable scripting, and identify DOM tree accessors. The use of scripting within a website, often through the use of JavaScript, can be done directly within your HTML code within the `script` tag, or within a separate file which is called in your HTML code. Scripting provides a more interactive user experience when browsing websites. It can be used for various tasks, such as form validation, dynamically changing the content of a website, and manipulating images. Since scripting can be turned off, the recommendation is to use scripting but not to rely on it. Scripting is enabled for a browser context when the conditions shown on the slide are true.

The browser in use supports scripting and the user has scripting enabled. HTML5 also defines a sandboxed media type which specifies an extra set of content restrictions and can be used when hosting untrusted content. This sandboxed browsing context can be set at the page level or specified as an attribute for embedded objects. Running a page that contains an embedded object without the sandbox attribute grants the embedded object the same permissions as the rest of your page. This implicitly gives a third-party vendors permission to run scripts with the same permissions that you have for that page, which is one way that you can inadvertently allow advertisements to occur in your application. So, to prevent granting implicit permissions to embedded objects, use the sandbox attribute on any tag that contains an embedded object. Each HTML document that is loaded into a browser page becomes a Document object.

The Document object provides access to all HTML elements in a page and can be accessed from within a script. The DOM tree accessors are HTML document APIs that provide access to all the HTML elements on a page. The property to access is prefixed by the word document. For example, document.head returns the first head element that is a child of the html element, if there is one, otherwise null. The function document.images returns an HTMLCollection of the image elements in the document. The function document.scripts returns an HTMLCollection of the script elements in the document. Here are some common HTML DOM tree methods: The document.getElementById(‘id’) function has one required parameter which is the id of the element you want to access.

The id is specified as an attribute on one of the elements that is coded elsewhere on the page. The document.getElementsByTagName(‘tag’) function has one required parameter which is the tag name of the element you want to access. This function returns a nodelist of all the elements with the tag that matches the required parameter. This is a fragment of HTML with JavaScript code that uses the document API. When Submit is clicked inside the page that is running in a web browser, the textChecker function begins. The document.getElementById(‘textField1’) retrieves the contents of what was typed into the input field that has the id of textField1 and places this content into a variable. The JavaScript logic then tests whether any data was typed into the field, and an alert dialog is displayed with the result.

A similar function will be used later in Exercise 1. Here is the output from running the code on the previous page that uses the document API. The user types “Test” in the input field and clicks Submit. The result is seen in an alert dialog box on the same page. In this video, you learned scripting is used to provide a more interactive user experience when browsing websites. Since scripting can be turned off, the recommendation is to use scripting but not to rely on it. Scripting is enabled when certain browser conditions are met.

HTML5 sandboxes enable you to manage iframe mash-ups; web pages that pull content from more than one site. HTML documents loaded into a browser page become Document objects, which you can access through scripts.

---

### 5. [VIDEO TRANSCRIPT] HTML5 Browser Support Video • 4 min
- **URL:** https://www.coursera.org/learn/introduction-to-web-development-with-html-css-javacript/lecture/CGwAf/html5-browser-support
- **Method:** `dom_transcript` | **Length:** 3304 chars

Welcome to HTML5 Browser Support. After watching this video, you will be able to explain how browsers support HTML5 features, list which browsers support which HTML5 features, and define browser support table. Not all browsers fully support all the features that are described in the HTML5 and CSS3 specifications. For example, older versions of browsers do not support certain features. The developers of different browsers are continually adding support for HTML5 features to their new browser versions. For the most comprehensive support of HTML5 features, consider using Google Chrome. Support tables show which features are supported by which browsers and can be a useful tool when developing web pages.

For example, caniuse.com has great support tables for HTML5, CSS3, etc. Here are the results of displaying the input type=‘date’ element in different browsers. The Google Chrome browser displays a calendar to enter the data. The Microsoft Edge browser displays spinning boxes to enter the data. Notice the difference in date formats (yyyy-mm-dd vs mm/dd/yyyy). The Firefox browser displays the date field as a text field. This could raise several issues regarding input format and validation.

This example shows a support table for the input type=‘date’ element. The numbers represent the browser version. The color determines the level of support. Green: Full support. Olive: Partial support. Red: No support. Edge, Chrome, and Opera browsers are green, meaning they support the input type=‘date’ element.

Internet Explorer and Safari browsers are red, meaning they do not support the input type=‘date’ element. Support levels change as developers of browsers add new features, so check back frequently to see if the features you require are supported. You can also use JavaScript to check whether a certain HTML5 element is supported by a browser. First, create a DOM element by typing document.createElement() and include the element type as a parameter argument. As a result, the DOM object gets created. If the browser does not support that element, the DOM object that gets created has a set of common properties, but nothing specific for that element. You then test for a known property or method on the DOM object that you created.

If that property or method does not exist, then the browser does not yet fully support the DOM element (or the HTML5 tag) that has been created. Browsers that do not support the element can revert to a fallback or default behavior such as displaying the field as a regular text field. Here is an example of using JavaScript to check whether a certain HTML5 element is supported by a browser. This code is used to test whether the browser supports the element input type=‘date’ / In the example, you dynamically create the DOM object for the input element, and then you set the type attribute to the value of "date.“ If the browser does not support the input type=date, the field is displayed in the browser as a regular text field. In this video, you learned not all browsers fully support all the features that are described in the HTML5 and CSS3 specifications, caniuse.com has good support tables that show what features are supported by which browsers, and you can use JavaScript to check whether a certain HTML5 element is supported by a browser.

---

### 6. [VIDEO TRANSCRIPT] Insiders' Viewpoints: Working with HTML and CSS Video • 2 min
- **URL:** https://www.coursera.org/learn/introduction-to-web-development-with-html-css-javacript/lecture/sqq3B/insiders-viewpoints-working-with-html-and-css
- **Method:** `dom_transcript` | **Length:** 2112 chars

Welcome to Insiders’ Viewpoints: Working with HTML and CSS. In this video, we will listen to several professionals discuss their experience working with hypertext markup language (HTML) and cascading style sheets (CSS). A typical challenge when writing in CSS, and when you are kind of new at it, is it can be hard to enter an element perfectly in a space, whether it be the whole page or within a box, can be hard to center things really nicely, and might just be off a little bit. And for that, it was really helpful to learn Flexbox. So I encourage you to give that a shot and understand that and be comfortable with Flexbox. While working with HTML and CSS, sometimes the main challenge is finding the errors or bugs in your code. It is important to validate your code frequently.

You can use an online HTML and CSS validation service to make sure that the code is properly formatted, and there is no missing parenthesis, incorrect property names, etc. To find out any CSS errors, you can also use developer tools in the browser. Another challenge is testing the code on different browsers. Some of the old browsers do not support modern HTML features. Once you have decided on the technologies you would be using, it is a good idea to research the browsers that would support these features. You should also add fallback mechanisms to your HTML code for browsers not supporting the new features. For example, if you're using HTML5 video, you can add a link to download video as a fallback option for browsers that don't support the HTML5 video player.

My answer is going to focus on CSS since it is far more complex than HTML. In my opinion, it’s unthinkable to tackle cross platform CSS without using a framework. So, the challenge is how do you pick your framework and here are some ideas. Bootstrap is one of the most popular, it has powerful cross browser capabilities. There is Foundation. It has a significant learning curve. There's the materialized framework from Google, which has an optimized feature set that many developers value.

There's also UI kit which is most popular in iOS development.

---

### 7. [READING] Module 1 Summary: HTML Overview Reading • 2 min
- **URL:** https://www.coursera.org/learn/introduction-to-web-development-with-html-css-javacript/supplement/Jn4Cw/module-1-summary-html-overview
- **Method:** `dom_reading_cml` | **Length:** 866 chars

In this module, you learned that:

- HTML provides the basic structure and content for a website using tags.
- Tags represent the elements of an HTML page.
- The HTML DOM Tree describes how a website is structured.
- HTML uses APIs to enhance the user experience, providing features for advanced animation, audio, and video.
- Scripting provides a more interactive user experience when browsing websites.
- It is recommended to not rely on scripting as it can be disabled.
- HTML5 sandboxes help manage iframe mashups.
- HTML5 Browser Support Tables describe which browsers support which HTML5 features.
- JavaScript is used to check if an element is supported by a browser.
- CSS provides consistent style and design throughout the website.
- There are multiple CSS layout approaches used to design websites, including fluid, fixed, flexbox, and grid-based layouts.

---
