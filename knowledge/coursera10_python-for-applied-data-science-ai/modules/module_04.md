# Module 4: Working with Data in Python

### 1. [VIDEO TRANSCRIPT] Reading Files with Open Video • 3 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/78ZHl/reading-files-with-open
- **Method:** `dom_transcript` | **Length:** 3273 chars

In this section, we will use Python's built-in open function to create a file object and obtain the data from a txt file. We will use Python's open function to get a file object. We can apply a method to that object to read data from the file. We can open the file Example1.txt as follows. We use the open function. The first argument is the file path. This is made up of the file name and the file directory.

The second parameter is the mode. Common values used include r for reading, w for writing, and a for appending. We will use r for reading. Finally, we have the file object. We can now use the file object to obtain information about the file. We can use the data attribute name to get the name of the file. The result is a string that contains the name of the file.

We can see what mode the object is in using the data attribute mode, and r is shown representing read. You should always close the file object using the method close. This may get tedious sometimes, so let's use the with statement. Using a with statement to open the file is better practice because it automatically closes the file. The code will run everything in the indent block, then closes the file. This code reads the file Example1.txt. We can use the file object file1.

The code will perform all operations in the indent block, then close the file at the end of the indent. The method read stores the values of the file in the variable file underscore stuff as a string. You can print the file content. You can check if the file content is closed, but you cannot read from it outside the indent. But you can print the file content outside the indent as well. We can print the file content. We will see the following.

When we examine the raw string, we will see the slash n. This is so Python knows to start a new line. We can output every line as an element in a list using the method readlines. The first line corresponds to the first element in the list. The second line corresponds to the second element in the list, and so on. We can use the method readline to read the first line of the file. If we run this command, it will store the first line in the variable file underscore stuff, then print the first line.

We can use the method readline twice. The first time is called. It will save the first line in the variable file underscore stuff, and then print the first line. The second time it's called, it will save the second line in the variable file underscore stuff, and then print the second line. We can use a loop to print out each line individually as follows. Let's represent every character in a string as a grid. We can specify the number of characters we would like to read from a string as an argument to the method readlines.

When we use a four as an argument in the method readlines, we print out the first four characters in the file. Each time we call the method, we will progress through the text. If we call the method with the argument 16, the first 16 characters are printed out and then the new line. If we call the method a second time, the next five characters are printed out. Finally, if we call the method the last time with the argument 9, the last nine characters are printed out. Check out the labs for more examples of methods and other file types.

---

### 2. [READING] Reading Files with Open Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/MaYmK/reading-files-with-open
- **Method:** `dom_reading_cml` | **Length:** 10451 chars

File handling is an essential aspect of programming, and Python provides built-in functions to interact with files. This guide will explore how to use Python's open function to read the text files ('.txt' files).

## Objectives

By the end of this reading, you'll learn about:

- Describe how to use the open() and read() Python functions to open and read the contents of a text file
- Explain how to use the with statement in Python
- Describe how to use the readline() function in Python
- Explain how to use the seek() function to read specific character(s) in a text file

## Introduction

Reading text files involves extracting and processing the data stored within them. Text files can have various structures, and how you read them depends on their format. Here's a general guide on reading text files with different structures.

### Plain text files

- Plain text files contain unformatted text without any specific structure
- You can read plain text files line by line or load all the content into your memory

## Opening the file

There are two methods for opening the file using the file handling concept.

### 1. Using Python's open function

Suppose we have a file named 'file.txt'.

Python's open function creates a file object and accesses the data within a text file. It takes two primary parameters:

- File path: The file path parameter consists of the filename and directory where the file is located.
- Mode: The mode parameter specifies the purpose of opening the file, such as 'r' for reading, 'w' for writing, or 'a' for appending.

12# Open the file in read ('r') modefile = open('file.txt', 'r')Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.open('file.txt', 'r'): This line opens a file named 'file.txt' in read mode ('r'). It returns a file object, which is stored in the variable file. The 'r' mode indicates that the file will be opened for reading.

### 2. Using 'with' statement

To simplify file handling and ensure proper closure of files, Python provides the "with" statement. It automatically closes the file when operations within the indented block are completed. This is considered best practice when working with files.

123# Open the file using 'with' in read ('r') modewith open('file.txt', 'r') as file:    # further codeInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Open the file using 'with' in read ('r') mode

with open('file.txt', 'r') as file: This line opens a file named 'file.txt' in read mode ('r') using the with statement, which is a context manager. The file is automatically closed when the code block inside the with statement exits.

## Advantages of using the with statement

The key advantages of using the 'with' statement are:

- Automatic resource management: The file is guaranteed to be closed when you exit the with block, even if an exception occurs during processing.
- Cleaner and more concise code: You don't need to explicitly call close(), making your code more readable and less error-prone.

Note: For most file reading and writing operations in Python, the 'with' statement is recommended.

## Let's perform a read operation on a file

### 1. Reading the entire content

You can read the entire content of a file using the read method, which stores the data as a string in a variable. This content can be printed or further manipulated as needed.

12345678910111213141516171819# Reading and Storing the Entire Content of a File # Using the read method, you can retrieve the complete content of a file# and store it as a string in a variable for further processing or display. # Step 1: Open the file you want to readwith open('file.txt', 'r') as file:     # Step 2: Use the read method to read the entire content of the file    file_stuff = file.read()     # Step 3: Now that the file content is stored in the variable 'file_stuff',    # you can manipulate or display it as needed.     # For example, let's print the content to the console:    print(file_stuff) # Step 4: The 'with' statement automatically closes the file when it's done,# ensuring proper resource management and preventing resource leaks.Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Step 1: Involves opening the file, specifying 'file.txt' as the file to be opened for reading ('r') mode using the with context manager.

Step 2: Utilizes the read() statement on the file object (file) to read the entire file. This content is then stored in the file_stuff variable.

Step 3: Explain that with the content now stored in file_stuff, you can perform various operations on it. In the example provided, the code prints the content to the console, but you can manipulate, analyze, search, or process the text data in file_stuff based on your specific needs.

Step 4: Emphasizes that the with block automatically closes the file when done, ensuring proper resource management and preventing resource leaks. This is a crucial aspect of using the with statement when working with files.

### 2. Reading the content line by line

Python provides methods to read files line by line:

- The 'readlines' method reads the file line by line and stores each line as an element in a list. The order of lines in the list corresponds to their order in the file.
- The 'readline' method reads individual lines from the file. It can be called multiple times to read subsequent lines.

In Python, the readline() method is like reading a book one line at a time. Imagine you have a big book and want to read it page by page. readline() helps you do just that with lines of text instead of pages.

#### Here's how it works:

Opening a file: First, you need to open the file you want to read using the open() function.

1file = open('file.txt', 'r')Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Reading line by line: Now, you can use readline() to read one line from the file at a time. It's like turning the pages of the book, but here, you're getting one sentence (or line) at each turn.

12line1 = file.readline()  # Reads the first lineline2 = file.readline()  # Reads the second lineInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Using the lines: You can do things with each line you read. For example, you can print it, check if it contains specific words, or save it somewhere else.

123print(line1)  # Print the first lineif 'important' in line2:    print('This line is important!')Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Looping through lines: Typically, you use a loop to read lines until no more lines are left. t's like reading the entire book, line by line.

12345while True:    line = file.readline()    if not line:        break  # Stop when there are no more lines to read    print(line)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Closing the book: When you're done reading, it's essential to close the file using file.close() to make sure you're not wasting resources.

1file.close()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.So, In simple terms, readline() helps you read a text file line by line, allowing you to work with each line of text as you go. It's like taking one sentence at a time from a book and doing something with it before moving on to the next sentence. Don't forget to close the book when you're done!

### 3. Reading specific characters

You can specify the number of characters to read using the readlines method. For example, reading the first four characters, the next five, and so on.

Reading specific characters from a text file in Python involves opening the file, navigating to the desired position, and then reading the characters you need. Here's a detailed explanation of how to read specific characters from a file:

#### Open the File

First, you need to open the file you want to read. Use the open() function with the appropriate file path and mode. For reading, use 'r' mode.

1file = open('file.txt', 'r')Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Navigate to the intended position (Optional)

If you want to read characters from a specific position in the file, you can use the seek() method. This method moves the file pointer (like a cursor) to a particular position. The position is specified in bytes, so you'll need to know the byte offset of the characters you want to read.

1file.seek(10)  # Move to the 11th byte (0-based index)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Read specific characters

To read specific characters, you can use the read() method with an argument that specifies the number of characters to read. It reads characters starting from the current position of the file pointer.

1characters = file.read(5)  # Read the next 5 charactersInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.In this example, it reads the next 5 characters from the current position of the file pointer.

#### Use the read characters

You can now use the characters variable to work with the specific characters you've read. You can print them, save them, manipulate them, or perform any other actions.

1print(characters)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Close the file

It's essential to close the file when you're done to free up system resources and ensure proper file handling.

1file.close()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Conclusion

In conclusion, this reading has provided a comprehensive overview of file handling in Python, with a focus on reading text files. File handling is a fundamental aspect of programming, and Python offers powerful built-in functions and methods to interact with files seamlessly.

---

### 3. [VIDEO TRANSCRIPT] Writing Files with Open Video • 2 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/2ijQE/writing-files-with-open
- **Method:** `dom_transcript` | **Length:** 2447 chars

We can also write to files using the open function. We will use Python's open function to get a file object to create a text file. We can apply method 'write' to write data to that file. As a result, text will be written to the file. We can create the file Example2.txt as follows. We use the 'open' function. The first argument is the file path.

This is made up of the file name (if you have that file in your directory, it will be overwritten,) and the file directory. We set the mode parameter to W for writing. Finally, we have the file object. As before, we use the 'with' statement. The code will run everything in the indent block, then close the file. We create the file object, File1. We use the open function.

This creates a file Example2.txt in your directory. We use the method write, to write data into the file. The argument is the text we would like input into the file. If we use the write method successively, each time it is called, it will write to the file. The first time it is called, we will write, "This is line A" with a slash-n to represent a new line. The second time we call the method, it will write, "This is line B" then it will close the file. We can write each element in a list to a file.

As before, we use a 'with' command and the open function to create a file. The list, Lines, has three elements consisting of text. We use a 'for' loop to read each element of the first lines and pass it to the variable line. The first iteration of the loop writes the first element of the list to the file Example2. The second iteration writes the second element of the list and so on. At the end of the loop, the file will be closed. We can set the mode to appended using a lowercase 'a'.

This will not create a new file, but just use the existing file. If we call the method write, it will just write to the existing file, then add "This is line C" then close the file. We can copy one file to a new file as follows. First, we read the file Example1 and interact with it via the file object, readfile. Then we create a new file Example3 and use the file object writefile to interact with it. The for loop takes a line from the file object, readfile, and stores it in the file Example3 using the file object, writefile. The first iteration copies the first line.

The second iteration copies the second line, till the end of the file is reached. Then both files are closed. Check out the labs for more examples. (Music)

---

### 4. [READING] Writing Files with Open Reading • 7 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/o3GEx/writing-files-with-open
- **Method:** `dom_reading_cml` | **Length:** 9023 chars

## Objectives

By the end of this reading, you'll learn about:

- Create and write data to a file in Python
- Write multiple lines of text to a file using lists and loops
- Add new information to an already existing file without erasing its content
- Compare and contrast the different file modes in Python, what they mean, and when to use them

## Writing to a file

You can create a new text file and write data to it using Python's open() function. The open() function takes two main arguments: the file path (including the file name) and the mode parameter, which specifies the operation you want to perform on the file. For writing, you should use the mode 'w' Here's an example:

12345# Create a new file Example2.txt for writingwith open('Example2.txt', 'w') as file1:    file1.write("This is line A\n")    file1.write("This is line B\n")    # file1 is automatically closed when the 'with' block exitsInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Line 2 explanation:

with open('Example2.txt', 'w') as file1

- We start by using the open function to open or create a file named Example2.txt for writing ('w' mode).
- The 'w' mode specifies that we intend to write data to the file.
- We use the with statement to ensure that the file is automatically closed when the code block exits. This helps manage resources efficiently.

### Line 3 explanation:

file1.write("This is line A\n")

- Here, we use the write() method on the file object, file1, to add the text This is line A to the file.
- The \n at the end represents a newline character, which starts a new line in the file.

### Line 4 explanation

file1.write("This is line" B\n")

- Similarly, we use the write() method again to add the text This is line B to the file on a new line.

## Writing multiple lines to a file using a list and loop

In Python, you can use a list to store multiple lines of text and then write these lines to a file using a loop. Here's an example code snippet that demonstrates this:

12345678# List of lines to write to the fileLines = ["This is line 1", "This is line 2", "This is line 3"] # Create a new file Example3.txt for writingwith open('Example3.txt', 'w') as file2:    for line in Lines:        file2.write(line + "\n")    # file2 is automatically closed when the 'with' block exitsInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Here's an explanation of the code:

- Line 2: We start by defining a list called Lines, which contains multiple lines of text that we want to write to the file. Each line is a string.
- Line 5: Next, we use the open() function to create a new text file named Example3.txt for writing, 'w' mode. The 'w' mode indicates that we intend to write data to the file.
- Line 6: We then enter a for loop to iterate through each element (line) in the Lines list.
- Line 7: Inside the loop, we use the write() method on the file object file2 to write the current line of text (line) to the file. We add \n at the end of each line to ensure that each line is followed by a newline character, which separates them in the file.
- Line 8: Finally, we add a comment indicating that the file file2 will be automatically closed when the code block within the with statement exits. Properly closing the file is essential for good resource management.

## Appending data to an existing file

In Python, you can use the 'a' mode when opening a file to append new data to an existing file without overwriting its contents. Here's an example code snippet that demonstrates this:

1234567# Data to append to the existing filenew_data = "This is line C" # Open an existing file Example2.txt for appendingwith open('Example2.txt', 'a') as file1:    file1.write(new_data + "\n")    # file1 is automatically closed when the 'with' block exitsInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Here's an explanation of the code:

- Line 2: We start by defining a variable new_data that contains the text we want to append to the existing file. In this case, it's the string This is line C.
- Line 5: Next, we use the open() function to open an existing file named Example2.txt for appending, 'a' mode. The 'a' mode indicates that we intend to append data to the file, and if the file doesn't exist, it will be created.
- Line 6: Within the with block, we use the write() method on the file object file1 to append the new_data to the file. We add "\n" at the end to ensure that the appended data starts on a new line, maintaining the file's readability.
- Finally, we add a comment indicating that the file file1 will automatically close when the code block within the with statement exits. Properly closing the file is essential for good resource management.

## Copying contents from one file to another

In Python, you can copy the contents of one file to another by reading from the source file and writing to the destination file. Here's an example code snippet that demonstrates this:

123456789# Open the source file for readingwith open('source.txt', 'r') as source_file:    # Open the destination file for writing    with open('destination.txt', 'w') as destination_file:        # Read lines from the source file and copy them to the destination file        for line in source_file:            destination_file.write(line)    # Destination file is automatically closed when the 'with' block exits# Source file is automatically closed when the 'with' block exitsInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Here's an explanation of the code:

- Line 2: We start by opening the source file, source.txt for reading, r mode, using the with statement and the open() function. This allows us to read data from the source file.
- Line 4: Inside the first with block, we open the destination file, destination.txt for writing, w mode, using another with statement and the open() function. This prepares the destination file for writing.
- Line 6: We use a for loop to iterate through each line in the source file source_file. This loop reads each line from the source file one by one.
- Line 7: Within the loop, we use the write() method to write each line from the source file to the destination file destination_file. This effectively copies the content of the source file to the destination file.
- Lines 8 and 9: After copying all the lines, both the source and destination files are automatically closed when their respective with blocks exit. Proper file closure is crucial for managing resources efficiently.

### File modes in Python (syntax and use cases)

The following table provides an overview of different file modes, their syntax, and common use cases. Understanding these modes is essential when working with files in Python for various data manipulation tasks.

| Mode | Syntax | Description |
| --- | --- | --- |
| ‘r’ | 'r' | Read mode. Opens an existing file for reading. Raises an error if the file doesn't exist. |
| ‘w’ | 'w' | Write mode. Creates a new file for writing. Overwrites the file if it already exists. |
| ‘a’ | 'a' | Append mode. Opens a file for appending data. Creates the file if it doesn't exist. |
| ‘x’ | 'x' | Exclusive creation mode. Creates a new file for writing but raises an error if the file already exists. |
| ‘rb’ | 'rb' | Read binary mode. Opens an existing binary file for reading. |
| ‘wb’ | 'wb' | Write binary mode. Creates a new binary file for writing. |
| ‘ab’ | 'ab' | Append binary mode. Opens a binary file for appending data. |
| ‘xb’ | 'xb' | Exclusive binary creation mode. Creates a new binary file for writing but raises an error if it already exists. |
| ‘rt’ | 'rt' | Read text mode. Opens an existing text file for reading. (Default for text files) |
| ‘wt’ | 'wt' | Write text mode. Creates a new text file for writing. (Default for text files) |
| ‘at’ | 'at' | Append text mode. Opens a text file for appending data. (Default for text files) |
| ‘xt’ | 'xt' | Exclusive text creation mode. Creates a new text file for writing but raises an error if it already exists. |
| ‘r+’ | 'r+' | Read and write mode. Opens an existing file for both reading and writing. |
| ‘w+’ | 'w+' | Write and read mode. Creates a new file for reading and writing. Overwrites the file if it already exists. |
| ‘a+’ | 'a+' | Append and read mode. Opens a file for both appending and reading. Creates the file if it doesn't exist. |
| ‘x+’ | 'x+' | Exclusive creation and read/write mode. Creates a new file for reading and writing but raises an error if it already exists. |

## Conclusion

Working with files is a fundamental aspect of programming, and Python provides powerful tools to perform various file operations. In this summary, we covered key concepts and code examples related to file handling in Python, including writing, appending, and copying files.

---

### 5. [VIDEO TRANSCRIPT] Pandas: Loading Data Video • 4 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/yBbKS/pandas-loading-data
- **Method:** `dom_transcript` | **Length:** 4092 chars

Dependencies or libraries are pre-written code to help solve problems. In this video, we will introduce Pandas, a popular library for data analysis. You can import the library or dependency, like Pandas, using the following command. Start with the import command followed by the name of the library. You now have access to a large number of pre-built classes and functions. This assumes the library is installed. In our lab environment, all the necessary libraries are installed.

Let us say we would like to load a csv file using pandas build-in function, readcsv. A csv is a typical file type used to store data. Simply type the word Pandas, then a dot, and the name of the function with all the inputs. Writing pandas all the time may get difficult, so you can use the 'as' statement to shorten the name of the library. In this case, use the standard abbreviation pd. Now type pd. Next type a dot followed by the name of the function you would like to use.

In this case, readcsv. You are not limited to the abbreviation pd. In this case, we use the term banana. However, we will stick with pd for the rest of this video. Let us examine this code in more detail. One way pandas allows you to work with data is in a DataFrame. Let us review the process of going from a csv file to a DataFrame.

This variable stores the path of the csv. It is used as an argument to the readCSV function. The result is stored to the variable df. This is short for DataFrame. Now that you have the data in a DataFrame, you can work with it. You can use the method head to examine the first five rows of a DataFrame. The process for loading an Excel file is similar.

Use the path of the Excel file, the function readexcel. The result is a DataFrame. A DataFrame is comprised of rows and columns. You can create a DataFrame out of a dictionary. The keys correspond to the column labels. The values are lists corresponding to the rows. You can then cast the dictionary to a DataFrame using the function DataFrame.

Notice the direct correspondence between the table. The keys correspond to the table headers. The values are lists corresponding to the rows. Create a new DataFrame consisting of one column and close the DataFrame name, in this case df, and the name of the column header in double brackets. The result is a new DataFrame comprised of the original column. You can do the same thing for multiple columns. Enclose the DataFrame name, in this case df, and the name of multiple column headers in double brackets.

The result is a new DataFrame comprised of the specified columns. One way to access unique elements is with the iloc method. The first input is an integer representing the row index, and the second is the integer representing the column index. You can access the first row and first column as follows. You can access the second row and first column as follows. You can access the first row, third column as follows, and you can access the second row, third column as follows. You can use the name of the row index and the column as well.

You can access the first row of the column named Artist as follows. Similarly, you can access the second row of the column named Artist. You can do the same for the column Released. loc can also be used if the index is not an integer. We create a new DataFrame called df_new. We replace the index 1, 2, 3, and so on with ABC. You can access the index A, that is, the first row of the column named Artist as follows. Similarly, you can access the index B, or the second row of the column named Artist.

You can do the same for the column Released. You can also slice DataFrames and assign the values to a new DataFrame. Assign the first two rows and the first three columns to the variable Z. The result is a DataFrame comprised of the selected rows and columns. You can also slice DataFrames and assign the values to a new DataFrame using loc. The code assigns the first two rows and all columns in between the columns named Artist and Released. The result is a new DataFrame Z with the corresponding values.

Check out the labs for more examples.

---

### 6. [VIDEO TRANSCRIPT] Pandas: Working with and Saving Data Video • 2 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/j1yDu/pandas-working-with-and-saving-data
- **Method:** `dom_transcript` | **Length:** 1813 chars

When we have a data frame we can work with the data and save the results in other formats. Consider the stack of 13 blocks of different colors. We can see there are three unique colors. Let's say you would like to find out how many unique elements are in a column of a data frame. This may be much more difficult because instead of 13 elements, you may have millions. Pandas has the method unique to determine the unique elements in a column of a data frame. Lets say we would like to determine the unique year of the albums in the data set.

We enter the name of the data frame, then enter the name of the column Released within brackets. Then we apply the method unique. The result is all of the unique elements in the column Released. Let's say we would like to create a new database consisting of songs from the 1980s and after. We can look at the column Released for songs made after 1979, then select the corresponding rows. We can accomplish this within one line of code in Pandas. But let's break up the steps.

We can use the inequality operators for the entire data frame in Pandas. The result is a series of Boolean values. For our case, we simply specify the column Released and the inequality for the albums after 1979. The result is a series of Boolean values. The result is true when the condition is true and false otherwise. We can select the specified columns in one line. We simply use the data frames names and square brackets we placed the previously mentioned inequality and assign it to the variable df1.

We now have a new data frame, where each album was released after 1979. We can save the new data frame using the method to_csv. The argument is the name of the csv file. Make sure you include a .csv extension. There are other functions to save the data frame in other formats. (Music)

---

### 7. [READING] Pandas Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/3mvwf/pandas
- **Method:** `dom_reading_cml` | **Length:** 10185 chars

## Objectives

By the end of this reading, you'll learn about:

- Learn what Pandas Series are and how to create them.
- Understand how to access and manipulate data within a Series.
- Discover the basics of creating and working with Pandas DataFrames.
- Learn how to access, modify, and analyze data in DataFrames.
- Gain insights into common DataFrame attributes and methods.

## What is Pandas?

Pandas is a popular open-source data manipulation and analysis library for the Python programming language. It provides a powerful and flexible set of tools for working with structured data, making it a fundamental tool for data scientists, analysts, and engineers.Pandas is designed to handle data in various formats, such as tabular data, time series data, and more, making it an essential part of the data processing workflow in many industries.

### Key features and functionalities of Pandas

Data Structures: Pandas offers two primary data structures - DataFrame and Series.

- A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).
- A Series is a one-dimensional labeled array, essentially a single column or row of data.

Data Import and Export: Pandas makes it easy to read data from various sources, including CSV files, Excel spreadsheets, SQL databases, and more. It can also export data to these formats, enabling seamless data exchange.

Data Merging and Joining: You can combine multiple DataFrames using methods like merge and join, similar to SQL operations, to create more complex datasets from different sources.

Efficient Indexing: Pandas provides efficient indexing and selection methods, allowing you to access specific rows and columns of data quickly.

Custom Data Structures: You can create custom data structures and manipulate data in ways that suit your specific needs, extending Pandas' capabilities.

## Importing Pandas

Import Pandas using the import command, followed by the library's name.Commonly, Pandas is imported as pd for brevity in code.

1import pandas as pdInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Data Loading

- Pandas can be used to load data from various sources, such as CSV and Excel files.
- The read_csv function is used to load data from a CSV file into a Pandas DataFrame.

To read a CSV (Comma-Separated Values) file in Python using the Pandas library, you can use the pd.read_csv() function. Here's the syntax to read a CSV file:

1234import pandas as pd # Read the CSV file into a DataFramedf = pd.read_csv('your_file.csv')Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Replace 'your_file.csv' with the actual file path of your CSV file. Make sure that the file is located in the same directory as your Python script, or you provide the correct file path.

## What is a Series?

A Series is a one-dimensional labeled array in Pandas. It can be thought of as a single column of data with labels or indices for each element. You can create a Series from various data sources, such as lists, NumPy arrays, or dictionariesHere's a basic example of creating a Series in Pandas:

12345import pandas as pd# Create a Series from a listdata = [10, 20, 30, 40, 50]s = pd.Series(data)print(s)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.In this example, we've created a Series named s with numeric data. Notice that Pandas automatically assigned numerical indices (0, 1, 2, 3, 4) to each element, but you can also specify custom labels if needed.

## Accessing Elements in a Series

You can access elements in a Series using the index labels or integer positions. Here are a few common methods for accessing Series data:

### Accessing by label

1print(s[2])     # Access the element with label 2 (value 30)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Accessing by position

1print(s.iloc[3]) # Access the element at position 3 (value 40)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Accessing multiple elements

1print(s[1:4])   # Access a range of elements by labelInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Series Attributes and Methods

Pandas Series come with various attributes and methods to help you manipulate and analyze data effectively. Here are a few essential ones:

- values: Returns the Series data as a NumPy array.
- index: Returns the index (labels) of the Series.
- shape: Returns a tuple representing the dimensions of the Series.
- size: Returns the number of elements in the Series.
- mean(), sum(), min(), max(): Calculate summary statistics of the data.
- unique(), nunique(): Get unique values or the number of unique values.
- sort_values(), sort_index(): Sort the Series by values or index labels.
- isnull(), notnull(): Check for missing (NaN) or non-missing values.
- apply(): Apply a custom function to each element of the Series.

## What is a DataFrames?

A DataFrame is a two-dimensional labeled data structure with columns of potentially different data types. Think of it as a table where each column represents a variable, and each row represents an observation or data point. DataFrames are suitable for a wide range of data, including structured data from CSV files, Excel spreadsheets, SQL databases, and more.

## Creating DataFrames from Dictionaries

DataFrames can be created from dictionaries, with keys as column labels and values as lists representing rows.

1234567891011import pandas as pd # Creating a DataFrame from a dictionarydata = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],        'Age': [25, 30, 35, 28],        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} df = pd.DataFrame(data) print(df) Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Column Selection

You can select a single column from a DataFrame by specifying the column name within double brackets.Multiple columns can be selected in a similar manner, creating a new DataFrame.

1print(df['Name'])  # Access the 'Name' columnInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Accessing Rows

You can access rows by their index using .iloc[] or by label using .loc[].

12print(df.iloc[2])   # Access the third row by positionprint(df.loc[1])    # Access the second row by labelInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Slicing

You can slice DataFrames to select specific rows and columns.

12print(df[['Name', 'Age']])  # Select specific columnsprint(df[1:3])             # Select specific rowsInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Finding Unique Elements

Use the unique method to determine the unique elements in a column of a DataFrame.

1unique_dates = df['Age'].unique()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Conditional Filtering

You can filter data in a DataFrame based on conditions using inequality operators.For instance, you can filter albums released after a certain year.

1high_above_102 = df[df['Age'] > 25]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Saving DataFrames

To save a DataFrame to a CSV file, use the to_csv method and specify the filename with a “.csv” extension.Pandas provides other functions for saving DataFrames in different formats.

1df.to_csv('trading_data.csv', index=False)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## DataFrame Attributes and Methods

DataFrames provide numerous attributes and methods for data manipulation and analysis, including:

- shape: Returns the dimensions (number of rows and columns) of the DataFrame.
- info(): Provides a summary of the DataFrame, including data types and non-null counts.
- describe(): Generates summary statistics for numerical columns.
- head(), tail(): Displays the first or last n rows of the DataFrame.
- mean(), sum(), min(), max(): Calculate summary statistics for columns.
- sort_values(): Sort the DataFrame by one or more columns.
- groupby(): Group data based on specific columns for aggregation.
- fillna(), drop(), rename(): Handle missing values, drop columns, or rename columns.
- apply(): Apply a function to each element, row, or column of the DataFrame.

Pandas offers a wide range of methods beyond these examples. For more detailed information, please refer to the official documentation available on the Pandas official website.

### Conclusion

In conclusion, mastering the use of Pandas Series and DataFrames is essential for effective data manipulation and analysis in Python. Series provide a foundation for handling one-dimensional data with labels, while DataFrames offer a versatile, table-like structure for working with two-dimensional data. Whether you're cleaning, exploring, transforming, or analyzing data, these Pandas data structures, along with their attributes and methods, empower you to efficiently and flexibly manipulate data to derive valuable insights. By incorporating Series and DataFrames into your data science toolkit, you'll be well-prepared to tackle a wide range of data-related tasks and enhance your data analysis capabilities.To further your skills in data analysis with Pandas, consider the following next steps:

- Work with real datasets to apply what you've learned and gain hands-on experience.
- Visit the Pandas official website to explore the extensive documentation and discover more functions and methods.

---

### 8. [VIDEO TRANSCRIPT] One Dimensional Numpy Video • 11 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/XCjRw/one-dimensional-numpy
- **Method:** `dom_transcript` | **Length:** 9684 chars

In this video, we will be covering NumPy in 1D, in particular, ndarrays. NumPy is a library for scientific computing. It has many useful functions. There are many other advantages like speed and memory. NumPy is also the basis for pandas, so check out our pandas video. In this video, we will be covering the basics and array creation, indexing and slicing, basic operations, universal functions. Let's go over how to create a NumPy array.

A Python list is a container that allows you to store and access data. Each element is associated with an index. We can access each element using a square bracket as follows. A NumPy array, or ndarray, is similar to a list. It's usually fixed in size, and each element is of the same type. In this case, integers. We can cast a list to a NumPy array by first importing NumPy.

We then cast the list as follows. We can access the data via an index. As with the lists, we can access each element with an integer and a square bracket. The value of a is stored as follows. If we check the type of the array, we get NumPy.ndarray. As NumPy arrays contain data of the same type, we can use the attribute dtype to obtain the data type of the array's elements. In this case, a 64-bit integer.

Let's review some basic array attributes using the array a. The attribute size is the number of elements in the array. As there are five elements, the result is five. The next two attributes will make more sense when we get to higher dimensions. But let's review them. The attribute ndim represents the number of array dimensions or the rank of the array, in this case, one. The attribute shape is a tuple of integers indicating the size of the array in each dimension.

We can create a NumPy array with real numbers. When we check the type of the array, we get NumPy.ndarray. If we examine the attribute dtype, we see float 64 as the elements are not integers. There are many other attributes. Check out NumPy.org. Let's review some indexing and slicing methods. We can change the first element of the array to 100 as follows.

The array's first value is now 100. We can change the fifth element of the array as follows. The fifth element is now zero. Like lists and tuples, we can slice a NumPy array. The elements of the array correspond to the following index. We can select the elements from one to three and assign it to a new NumPy array, d, as follows. The elements in d correspond to the index.

Like lists, we do not count the element corresponding to the last index. We can assign the corresponding indices to new values as follows. The array c now has new values. See the labs or NumPy.org for more examples of what you can do with NumPy. NumPy makes it easier to do many operations that are commonly performed in data science. These same operations are usually computationally faster and require less memory in NumPy compared to regular Python. Let's review some of these operations on one-dimensional arrays.

We will look at many of the operations in the context of Euclidean vectors to make things more interesting. Vector addition is a widely used operation in data science. Consider the vector u with two elements. The elements are distinguished by the different colors. Similarly, consider the vector v with two components. In vector addition, we create a new vector, in this case z. The first component of z is the addition of the first component of vectors u and v. Similarly, the second component is the sum of the second components of u and v. This new vector z is now a linear combination of the vector u and v. Representing vector addition with line segment or arrows is helpful.

The first vector is represented in red. The vector will point in the direction of the two components. The first component of the vector is 1. As a result, the arrow is offset one unit from the origin in the horizontal direction. The second component is 0. We represent this component in the vertical direction. As this component is 0, the vector does not point in the vertical direction.

We represent the second vector in blue. The first component is 0. Therefore, the arrow does not point to the horizontal direction. The second component is 1. As a result, the vector points in the vertical direction one unit. When we add the vector u and v, we get the new vector z. We add the first component.

This corresponds to the horizontal direction. We also add the second component. It's helpful to use the tip-to-tail method when adding vectors, placing the tail of a vector v on the tip of vector u. The new vector z is constructed by connecting the base of the first vector u with the tail of the second v. The following three lines of code will add the two lists and place the result in the list z. We can also perform vector addition with one line of NumPy code. It would require multiple lines to perform vector addition on two lists, as shown on the right side of the screen.

In addition, the NumPy code will run much faster. This is important if you have lots of data. We can also perform vector subtraction by changing the addition sign to a subtraction sign. It would require multiple lines to perform vector subtraction on two lists, as shown on the right side of the screen. Vector multiplication with a scalar is another commonly performed operation. Consider the vector y. Each component is specified by a different color.

We simply multiply the vector by a scalar value, in this case 2. Each component of the vector is multiplied by 2. In this case, each component is doubled. We can use the line segment or arrows to visualize what's going on. The original vector y is in purple. After multiplying it by a scalar value of 2, the vector is stretched out by 2 units, as shown in red. The new vector is twice as long in each direction.

Vector multiplication with a scalar only requires one line of code using NumPy. It would require multiple lines to perform the same task as shown with Python lists, as shown on the right side of the screen. In addition, the operation would also be much slower. Hadamard product is another widely used operation in data science. Consider the following two vectors, u and v. The Hadamard product of u and v is a new vector z. The first component of z is the product of the first element of u and v. Similarly, the second component is the product of the second element of u and v.

The resultant vector consists of the entry-wise product of u and v. We can also perform Hadamard product with one line of code in NumPy. It would require multiple lines to perform Hadamard product on two lists, as shown on the right side of the screen. The dot product is another widely used operation in data science. Consider the vector u and v. The dot product is a single number given by the following term and represents how similar two vectors are. We multiply the first component from v and u.

We then multiply the second component and add the result together. The result is a number that represents how similar the two vectors are. We can also perform dot product using the NumPy function dot and assign it with the variable result as follows. Consider the array u. The array contains the following elements. If we add a scalar value to the array, NumPy will add that value to each element. This property is known as broadcasting.

A universal function is a function that operates on nd arrays. We can apply a universal function to a NumPy array. Consider the arrays a. We can calculate the mean or average value of all the elements in a using the method mean. This corresponds to the average of all the elements. In this case, the result is zero. There are many other functions.

For example, consider the NumPy arrays b. We can find the maximum value using the method max. We see the largest value is 5. Therefore, the method max returns a 5. We can use NumPy to create functions that map NumPy arrays to new NumPy arrays. Let's implement some code on the left side of the screen and use the right side of the screen to demonstrate what's going on. We can access the value of pi in NumPy as follows.

We can create the following NumPy array in radians. This array corresponds to the following vector. We can apply the function sine to the array x and assign the values to the array y. This applies the sine function to each element in the array. This corresponds to applying the sine function to each component of the vector. The result is a new array y where each value corresponds to a sine function being applied to each element in the array x. A useful function for plotting mathematical functions is line space.

Line space returns evenly spaced numbers over specified interval. We specify the starting point of the sequence, the ending point of the sequence, the parameter num indicates the number of samples to generate, in this case, 5. The space between samples is 1. If we change the parameter num to 9, we get 9 evenly spaced numbers over the interval from negative 2 to 2. The result is the difference between subsequent samples is 0.5 as opposed to 1 as before. We can use the function line space to generate 100 evenly spaced samples from the interval 0 to 2 pi. We can use the NumPy function sine to map the array x to a new array y.

We can import the library pi plot as plt to help us plot the function. As we are using a Jupyter notebook, we use the command matplotlib inline to display the plot. The following command plots a graph. The first input corresponds to the values for the horizontal or x-axis. The second input corresponds to the values for the vertical or y-axis. There is a lot more you can do with NumPy. Check out the labs at numpy.org for more.

Thanks for watching this video.

---

### 9. [READING] Matrix Mathematics Reading • 5 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/c0J4L/matrix-mathematics
- **Method:** `dom_reading_cml` | **Length:** 2068 chars

You have seen that you can use Numpy package functions to perform different types of operations on arrays and matrices. In this reading, you will learn how these operations work mathematically.

## 1D Arrays : Vectors

A 1D array is often termed as a vector. Depending upon the orientation of the data, the vector can be classified as a row vector or a column vector. This is illustrated in the image below.

Mathematically, we can add, subtract, and take the product of two vectors, provided they are the same shape. The images below highlight the mathematical operations conducted on a pair of vectors.

All three of these operations are conducted on corresponding elements of individual vectors. The resulting array always has the same size as that of the two original vectors.

To a single vector, we can also add a constant (scalar addition), subtract a constant (scalar subtraction) and multiply a constant (scalar multiplication) to any vector. The images below illustrate these operations.

## 2D Arrays : Matrices

A 2D array is also called a Matrix. These are typically rectangular arrays with data stored in different rows. All of the operations mentioned above are also applicable to the 2D arrays.

As illlustrated in the images below, the dot product is carried out by multiplying and adding corresponding elements of rows of the first matrix with the elements of columns of the second matrix. As a result, the output matrix from the multiplication will have a modified shape.

The general rule is that the dot product of an m X n matrix can be done only with an n X p matrix, and the resultant matrix will have the shape m X p. In the example shown below, the 4 X 2 matrix is multiplied with the 2 X 4 matrix to generate a 4 X 4 matrix.

In the reverse example, when 2 X 4 matrix is multiplied with the 4 X 2 one, the resultant will be a 2 X 2 matrix.

Note: Dot product of a row vector with a column vector, with the same number of elements, would return a single scalar value. Dot product of a column vector with a row vector, will return a 2D matrix.

---

### 10. [VIDEO TRANSCRIPT] Two Dimensional Numpy Video • 7 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/0oVHr/two-dimensional-numpy
- **Method:** `dom_transcript` | **Length:** 6354 chars

We can create Numpy arrays with more than one dimension. This section will focus only on 2D arrays but you can use Numpy to build arrays of much higher dimensions. In this video, we will cover the basics and array creation in 2D, indexing and slicing in 2D, and basic operations in 2D. Consider the list a, the list contains three nested lists each of equal size. Each list is color-coded for simplicity. We can cast the list to a Numpy array as follows. It is helpful to visualize the Numpy array as a rectangular array each nested lists corresponds to a different row of the matrix.

We can use the attribute ndim to obtain the number of axes or dimensions referred to as the rank. The term rank does not refer to the number of linearly independent columns like a matrix. It's useful to think of ndim as the number of nested lists. The first list represents the first dimension. This list contains another set of lists. This represents the second dimension or axis. The number of lists the list contains does not have to do with the dimension but the shape of the list.

As with a 1D array, the attribute shape returns a tuple. It's helpful to use the rectangular representation as well. The first element in the tuple corresponds to the number of nested lists contained in the original list or the number of rows in the rectangular representation, in this case three. The second element corresponds to the size of each of the nested list or the number of columns in the rectangular array zero. The convention is to label this axis zero and this axis one as follows. We can also use the attribute size to get the size of the array. We see there are three rows and three columns.

Multiplying the number of columns and rows together, we get the total number of elements, in this case nine. Check out the labs for arrays of different shapes and other attributes. We can use rectangular brackets to access the different elements of the array. The following image demonstrates the relationship between the indexing conventions for the lists like representation. The index in the first bracket corresponds to the different nested lists each a different color. The second bracket corresponds to the index of a particular element within the nested list. Using the rectangular representation, the first index corresponds to the row index.

The second index corresponds to the column index. We could also use a single bracket to access the elements as follows. Consider the following syntax. This index corresponds to the second row, and this index the third column, the value is 23. Consider this example, this index corresponds to the first row and the second index corresponds to the first column, and a value of 11. We can also use slicing in Numpy arrays. The first index corresponds to the first row.

The second index accesses the first two columns. Consider this example, the first index corresponds to the first two rows. The second index accesses the last column. We can also add arrays, the process is identical to matrix addition. Consider the matrix X, each element is colored differently. Consider the matrix Y. Similarly, each element is colored differently.

We can add the matrices. This corresponds to adding the elements in the same position, i.e adding elements contained in the same color boxes together. The result is a new matrix that has the same size as matrix Y or X. Each element in this new matrix is the sum of the corresponding elements in X and Y. To add two arrays in Numpy, we define the array in this case X. Then we define the second array Y, we add the arrays. The result is identical to matrix addition.

Multiplying a Numpy array by a scalar is identical to multiplying a matrix by a scalar. Consider the matrix Y. If we multiply the matrix by this scalar two, we simply multiply every element in the matrix by two. The result is a new matrix of the same size where each element is multiplied by two. Consider the array Y. We first define the array, we multiply the array by a scalar as follows and assign it to the variable Z. The result is a new array where each element is multiplied by two.

Multiplication of two arrays corresponds to an element-wise product, or Hadamard product. Consider array X and array Y. Hadamard product corresponds to multiplying each of the elements in the same position i.e multiplying elements contained in the same color boxes together. The result is a new matrix that is the same size as matrix Y or X. Each element in this new matrix is the product of the corresponding elements in X and Y. Consider the array X and Y. We can find the product of two arrays X and Y in one line, and assign it to the variable Z as follows.

The result is identical to Hadamard product. We can also perform matrix multiplication with Numpy arrays. Matrix multiplication is a little more complex but let's provide a basic overview. Consider the matrix A where each row is a different color. Also, consider the matrix B where each column is a different color. In linear algebra, before we multiply matrix A by matrix B, we must make sure that the number of columns in matrix A in this case three is equal to the number of rows in matrix B, in this case three. From matrix multiplication, to obtain the ith row and jth column of the new matrix, we take the dot product of the ith row of a with the jth columns of B.

For the first column, first row we take the dot product of the first row of A with the first column of B as follows. The result is zero. For the first row and the second column of the new matrix, we take the dot product of the first row of the matrix A, but this time we use the second column of matrix B, the result is two. For the second row and the first column of the new matrix, we take the dot product of the second row of the matrix A. With the first column of matrix B, the result is zero. Finally, for the second row and the second column of the new matrix, we take the dot product of the second row of the matrix A with the second column of matrix B, the result is two. In Numpy, we can define the Numpy arrays A and B.

We can perform matrix multiplication and assign it to array C. The result is the array C. It corresponds to the matrix multiplication of array A and B. There is a lot more you can do with it in Numpy. Check out numpy.org. Thanks for watching this video. (Music)

---

### 11. [READING] Beginner's Guide to NumPy Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/v9kfI/beginners-guide-to-numpy
- **Method:** `dom_reading_cml` | **Length:** 8403 chars

## Objectives

In this reading, you'll learn about:

- Basics of NumPy
- How to create NumPy arrays
- Array attributes and indexing
- Basic operations like addition and multiplication

## What is NumPy?

NumPy, short for Numerical Python, is a fundamental library for numerical and scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of high-level mathematical functions to operate on these arrays. NumPy serves as the foundation for many data science and machine learning libraries, making it an essential tool for data analysis and scientific research in Python.

### Key aspects of NumPy in Python:

- Efficient data structures: NumPy introduces efficient array structures, which are faster and more memory-efficient than Python lists. This is crucial for handling large data sets.
- Multi-dimensional arrays: NumPy allows you to work with multi-dimensional arrays, enabling the representation of matrices and tensors. This is particularly useful in scientific computing.
- Element-wise operations: NumPy simplifies element-wise mathematical operations on arrays, making it easy to perform calculations on entire data sets in one go.
- Random number generation: It provides a wide range of functions for generating random numbers and random data, which is useful for simulations and statistical analysis.
- Integration with other libraries: NumPy seamlessly integrates with other data science libraries like SciPy, Pandas, and Matplotlib, enhancing its utility in various domains.
- Performance optimization: NumPy functions are implemented in low-level languages like C and Fortran, which significantly boosts their performance. It's a go-to choice when speed is essential.

## Installation

If you haven't already installed NumPy, you can do so using pip:

1pip install numpyInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Creating NumPy arrays

You can create NumPy arrays from Python lists. These arrays can be one-dimensional or multi-dimensional.

### Creating 1D array

1import numpy as npInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.import numpy as np: In this line, the NumPy library is imported and assigned an alias np to make it easier to reference in the code.

12# Creating a 1D arrayarr_1d = np.array([1, 2, 3, 4, 5]) # **np.array()** is used to create NumPy arrays.Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.arr_1d = np.array([1, 2, 3, 4, 5]): In this line, a one-dimensional NumPy array named arr_1d is created. It uses the np.array() function to convert a Python list [1, 2, 3, 4, 5] into a NumPy array. This array contains five elements, which are 1, 2, 3, 4, and 5. arr_1d is a 1D array because it has a single row of elements.

### Creating 2D array

1import numpy as npInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.import numpy as np: In this line, the NumPy library is imported and assigned an alias np to make it easier to reference in the code.

12# Creating a 2D arrayarr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]): In this line, a two-dimensional NumPy array named arr_2d is created. It uses the np.array() function to convert a list of lists into a 2D NumPy array.The outer list contains three inner lists, each of which represents a row of elements. So, arr_2d is a 2D array with three rows and three columns. The elements in this array form a matrix with values from 1 to 9, organized in a 3x3 grid.

### Array attributes

NumPy arrays have several useful attributes:

1234567# Array attributesprint(arr_2d.ndim)  # ndim : Represents the number of dimensions or "rank" of the array.# output : 2print(arr_2d.shape)  # shape : Returns a tuple indicating the number of rows and columns in the array.# Output : (3, 3)print(arr_2d.size) # size: Provides the total number of elements in the array.# Output : 9Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Indexing and slicing

You can access elements of a NumPy array using indexing and slicing:

In this line, the third element (index 2) of the 1D array arr_1d is accessed.

12# Indexing and slicingprint(arr_1d[2])          # Accessing an element (3rd element)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.In this line, the element in the 2nd row (index 1) and 3rd column (index 2) of the 2D array arr_2d is accessed.

1print(arr_2d[1, 2])       # Accessing an element (2nd row, 3rd column)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.In this line, the 2nd row (index 1) of the 2D array arr_2d is accessed.

1print(arr_2d[1, 2])       # Accessing an element (2nd row, 3rd column)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.In this line, the 2nd column (index 1) of the 2D array arr_2d is accessed.

1print(arr_2d[:, 1])       # Accessing a column (2nd column)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Basic operations

NumPy simplifies basic operations on arrays:

### Element-wise arithmetic operations:

Addition, subtraction, multiplication, and division of arrays with scalars or other arrays.

#### Array addition

12345# Array additionarray1 = np.array([1, 2, 3])array2 = np.array([4, 5, 6])result = array1 + array2print(result)  # [5 7 9]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Scalar multiplication

1234# Scalar multiplicationarray = np.array([1, 2, 3])result = array * 2 # each element of an array is multiplied by 2print(result)  # [2 4 6]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Element-wise multiplication (Hadamard Product)

12345# Element-wise multiplication (Hadamard product)array1 = np.array([1, 2, 3])array2 = np.array([4, 5, 6])result = array1 * array2print(result)  # [4 10 18]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Matrix multiplication

1234567# Matrix multiplicationmatrix1 = np.array([[1, 2], [3, 4]])matrix2 = np.array([[5, 6], [7, 8]])result = np.dot(matrix1, matrix2)print(result)# [[19 22]#  [43 50]]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.NumPy simplifies these operations, making it easier and more efficient than traditional Python lists.

## Operation with NumPy

Here's the list of operation which can be performed using Numpy

| Operation | Description | Example |
| --- | --- | --- |
| Array Creation | Creating a NumPy array. | arr = np.array([1, 2, 3, 4, 5]) |
| Element-Wise Arithmetic | Element-wise addition, subtraction, and so on. | result = arr1 + arr2 |
| Scalar Arithmetic | Scalar addition, subtraction, and so on. | result = arr * 2 |
| Element-Wise Functions | Applying functions to each element. | result = np.sqrt(arr) |
| Sum and Mean | Calculating the sum and mean of an array.Calculating the sum and mean of an array. | total = np.sum(arr) average = np.mean(arr) |
| Maximum and Minimum Values | Finding the maximum and minimum values. | max_val = np.max(arr) min_val = np.min(arr) |
| Reshaping | Changing the shape of an array. | reshaped_arr = arr.reshape(2, 3) |
| Transposition | Transposing a multi-dimensional array. | transposed_arr = arr.T |
| Matrix Multiplication | Performing matrix multiplication. | result = np.dot(matrix1, matrix2) |

## Conclusion

NumPy is a fundamental library for data science and numerical computations. This guide covers the basics of NumPy, and there's much more to explore. Visit numpy.org for more information and examples.

---

### 12. [READING] Module 4 Summary: Working with Data in Python Reading • 5 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/yuJMo/module-4-summary-working-with-data-in-python
- **Method:** `dom_reading_cml` | **Length:** 4019 chars

Congratulations! You have completed this module. At this point, you know that:

- Python uses the open() function and allows you to read and write files, providing access to the content within the file for reading. It also allows overwriting it for writing and specifies the file mode (for example, r for reading, w for writing, a for appending). - To read a file, Python uses an open function along with r. - Python uses the open with function to read and process a file attribute, that is, from open to close. - In Python, you use the open method to edit or overwrite a file. - To write a file, Python uses the open function along with w. - In Python, "a" indicates that the program has appended to the file. - In Python, “\n” signifies that the code should start on a new line. - Python uses various methods to print lines from attributes.
- Pandas is a powerful Python library for data manipulation and analysis, providing data structures and functions to work with structured data like data frames and series. - You import the file (panda) by using the import command followed by the file name. - In Python, you use the as command to provide a shorter name for the file. - In Pandas, you use a data frame (df) to specify the files to read. - DataFrames consist of rows and columns. - You can create new DataFrames by using the column or columns of a specific DataFrame. - We can work with data in a DataFrames and save the results in different formats. - In Python, you use the Unique method to determine unique elements in a column of the DataFrames. - You use the inequality operator along with df to assign a Boolean value to the selected column in DataFrames. - You save a new DataFrame as a different DataFrame, which may contain values from an earlier DataFrame.
- NumPy is a Python library for numerical and matrix operations, offering multidimensional array objects and a variety of mathematical functions to work with data efficiently. - NumPy is a basis for Pandas. - A NumPy array or ND array is similar to a list, usually of a fixed size with the same kind of element.
- A one-dimensional NumPy array is a linear sequence of elements with a single axis, like a traditional list, but optimized for numerical computations and array operations. - You can access elements in a NumPy using an index. - You use the attribute dtype to get the data type of the array elements. - You use size and ndim to get the size and dimension of the array, respectively. - You can use indexing and slicing methods in NumPy. - Vector additions are widely used operations in Python. - Representing vector addition with line segments or arrows is useful. - NumPy codes work much faster, which is helpful with lots of data. - You perform vector subtraction by replacing the addition sign with a negative sign. - Multiplying an array by a scalar in Python entails multiplying each element of the array by the scalar value, leading to a new array in which each element scales by the scalar. - Hadamard product refers to the element-wise multiplication of two arrays of the same shape, resulting in a new array where each element is the product of the corresponding elements in the input arrays. - The dot product in Python is the sum of the element-wise products of two arrays, often used for vector and matrix operations to find the scalar result of multiplying corresponding elements and summing them. - When working with NumPy, it is common to utilize libraries like Matplotlib to create graphs and visualizations from numerical data stored in NumPy arrays.
- A two-dimensional NumPy array is a grid-like structure with rows and columns suitable for representing data as a matrix or a table for numerical computations. - In NumPy, "shape" refers to an array's dimensions (number of rows and columns), indicating its size and structure. - You use the attribute "size" to obtain the size of an array. - You use rectangular attributes to access the various elements in an array. - You use a scalar to multiply elements in NumPy.

---

### 13. [READING] Cheat Sheet: Working with Data in Python Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/mVm9g/cheat-sheet-working-with-data-in-python
- **Method:** `dom_reading_cml` | **Length:** 12003 chars

## Reading and writing files

### File opening modes

Different modes to open files for specific operations.

Syntax: r (reading) w (writing) a (appending) + (updating: read/write) b (binary, otherwise text)

1Examples: with open("data.txt", "r") as file: content = file.read() print(content) with open("output.txt", "w") as file: file.write("Hello, world!") with open("log.txt", "a") as file: file.write("Log entry: Something happened.") with open("data.txt", "r+") as file: content = file.read() file.write("Updated content: " + content)</td>Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### File reading methods

Different methods to read file content in various ways.

Syntax:

123file.readlines() # reads all lines as a listreadline() # reads the next line as a stringfile.read() # reads the entire file content as a stringInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1234with open("data.txt", "r") as file:    lines = file.readlines()    next_line = file.readline()    content = file.read()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### File writing methods

Different write methods to write content to a file.

Syntax:

12file.write(content) # writes a string to the filefile.writelines(lines) # writes a list of strings to the fileInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

123lines = ["Hello\n", "World\n"]with open("output.txt", "w") as file:    file.writelines(lines)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Iterating over lines

Iterates through each line in the file using a loop.

Syntax:

1for line in file: # Code to process each lineInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

12with open("data.txt", "r") as file:for line in file: print(line)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### open() and close()

Opens a file, performs operations, and explicitly closes the file using the close() method.

Syntax:

12file = open(filename, mode) # Code that uses the filefile.close()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

123file = open("data.txt", "r")content = file.read()file.close()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### with open()

Opens a file using a with block, ensuring automatic file closure after usage.

Syntax:

1with open(filename, mode) as file: # Code that uses the fileInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

12with open("data.txt", "r") as file:content = file.read()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Pandas

### .read_csv()

Reads data from a .csv file and creates a DataFrame.

Syntax:

1dataframe_name = pd.read_csv("filename.csv") Example: df = pd.read_csv("data.csv")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### .read_excel()

Reads data from an Excel file and creates a DataFrame.

Syntax:

1dataframe_name = pd.read_excel("filename.xlsx")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1df = pd.read_excel("data.xlsx")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### .to_csv()

Writes DataFrame to a CSV file.

Syntax:

1dataframe_name.to_csv("output.csv", index=False)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1df.to_csv("output.csv", index=False)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Access Columns

Accesses a specific column using [] in the DataFrame.

Syntax:

12dataframe_name["column_name"] # Accesses single columndataframe_name[["column1", "column2"]] # Accesses multiple columnsInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

12df["age"]df[["name", "age"]]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### describe()

Generates a statistics summary of numeric columns in the DataFrame.

Syntax:

1dataframe_name.describe()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1df.describe()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### drop()

Removes specified rows or columns from the DataFrame. axis=1 indicates columns. axis=0 indicates rows.

Syntax:

12dataframe_name.drop(["column1", "column2"], axis=1, inplace=True)dataframe_name.drop(index=[row1, row2], axis=0, inplace=True)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

12df.drop(["age", "salary"], axis=1, inplace=True) # Will drop columnsdf.drop(index=[5, 10], axis=0, inplace=True) # Will drop rowsInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### dropna()

Removes rows with missing NaN values from the DataFrame. axis=0 indicates rows.

Syntax:

1dataframe_name.dropna(axis=0, inplace=True)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1df.dropna(axis=0, inplace=True)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### duplicated()

Identifies duplicate or repetitive values or records within a dataset.

Syntax:

1dataframe_name.duplicated()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1duplicate_rows = df[df.duplicated()]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Filter Rows

Creates a new DataFrame with rows that meet specified conditions.

Syntax:

1filtered_df = dataframe_name[(Conditional_statements)]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1filtered_df = df[(df["age"] > 30) & (df["salary"] < 50000)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### groupby()

Splits a DataFrame into groups based on specified criteria, enabling subsequent aggregation, transformation, or analysis within each group.

Syntax:

12grouped = dataframe_name.groupby(by, axis=0, level=None, as_index=True,sort=True, group_keys=True, squeeze=False, observed=False, dropna=True)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1grouped = df.groupby(["category", "region"]).agg({"sales": "sum"})Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### head()

Displays the first n rows of the DataFrame.

Syntax:

1dataframe_name.head(n)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1df.head(5)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Import pandas

Imports the Pandas library with the alias pd.

Syntax:

1import pandas as pdInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1import pandas as pdInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### info()

Provides information about the DataFrame, including data types and memory usage.

Syntax:

1dataframe_name.info()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1df.info()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### merge()

Merges two DataFrames based on multiple common columns.

Syntax:

1merged_df = pd.merge(df1, df2, on=["column1", "column2"])Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1merged_df = pd.merge(sales, products, on=["product_id", "category_id"])Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### print DataFrame

Displays the content of the DataFrame.

Syntax:

1print(df) # or just type dfInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

12print(df)dfInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### replace()

Replaces specific values in a column with new values.

Syntax:

1dataframe_name["column_name"].replace(old_value, new_value, inplace=True)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1df["status"].replace("In Progress", "Active", inplace=True)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### tail()

Displays the last n rows of the DataFrame.

Syntax:

1dataframe_name.tail(n)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1df.tail(5)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## NumPy

### Importing NumPy

Imports the NumPy library.

Syntax:

1import numpy as npInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1import numpy as npInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### np.array()

Creates a one-dimensional or multi-dimensional array.

Syntax:

12array_1d = np.array([list1 values]) # 1D Arrayarray_2d = np.array([[list1 values], [list2 values]]) # 2D ArrayInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

12array_1d = np.array([1, 2, 3]) # 1D Arrayarray_2d = np.array([[1, 2], [3, 4]]) # 2D ArrayInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### NumPy Array Attributes

Common NumPy operations on arrays:

- Calculates the mean of array elements
- Calculates the sum of array elements
- Finds the minimum value in the array
- Finds the maximum value in the array
- Computes the dot product of two arrays

Example:

12345np.mean(array)np.sum(array)np.min(arraynp.max(array)np.dot(array_1, array_2)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.

---

### 14. [READING] Module 4 Glossary: Working with Data in Python Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/taijZ/module-4-glossary-working-with-data-in-python
- **Method:** `dom_reading_cml` | **Length:** 5866 chars

Welcome! This alphabetized glossary contains many of the terms you'll find within this course. This comprehensive glossary also includes additional industry-recognized terms not used in course videos. These terms are important for you to recognize when working in the industry, participating in user groups, and participating in other certificate programs.

| Term | Definition |
| --- | --- |
| .csv file | A .csv (Comma-Separated Values) file is a plain text file format for storing tabular data, where each line represents a row and uses commas to separate values in different columns. |
| .txt file | A .txt (Text) file is a common file format that contains plain text without specific formatting, making it suitable for storing and editing textual data. |
| Append | To "append" means to add or attach something to the end of an existing object, typically used in the context of adding data to a file or elements to a data structure like a list in Python. |
| Attribute | An "attribute" in Python refers to a property or characteristic associated with an object, which can be accessed using dot notation. |
| Broadcasting in NumPy | Broadcasting in NumPy allows arrays with different shapes to be combined in element-wise operations by automatically extending smaller arrays to match the shape of larger ones, making operations more flexible. |
| Component | In NumPy, a "component" typically refers to a specific element or value within a multi-dimensional array, which can be accessed using indexing. |
| Computation | Computation in NumPy involves performing numerical operations on arrays and matrices, making it a powerful library for mathematical and scientific computing in Python. |
| Data analysis | Data analysis is the process of inspecting, cleaning, transforming, and interpreting data to discover useful information, draw conclusions, and support decision-making. |
| DataFrames | A DataFrames in Pandas is a two-dimensional, tabular data structure for storing and analyzing data, consisting of rows and columns. |
| Dependencies | Dependencies in Pandas are external libraries or modules, such as NumPy, that Pandas rely on for fundamental data manipulation and analysis functionality. |
| File attribute | File attributes generally refer to properties or metadata associated with files, which are managed at the operating system level. |
| File object | A "file object" in Python represents an open file, allowing reading from or writing to the file. |
| Grid | In Python, a "grid" typically refers to a two-dimensional structure composed of rows and columns, often used to represent data in a tabular format or for organizing objects in a coordinate system. |
| Hadamard Product | The Hadamard product is a mathematical operation that involves element-wise multiplication of two matrices or arrays of the same shape, producing a new matrix with each element being the product of the corresponding elements in the input matrices. |
| Importing pandas | To import Pandas in Python, you use the statement: import pandas as pd, which allows you to access Pandas functions and data structures using the abbreviation "pd." |
| Index | In Python, an "index" typically refers to a position or identifier used to access elements within a sequence or data structure, such as a list or string. |
| Libraries | Libraries in Python are collections of pre-written code modules that provide reusable functions and classes to simplify and enhance software development. |
| Linspace | In Python, "linspace" refers to a NumPy function that generates an array of evenly spaced values within a specified range. |
| NumPy | NumPy in Python is a fundamental library for numerical computing that provides support for large, multi-dimensional arrays and matrices, as well as a variety of high-level mathematical functions to operate on these arrays. |
| One dimensional NumPy | A one-dimensional NumPy array is a linear data structure that stores elements in a single sequence, often used for numerical computations and data manipulation. |
| Open function | In Python, the "open" function is used to access and manipulate files, allowing you to read from or write to a specified file. |
| Pandas | Pandas is a popular Python library for data manipulation and analysis, offering data structures and tools for working with structured data like tables and time series. |
| Pandas library | Pandas library in Python refer to the various modules and functions within the Pandas library, which provides powerful data structures and data analysis tools for working with structured data. |
| Plotting Mathematical Functions | Plotting mathematical functions in Python involves using libraries like Matplotlib to create graphical representations of mathematical equations, aiding visualization, and analysis. |
| Shape | In NumPy, "shape" refers to an array's dimensions (number of rows and columns), describing its size and structure. |
| Slicing | Slicing in NumPy entails extracting specific portions of an array by specifying a range of indices, enabling you to work with subsets of the data. |
| Two dimensional NumPy | A two-dimensional NumPy array is a structured data representation with rows and columns, resembling a matrix or table, ideal for various data manipulation and analysis tasks. |
| Universal Functions | Universal functions (ufuncs) in NumPy are functions that operate element-wise on arrays, providing efficient and vectorized operations for a wide range of mathematical and logical operations. |
| Vector addition | Vector addition in Python involves adding corresponding elements of two or more vectors, producing a new vector with the sum of their components. |
| Visualizations | Visualizations in Python refer to the creation of graphical representations, such as charts, plots, and graphs, to illustrate and communicate data and trends visually. |

---
