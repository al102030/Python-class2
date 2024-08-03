# Python-class2

A Python Programing full Crash cours in Kadoos EDU

# <span style="color: #ce1403; font-weight: Bold">Python</span>

### <span style="color: #ebce14;">A Python Programing full Crash cours in Kadoos EDU</span>

### <span style="color: #03ce14;">Getting started</span>

- <span style="color: Red;">About Python</span>

  - The World's Fastest growing programming language
  - Most Popular among Software Engi., Data Analysts, Math, Science, Net Engi., and Kids
  - Google, Facebook, Spotify, DropBox, and etc. use Python
  - Python is simple
  - ![](Images/1.png)
  -
  - Python is a multipurpose Language
  -
  - ![](Images/2.png)
  -
  - Most Desirable language
  - ![](Images/3.png)
  -
  - Python2 and Python3
  -

- <span style="color: Red;">Installation Instruction</span>

  - Install python (Download and install)
  - Note "check `Add python 3 to PATH`"
  - check your installation on windows Command prompt

- <span style="color: Red;">Python Interpreter</span>

  - Check some code in it
  - Check errors

- <span style="color: Red;">Editors</span>

  - Text Editors `Notepad` , `Atom`, `Sublime`
  - IDEs `Pycharm`,
  - Use `VSCode` for this class

- <span style="color: Red;">Create Your First Python File</span>

  - Open your folder in VSCode And create .py file
  - Talk about extensions
  - First Built-in Function `Print()`
  - Execute first code in terminal

- <span style="color: Red;">Turn VSCode to a Powerful IDE Using Extensions</span>

  - Install python Extension in VSCode
  - ![](Images/4.png)
  - Install Linter to find Potential errors
  - Select right Python for your Project

- <span style="color: Red;">PyLint</span>

  - Check PyLint Functionality
  - Check errors in problems panel
  - Talk about command pallet `Shift + ctrl + p`
  - Choose Right linter - `pylint`

- <span style="color: Red;">Python Enhancement Proposal</span>

  - PEPs In google
  - PEP8
  - Talk about Python code formats
  - Format Document In command pallet
  - autopep8 Installation
  - Talk about some developer mistake in formatting code
  - Turn auto format on save in `Code>Preferences>sittings`
  - Search for FormatOnSave and turn it on

- <span style="color: Red;">Running Python Code</span>

  - Install Code Runner
  - Running Code by Key or `ctrl+alt+n`

- <span style="color: Red;">Python Implementation</span>

  - Cpython and python interpreter
  - Other Implementations of python Jython, IronPython, PyPy
  - These implementations help us to use other languages code in our python code

- <span style="color: Red;">Execution of Python code</span>

  - Cpython and python interpreter
  -
  - C Translation to machine code
  - - ![](Images/5.png)
  - Codes are different in Mac and Windows based on compliers
  -
  - - ![](Images/6.png)
  -
  - Java Solve the problem
  -
  - - ![](Images/7.png)
  -
  - Python use it
  - - ![](Images/8.png)
  -
  - Jython Workflow
  -
  - - ![](Images/9.png)

### <span style="color: #03ce14;">Primitive Types</span>

- <span style="color: Red;">Variables</span>

  - Core concept of storing data by programming languages
  - Three different built-in primitive types in python
  - Numbers (100, 4.9,...), Booleans (True/False), Strings ("Your Name")
  - All your variables' name should be descriptive and meaningful
  - All letters in your variable's name should be in lower case
  - Set a space before and after your equal sign
  - Use Underline between separate word

- <span style="color: Red;">Strings</span>

  - Surround your text with `"` or `'`
  - For multiline text (long text) we use `"""`
  - Talk about built-in function for String type
  - `len()`
  - Calling Functions concept by using `()`
  - Indexing concept in Python for strings and `[]`
  - End of the string using `[-1]`
  - Slicing strings Using `[:]` (check all options)
  - Using backslash `\` to scape special characters (e.g. `\"`, `\'`, `\\`, `\n`)
  - Concatenate strings using `+`
  - Formatted Strings using `f` and `{}`

- <span style="color: Red;">String Methods</span>

  - Talk about methods and OOP (Dot Notation)
  - `upper()`, `lower()`, and `title()` methods
  - Notice that the original string is not changed after using those methods
  - Use `strip()` method for users input strings (`lstrip()` and `rstrip()`)
  - Use `find()` method to find a special character or series of characters (return an index or `-1`)
  - Use `replace("1", "2")` to change one or sequence of characters
  - `in` and `not in` expressions for checking the existence of something
  - Different between the `find()` and `in` expression is in return value (`index`, `True/False`)

- <span style="color: Red;">Numbers</span>

  - There is three different number type in python
  - `Integer`, `float`, and `complex` (a + bi)
  - Talk about comments `#`

- <span style="color: Red;">Standard Arithmetic Operations</span>

  - `+`, `-`, `*`, `/`, `//`, `%` and `**`
  - Augmented Operations `+=`, `-=`, `*=`, `/=`

- <span style="color: Red;">Built-in Functions for Numbers</span>

  - `round()`
  - `abs()`
  - Talk about modules (`math`) and import the library and check `.` notation
  - Check `math` modules in Google (`Python 3 math modules`)

- <span style="color: Red;">Type Conversion</span>
  - Use input function to get data from user
  - Check the error and explain the reason
  - Built-in Conversion methods in python
  - `int()`, `float`, `bool`, and `str`
  - talk about `type()` method
  - All falsy values in python: `""`, `0`, `False`, and `None`
  - Check in interpreter

### <span style="color: #03ce14;">Control Flow </span>

- <span style="color: Red;">Comparison Operators</span>

  - `>`, `<`, `<=` `>=`, `==`, `!=`
  - An integer and a string value save differentially in memory `10 == "10"` is wrong
  - every character has unique numeric representation ()unicode, so `"bag" == "BAG"` is wrong
  - Use `ord()` function to show differences

- <span style="color: Red;">Conditional statement</span>

  - `if` statement (always terminate it with `:`)
  - Explain about code block and indentation on a simple example `temperature`
  - Simple example (`if statement : pass`)
  - Talk about indentation and code block with example of three print under an if statement
  - Explain codes out of if block
  - With `elif` statement we can add more condition to our code
  - If all our conditions are not True we use `else` statement to execute last condition (lots of `elif` and one `else`)
  - nested if statements

- <span style="color: Red;">Ternary Operator</span>

  - Turn 5 line code to one
  - `X = elem1 if rule1 else elem2`
  - message = "OK" if time >= 10 else "Not OK"

- <span style="color: Red;">Logical Operator</span>

  - `and`, `or`, and `not`
  - `and` operator return True if both conditions are True
  - `or` operator return True if one of conditions is True
  - `not` changes the value of a boolean variable
  - Don't use `==` for check a boolean variable
  - Separate conditions logical comparison to make accurate comparison
  - Avoid short circuit in the process of working with logical operators
  - Chain logical operators instead of using theme in word format
  - Use `18 <= age < 40` instead of `age >= 18 and age < 40`

- <span style="color: Red;">For Loops</span>

  - When we need to repeat a task for number of times `For loop' can do it (Ex: print something for 10 times)
  - Talk about counter(`number`) and `range` function (step) and add `... * "."`

- <span style="color: Red;">For...else</span>

  - `else` execute when a loop completely was executed and aBreak didn't happen

- <span style="color: Red;">Nested Loops</span>

  - Talk about Outer and inner Loops
  - Explain how exactly python interpreter execute nested loops

- <span style="color: Red;">Iterables</span>

  - Use type for range() function to explain
  - Range is complex type
  - Iterable of strings or lists
  - You can create a `iterable` object and use it in `For` loop

- <span style="color: Red;">While Loop</span>

  - We use `While` loop to repeat something as log as a condition is true
  - Explain While loop in python interpreter as real world example
  - Simulate Terminal using a while loop as extra example
  - Check case sensitive characteristic of python
  - Check a poor way of condition for while loop (A `and` B)

- <span style="color: Red;">Infinite Loop</span>

  - Infinite loop is a loop that runs forever
  - You should always have a way to break the infinite loop
  - it can cause crash for your system

- <span style="color: Red;">Exercise/span>
  - A python code that shows even number between 1 to 10 and count them

### <span style="color: #03ce14;">Functions</span>

- <span style="color: Red;">How to Define a Function</span>

  - In programming we should break our code in small, reusable, and more maintainable chunks of code
  - Use `def` keyword (short form of define) to declare your function
  - Make sure your function names are meaningful and descriptive
  - Name conventions should apply for functions naming
  - After definition of a function for using it you should call it (Two line break - pep8)

- <span style="color: Red;">Arguments</span>

  - Talk about differences between `print` and our function
  - Define parameters in our function
  - A parameter is the input that you define for your function but an argument is actual value for a given parameter

- <span style="color: Red;">Types of Functions</span>

  - There is two type of Functions
  - A: A function that perform a task (`say_hello()`, `print()`)
  - B: A function that calculate and return a value (`round()`)
  - We use `return` statement to return a value from a function
  - Write `say_hello()` function with `return` and get it in variable
  - Talk about print a function that doesn't return any value
  - By default all functions return a `None` value (indicator of absence a value)

- <span style="color: Red;">Keyword Arguments</span>

  - Talk about temporary argument that python create for us when we pass a function to another function
  - Make your code more readable when you are calling your function by using keyword arguments
  - By adding a default value to a parameter we can make it optional
  - (`Important`) All optional parameters should come after the required parameters

- <span style="color: Red;">xargs</span>

  - To pass a list of parameters to function we can use `xargs`
  - It returns a `Tuple`
  - By adding an asterisk (`*`) at beginning of a parameter it can take a list of values
  - Talk about tuples and lists by return xargs argument

- <span style="color: Red;">xxargs</span>

  - To pass a series of keyword arguments to a function we can use `xxargs` parameter
  - By adding double asterisk (`**`) at beginning of a parameter it can take a list of key value peers
  - It returns a `Dictionary`
  - By using `bracket` notation we can get the values of a dictionary

- <span style="color: Red;">Scope</span>
  - It's Impossible to call a variable which defined inside a function, outside of it
  - A local variable only works inside the scope
  - Thc completely equal variable in two different function is completely separate
  - When a function called, python interpreter allocate a memory to it's variables and release it at end function's execution
  - On the other side we have global variables which can be used anywhere in code
  - Global use memory for long time and you should not use them often
  -
