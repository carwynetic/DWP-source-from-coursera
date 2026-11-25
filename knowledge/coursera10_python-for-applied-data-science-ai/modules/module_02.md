# Module 2: Python Data Structures

### 1. [VIDEO TRANSCRIPT] Lists and Tuples Video • 8 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/bUWEy/lists-and-tuples
- **Method:** `dom_transcript` | **Length:** 7487 chars

In this video, we will cover lists and tuples. These are called compound data types and are one of the key types of data structures in Python. Tuples Tuples are an ordered sequence. Here is a tuple ratings. Tuples are expressed as comma-separated elements within parentheses. These are values inside the parentheses. In Python, there are different types, strings, integer, float.

They can all be contained in a tuple, but the type of the variable is tuple. Each element of a tuple can be accessed via an index. The following table represents the relationship between the index and the elements in the tuple. The first element can be accessed by the name of the tuple followed by a square bracket with the index number. In this case, zero. We can access the second element as follows. We can also access the last element.

In Python, we can use negative index. The relationship is as follows. The corresponding values are shown here. We can concatenate or combine tuples by adding them. The result is the following with the following index. If we would like multiple elements from a tuple, we can also slice tuples. For example, if we want the first three elements, we use the following command.

The last index is one larger than the index you want. Similarly, if we want the last two elements, we use the following command. Notice how the last index is one larger than the last index of the tuple. We can use the len command to obtain the length of a tuple. As there are five elements, the result is five. Tuples are immutable, which means we can't change them. To see why this is important, let's see what happens when we set the variable ratings 1 to ratings.

Let's use the image to provide a simplified explanation of what's going on. Each variable does not contain a tuple, but references the same immutable tuple object. See the Objects and Classes module for more about objects. Let's say we want to change the element at index 2. Because tuples are immutable, we can't. Therefore, ratings 1 will not be affected by a change in rating because the tuple is immutable, i.e. we can't change it. We can assign a different tuple to the ratings variable.

The variable ratings now references another tuple. As a consequence of immutability, if we would like to manipulate a tuple, we need to create a new object instead. For example, if we would like to sort a tuple, we use the function sorted. The input is the original tuple. The output is a new sorted list. For more on functions, see our video on functions. A tuple can contain other tuples as well as other complex data types.

This is called nesting. We can access these elements using the standard indexing methods. If we select an index with a tuple, the same index convention applies. As such, we can then access values in the tuple. For example, we could access the second element. We can apply this indexing directly to the tuple variable nt. It is helpful to visualize this as a tree.

We can visualize this nesting as a tree. The tuple has the following indexes. If we consider indexes with other tuples, we see the tuple at index 2 contains a tuple with two elements. We can access those two indexes. The same convention applies to index 3. We can access the elements in those tuples as well. We can continue the process.

We can even access deeper levels of the tree by adding another square bracket. We can access different characters in the string, or various elements in the second tuple contained in the first. Lists are also a popular data structure in Python. Lists are also an ordered sequence. Here is a list L. A list is represented with square brackets. In many respects, lists are like tuples.

One key difference is they are mutable. Lists can contain strings, floats, integers. We can nest other lists. We also nest tuples and other data structures. The same indexing conventions apply for nesting. Like tuples, each element of a list can be accessed via an index. The following table represents the relationship between the index and the elements in the list.

The first element can be accessed by the name of the list followed by a square bracket with the index number, in this case, 0. We can access the second element as follows. We can also access the last element. In Python, we can use a negative index. The relationship is as follows. The corresponding indexes are as follows. We can also perform slicing in lists.

For example, if we want the last two elements in this list, we use the following command. Notice how the last index is one larger than the length of the list? The index conventions for lists and tuples are identical. Check the labs for more examples. We can concatenate or combine lists by adding them. The result is the following. The new list has the following indices.

Lists are mutable, therefore we can change them. For example, we apply the method extends by adding a dot followed by the name of the method, and then parentheses. The argument inside the parentheses is a new list that we are going to concatenate to the original list. In this case, instead of creating a new list, L1, the original list, L, is modified by adding two new elements. To learn more about methods, check out our video on objects and classes. Another similar method is append. If we apply append instead of extended, we add one element to the list.

If we look at the index, there is only one more element. Index 3 contains the list we appended. Every time we apply a method, the list changes. If we apply extend, we add two new elements to the list. The list L is modified by adding two new elements. If we append the string A, we further change the list adding the string A. As lists are mutable, we can change them.

For example, we can change the first element as follows. The list now becomes HardRock 10 1.2. We can delete an element of a list using the del command. We simply indicate the list item we would like to remove as an argument. For example, if we would like to remove the first element, the result becomes 10 1.2. We can delete the second element. This operation removes the second element off the list.

We can convert a string to a list using split. For example, the method split converts every group of characters separated by a space into an element of a list. We can use the split function to separate strings on a specific character, known as a delimiter. We simply pass the delimiter we would like to split on as an argument, in this case a comma. The result is a list, each element corresponds to a set of characters that have been separated by a comma. When we set one variable, b, equal to a, both a and b are referencing the same list. Multiple names referring to the same object is known as aliasing.

We know from the list slide that the first element in b is set as HardRock. If we change the first element in a to banana, we get a side effect. The value of b will change as a consequence. a and b are referencing the same list, therefore if we change a, list b also changes. If we check the first element of b after changing list a, we get banana instead of HardRock. You can clone list a by using the following syntax. Variable a references one list. Variable b references a new copy or clone of the original list.

Now if you change a, b will not change. We can get more info on lists, tuples, and many other objects in Python using the help command. Simply pass in the list, tuple, or any other Python object. See the labs for more things you can do with lists.

---

### 2. [READING] Cheat Sheet: Lists and Tuples Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/mdRVq/cheat-sheet-lists-and-tuples
- **Method:** `dom_reading_cml` | **Length:** 9205 chars

Use this cheat sheet for various packages/methods, their descriptions, and examples.

## List

### append()

The append() method is used to add an element to the end of a list.

Syntax:

1list_name.append(element)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

12fruits = ["apple", "banana", "orange"] fruits.append("mango") print(fruits)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### copy()

The copy() method is used to create a shallow copy of a list.

Example:

123my_list = [1, 2, 3, 4, 5] new_list = my_list.copy() print(new_list) # Output: [1, 2, 3, 4, 5]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### count()

The count() method is used to count the number of occurrences of a specific element in a list in Python.

Example:

123my_list = [1, 2, 2, 3, 4, 2, 5, 2] count = my_list.count(2) print(count) # Output: 4Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Creating a List

A list is a built-in data type that represents an ordered and mutable collection of elements. Lists are enclosed in square brackets [] and elements are separated by commas.

Example:

1fruits = ["apple", "banana", "orange", "mango"]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### del

The del statement is used to remove an element from list. It removes the element at the specified index.

Example:

123my_list = [10, 20, 30, 40, 50] del my_list[2] # Removes the element at index 2 print(my_list) # Output: [10, 20, 40, 50]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### extend()

The extend() method is used to add multiple elements to a list. It takes an iterable (such as another list, tuple, or string) and appends each element of the iterable to the original list.

Syntax:

1list_name.extend(iterable) Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1234fruits = ["apple", "banana", "orange"] more_fruits = ["mango", "grape"] fruits.extend(more_fruits) print(fruits)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Indexing

Indexing in a list allows you to access individual elements by their position. In Python, indexing starts from 0 for the first element and goes up to 'length_of_list - 1'.

Example:

12345my_list = [10, 20, 30, 40, 50] print(my_list[0]) # Output: 10 (accessing the first element) print(my_list[-1]) # Output: 50 (accessing the last element using negative indexing)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### insert()

The insert() method is used to insert an element.

Syntax:

1list_name.insert(index, element) Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

123my_list = [1, 2, 3, 4, 5] my_list.insert(2, 6) print(my_list)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Modifying a List

You can use indexing to modify or assign new values to specific elements in the list.

Example:

1234my_list = [10, 20, 30, 40, 50] my_list[1] = 25 # Modifying the second element print(my_list) # Output: [10, 25, 30, 40, 50]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### pop()

The pop() method is another way to remove an element from a list in Python. It removes and returns the element at the specified index. If you don't provide an index to the pop() method, it will remove and return the last element of the list by default

Example 1:

1234567my_list = [10, 20, 30, 40, 50] removed_element = my_list.pop(2) # Removes and returns the element at index 2 print(removed_element) # Output: 30  print(my_list) # Output: [10, 20, 40, 50] Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example 2:

1234567my_list = [10, 20, 30, 40, 50] removed_element = my_list.pop() # Removes and returns the last element print(removed_element) # Output: 50  print(my_list) # Output: [10, 20, 30, 40]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### remove()

To remove an element from a list. The remove() method removes the first occurrence of the specified value.

Example:

1234my_list = [10, 20, 30, 40, 50] my_list.remove(30) # Removes the element 30 print(my_list) # Output: [10, 20, 40, 50]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### reverse()

The reverse() method is used to reverse the order of elements in a list

Example:

123my_list = [1, 2, 3, 4, 5] my_list.reverse() print(my_list) # Output: [5, 4, 3, 2, 1]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Slicing

You can use slicing to access a range of elements from a list.

Syntax:

1list_name[start:end:step] Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

123456789101112my_list = [1, 2, 3, 4, 5] print(my_list[1:4]) # Output: [2, 3, 4] (elements from index 1 to 3) print(my_list[:3]) # Output: [1, 2, 3] (elements from the beginning up to index 2)  print(my_list[2:]) # Output: [3, 4, 5] (elements from index 2 to the end)  print(my_list[::2]) # Output: [1, 3, 5] (every second element)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### sort()

The sort() method is used to sort the elements of a list in ascending order. If you want to sort the list in descending order, you can pass the 'reverse=True' argument to the sort() method.

Example 1:

1234my_list = [5, 2, 8, 1, 9] my_list.sort() print(my_list) # Output: [1, 2, 5, 8, 9] Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example 2:

1234my_list = [5, 2, 8, 1, 9] my_list.sort(reverse=True) print(my_list) # Output: [9, 8, 5, 2, 1]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Tuple

### count()

The count() method for a tuple is used to count how many times a specified element appears in the tuple.

Syntax:

1tuple.count(value)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

123fruits = ("apple", "banana", "apple", "orange")print(fruits.count("apple")) #Counts the number of times apple is found in tuple.#Output: 2Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### index()

The index() method in a tuple is used to find the first occurrence of a specified value and returns its position (index). If the value is not found, it raises a ValueError.

Syntax:

1tuple.index(value) Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

123fruits = ("apple", "banana", "orange","apple")print(fruits.index("apple")) #Returns the index value at which apple is present.#Output: 0Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### sum()

The sum() function in Python can be used to calculate the sum of all elements in a tuple, provided that the elements are numeric (integers or floats).

Syntax:

1sum(tuple) Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

123numbers = (10, 20, 5, 30)print(sum(numbers))#Output: 65Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### min() and max()

Find the smallest (min()) or largest (max()) element in a tuple.

Example:

12345numbers = (10, 20, 5, 30)print(min(numbers))  #Output: 5print(max(numbers))#Output: 30Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### len()

Get the number of elements in the tuple using len().

Syntax:

1len(tuple)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

123fruits = ("apple", "banana", "orange")print(len(fruits)) #Returns length of the tuple.#Output: 3Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.

---

### 3. [VIDEO TRANSCRIPT] Dictionaries Video • 2 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/4c7Hw/dictionaries
- **Method:** `dom_transcript` | **Length:** 2134 chars

Let's cover dictionaries in Python. Dictionaries are a type of collection in Python. If you recall, a list has integer indexes. These are like addresses. A list also has elements. A dictionary has keys and values. The key is analogous to the index.

They are like addresses, but they don't have to be integers. They are usually characters. The values are similar to the element in a list and contain information. To create a dictionary, we use curly brackets. The keys are the first elements. They must be immutable and unique. Each key is followed by a value separated by a colon.

The values can be immutable, mutable, and duplicates. Each key and value pair is separated by a comma. Consider the following example of a dictionary. The album title is the key, and the value is the release data. We can use yellow to highlight the keys and leave the values in white. It is helpful to use the table to visualize a dictionary where the first column represents the keys and the second column represents the values. We can add a few more examples to the dictionary.

We can also assign the dictionary to a variable. The key is used to look up the value. We use square brackets. The argument is the key. This outputs the value. Using the key of back in black, this returns the value of 1980. The key the dark side of the moon gives us the value of 1973.

Using the key the bodyguard gives us the value 1992, and so on. We can add a new entry to the dictionary as follows. This will add the value 2007 with a new key called graduation. We can delete an entry as follows. This gets rid of the key thriller and its value. We can verify if an element is in the dictionary using the in command as follows. The command checks the keys.

If they are in the dictionary, they return a true. If we try the same command with a key that is not in the dictionary, we get a false. In order to see all the keys in a dictionary, we can use the method keys to get the keys. The output is a list like object with all the keys. In the same way, we can obtain the values using the method values. Check out the labs for more examples and info on dictionaries.

---

### 4. [VIDEO TRANSCRIPT] Sets Video • 5 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/7GcLY/sets
- **Method:** `dom_transcript` | **Length:** 4174 chars

Let's cover sets. They are also a type of collection. Sets are a type of collection. This means that like lists and tuples, you can input different Python types. Unlike lists and tuples, they are unordered. This means sets do not record element position. Sets only have unique elements. This means there is only one of a particular element in a set.

To define a set, you use curly brackets. You place the elements of a set within the curly brackets. You notice there are duplicate items. When the actual set is created, duplicate items will not be present. You can convert a list to a set by using the function set. This is called typecasting. You simply use the list as the input to the function set. The result will be a list converted to a set.

Let's go over an example. We start off with a list. We input the list to the function set. The function set returns a set. Notice how there are no duplicate elements. Let's go over set operations. These can be used to change the set.

Consider the set A. Let's represent this set with a circle. If you are familiar with sets, this can be part of a Venn diagram. A Venn diagram is a tool that uses shapes usually to represent sets. We can add an item to a set using the add method. We just put the set name followed by a dot, then the add method. The argument is the new element of the set we would like to add, in this case, inSync.

The set A now has inSync as an item. If we add the same item twice, nothing will happen as there can be no duplicates in a set. Let's say we would like to remove inSync from set A. We can also remove an item from a set using the remove method. We just put the set name followed by a dot, then the remove method. The argument is the element of the set we would like to remove, in this case, inSync. After the remove method is applied to the set, set A does not contain the item inSync.

You can use this method for any item in the set. We can verify if an element is in the set using the in command as follows. The command checks that the item, in this case, ACDC, is in the set. If the item is in the set, it returns true. If we look for an item that is not in the set, in this case for the item Who, as the item is not in the set, we will get a false. These are types of mathematical set operations. There are other operations we can do.

There are lots of useful mathematical operations we can do between sets. Let's define the set AlbumSet1. We can represent it using a red circle or Venn diagram. Similarly, we can define the set AlbumSet2. We can also represent it using a blue circle or Venn diagram. The intersection of two sets is a new set containing elements which are in both of those sets. It's helpful to use Venn diagrams.

The two circles that represent the sets combine. The overlap represents the new set. As the overlap is comprised of the red circle and blue circle, we define the intersection in terms of AND. In Python, we use an ampersand to find the intersection of two sets. If we overlay the values of the set over the circle placing the common elements in the overlapping area, we see the correspondence. After applying the intersection operation, all the items that are not in both sets disappear. In Python, we simply just place the ampersand between the two sets.

We see that both ACDC and BackInBlack are in both sets. The result is a new set AlbumSet3 containing all the elements in both AlbumSet1 and AlbumSet2. The union of two sets is the new set of elements which contain all the items in both sets. We can find the union of the sets AlbumSet1 and AlbumSet2 as follows. The result is a new set that has all the elements of AlbumSet1 and AlbumSet2. This new set is represented in green. Consider the new album SetAlbumSet3.

The set contains the elements ACDC and BackInBlack. We can represent this with a Venn diagram, as all the elements in AlbumSet3 are in AlbumSet1. The circle representing AlbumSet1 encapsulates the circle representing AlbumSet3. We can check if a set is a subset using the isSubset method. As AlbumSet3 is a subset of the AlbumSet1, the result is true. There is a lot more you can do with sets. Check out the lab for more examples.

---

### 5. [READING] Module 2 Summary: Python Data Structures Reading • 5 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/oRkkv/module-2-summary-python-data-structures
- **Method:** `dom_reading_cml` | **Length:** 3115 chars

Congratulations! You have completed this module. At this point, you know that:

- In Python, we often use tuples to group related data together.Tuples refer to ordered and immutable collections of elements.
- Tuples are usually written as comma-separated elements in parentheses “()".
- You can include strings, integers, and floats in tuples and access them using both positive and negative indices.
- You can perform operations such as combining, concatenating, and slicing on tuples.
- Tuples are immutable, so you need to create a new tuple to manipulate it.
- Tuples, termed nesting, can include other tuples of complex data types.
- You can access elements in a nested tuple through indexing.
- Lists in Python contain ordered collections of items that can hold elements of different types and are mutable, allowing for versatile data storage and manipulation.
- A list is an ordered sequence, represented with square brackets "[]".
- Lists possess mutability, rendering them akin to tuples.
- A list can contain strings, integers, and floats; you can nest lists within it.
- You can access each element in a list using both positive and negative indexing.
- Concatenating or appending a list will result in the modification of the same list.
- You can perform operations such as adding, deleting, splitting, and so forth on a list.
- You can separate elements in a list using delimiters.
- Aliasing occurs when multiple names refer to the same object.
- You can also clone a list to create another list.
- Dictionaries in Python are key-value pairs that provide a flexible way to store and retrieve data based on unique keys.
- Dictionaries consist of keys and values, both composed of string elements.
- You denote dictionaries using curly brackets.
- The keys necessitate immutability and uniqueness.
- The values may be either immutable or mutable, and they allow duplicates.
- You separate each key-value pair with a comma, and you can use color highlighting to make the key more visible.
- You can assign dictionaries to a variable.
- You use the key as an argument to retrieve the corresponding value.
- You can make additions and deletions to dictionaries.
- You can perform an operation on a dictionary to check the key, which results in a true or false output.
- You can apply methods to obtain a list of keys and values in a dictionary.
- Sets in Python are collections of unique elements, useful for tasks such as removing duplicates and performing set operations like union and intersection. Sets lack order.
- Curly brackets "{}" are helpful for defining elements of a set.
- Sets do not contain duplicate items.
- A list passed through the set function generates a set containing unique elements.
- You use “Set Operations” to perform actions such as adding, removing, and verifying elements in a set.
- You can combine sets using the ampersand "&" operator to obtain the common elements from both sets.
- You can use the Union function to combine two sets, including both the common and unique elements from both sets.
- The sub-set method is used to determine if two or more sets are subsets.

---

### 6. [READING] CheatSheet: Dictionaries & Sets Reading • 10 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/RdPlN/cheatsheet-dictionaries-sets
- **Method:** `dom_reading_cml` | **Length:** 8417 chars

Use this cheat sheet for various packages/methods, their descriptions, and examples.

## Dictionaries

### Creating a Dictionary

A dictionary in Python is a built-in data structure that stores information in key-value pairs. Each key must be unique, and it is used to access its corresponding value. Dictionaries are enclosed in curly braces {}, and each pair is separated by a comma.

Example:

12dict_name = {} #Creates an empty dictionaryperson = { "name": "John",  "age": 30, "city": "New York"}Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Accessing Values

You can access the values in a dictionary using their corresponding keys.

Syntax:

1Value = dict_name["key_name"]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

12name = person["name"]age = person["age"]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Add or modify

You can add or modify elements in a dictionary by assigning a value to a key using the assignment operator =. When you assign a value to a key that does not already exist, Python automatically creates a new key-value pair and adds it to the dictionary. However, if the key already exists, the existing value will be replaced with the new one.

Syntax:

1dict_name[key] = valueInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

12person["Country"] = "USA" # A new entry will be created.person["city"] = "Chicago"  # Update the existing value for the same keyInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### del

Removes the specified key-value pair from the dictionary. Raises a KeyError if the key does not exist.

Syntax:

1del dict_name[key]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1del person["Country"]Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Key existence

You can check for the existence of a key in a dictionary using the in keyword.

Example:

12if "name" in person:    print("Name exists in the dictionary.")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Keys()

Retrieves all keys from the dictionary and converts them into a list. Useful for iterating or processing keys using list methods.

Syntax:

1keys_list = list(dict_name.keys())Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1person_keys = list(person.keys())Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Values()

Extracts all values from the dictionary and converts them into a list. This list can be used for further processing or analysis.

Syntax:

1values_list = list(dict_name.values())Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1person_values = list(person.values())Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Items()

Retrieves all key-value pairs as tuples and converts them into a list of tuples. Each tuple consists of a key and its corresponding value.

Syntax:

1items_list = list(dict_name.items())Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1info = list(person.items())Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
## Sets

### Add()

Add elements to a set. You can use the add() method to insert a new element into a set. If the element already exists, it will not be added again, since sets automatically store only unique values.

Syntax:

1set_name.add(element) Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1fruits.add("mango")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Defining Sets

A set in Python is an unordered collection that stores unique elements, meaning it automatically removes duplicates. Sets are enclosed in curly braces {} and are commonly used when you need to store a group of distinct values or perform mathematical operations such as union, intersection, and difference.

Because sets are unordered, the elements have no fixed position or index, and their order may change each time you print or iterate over them.

Example: Note that these two sets will be used in the examples that follow.

123empty_set = set() #Creating an Empty Set fruits = {"apple", "banana", "orange"}colors = ("orange", "red", "green")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### in

Checks if an element exists in a set. Use the in keyword to verify whether a specific element is present in a set. It returns True if the element exists, and False otherwise.

Syntax:

1element in set_nameInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1"banana" in fruitsInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### issubset()

Check if one set is a subset of another. The issubset method is used to determine whether all elements of one set exist within another set. If every element of the current set is found in the specified set, it returns True; otherwise, it returns False.

Syntax:

1is_subset = set1.issubset(set2)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1is_subset = fruits.issubset(colors)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### issuperset()

Check if one set is a superset of another. The issuperset() method is used to verify whether the current set contains all elements of another set. It returns True if every element of the specified set exists within the current set; otherwise, it returns False.

Syntax:

1is_superset = set1.issuperset(set2) Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1is_superset = colors.issuperset(fruits)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### remove()

Remove a specific element from a set. The remove() method is used to delete a particular element from a set. If the element you try to remove does not exist, Python will raise a KeyError, which means you must ensure the element is present before calling this method.

This method is useful when you are certain that the item you want to remove is already in the set.

Syntax:

1set_name.remove(element) Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1fruits.remove("banana")Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
### Set Operations

Perform various operations on sets: union, intersection, difference, symmetric difference.

Syntax:

1234union_set = set1.union(set2) intersection_set = set1.intersection(set2) difference_set = set1.difference(set2) sym_diff_set = set1.symmetric_difference(set2) Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.Example:

1234combined = fruits.union(colors) common = fruits.intersection(colors) unique_to_fruits = fruits.difference(colors) sym_diff = fruits.symmetric_difference(colors)Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
##

---

### 7. [READING] Module 2 Glossary: Python Data Structures Reading • 5 min
- **URL:** https://www.coursera.org/learn/python-for-applied-data-science-ai/supplement/gAEWZ/module-2-glossary-python-data-structures
- **Method:** `dom_reading_cml` | **Length:** 3523 chars

Welcome! This alphabetized glossary contains many of the terms in this course. This comprehensive glossary also includes additional industry-recognized terms not used in course videos. These terms are important for you to recognize when working in the industry, participating in user groups, and participating in other certificate programs.

| Term | Definition |
| --- | --- |
| Aliasing | Aliasing refers to giving another name to a function or a variable. |
| Ampersand | A character typically "&" standing for the word "and." |
| Compound elements | Compound statements contain (groups of) other statements; they affect or control the execution of those other statements in some way. |
| Delimiter | A delimiter in Python is a character or sequence of characters used to separate or mark the boundaries between elements or fields within a larger data structure, such as a string or a file. |
| Dictionaries | A dictionary in Python is a data structure that stores a collection of key-value pairs, where each key is unique and associated with a specific value. |
| Function | A function is a block of code, defining a set procedure, which is executed only when it is called. |
| Immutable | Immutable Objects are of in-built datatypes like int, float, bool, string, Unicode, and tuple. In simple words, an immutable object can't be changed after it is created. |
| Intersection | The intersection of two sets is a new set containing only the elements that are present in both sets. |
| Keys | The keys () method in Python Dictionary, returns a view object that displays a list of all the keys in the dictionary in order of insertion using Python. |
| Lists | A list is any list of data items, separated by commas, inside square brackets. |
| Logic operations | In Python, logic operations refer to the use of logical operators such as "and," "or," and "not" to perform logical operations on Boolean values (True or False). |
| Mutable | Mutable objects in Python are objects whose values can be changed after they are created. These objects allow modifications such as adding, removing, or altering elements without creating a new object. |
| Nesting | A nested function is simply a function within another function and is sometimes called an "inner function". |
| Ratings in python | Ratings in Python typically refer to a numerical or qualitative measure assigned to something to indicate its quality, performance, or value. |
| Set operations | Set operations in Python refer to mathematical operations performed on sets, which are unordered collections of unique elements. |
| Sets in python | A set is an unordered collection of unique elements. |
| Syntax | The rules that define the structure of the language for python is called its syntax. |
| Tuples | These are used store multiple items in a single variable. |
| Type casting | In python, this is converting one data type to another. |
| Variables | In python, a variable is a symbolic name or identifier used to store and manipulate data. Variables serve as containers for values, and these values can be of various data types, including numbers, strings, lists, and more. |
| Venn diagram | A Venn diagram is a graphical representation that uses overlapping circles to illustrate the relationships and commonalities between sets or groups of items. |
| Versatile data | Versatile data, in a general context, refers to data that can be used in multiple ways, is adaptable to different applications or purposes, and is not restricted to a specific use case. |

---
