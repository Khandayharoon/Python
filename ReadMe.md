# python is high level interpreted general purpose programming language that was  created by Guido Van Rossum in 1991 and imagine  us, learning it in 2025 November
* easy to code and maintain
* an object oriented programming (OOP) language
*  robust code standard library
* unit test implementation


## 1.1 Data structures
 A variable is used to store and label data so that it can be referenced and manipulated.python is a dynamically typed language where at the runtime the type of data can be store as a mutable object , meaning that can be changed after it has been created and in the python there is no need to declare a variable at all , if we assign the value 3.14 to a pi variable , the python interpreter assumes  that pi is a float variable.

 Data structure are collection of related data that defines the relationship between the data and determine operations that can be performed on the data. in CS data structure are divided into two main types:

 #### 1:- Primitives
 #### 2:- Non_Primitives


 ### Primitives 
 Data structure are the main building blocks for data manipulation , in python the following are all primitive data structure
 * Integers
 * Floats
 * Strings
 * Boolean

 all above primitives can only hold single value for example
 integer variable
        year = 2029
float variable
        pi = 3.14
string variable
        name = "Harry"
Boolean variable 
        file_exists = True

### Non_primitives 
Non_primitives data structure represent ordered and unordered sequences of objects in python , these structure are listed below:
* List are ordered sequences of any objects enclosed in brackets and lists are mutable: eg
        list_example = [1,3,'harry',45,"UI",90,-4,"FU"]

* Tuple are ordered sequences of any object enclosed in parentheses and Tuple are immutable : eg
        tuple_example = (1,34,353,"Haroon", "Berlin","Money",11,-34)

* Dictionaries are ordered sequence of any object that are key-value pairs enclosed in curly brackets 
        dictionary_example = {"Name":"haroon", "City":"Berlin", "pin":191102}

* Sets are unordered sequence of unique objects 
        set_example = set([1,34,4,7,57,686,45])

* Frozen sets are immutable sets objects 
        frozen sets_example = frozenset({1,4,64,55,575,234})


## String Manipulation 
Python string objects are immutable. means we cannot change them once created.
there are very much methods to manipulate the string like few are below
* string.len()
* string[2:6]
* string[:6]
* string[4:]
* string[:-4]
* string.count()
* string.find()
* string.split()
* string.replace()
* string.strip()
* string = "word" is in string
* string = "word" not in string



## 1.2 Functions
 A function is a reusable piece of code that written to solve a predefined task. in general,the main idea of creating function in computer programming is to create a sub_program  that can be called as many times as needed .Functions are the main components of class objects..
 In python we are using three types of functions
   #### 1 :- Built_in functions
        these are already developed functions inside the python interpreter.like 
        Print() , max() and others
  #### 2 : - user_defined functions
        this is a custom functions developed by a user for their daily program needs
 #### 3:- Anonymous Functions
        these are functions that are defined without any name.Anonymous functions are defined using a keyword "lambda", these functions  run quickly in python

        how to write a function
        Def function_name(parameters):
        """
        Function comments or docstring (function task, parameters definition etc)
        """
        <statement>
        return <expression>

  Parameters are the methods arguments passed to the function .sometimes these are called input parameters and they are passed by value or by reference . To pass by value means that a copy of the actual parameter's value is made in memory. when pass by reference (by address) occur's a copy of the address of the actual parameter is stored. by default python passes parameters by reference ..there can be one or many parameters.
  * Variable Number of Parameters
  There may be a case when we do not know the exact amount of input parameters to be passed to a function. In a case such as this, the following syntax single-asterisk parameters *args or double-asterisk **kwargs would to be used. We will now examine the program below using the single-asterisk parameters *args.
  * Because *args was used to send a variable-length argument list to the sum_number() function, we can pass as many parameters as necessary to the calling function.The double-asterisk parameter **kwargs can be used to pass variable-length dictionary structure to the function. The function below is an example of this.


## 1.2.2 Variable Scopes
The place in the program where a name (variable) is defined is called scope. Python supports two types of variable scopes.
#### 1:-  Local variable 
        by default, this is any variable defined inside the function

#### 2:- Global variable
        This is any variable defined outside the function. If a global keyword is used inside the function, a variable will become global for the whole program. Global variable declaration is not often used in Python today.

### Lambda Functions
Lambda functions are known as anonymous functions as they have no name. The return statement is not required as they always return a value. The best way to use these functions is inside another standard def function.
        function_double = lambda x : x *2


## 1.3 Flow control 
By definition, conditional statements are features of a programming language that perform different computations or actions depending on whether a programmer-specified Boolean condition evaluates to true or false. This statement is generally used to control the code flow based on specific program requirements. In Python, the easiest conditional “if” statement can be defined as
        if <Expression>:
        <statement>