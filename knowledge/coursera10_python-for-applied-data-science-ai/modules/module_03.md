# Module 3: Python Programming Fundamentals

### 1. [VIDEO TRANSCRIPT] Conditions and Branching Video • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/WuZVi/conditions-and-branching
- **Method:** `dom_transcript` | **Length:** 8980 chars

In this video, you will learn about conditions and branching. Comparison operations compare some value or operand. Then, based on some condition, they produce a Boolean. Let's say we assign a value of a to 6. We can use the equality operator denoted with two equal signs to determine if two values are equal. In this case, if 7 is equal to 6. In this case, as 6 is not equal to 7, the result is false.

If we performed an equality test for the value 6, the two values would be equal. As a result, we would get a true. Consider the following equality comparison operator. If the value of the left operand, in this case the variable, i, is greater than the value of the right operand, in this case 5, the condition becomes true, or else we get a false. Let's display some values for i on the left. Let's see the values greater than 5 in green, and the rest in red. If we set i equal to 6, we see that 6 is larger than 5, and as a result, we get a true.

We can also apply the same operations to floats. If we modify the operator as follows, if the left operand i is greater than or equal to the value of the right operand, in this case 5, then the condition becomes true. In this case, we include the value of 5 in the number line, and the color changes to green accordingly. If we set the value of i equal to 5, the operand will produce a true. If we set the value of i to 2, we would get a false, because 2 is less than 5. We can change the inequality. If the value of the left operand, in this case i, is less than the value of the right operand, in this case 6, then condition becomes true.

Again, we can represent this with a colored number line. The areas where the inequality is true are marked in green, and red where the inequality is false. If the value for i is set to 2, the result is a true, as 2 is less than 6. The inequality test uses an explanation mark preceding the equal sign. If two operands are not equal, then the condition becomes true. We can use a number line. When the condition is true, the corresponding numbers are marked in green, and red for where the condition is false.

If we set i equal to 2, the operator is true, as 2 is not equal to 6. We compare strings as well. Comparing AC, DC, and Michael Jackson, using the equality test, we get a false, as the strings are not the same. Using the inequality test, we get a true, as the strings are different. See the labs for more examples. Branching allows us to run different statements for a different input. It's helpful to think of an if statement as a locked room.

If the statement is true, you can enter the room, and your program can run some predefined task. If the statement is false, your program will skip the task. For example, consider the blue rectangle representing an AC, DC concert. If the individual is 18 or older, they can enter the AC, DC concert. If they are under the age of 18, they cannot enter the concert. Individual proceeds to the concert. Their age is 17.

Therefore, they are not granted access to the concert, and they must move on. If the individual is 19, the condition is true. They can enter the concert. Then they can move on. This is the syntax of the if statement from our previous example. We have the if statement. We have the expression that can be true or false.

The brackets are not necessary. We have a colon. Within an indent, we have the expression that is run if the condition is true. The statements after the if statement will run regardless if the condition is true or false. For the case where the age is 17, we set the value of the variable age to 17. We check the if statement. The statement is false.

Therefore, the program will not execute the statement to print. You will enter. In this case, it will just print move on. For the case where the age is 19, we set the value of the variable age to 19. We check the if statement. The statement is true. Therefore, the program will execute the statement to print.

You will enter. Then it will just print move on. The else statement will run a different block of code if the same condition is false. Let's use the ACDC concert analogy again. If the user is 17, they cannot go to the ACDC concert. But they can go to the meatloaf concert represented by the purple square. If the individual is 19, the condition is true.

They can enter the ACDC concert. Then they can move on as before. The syntax of the else statement is similar. We simply append the statement else. We then add the expression we would like to execute with an indent. For the case where the age is 17, we set the value of the variable age to 17. We check the if statement.

The statement is false. Therefore, we progress to the else statement. We run the statement in the indent. This corresponds to the individual attending the meatloaf concert. The program will then continue running. For the case where the age is 19, we set the value of the variable age to 19. We check the if statement.

The statement is true. Therefore, the program will execute the statement to print you will enter. The program skips the expressions in the else statement. And continues to run the rest of the expressions. The elif statement, short for else if, allows us to check additional conditions. If the preceding condition is false. If the condition is true, the alternate expressions will be run.

Consider the concert example. If the individual is 18, they will go to the Pink Floyd concert. Instead of attending the ACDC or meatloaf concerts. The person of 18 years of age enters the area as they are not over 19 years of age. They cannot see ACDC. But as they are 18 years, they attend Pink Floyd. After seeing Pink Floyd, they move on.

The syntax of the elif statement is similar. We simply add the statement elif with the condition. We then add the expression we would like to execute if the statement is true. With an indent. Let's illustrate the code on the left. An 18 year old enters. They are not older than 18 years of age.

Therefore, the condition is false. So the condition of the elif statement is checked. The condition is true. So then we would print go see Pink Floyd. Then we would move on as before. If the variable age was 17, the statement go see meatloaf would print. Similarly, if the age was greater than 18, the statement you can enter would print.

Check the labs for more examples. Now let's take a look at logic operators. Logic operations take Boolean values and produce different Boolean values. The first operation is the not operator. If the input is true, the result is a false. Similarly, if the input is false, the result is a true. Let A and B represent Boolean variables.

The or operator takes in the two values and produces a new Boolean value. We can use this table to represent the different values. The first column represents the possible values of A. The second column represents the possible values of B. The final column represents the result of applying the or operation. We see the or operator only produces a false if all the Boolean values are false. The following lines of code will print out.

This album was made in the 70s or 90s. If the variable album year does not fall in the 80s. Let's see what happens when we set the album year to 1990. The colored number line is green when the condition is true and red when the condition is false. In this case, the condition is false. Examining the second condition, we see that 1990 is greater than 1989. So the condition is true.

We can verify by examining the corresponding second number line. In the final number line, the green region indicates where the area is true. This region corresponds to where at least one statement is true. We see that 1990 falls in the area. Therefore, we execute the statement. Let A and B represent Boolean variables. The and operator takes in the two values and produces a new Boolean value.

We can use this table to represent the different values. The first column represents the possible values of A. The second column represents the possible values of B. The final column represents the result of applying the and operation. We see the and operator only produces a true if all the Boolean values are true. The following lines of code will print out. This album was made in the 80s if the variable album year is between 1980 and 1989.

Let's see what happens when we set the album year to 1983. As before, we can use the colored number line to examine where the condition is true. In this case, 1983 is larger than 1980. So the condition is true. Examining the second condition, we see that 1990 is greater than 1983. So this condition is also true. We can verify by examining the corresponding second number line.

In the final number line, the green region indicates where the area is true. Similarly, this region corresponds to where both statements are true. We see that 1983 falls in the area. Therefore, we execute the statement. Branching allows us to run different statements for different inputs.

---

### 2. [READING] Conditions and Branching Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/wx3nb/conditions-and-branching
- **Method:** `dom_reading_cml` | **Length:** 5199 chars

## Objectives

In this reading, you'll learn about:

- Comparison operators
- Branching
- Logical operators

## Comparison operations

Comparison operations are essential in programming. They help compare values and make decisions based on the results.

### Equality operator

The equality operator == checks if two values are equal. For example, in Python:

123age = 25if age == 25:    print("You are 25 years old.")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Here, the code checks if the variable age is equal to 25 and prints a message accordingly.

### Inequality operator

The inequality operator != checks if two values are not equal:

12if age != 30:    print("You are not 30 years old.")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Here, the code checks if the variable age is not equal to 30 and prints a message accordingly.

### Greater than and less than

You can also compare if one value is greater than another.

12if age>= 20:    Print("Yes, the Age is greater than 20")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Here, the code checks if the variable age is greater than or equal to 20 and prints a message accordingly.

## Branching

Branching is like making decisions in your program based on conditions. Think of it as real-life choices.

### The IF statement

Consider a real-life scenario of entering a bar. If you're above a certain age, you can enter; otherwise, you cannot.

12345age = 20if age >= 21:    print("You can enter the bar.")else:    print("Sorry, you cannot enter.")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Here, you are using the if statement to make a decision based on the age variable.

### The ELIF Statement

Sometimes, there are multiple conditions to check. For example, if you're not old enough for the bar, you can go to a movie instead.

123456if age >= 21:    print("You can enter the bar.")elif age >= 18:    print("You can watch a movie.")else:    print("Sorry, you cannot do either.")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Real-life example: Automated Teller Machine (ATM)

When a user interacts with an ATM, the software in the ATM can use branching to make decisions based on the user's input. For example, if the user selects "Withdraw Cash" the ATM can branch into different denominations of bills to dispense based on the amount requested.

123456789user_choice = "Withdraw Cash"if user_choice == "Withdraw Cash":    amount = int(input("Enter the amount to withdraw: "))    if amount % 10 == 0:        print("Amount dispensed: ", amount)    else:        print("Please enter a multiple of 10.")else:    print("Thank you for using the ATM.")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Logical operators

Logical operators help combine and manipulate conditions.

### The NOT operator

#### Real-life example: Notification settings

In a smartphone's notification settings, you can use the NOT operator to control when to send notifications. For example, you might only want to receive notifications when your phone is not in "Do Not Disturb" mode.

The not operator negates a condition.

123is_do_not_disturb = Trueif not is_do_not_disturb:    send_notification("New message received")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### The AND operator

#### Real-life example: Access control

In a secure facility, you can use the AND operator to check multiple conditions for access. To open a high-security door, a person might need both a valid ID card and a matching fingerprint.

The AND operator checks if all required conditions are true, like needing both keys to open a safe.

1234has_valid_id_card = Truehas_matching_fingerprint = Trueif has_valid_id_card and has_matching_fingerprint:    open_high_security_door()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### The OR operator

#### Real-life example: Movie night decision

When planning a movie night with friends, you can use the OR operator to decide on a movie genre. You'll choose a movie if at least one person is interested.

The OR operator checks if at least one condition is true. It's like choosing between different movies to watch.

12345friend1_likes_comedy = Truefriend2_likes_action = Falsefriend3_likes_drama = Falseif friend1_likes_comedy or friend2_likes_action or friend3_likes_drama:    choose a movie()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Summary

In this reading, you delved into the most frequently used operator and the concept of conditional branching, which encompasses the utilization of if statements and if-else statements.

---

### 3. [VIDEO TRANSCRIPT] Loops Video • 6 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/19yQq/loops
- **Method:** `dom_transcript` | **Length:** 6113 chars

In this video, we will cover loops, in particular, for loops and while loops. We will use many visual examples in this video. See the labs for examples with data. Before we talk about loops, let's go over the range function. The range function outputs an ordered sequence as a list i. If the input is a positive integer, the output is a sequence. The sequence contains the same number of elements as the input, but starts at 0.

For example, if the input is 3, the output is the sequence 0, 1, 2. If the range function has two inputs, or the first input is smaller than the second input, the output is a sequence that starts at the first input. Then the sequence iterates up to, but not including, the second number. For the input 10 and 15, we get the following sequence. See the labs for more capabilities of the range function. Please note, if you use Python 3, the range function will not generate a list explicitly like in Python 2. In this section, we will cover four loops.

We will focus on lists, but many of the procedures can be used on tuples. Loops perform a task over and over. Consider the group of colored squares. Let's say we would like to replace each colored square with a white square. Let's give each square a number to make things a little easier, and refer to all the group of squares as squares. If we wanted to tell someone to replace square 0 with a white square, we would say, equals replace square 0 with a white square. Or we can say, for square 0 in squares, square 0 equals white square.

Similarly, for the next square, we can say, for square 1 in squares, square 1 equals white square. For the next square, we can say, for square 2 in squares, square 2 equals white square. We repeat the process for each square. The only thing that changes is the index of the square we are referring to. If we are going to perform a similar task in Python, we cannot use actual squares. So let's use a list to represent the boxes. Each element in the list is a string representing the color.

We want to change the name of the color in each element to white. Each element in the list has the following index. This is a syntax to perform a loop in Python. Notice the indent. The range function generates a list. The code will simply repeat everything in the indent 5 times. If you were to change the value to 6, it would do it 6 times.

However, the value of i is incremented by 1 each time. In this segment, we change the ith element of the list to the string white. The value of i is set to 0. Each iteration of the loop starts at the beginning of the indent. We then run everything in the indent. The first element in the list is set to white. We then go to the start of the indent.

We progress down each line. When we reach the line to change the value of the list, we set the value of index 1 to white. The value of i increases by 1. We repeat the process for index 2. The process continues for the next index until we have reached the final element. We can also iterate through a list or tuple directly in Python. We do not even need to use indices.

Here is the list squares. Each iteration of the list we pass one element of the list squares to the variable square. Let's display the value of the variable square on this section. For the first iteration, the value of square is red. We then start the second iteration. For the second iteration, the value of square is yellow. We then start the third iteration.

For the final iteration, the value of square is green. A useful function for iterating data is enumerate. It can be used to obtain the index and the element in the list. Let's use the box analogy with the numbers representing the index of each square. This is the syntax to iterate through a list and provide the index of each element. We use the list squares and use the names of the colors to represent the colored squares. The argument of the function enumerate is the list, in this case squares.

The variable i is the index and the variable square is the corresponding element in the list. Let's use the left part of the screen to display the different values of the variable square and i for the various iterations of the loop. For the first iteration, the value of the variable is red, corresponding to the zeroth index and the value for i is zero. For the second iteration, the value of the variable square is yellow and the value of i corresponds to its index, i.e. 1. We repeat the process for the last index. While loops are similar to for loops, but instead of executing a statement a set number of times, a while loop will only run if a condition is met.

Let's say we would like to copy all the orange squares from the list squares to the list new squares, but we would like to stop if we encounter a non-orange square. We don't know the value of the squares beforehand. We would simply continue the process while the square is orange or see if the square equals orange. If not, we would stop. For the first example, we would check if the square was orange. It satisfies the condition, so we would copy the square. We repeat the process for the second square.

The condition is met, so we copy the square. In the next iteration, we encounter a purple square. The condition is not met, so we stop the process. This is essentially what a while loop does. Let's use the figure on the left to represent the code. We will use a list with the names of the color to represent the different squares. We create an empty list of new squares.

In reality, the list is of indeterminate size. We start the index at 0. The while statement will repeatedly execute the statements within the indent until the condition inside the bracket is false. We append the value of the first element of the list squares to the list new squares. We increase the value of i by 1. We append the value of the second element of the list squares to the list new squares. We increment the value of i.

Now the value in the array squares is purple. Therefore, the condition for the while statement is false, and we exit the loop. Check out the labs for more examples of loop, many with real data.

---

### 4. [READING] Introduction to Loops in Python Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/9cMBm/introduction-to-loops-in-python
- **Method:** `dom_reading_cml` | **Length:** 9247 chars

## Objectives

In this reading, you'll learn about:

- Understand Python loops.
- How the loop Works
- Learn about the needs for loop
- Utilize Python's Range function.
- Familiarize with Python's enumerate function.
- Apply while loops for conditional tasks.
- Distinguish appropriate loop selection.

## What is a Loop?

In programming, a loop is like a magic trick that allows a computer to do something over and over again. Imagine you are a magician's assistant, and your magician friend asks you to pull a rabbit out of a hat, but not just once - they want you to keep doing it until they tell you to stop. That is what loops do for computers - they repeat a set of instructions as many times as needed.

## How Loop works?

Here's how it works in Python:

- Start: The for loop begins with the keyword for, followed by a variable that will take on each value in a sequence.
- Condition: After the variable, you specify the keyword in and a sequence, such as a list or a range, that the loop will iterate through.

#### If Condition True:

- The loop takes the first value from the sequence and assigns it to the variable.
- The indented block of code following the loop header is executed using this value.
- The loop then moves to the next value in the sequence and repeats the process until all values have been used.

- Statement: Inside the indented block of the loop, you write the statements that you want to repeat for each value in the sequence.
- Repeat: The loop continues to repeat the block of code for each value in the sequence until there are no more values left.

#### If Condition False:

- Once all values in the sequence have been processed, the loop terminates automatically.
- The loop completes its execution, and the program continues to the next statement after the loop.

## The Need for Loops

Think about when you need to count from 1 to 10. Doing it manually is easy, but what if you had to count to a million? Typing all those numbers one by one would be a nightmare! This is where loops come in handy. They help computers repeat tasks quickly and accurately without getting tired.

## Main Types of Loops

### For Loops

For loops are like a superhero's checklist. A for loop in programming is a control structure that allows the repeated execution of a set of statements for each item in a sequence, such as elements in a list or numbers in a range, enabling efficient iteration and automation of tasks.

#### Syntax of for loop:

12for val in sequence:      # statement(s) to be executed in sequence as a part of the loop.Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Example of for loop:

Imagine you're a painter, and you want to paint a beautiful rainbow with seven colors. Instead of picking up each color one by one and painting the rainbow, you could tell a magical painter's assistant to do it for you. This is what a basic for loop does in programming.

We have a list of colors.

1colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Let's print the colour name in the new line using for loop.

12for color in colors:    print(color)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.In this example, the for loop picks each color from the colors list and prints it on the screen. You don't have to write the same code for each color - the loop does it automatically!

Sometimes you do not want to paint a rainbow, but you want to count the number of steps to reach your goal. A range-based for loop is like having a friendly step counter that helps you reach your target.Here is how you might use a for loop to count from 1 to 10:

12for number in range(1, 11):    print(number)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Here, the range(1, 11) generates a sequence from 1 to 10, and the for loop goes through each number in that sequence, printing it out. It's like taking 10 steps, and you're guided by the loop!

### Range Function

The range function in Python generates an ordered sequence that can be used in loops. It takes one or two arguments:

- If given one argument (e.g., range(11)), it generates a sequence starting from 0 up to (but not including) the given number.

12for number in range(11):    print(number)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
- If given two arguments (e.g., range(1, 11)), it generates a sequence starting from the first argument up to (but not including) the second argument.

12for number in range(1, 11):    print(number)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### The Enumerated For Loop

Have you ever needed to keep track of both the item and its position in a list? An enumerated for loop comes to your rescue. It's like having a personal assistant who not only hands you the item but also tells you where to find it.

#### Example:

123fruits = ["apple", "banana", "orange"]for index, fruit in enumerate(fruits):    print(f"At position {index}, I found a {fruit}")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.With this loop, you not only get the fruit but also its position in the list. It's as if you have a magical guide pointing out each fruit's location!

### While Loops

While loops are like a sleepless night at a friend's sleepover. Imagine you and your friends keep telling ghost stories until someone decides it's time to sleep. As long as no one says, "Let's sleep" you keep telling stories.A while loop works similarly - it repeats a task as long as a certain condition is true. It's like saying, "Hey computer, keep doing this until I say stop!"

#### Syntax:

123while condition:    # Code to be executed while the condition is true    # Indentation is crucial to indicate the scope of the loopInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Example:

Here's how you might use a while loop to count from 1 to 10:

1234count = 1while count <= 10:    print(count)    count += 1Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Here's a breakdown of the above code:

- There is a variable named count initialized with the value 1.
- The while loop is used to repeatedly execute a block of code as long as a given condition is True. In this case, the condition is count <= 10, meaning the loop will continue as long as count is less than or equal to 10.
- Inside the loop: - The print(count) statement outputs the current value of the count variable. - The count += 1 statement increments the value of count by 1. This step ensures that the loop will eventually terminate when count becomes greater than 10.
- The loop will continue executing as long as the condition count <= 10 is satisfied.
- The loop will print the numbers 1 to 10 in consecutive order since the print statement is inside the loop block and executed during each iteration.
- Once count reaches 11, the condition count <= 10 will evaluate to False, and the loop will terminate.
- The output of the code will be the numbers 1 to 10, each printed on a separate line.

### The Loop Flow

Both for and while loops have their special moves, but they follow a pattern:

- Initialization: You set up things like a starting point or conditions.
- Condition: You decide when the loop should keep going and when it should stop.
- Execution: You do the task inside the loop.
- Update: You make changes to your starting point or conditions to move forward.
- Repeat: The loop goes back to step 2 until the condition is no longer true.

### When to Use Each

For Loops: Use for loops when you know the number of iterations in advance and want to process each element in a sequence. They are best suited for iterating over collections and sequences where the length is known.

While Loops: Use while loops when you need to perform a task repeatedly as long as a certain condition holds true. While loops are particularly useful for situations where the number of iterations is uncertain or where you're waiting for a specific condition to be met.

## Summary

In this adventure into coding, we explored loops in Python - special tools that help us do things over and over again without getting tired. We met two types of loops: "for loops" and "while loops."

For Loops were like helpers that made us repeat tasks in order. We painted colors, counted numbers, and even got a helper to tell us where things were in a list. For loops made our job easier and made our code look cleaner.

While Loops were like detectives that kept doing something as long as a rule was true. They helped us take steps, guess numbers, and work until we were tired. While loops were like smart assistants that didn't stop until we said so.

---

### 5. [VIDEO TRANSCRIPT] Functions Video • 13 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/zLQQX/functions
- **Method:** `dom_transcript` | **Length:** 11423 chars

In this video, we will cover functions. You will learn how to use some of Python's built-in functions, as well as how to build your own function. Functions take some input, then produce some output or change. The function is just a piece of code you can reuse. You can implement your own function, but in many cases, you use other people's functions. In this case, you just have to know how the function works, and in some cases, how to import the functions. Let the orange and yellow squares represent similar blocks of code.

We can run the code using some input and get an output. If we define a function to do the task, we just have to call the function. Let the small squares represent the lines of code used to call the function. We can replace these long lines of code by just calling the function a few times. Now we can just call the function. Our code is much shorter. The code performs the same task.

You can think of the process like this. When we call the function f1, we pass an input to the function. These values are passed to all those lines of code you wrote. This returns a value. You can use the value. For example, you can input this value to a new function, f2. When we call this new function, f2, the value is passed to another set of lines of code.

The function returns a value. The process is repeated, passing the values to the function you call. You can save these functions and reuse them, or use other people's functions. Python has many built-in functions. You don't have to know how those functions work internally, but simply what task those functions perform. The function len takes in an input of type sequence, such as a string or list or type collection, such as a dictionary or set, and returns the length of that sequence or collection. Consider the following list.

The len function takes this list as an argument, and we assign the result to the variable l. The function determines there are eight items in the list, then returns the length of the list, in this case, eight. The function sum takes in an iterable, like a tuple or list, and returns the total of all the elements. Consider the following list. We pass the list into the sum function and assign the result to the variable s. The function determines the total of all the elements, then returns it. In this case, the value is 70.

There are two ways to sort a list. The first is using the function sorted. We can also use the list method sort. Methods are similar to functions. Let's use this as an example to illustrate the difference. The function sorted returns a new sorted list or tuple. Consider the list album ratings.

We can apply the function sorted to the list album ratings and get a new list sorted album rating. The result is a new sorted list. If we look at the list album ratings, nothing has changed. Generally, functions take an input, in this case, a list. They produce a new output, in this instance, a sorted list. If we use the method sort, the list album ratings will change and no new list will be created. Let's use the diagram to help illustrate the process.

In this case, the rectangle represents the list album ratings. When we apply the method sort to the list, the list album rating changes. Unlike the previous case, we see that the list album rating has changed. In this case, no new list is created. Now that we've gone over how to use functions in Python, let's see how to build our own functions. We will now get you started on building your own functions in Python. This is an example of a function in Python that returns its input value plus one.

To define a function, we start with the keyword def. The name of the function should be descriptive of what it does. We have the function formal parameter a in parentheses, followed by a colon. We have a code block with an indent. For this case, we add one to a and assign it to b. We return, or output, the value for b. After we define the function, we can call it.

The function will add one to five and return a six. We can call the function again, this time assign it to the variable c. The value for c is 11. Let's explore this further. Let's go over an example when you call a function. It should be noted that this is a simplified model of Python, and Python does not work like this under the hood. We call the function, giving it an input five.

It helps to think of the value of five as being passed to the function. Now the sequences of commands are run. The value of a is five. b would be assigned a value of six. We then return the value of b. In this case, as b was assigned a value of six, the function returns a six. If we call the function again, the process starts from scratch. We pass in an eight.

The subsequent operations are performed. Everything that happened the last call will happen again, with a different value of a. The function returns a value, in this case, nine. Again, this is just a helpful analogy. Let's try and make this function more complex. It's customary to document the function on the first few lines. This tells anyone who uses the function what it does.

This documentation is surrounded in triple quotes. You can use the help command on the function to display the documentation as follows. This will print out the function name and the documentation. We will not include the documentation in the rest of the examples. A function can have multiple parameters. The function mult multiplies two numbers. In other words, it finds their product.

If we pass the integers two and three, the result is a new integer. If we pass the integer 10 and the float 3.14, the result is a float 31.4. If we pass in the integer two and the string Michael Jackson, the string Michael Jackson is repeated two times. This is because the multiplication symbol can also mean repeat a sequence. If you accidentally multiply an integer with a string instead of two integers, you won't get an error. Instead, you will get a string and your program will progress, potentially failing later because you have a string where you expected an integer. This property will make coding simpler, but you must test your code more thoroughly.

In many cases, a function does not have a return statement. In these cases, Python will return the special none object. Practically speaking, if your function has no return statement, you can treat it as if the function returns nothing at all. The function MJ simply prints the name Michael Jackson. We call the function. The function prints Michael Jackson. Let's define the function no work that performs no task.

Python doesn't allow a function to have an empty body, so we can use the keyword pass, which doesn't do anything, but satisfies the requirement of a non-empty body. If we call the function and print it out, the function returns a none. In the background, if the return statement is not called, Python will automatically return a none. It is helpful to view the function no work with the following return statement. Usually, functions perform more than one task. This function prints a statement then returns a value. Let's use this table to represent the different values as the function is called.

We call the function with an input of 2. We find the value of b. The function prints the statement with the value of a and b. Finally, the function returns the value of b, in this case 3. We can use loops in functions. This function prints out the values and indexes of a loop or tuple. We call the function with the list album ratings as an input.

Let's display the list on the right with its corresponding index. Stuff is used as an input to the function enumerate. This operation will pass the index to i and the value in the list to s. The function will begin to iterate through the loop. The function will print the first index and the first value in the list. We continue iterating through the loop. The values of i and s are updated.

The print statement is reached. Similarly, the next values of the list and index are printed. The process is repeated. The values of i and s are updated. We continue iterating until the final values in the list are printed out. Variadic parameters allow us to input a variable number of elements. Consider the following function.

The function has an asterisk on the parameter names. When we call the function, three parameters are packed into the tuple names. We then iterate through the loop. The values are printed out accordingly. If we call the same function with only two parameters as inputs, the variable names only contain two elements. The result is only two values are printed out. The scope of a variable is the part of the program where that variable is accessible.

Variables are defined outside of any function are said to be within the global scope, meaning they can be accessed anywhere after they are defined. Here we have a function that adds the string dc to the parameter x. When we reach the part where the value of x is set to ac, this is within the global scope, meaning x is accessible anywhere after it is defined. A variable defined in the global scope is called a global variable. When we call the function, we enter a new scope or the scope of add dc. We pass as an argument the add dc function, in this case ac. Within the scope of the function, the value of x is set to ac dc.

The function returns the value and is assigned to z. Within the global scope, the value z is set to ac dc. After the value is returned, the scope of the function is deleted. Local variables only exist within the scope of a function. Consider the function thriller. The local variable date is set to 1982. When we call the function, we create a new scope.

Within that scope of the function, the value of the date is set to 1982. The value of date does not exist within the global scope. Variables inside the global scope can have the same name as variables in the local scope with no conflict. Consider the function thriller. The local variable date is set to 1982. The global variable date is set to 2017. When we call the function, we create a new scope.

Within that scope, the value of the date is set to 1982. If we call the function, it returns the value of date in the local scope. In this case, 1982. When we print in the global scope, we use the global variable value. The global value of the variable is 2017. Therefore, the value is set to 2017. If a variable is not defined within a function, Python will check the global scope.

Consider the function ac dc. The function has the variable rating with no value assigned. If we define the variable rating in the global scope, then call the function, Python will see there is no value for the variable rating. As a result, Python will leave the scope and check if the variable ratings exists in the global scope. It will use the value of ratings in the global scope within the scope of ac dc. In the function, we'll print out a 9. The value of z in the global scope will be 10 as we added 1.

The value of rating will be unchanged within the global scope. Consider the function, Pink Floyd. If we define the variable claimed sales with the keyword global, the variable will be a global variable. We call the function, Pink Floyd. The variable claimed sales is set to the string 45 million in the global scope. When we print the variable, we get a value of 45 million. There is a lot more you can do with functions.

Check out the lab for more examples.

---

### 6. [READING] Exploring Python Functions Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/bl2Z6/exploring-python-functions
- **Method:** `dom_reading_cml` | **Length:** 15775 chars

## Objectives

In this reading, you'll learn about:

- Describe the function concept and the importance of functions in programming
- Write a function that takes inputs and performs tasks
- Use built-in functions like len(), sum(), and others effectively
- Define and use your functions in Python
- Differentiate between global and local variable scopes
- Use loops within the function
- Modify data structures using functions

## Introduction to functions

A function is a fundamental building block that encapsulates specific actions or computations. As in mathematics, where functions take inputs and produce outputs, programming functions perform similarly. They take inputs, execute predefined actions or calculations, and then return an output.

### Purpose of functions

Functions promote code modularity and reusability. Imagine you have a task that needs to be performed multiple times within a program. Instead of duplicating the same code at various places, you can define a function once and call it whenever you need that task. This reduces redundancy and makes the code easier to manage and maintain.

### Benefits of using functions

- Modularity: Functions break down complex tasks into manageable components
- Reusability: Functions can be used multiple times without rewriting code
- Readability: Functions with meaningful names enhance code understanding
- Debugging: Isolating functions eases troubleshooting and issue fixing
- Abstraction: Functions simplify complex processes behind a user-friendly interface
- Collaboration: Team members can work on different functions concurrently
- Maintenance: Changes made in a function automatically apply wherever it's used

## How functions take inputs, perform tasks, and produce outputs

### Inputs (Parameters)

Functions operate on data, and they can receive data as input. These inputs are known as parameters or arguments. Parameters provide functions with the necessary information they need to perform their tasks. Consider parameters as values you pass to a function, allowing it to work with specific data.

### Performing tasks

Once a function receives its input (parameters), it executes predefined actions or computations. These actions can include calculations, operations on data, or even more complex tasks. The purpose of a function determines the tasks it performs. For instance, a function could calculate the sum of numbers, sort a list, format text, or fetch data from a database.

### Producing outputs

After performing its tasks, a function can produce an output. This output is the result of the operations carried out within the function. It's the value that the function “returns” to the code that called it. Think of the output as the end product of the function's work. You can use this output in your code, assign it to variables, pass it to other functions, or even print it out for display.

#### Example:

Consider a function named calculate_total that takes two numbers as input (parameters), adds them together, and then produces the sum as the output. Here's how it works:

123456def calculate_total(a, b):  # Parameters: a and b    total = a + b           # Task: Addition    return total            # Output: Sum of a and b result = calculate_total(5, 7)  # Calling the function with inputs 5 and 7print(result)  # Output: 12Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Python's built-in functions

Python has a rich set of built-in functions that provide a wide range of functionalities. These functions are readily available for you to use, and you don't need to be concerned about how they are implemented internally. Instead, you can focus on understanding what each function does and how to use it effectively.

### Using built-in functions or Pre-defined functions

To use a built-in function, you simply call the function's name followed by parentheses. Any required arguments or parameters are passed into the function within these parentheses. The function then performs its predefined task and may return an output you can use in your code.

#### Here are a few examples of commonly used built-in functions:

- len(): Calculates the length of a sequence or collection

12string_length = len("Hello, World!")  # Output: 13list_length = len([1, 2, 3, 4, 5])   # Output: 5Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
- sum(): Adds up the elements in an iterable (list, tuple, and so on)

1total = sum([10, 20, 30, 40, 50])  # Output: 150Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
- max(): Returns the maximum value in an iterable

1highest = max([5, 12, 8, 23, 16])  # Output: 23Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
- min(): Returns the minimum value in an iterable

1lowest = min([5, 12, 8, 23, 16])  # Output: 5Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Python's built-in functions offer a wide array of functionalities, from basic operations like len() and sum() to more specialized tasks.

## Defining your functions

### Defining a function is like creating your mini-program:

Use def followed by the function name and parentheses. Here is the syntax to define a function:

12def function_name():    passInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.A "pass" statement in a programming function is a placeholder or a no-op (no operation) statement. Use it when you want to define a function or a code block syntactically but do not want to specify any functionality or implementation at that moment.

- Placeholder: "pass" acts as a temporary placeholder for future code that you intend to write within a function or a code block.
- Syntax Requirement: In many programming languages like Python, using "pass" is necessary when you define a function or a conditional block. It ensures that the code remains syntactically correct, even if it doesn't do anything yet.
- No Operation: "pass" itself doesn't perform any meaningful action. When the interpreter encounters "pass", it simply moves on to the next statement without executing any code.

### Function Parameters:

- Parameters are like inputs for functions
- They go inside parentheses when defining the function
- Functions can have multiple parameters

#### Example:

12345def greet(name):    return "Hello, " + name result = greet("Alice")print(result)  # Output: Hello, AliceInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Docstrings (Documentation Strings):

- Docstrings explain what a function does
- Placed inside triple quotes under the function definition
- Helps other developers understand your function

#### Example:

12345678def multiply(a, b):    """    This function multiplies two numbers.    Input: a (number), b (number)    Output: Product of a and b    """    print(a * b)multiply(2,6)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Return Statement:

- Return gives back a value from a function
- Ends the function's execution and sends the result
- A function can return various types of data

#### Example:

1234def add(a, b):    return a + b sum_result = add(3, 5)  # sum_result gets the value 8Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Understanding scopes and variables

Scope is where a variable can be seen and used:

- Global Scope: Variables defined outside functions; accessible everywhere
- Local Scope: Variables inside functions; only usable within that function

### Part 1: Global variable declaration

1global_variable = "I'm global"Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.This line initializes a global variable called global_variable and assigns it the value "I'm global".

Global variables are accessible throughout the entire program, both inside and outside functions.

### Part 2: Function definition

1234def example_function():    local_variable = "I'm local"    print(global_variable)  # Accessing global variable    print(local_variable)   # Accessing local variableInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Here, you define a function called example_function().

Within this function:

- A local variable named local_variable is declared and initialized with the string value "I'm local." This variable is local to the function and can only be accessed within the function's scope.
- The function then prints the values of both the global variable (global_variable) and the local variable (local_variable). It demonstrates that you can access global and local variables within a function.

### Part 3: Function call

1example_function()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.In this part, you call the example_function() by invoking it. This results in the function's code being executed.

As a result of this function call, it will print the values of the global and local variables within the function.

### Part 4: Accessing global variable outside the function

1print(global_variable)  # Accessible outside the functionInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.After calling the function, you print the value of the global variable global_variable outside the function. This demonstrates that global variables are accessible inside and outside of functions.

### Part 5: Attempting to access local variable outside the function

1# print(local_variable)  # Error, local variable not visible hereInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.In this part, you are attempting to print the value of the local variable local_variable outside of the function. However, this line would result in an error.

Local variables are only visible and accessible within the scope of the function where they are defined.

Attempting to access them outside of that scope would raise a "NameError".

## Using functions with loops

### Functions and loops together

- Functions can contain code with loops
- This makes complex tasks more organized
- The loop code becomes a repeatable function

#### Example:

12345def greet(name):    return "Hello, " + name for _ in range(3):    print(greet("Alice"))Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Enhancing code organization and reusability

- Functions group similar actions for easy understanding
- Looping within functions keeps code clean
- You can reuse a function to repeat actions

#### Example:

12345def greet(name):    return "Hello, " + name for _ in range(3):    print(greet("Alice"))Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Modifying data structure using functions

You'll use Python and a list as the data structure for this illustration. In this example, you will create functions to add and remove elements from a list.

### Part 1: Initialize an empty list

12# Define an empty list as the initial data structuremy_list = []Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.In this part, you start by creating an empty list named my_list. This empty list serves as the data structure that you will modify throughout the code.

### Part 2: Define a function to add elements

123# Function to add an element to the listdef add_element(data_structure, element):    data_structure.append(element)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Here, you define a function called add_element. This function takes two parameters:

- data_structure: This parameter represents the list to which you want to add an element
- element: This parameter represents the element you want to add to the list

Inside the function, you use the append method to add the provided element to the data_structure, which is assumed to be a list.

### Part 3: Define a function to remove elements

123456# Function to remove an element from the listdef remove_element(data_structure, element):    if element in data_structure:        data_structure.remove(element)    else:        print(f"{element} not found in the list.")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.In this part, you define another function called remove_element. It also takes two parameters:

- data_structure: The list from which we want to remove an element
- element: The element we want to remove from the list

Inside the function, you use conditional statements to check if the element is present in the data_structure. If it is, you use the remove method to remove the first occurrence of the element. If it's not found, you print a message indicating that the element was not found in the list.

### Part 4: Add elements to the list

1234# Add elements to the list using the add_element functionadd_element(my_list, 42)add_element(my_list, 17)add_element(my_list, 99)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Here, you use the add_element function to add three elements (42, 17, and 99) to the my_list. These are added one at a time using function calls.

### Part 5: Print the current list

12# Print the current listprint("Current list:", my_list)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.This part simply prints the current state of the my_list to the console, allowing us to see the elements that have been added so far.

### Part 6: Remove elements from the list

123# Remove an element from the list using the remove_element functionremove_element(my_list, 17)remove_element(my_list, 55)  # This will print a message since 55 is not in the listInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.In this part, you use the remove_element function to remove elements from the my_list. First, you attempt to remove 17 (which is in the list), and then you try to remove 55 (which is not in the list). The second call to remove_element will print a message indicating that 55 was not found.

### Part 7: Print the updated list

12# Print the updated listprint("Updated list:", my_list)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Finally, you print the updated my_list to the console. This allows us to observe the modifications made to the list by adding and removing elements using the defined functions.

## Conclusion

Congratulations! You've completed the Reading Instruction Lab on Python functions. You've gained a solid understanding of functions, their significance, and how to create and use them effectively. These skills will empower you to write more organized, modular, and powerful code in your Python projects.

---

### 7. [VIDEO TRANSCRIPT] Exception Handling Video • 3 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/3dEjg/exception-handling
- **Method:** `dom_transcript` | **Length:** 3490 chars

Hello. Welcome to Exception Handling. After watching this video, you will be able to explain exception handling, demonstrate the use of exception handling, and understand the basics of exception handling. Have you ever mistakenly entered a number when you were supposed to enter text in an input field? Most of us have either in error or when testing out a program, but do you know why it gave an error message instead of completing and terminating the program? In order for the error message to appear, an event was triggered in the background. This event was activated because the program tried to perform a computation on the name entry and realized the entry contained numbers and not letters.

By encasing this code in an exception handler the program knew how to deal with this type of error and was able to output the error message to continue along with the program. This is one of many errors that can happen when asking for user input, so let’s see how exception handling works. We will first explore the try…except statement. This type of statement will first attempt to execute the code in the “try” block, but if an error occurs it will kick out and begin searching for the exception that matches the error. Once it finds the correct exception to handle the error, it will then execute that line of code. For example, perhaps you are writing a program that will open and write a file. After starting the program, an error occurred as the data was not able to be read.

Because of this error the program skipped over the code lines under the “try” statement and went directly to the exception line. Since this error fell within the IOError guidelines it printed “Unable to open or read the data in the file.” to our console. When writing simple programs we can sometimes get away with only one except statement, but what happens if another error occurs that is not caught by the IOError? If that happened we would need to add another except statement. For this except statement you will notice that the type of error to catch is not specified. While this may seem a logical step so the program will catch all errors and not terminate, this is not a best practice. For example, let’s say our small program was just one section of a much larger program that was over a thousand lines of code.

Our task was to debug the program as it kept throwing an error causing a disruption for our users. When investigating the program you found this error kept appearing. Because this error had no details you ended up spending hours trying to pinpoint and fix the error. So far in our program we have defined that an error message should print out if an error occurs, but we do not receive any messages that the program executed properly. This is where we can now add an else statement to give us that notification. By adding this else statement it will provide us a notification to the console that “The file was written successfully.” Now that we have defined what will happen if our program executes properly, or if an error occurs there is one last statement to add.

For this example, since we are opening a file the last thing we need to do is close the file. By adding a finally statement it will tell the program to close the file no matter the end result and print “File is now closed” to our console. In this video, you learned how to write a try…except statement, why it is important to always define errors when creating exceptions, and how to add an else and finally statement.

---

### 8. [READING] Exception Handling Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/xo9ex/exception-handling
- **Method:** `dom_reading_cml` | **Length:** 7007 chars

## Objectives

At the end of this reading, you'll learn about:

- Understanding Exceptions
- Distinguishing Errors from Exceptions
- Familiarity with Common Python Exceptions
- Managing Exceptions Effectively

In the world of programming, errors and unexpected situations are certain. Python, a popular and versatile programming language, equips developers with a powerful toolset to manage these unforeseen scenarios through exceptions and error handling.

## What are exceptions?

Exceptions are alerts when something unexpected happens while running a program. It could be a mistake in the code or a situation that was not planned for. Python can raise these alerts automatically, but we can also trigger them on purpose using the raise command. The cool part is that we can prevent our program from crashing by handling exceptions.

## Errors vs. Exceptions

Hold on, what is the difference between errors and exceptions? Well, errors are usually big problems that come from the computer or the system. They often make the program stop working completely. On the other hand, exceptions are more like issues we can control. They happen because of something we did in our code and can usually be fixed, so the program keeps going.

Here is the difference between Errors and exceptions:

| Aspect | Errors | Exceptions |
| --- | --- | --- |
| Origin | Errors are typically caused by the environment, hardware, or operating system. | Exceptions are usually a result of problematic code execution within the program. |
| Nature | Errors are often severe and can lead to program crashes or abnormal termination. | Exceptions are generally less severe and can be caught and handled to prevent program termination. |
| Handling | Errors are not usually caught or handled by the program itself. | Exceptions can be caught using try-except blocks and dealt with gracefully, allowing the program to continue execution. |
| Examples | Examples include “SyntaxError” due to incorrect syntax or “NameError” when a variable is not defined. | Examples include “ZeroDivisionError” when dividing by zero, or “FileNotFoundError” when attempting to open a non-existent file. |
| Categorization | Errors are not classified into categories. | Exceptions are categorized into various classes, such as “ArithmeticError,” “IOError,” ValueError,” etc., based on their nature. |

## Common Exceptions in Python

Here are a few examples of exceptions we often run into and can handle using this tool:

### ZeroDivisionError

This error arises when an attempt is made to divide a number by zero. Division by zero is undefined in mathematics, causing an arithmetic error.

#### For example:

123result = 10 / 0 print(result)# Raises ZeroDivisionErrorInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### ValueError

This error occurs when an inappropriate value is used within the code. An example of this is when trying to convert a non-numeric string to an integer.

#### For example:

12num = int("abc")# Raises ValueErrorInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### FileNotFoundError

This exception is encountered when an attempt is made to access a file that does not exist.

#### For example:

12with open("nonexistent_file.txt", "r") as file:        content = file.read()   # Raises FileNotFoundErrorInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### IndexError

An IndexError occurs when an index is used to access an element in a list that is outside the valid index range.

#### For example:

123my_list = [1, 2, 3]value = my_list[1]  # No IndexError, within rangemissing = my_list[5]  # Raises IndexErrorInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### KeyError

The KeyError arises when an attempt is made to access a non-existent key in a dictionary.

#### For example:

123my_dict = {"name": "Alice", "age": 30}value = my_dict.get("city")  # No KeyError, using .get() methodmissing = my_dict["city"]  # Raises KeyErrorInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### TypeError

The TypeError occurs when an object is used in an incompatible manner. An example includes trying to concatenate a string and an integer.

#### For example:

12result = "hello" + 5   # Raises TypeErrorInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### AttributeError

An AttributeError occurs when an attribute or method is accessed on an object that doesn't possess that specific attribute or method.

#### For example:

123text = "example"length = len(text)  # No AttributeError, correct method usagemissing = text.some_method()  # Raises AttributeErrorInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### ImportError

This error is encountered when an attempt is made to import a module that is unavailable.

For example: import non_existent_module

Note: Please remember, the exceptions you will encounter are not limited to just these. There are many more in Python. However, there is no need to worry. By using the technique provided below and following the correct syntax, you will be able to handle any exceptions that come your way.

## Handling Exceptions

Python has a handy tool called try and except that helps us manage exceptions.

Try and Except: You can use the try and except blocks to prevent your program from crashing due to exceptions.

Here's how they work:

- The code that may result in an exception is contained in the try block.
- If an exception occurs, the code directly jumps to except block.
- In the except block, you can define how to handle the exception gracefully, like displaying an error message or taking alternative actions.
- After the except block, the program continues executing the remaining code.

### Example: Attempting to divide by zero

123456789# using Try- except try:    # Attempting to divide 10 by 0    result = 10 / 0except ZeroDivisionError:    # Handling the ZeroDivisionError and printing an error message    print("Error: Cannot divide by zero")# This line will be executed regardless of whether an exception occurredprint("outside of try and except block")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Next Steps

As we finish up this reading, you are ready to move on to the next part where you will practice handling errors. For better learning, try out different types of data in the lab. This way, you will encounter various errors and learn how to deal with them effectively. This knowledge will help you write stronger and more reliable code in the future.

---

### 9. [VIDEO TRANSCRIPT] Objects and Classes Video • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/KgVed/objects-and-classes
- **Method:** `dom_transcript` | **Length:** 10171 chars

In this module, we are going to talk about objects and classes. Python has many different kinds of data types, integers, floats, strings, lists, dictionaries, Booleans. In Python, each is an object. Every object has the following; a type, internal representation, a set of functions called methods to interact with the data. An object is an instance of a particular type. For example, we have two types, Type 1 and Type 2. We can have several objects of Type 1 as shown in yellow.

Each object is an instance of Type 1. We also have several objects of Type 2 shown in green. Each object is an instance of Type 2. Let's do several less abstract examples. Every time we create an integer, we are creating an instance of type integer, or we are creating an integer object. In this case, we are creating five instances of type integer or five integer objects. Similarly, every time we create a list, we are creating an instance of type list, or we are creating a list object.

In this case, we are creating five instances of type list or five list objects. We can find out the type of an object by using the type command. In this case, we have an object of type list. We have an object of type integer. We have an object of type string. Finally, we have an object of type dictionary. A class or type methods are functions that every instance of that class or type provides.

It's how you interact with the object. We have been using methods all this time, for example, on lists. Sorting is an example of a method that interacts with the data in the object. Consider the list ratings. The data is a series of numbers contained within the list. The method sort will change the data within the object. We call the method by adding a period at the end of the object's name, and the method's name we would like to call with parentheses.

We have the ratings list represented in orange. The data contained in the list is a sequence of numbers. We call the sort method. This changes the data contained in the object. You can say it changes the state of the object. We can call the reverse method on the list, changing the list again. We call the method reversing the order of the sequence within the object.

In many cases, you don't have to know the inner workings of the class and its methods, you just have to know how to use them. Next, we will cover how to construct your own classes. You can create your own type or class in Python. In this section, you'll create a class. The class has data attributes. The class has methods. We then create instances or instances of that class or objects.

The class data attributes define the class. Let's create two classes. The first class will be a circle. The second will be a rectangle. Let's think about what constitutes a circle. Examining this image, all we need is a radius to define a circle and let's add color to make it easier to distinguish between different instances of the class later. Therefore, our class data attributes are radius and color.

Similarly, examining the image in order to define a rectangle, we need the height and width. We will also add color to distinguish between instances later. Therefore, the data attributes are color, height and width. To create the class circle, you will need to include the class definition. This tells Python you are creating your own class, the name of the class. For this course in parentheses, you will always place the term object. This is the parent of the class.

For the class rectangle, we change the name of the class, but the rest is kept the same. Classes are outlines we have to set the attributes to create objects. We can create an object that is an instance of type circle. The color data attribute is red, and the data attribute radius is four. We can also create a second object that is an instance of type circle. In this case, the color data attribute is green, and the data attribute radius is two. We can also create an object that is an instance of type rectangle.

The color data attribute is blue, and the data attribute of height and width is two. The second object is also an instance of type rectangle. In this case, the color data attribute is yellow, and the height is one, and the width is three. We now have different objects of class circle or type circle. We also have different objects of class rectangle or type rectangle. Let us continue building the circle class in Python. We define our class.

We then initialize each instance of the class with data attributes, radius and color using the class constructor. Function in it is a constructor. It's a special function that tells Python you are making a new class. There are other special functions in Python to make more complex classes. The radius and color parameters are used to initialize the radius and color data attributes of the class instance. The self parameter refers to the newly created instance of the class. The parameters radius and color can be used in the constructor's body to access the values passed to the class constructor when the class is constructed.

We can set the value of the radius and color data attributes to the values passed to the constructor method. Similarly, we can define the class rectangle in Python. The name of the class is different. This time, the class data attributes are color, height and width. After we have created the class, in order to create an object of class circle, we introduce a variable. This will be the name of the object. We create the object by using the object constructor.

The object constructor consists of the name of the class, as well as the parameters. These are the data attributes. When we create a circle object, we call the code like a function. The arguments passed to the circle constructor are used to initialize the data attributes of the newly created circle instance. It is helpful to think of self as a box that contains all the data attributes of the object. Typing the object's name followed by a dot and the data attribute name gives us the data attribute value, for example, radius. In this case, the radius is 10.

We can do the same for color. We can see the relationship between the self parameter and the object. In Python, we can also set or change the data attribute directly, typing the object's name followed by a dot and the data attribute name and set it equal to the corresponding value. We can verify that the color data attribute has changed. Usually, in order to change the data in an object, we define methods in the class. Let's discuss methods. We have seen how data attributes consist of the data defining the objects.

Methods are functions that interact and change the data attributes, changing or using the data attributes of the object. Let's say we would like to change the size of a circle. This involves changing the radius attribute. We add a method at radius to the class circle. The method is a function that requires a self as well as other parameters. In this case, we are going to add a value to the radius. We denote that value as r. We are going to add r to the data attribute radius.

Let's see how this part of the code works when we create an object and call the add radius method. As before, we create an object with the object constructor. We pass two arguments to the constructor. The radius is set to two and the color is set to red. In the constructor's body, the data attributes are set. We can use the box analogy to see the current state of the object. We call the method by adding a dot followed by the method name and parentheses.

In this case, the argument of the function is the amount we would like to add. We do not need to worry about the self parameter when calling the method. Just like with the constructor, Python will take care of that for us. In many cases, there may not be any parameters other than self specified in the methods definition, so we don't pass any arguments when calling the function. Internally, the method is called with a value of eight and the proper self object. The method assigns a new value to self.radius. This changes the object, in particular, the radius data attribute.

When we call the add radius method, this changes the object by changing the value of the radius data attribute. We can add default values to the parameters of a class's constructor. In the labs, we also create the method called drawCircle. See the lab for the implementation of drawCircle. In the labs, we can create a new object of type circle using the constructor. The color will be red and the radius will be three. We can access the data attribute radius.

We can access the attribute color. Finally, we can use the method drawCircle to draw the circle. Similarly, we can create a new object of type circle. We can access the data attribute of radius. We can access the data attribute color. We can use the method drawCircle to draw the circle. In summary, we have created an object of class circle called RedCircle with a radius attribute of three and a color attribute of red.

We also created an object of class circle called BlueCircle with a radius attribute of 10 and a color attribute of blue. In the lab, we have a similar class for rectangle. We can create a new object of type rectangle using the constructor. We can access a data attribute of height. We can also access the data attribute of width. We can do the same for the data attribute of color. We can use the method drawRectangle to draw the rectangle.

We have a class, an object that is a realization or instantiation of that class. For example, we can create two objects of class circle or two objects of class rectangle. The dir function is useful for obtaining the list of data attributes and methods associated with a class. The object you're interested in is passed as an argument. The return value is a list of that object's data attributes. The attributes surrounded by underscores are for internal use, and you shouldn't have to worry about them. The regular looking attributes are the ones you should concern yourself with.

These are the objects methods and data attributes. There is a lot more you can do with objects in Python. Check python.org for more info.

---

### 10. [READING] Objects and Classes Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/kUelV/objects-and-classes
- **Method:** `dom_reading_cml` | **Length:** 13583 chars

## Objectives

In this reading, you will learn about:

- Fundamental concepts of Python objects and classes.
- Structure of classes and object code.
- Real-world examples related to objects and classes.

## Introduction to classes and object

Python is an object-oriented programming (OOP) language that uses a paradigm centered around objects and classes.

Let's look at these fundamental concepts.

### Classes

A class is a blueprint or template for creating objects. It defines the structure and behavior that its objects will have.

Think of a class as a cookie cutter and objects as the cookies cut from that template.

In Python, you can create classes using the class keyword.

#### Creating Classes

When you create a class, you specify the attributes(data) and methods (functions) that objects of that class will have.

Attributes are defined as variables within the class, and methods are defined as functions.

For example, you can design a "Car" class with attributes such as "color" and "speed," along with methods like "accelerate."

### Objects

An object is a fundamental unit in Python that represents a real-world entity or concept.Objects can be tangible (like a car) or abstract (like a student's grade).

Every object has two main characteristics:

### State

The attributes or data that describe the object. For your "Car" object, this might include attributes like "color", "speed", and "fuel level".

### Behavior

The actions or methods that the object can perform. In Python, methods are functions that belong to objects and can change the object's state or perform specific operations.

### Instantiating objects

- Once you've defined a class, you can create individual objects (instances) based on that class.
- Each object is independent and has its own set of attributes and methods.
- To create an object, you use the class name followed by parentheses, so: "my_car = Car()"

### Interacting with objects

You interact with objects by calling their methods or accessing their attributes using dot notation.

For example, if you have a Car object named my_car, you can set its color with my_car.color = "blue" and accelerate it with my_car.accelerate() if there's an accelerate method defined in the class.

## Structure of classes and object code

Please don't directly copy and use this code because it is a template for explanation and not for specific results.

### Class declaration (class ClassName)

- The class keyword is used to declare a class in Python.
- ClassName is the name of the class, typically following CamelCase naming conventions.

1class ClassName:Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Class attributes (class_attribute = value)

- Class attributes are variables shared among all class instances (objects).
- They are defined within the class but outside of any methods.

123class ClassName:    # Class attributes (shared by all instances)    class_attribute = valueInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Constructor method (def init(self, attribute1, attribute2, …):)

- The __init__ method is a special method known as the constructor.
- It initializes the instance attributes (also called instance variables) when an object is created.
- The self parameter is the first parameter of the constructor, referring to the instance being created.
- attribute1, attribute2, and so on are parameters passed to the constructor when creating an object.
- Inside the constructor, self.attribute1, self.attribute2, and so on are used to assign values to instance attributes.

12345678class ClassName:    # Class attributes (shared by all instances)    class_attribute = value     # Constructor method (initialize instance attributes)    def __init__(self, attribute1, attribute2, ...):        pass        # ...Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Instance attributes (self.attribute1 = attribute1)

- Instance attributes are variables that store data specific to each class instance.
- They are initialized within the __init__ method using the self keyword followed by the attribute name.
- These attributes hold unique data for each object created from the class.

123456789class ClassName:    # Class attributes (shared by all instances)    class_attribute = value     # Constructor method (initialize instance attributes)    def __init__(self, attribute1, attribute2, ...):        self.attribute1 = attribute1        self.attribute2 = attribute2        # ...Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Instance methods (def method1(self, parameter1, parameter2, …):)

- Instance methods are functions defined within the class.
- They operate on the instance's data (instance attributes) and can perform actions specific to instances.
- The self parameter is required in instance methods, allowing them to access instance attributes and call other methods within the class.

1234567891011121314class ClassName:    # Class attributes (shared by all instances)    class_attribute = value     # Constructor method (initialize instance attributes)    def __init__(self, attribute1, attribute2, ...):        self.attribute1 = attribute1        self.attribute2 = attribute2        # ...     # Instance methods (functions)    def method1(self, parameter1, parameter2, ...):        # Method logic        passInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Using the same steps you can define multiple instance methods.

123456789101112131415161718class ClassName:    # Class attributes (shared by all instances)    class_attribute = value     # Constructor method (initialize instance attributes)    def __init__(self, attribute1, attribute2, ...):        self.attribute1 = attribute1        self.attribute2 = attribute2        # ...     # Instance methods (functions)    def method1(self, parameter1, parameter2, ...):        # Method logic        pass     def method2(self, parameter1, parameter2, ...):        # Method logic        passInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Note: Now, you have successfully created a dummy class.

### Creating objects (Instances)

- To create objects (instances) of the class, you call the class like a function and provide arguments the constructor requires.
- Each object is a distinct instance of the class, with its own instance attributes and the ability to call methods defined in the class.

123# Create objects (instances) of the classobject1 = ClassName(arg1, arg2, ...)object2 = ClassName(arg1, arg2, ...)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Calling methods on objects

- In this section, you will call methods on objects, specifically object1 and object2.
- The methods method1 and method2 are defined in the ClassName class, and you're calling them on object1 and object2 respectively.
- You pass values param1_value and param2_value as arguments to these methods. These arguments are used within the method's logic.

#### Method 1: Using dot notation

- This is the most straightforward way to call an object's method. In this, use the dot notation (object.method()) to invoke the method on the object directly.
- For example, result1 = object1.method1(param1_value, param2_value, ...) calls method1 on object1.

1234# Calling methods on objects# Method 1: Using dot notationresult1 = object1.method1(param1_value, param2_value, ...)result2 = object2.method2(param1_value, param2_value, ...)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Method 2: Assigning object methods to variables

- Here's an alternative way to call an object's method by assigning the method reference to a variable.
- method_reference = object1.method1 assigns the method method1 of object1 to the variable method_reference.
- Later, call the method using the variable like this: result3 = method_reference(param1_value, param2_value, …).

123# Method 2: Assigning object methods to variablesmethod_reference = object1.method1  # Assign the method to a variableresult3 = method_reference(param1_value, param2_value, ...)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Accessing object attributes

- Here, you are accessing an object's attribute using dot notation.
- attribute_value = object1.attribute1 retrieves the value of the attribute attribute1 from object1 and assigns it to the variable attribute_value.

12# Accessing object attributesattribute_value = object1.attribute1  # Access the attribute using dot notationInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Modifying object attributes

- You will modify an object's attribute using dot notation.
- object1.attribute2 = new_value sets the attribute attribute2 of object1 to the new value new_value.

12# Modifying object attributesobject1.attribute2 = new_value  # Change the value of an attribute using dot notationInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Accessing class attributes (shared by all instances)

- Finally, access a class attribute shared by all class instances.
- class_attr_value = ClassName.class_attribute accesses the class attribute class_attribute from the ClassName class and assigns its value to the variable class_attr_value.

12# Accessing class attributes (shared by all instances)class_attr_value = ClassName.class_attributeInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Real-world example

Let's write a python program that simulates a simple car class, allowing you to create car instances, accelerate them, and display their current speeds.

Let's start by defining a Car class that includes the following attributes and methods:

- Class attribute max_speed, which is set to 120 km/h.
- Constructor method __init__ that takes parameters for the car's make, model, color, and an optional speed (defaulting to 0). This method initializes instance attributes for make, model, color, and speed.
- Method accelerate(self, acceleration) that allows the car to accelerate. If the acceleration does not exceed the max_speed, update the car's speed attribute. Otherwise, set the speed to the max_speed.
- Method get_speed(self) that returns the current speed of the car.

123456789101112131415161718192021class Car:    # Class attribute (shared by all instances)    max_speed = 120  # Maximum speed in km/h     # Constructor method (initialize instance attributes)    def __init__(self, make, model, color, speed=0):        self.make = make        self.model = model        self.color = color        self.speed = speed  # Initial speed is set to 0     # Method for accelerating the car    def accelerate(self, acceleration):        if self.speed + acceleration <= Car.max_speed:            self.speed += acceleration        else:            self.speed = Car.max_speed     # Method to get the current speed of the car    def get_speed(self):        return self.speedInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Now, you will instantiate two objects of the Car class, each with the following characteristics:

- car1: Make = "Toyota", Model = "Camry", Color = "Blue"
- car2: Make = "Honda", Model = "Civic", Color = "Red"

123# Create objects (instances) of the Car classcar1 = Car("Toyota", "Camry", "Blue")car2 = Car("Honda", "Civic", "Red")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Using the accelerate method, you will increase the speed of car1 by 30 km/h and car2 by 20 km/h.

123# Accelerate the carscar1.accelerate(30)car2.accelerate(20)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Lastly, you will display the current speed of each car by utilizing the get_speed method.

123# Print the current speeds of the carsprint(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Next steps

In conclusion, this reading provides a fundamental understanding of objects and classes in Python, essential concepts in object-oriented programming. Classes serve as blueprints for creating objects, encapsulating data attributes and methods. Objects represent real-world entities and possess their unique state and behavior. The structured code example presented in the reading outlines the key elements of a class, including class attributes, the constructor method for initializing instance attributes, and instance methods for defining object-specific functionality.

In the upcoming laboratory session, you can apply the concepts of objects and classes to gain hands-on experience.

---

### 11. [READING] Module 3 Summary: Python Programming Fundamentals Reading • 5 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/bqVzB/module-3-summary-python-programming-fundamentals
- **Method:** `dom_reading_cml` | **Length:** 4737 chars

Congratulations! You have completed this module. At this point, you know that:

- Python conditions use “if” statements to execute code based on true/false conditions created by comparisons and Boolean expressions.
- Comparison operations require using comparison operators such as == (equal to), > (greater than), and < (less than).
- Python uses the "!=" operator to determine whether two values are not equal.
- You can compare integers, strings, and floats.
- Python branching directs program flow by using conditional statements (for example, if, else, elif) to execute different code blocks based on conditions or tests.
- You can use the "if" statement with conditions to define actions if true.
- To perform actions when all previous conditions are false, you can use the "else" statement without a condition.
- The elif statement allows for additional checks only if the initial condition is false.
- To execute various operations on Boolean values, we use Boolean logic operators.
- Python loops are control structures that automate repetitive tasks and iterate over data structures like lists or dictionaries.
- The range() function generates a sequence of numbers with a specified start, stop, and step value for loops in Python.
- A for loop in Python iterates over a sequence, such as a list, tuple, or string, and executes a block of code for each item in the sequence.
- A while loop in Python executes a block of code as long as a specified condition remains true.
- Python functions are reusable code blocks that perform specific tasks, take input parameters, and often return results, enhancing code modularity and reusability.
- You may or may not have written the codes that are often included in functions.
- Python has a set of built-in functions such as "len" to find the length of a sequence or "sum" to find the total sum of a sequence.
- The "sorted" function creates a new sorted list, while "sort" sorts items in the original list.
- You can also create your own functions in Python.
- To ensure clarity and organization and facilitate understanding and maintenance of the code, developers must document functions using a documentation string enclosed in three quotes.
- The help command will return the documentation defined for a particular function.
- A function can have multiple parameters.
- If a function does not include a return statement, it returns None by default.
- You can use the "pass" keyword in a function to indicate that it does nothing (a placeholder for future code).
- A function will usually perform more than one task.
- In Python, the scope of a variable determines where you can access or modify that variable. Global scope allows access from anywhere, while local scope restricts it to a block or function.
- In Python, a programmer defines a local variable within a specific block or function, which can only be accessed or modified within that block or function.
- In Python, a global variable is a variable defined at the top level of a program that any part of the code can access or modify.
- Exception handling in Python is a mechanism for managing and responding to errors and exceptions that may occur during program execution, preventing them from crashing the program.
- In Python, you use the "try-except" statement to attempt a block of code and specify alternative actions to execute if an error occurs, allowing you to handle exceptions.
- In Python, you use the "try-except-else" statement to attempt a block of code, handle exceptions in the "except" block, and execute code in the "else" block when no exceptions occur.
- Python developers use the "try-except-else-finally" statement to attempt a block of code, catch exceptions in the "except" block, execute code in the "else" block when no exceptions occur, and ensure that the "finally" block always runs, regardless of whether exception was raised or not.
- In Python, objects are instances of classes that encapsulate data and behavior, serving as the foundation for creating and working with various data types and custom data structures.
- To determine the type of an object in Python, you can use the `type()` command.
- Methods may modify an object’s internal state, but the object’s type usually remains the same.
- Classes in Python are blueprints for creating objects, defining their attributes and methods, enabling code organization, and object-oriented programming.
- Function "init" is a special method used to initialize data attributes.
- We can create instances of a class in Python.
- Data attributes consist of the data defining the objects.
- Methods are functions that interact and change the data attributes.
- The method has a function that requires the self as well as other parameters.

---

### 12. [READING] Cheat Sheet: Python Programming Fundamentals Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/3vVPB/cheat-sheet-python-programming-fundamentals
- **Method:** `dom_reading_cml` | **Length:** 13707 chars

Use this cheat sheet for various packages/methods, their descriptions, and examples.

### AND

Returns True if both statement1 and statement2 are True. Otherwise, returns False.

Example:

1statement1 and statement2 Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Syntax:

123456789marks = 90attendance_percentage = 87 if marks >= 80 and attendance_percentage >= 85:    print("qualify for honors")else:    print("Not qualified for honors") # Output = qualify for honorsInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Class Definition

Defines a blueprint for creating objects and defining their attributes and behaviors.

Syntax:

1class ClassName: # Class attributes and methods Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1234class Person:     def __init__(self, name, age):         self.name = name         self.age = ageInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Define Function

A function is a reusable block of code that performs a specific task or set of tasks when called.

Syntax:

1def function_name(parameters): # Function body Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1def greet(name): print("Hello,", name)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Equal (==)

Checks if two values are equal.

Syntax:

1variable1 == variable2 Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example 1:

15 == 5 Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.returns True

Example 2:

12age = 25 age == 30 Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.returns False

### For Loop

A for loop repeatedly executes a block of code for a specified number of iterations or over a sequence of elements (list, range, string, etc.).

Syntax:

1for variable in sequence: # Code to repeat Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example 1:

12for num in range(1, 10):     print(num) Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example 2:

123fruits = ["apple", "banana", "orange", "grape", "kiwi"] for fruit in fruits:    print(fruit)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Function Call

A function call is the act of executing the code within the function using the provided arguments.

Syntax:

1function_name(arguments) Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1greet("Alice")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Greater Than or Equal To(>=)

Checks if the value of variable1 is greater than or equal to variable2.

Syntax:

1variable1 >= variable2Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example 1:

15 >= 5 and 9 >= 5 Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.returns True

Example 2:

123quantity = 105 minimum = 100 quantity >= minimum Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.returns True

### Greater Than(>)

Checks if the value of variable1 is greater than variable2.

Syntax:

1variable1 > variable2 Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example 1:

19 > 6Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.returns True

Example 2:

123age = 20 max_age = 25 age > max_age Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.returns False

### If Statement

Executes code block if the condition is True.

Syntax:

1if condition: #code block for if statement Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

12if temperature > 30:     print("It's a hot day!")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### If-Elif-Else

Executes the first code block if condition1 is True, otherwise checks condition2, and so on. If no condition is True, the else block is executed.

Syntax:

12345678if condition1:# Code if condition1 is True elif condition2:# Code if condition2 is True else:# Code if no condition is TrueInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

123456789score = 85  # Example scoreif score >= 90:    print("You got an A!")elif score >= 80:    print("You got a B.")else:    print("You need to work harder.") # Output = You got a B.Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### If-Else Statement

Executes the first code block if the condition is True, otherwise the second block.

Syntax:

12if condition: # Code, if condition is True else: # Code, if condition is False Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1234if age >= 18:    print("You're an adult.")else:    print("You're not an adult yet.")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Less Than or Equal To(<=)

Checks if the value of variable1 is less than or equal to variable2.

Syntax:

1variable1 <= variable2           Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example 1:

15 <= 5 and 3 <= 5 Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.returns True

Example 2:

123size = 38 max_size = 40 size <= max_size Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.returns True

### Less Than(<)

Checks if the value of variable1 is less than variable2.

Syntax:

1variable1 < variable2Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example 1:

14 < 6 Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.returns True

Example 2:

123score = 60 passing_score = 65 score < passing_score Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.returns True

### Loop Controls

break exits the loop prematurely. continue skips the rest of the current iteration and moves to the next iteration.

Syntax:

1234567for: # Code to repeat     if # boolean statement        break  for: # Code to repeat      if # boolean statement        continueInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example 1:

1234for num in range(1, 6):    if num == 3:        break    print(num)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example 2:

1234for num in range(1, 6):    if num == 3:        continue    print(num)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### NOT

Returns True if variable is False, and vice versa.

Syntax:

1not variableInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

12isLocked = Falseprint(not isLocked)  Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.returns True if the variable is False (i.e., unlocked).

### Not Equal(!=)

Checks if two values are not equal.

Syntax:

1variable1 != variable2 Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example 1:

123a = 10 b = 20 a != b Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.returns True

Example 2:

12count=0 count != 0 Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.returns False

### Object Creation

Creates an instance of a class (object) using the class constructor.

Syntax:

1object_name = ClassName(arguments) Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1person1 = Person("Alice", 25)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### OR

Returns True if either statement1 or statement2 (or both) are True. Otherwise, returns False.

Syntax:

1statement1 or statement2Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

123456"Farewell Party Invitation" grade = 12 if grade == 11 or grade == 12:    print("Farewell Party Invitation")else:    print("Not eligible") Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.returns True

### range()

Generates a sequence of numbers within a specified range.

Syntax:

123range(stop) range(start, stop) range(start, stop, step) Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

123range(5) #generates a sequence of integers from 0 to 4. range(2, 10) #generates a sequence of integers from 2 to 9. range(1, 11, 2) #generates odd integers from 1 to 9.Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Return Statement

Return is a keyword used to send a value back from a function to its caller.

Syntax:

1return value Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

12def add(a, b): return a + b result = add(3, 5)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Try-Except Block

Tries to execute the code in the try block. If an exception of the specified type occurs, the code in the except block is executed.

Syntax:

12try: # Code that might raise an exception except ExceptionType: # Code to handle the exception Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1234try:     num = int(input("Enter a number: ")) except ValueError:     print("Invalid input. Please enter a valid number.")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Try-Except with Else Block

Code in the else block is executed if no exception occurs in the try block.

Syntax:

123try: # Code that might raise an exception except ExceptionType: # Code to handle the exception else: # Code to execute if no exception occurs Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

123456try:     num = int(input("Enter a number: ")) except ValueError:     print("Invalid input. Please enter a valid number") else:     print("You entered:", num)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Try-Except with Finally Block

Code in the finally block always executes, regardless of whether an exception occurred.

Syntax:

123try: # Code that might raise an exception except ExceptionType: # Code to handle the exception finally: # Code that always executes Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1234567try:     file = open("data.txt", "r")     data = file.read() except FileNotFoundError:     print("File not found.") finally:     file.close()Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### While Loop

A while loop repeatedly executes a block of code as long as a specified condition remains True.

Syntax:

1while condition: # Code to repeat Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1234count = 0 while count < 5:    print(count)    count += 1Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.

---

### 13. [READING] Module 3 Glossary: Python Programming Fundamentals Reading • 5 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/9mpgr/module-3-glossary-python-programming-fundamentals
- **Method:** `dom_reading_cml` | **Length:** 4688 chars

Welcome! This alphabetized glossary contains many of the terms you'll find within this course. This comprehensive glossary also includes additional industry-recognized terms not used in course videos. These terms are important for you to recognize when working in the industry, participating in user groups, and participating in other certificate programs.

| Term | Definition |
| --- | --- |
| Analogy | Refers to a concept or comparison outside the scope of the programming language itself, used to explain or relate one concept to another in a more understandable way. |
| Attributes | Attributes in Python refer to the characteristics or properties of an object, and they can be accessed using dot notation. |
| Branching | Branching in Python is a process of altering the flow of a program based on conditions, typically using if, elif, and else statements. |
| Comparison operators | Comparison operators in Python are used to compare values and return Boolean results (True or False), including operators like == (equal),!= (not equal), < (less than), > (greater than), <= (less than or equal to), and >= (greater than or equal to). |
| Conditions | Conditions in Python are used to make decisions in code, executing specific blocks of code based on whether a given expression evaluates to True or False. |
| Enumerate | In Python, "enumerate" is a built-in function that adds a counter to an iterable, allowing you to loop through both the elements and their corresponding indices. |
| Exception handling | Exception handling in Python is a mechanism for gracefully managing and responding to errors or exceptional conditions that may occur during program execution. |
| Explicitly | In Python, the term "explicitly" refers to performing an action or specifying something in a clear, unambiguous, and direct manner. |
| For loops | For loops in Python are used for iterating over a sequence (such as a list, tuple, or string) or other iterable objects, executing a set of statements for each item in the sequence. |
| Global variable | Global variables in Python are variables defined outside of any function or block and can be accessed and modified from any part of the code. |
| Incremented | "Incremented" in Python means to increase the value of a variable by a specified amount, typically done using the += operator or by adding a fixed value. |
| Indent | In Python, "indent" refers to the use of whitespace at the beginning of a line to signify the structure and scope of code blocks, such as loops and functions. |
| Indices | In Python, "indices" refer to the position or location of elements in a sequence, like a string, list, or tuple, starting with 0 for the first element. |
| Iterate | In Python, "iterate" means to repeatedly perform a set of operations or steps on each item in a collection, such as a list, tuple, or dictionary, typically using loops or iterators. |
| Local variables | Local variables in Python are variables defined within a specific function or block of code and are only accessible within that function or block. |
| Logic operators | Logic operators in Python are used to perform logical operations on Boolean values, including operators like and (logical AND), or (logical OR), and not (logical NOT). |
| Loops | Loops in Python are constructs for repeating a block of code, enabling the execution of the same code multiple times. |
| Parameters | Parameters in Python are placeholders in a function definition, used to accept and work with values provided to the function when it is called. |
| Programming Fundamentals | Programming fundamentals in Python involve variables, control structures, functions, data structures, input/output, and error handling for building software. |
| Range function | The range function in Python generates a sequence of numbers that can be used for iterating in a loop and is typically used as range (start, stop, step), where it creates numbers from start to stop-1 with the given step increment. |
| Scope of function | The "scope of a function" in Python refers to the region of code where a variable defined within that function is accessible or visible. |
| Sequences | Sequences in Python are ordered collections of items that can include data types like strings, lists, and tuples, allowing for indexing and iteration. |
| Syntax | In Python, "Syntax" refers to the set of rules that dictate how code must be written and structured to be correctly interpreted by the Python interpreter. It includes correct use of keywords, indentation, operators, and punctuation. |
| While loops | While loops in Python are used to repeatedly execute a block of code as long as a specified condition is true. |

---
