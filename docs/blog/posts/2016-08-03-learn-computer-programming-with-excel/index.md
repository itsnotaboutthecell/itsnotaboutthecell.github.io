---
title: "What The Func?!"
date: 2016-08-03
categories: 
  - "excel"
tags: 
  - "boolean"
  - "char"
  - "concatenate"
  - "data"
  - "excel"
  - "function"
  - "microsoft-excel"
  - "number"
  - "spreadsheet"
  - "text"
comments: true
---

Undoubtedly you have called a function a formula and a formula a function; it's just the nature of the Excel-lingo beast. **T****hat stops now**. I want you to see functions for what they truly are: computer programming. You may feel like you are not yet ready to call yourself a computer programmer **\-** but you are. And I want to get you from here - **to here** - not through keyboard shortcuts but by taking the things that you are currently doing and giving you you the knowledge and confidence to know why you are doing them.

<!-- more -->

* * *

Function: **EXACT**

**Describe It**:

- Determine whether two text strings are exactly the same, and return TRUE or FALSE (BOOLEAN).
    - EXACT is case-sensitive.
    - Numbers can be evaluated but will be passed through the function as strings

**Syntax**:

- \=EXACT(text1, text2)
    - text1 is the first string
    - text2 is the second string to be compared against text1

**Make It:**

\=EXACT("DOG","Dog")

* * *

### **Data should always be viewed** **objectively.**

* * *

The EXACT function isn't rocket science - while phonetically the values may sound the same your computer interprets them in a much more _**exact**_ manner. Using the [ASCII](http://www.ascii-code.com/) (American Standard Code for Information Interchange) decimal codes below for each character's value you can better visualize how your computer is interpreting the words "DOG" vs "Dog".

* * *

**CHAR(68), CHAR(79), CHAR(71)**

**CHAR(68), CHAR(111), CHAR(103)**

* * *

Function: **CHAR**

**Describe It**:

- Returns the character specified by the code number from the character set for your computer

**Syntax**:

- \=CHAR(number)
    - number is a character set value between 1 and 255

**Make It:**

\=CHAR(68)

\=CHAR(111)

\=CHAR(103)

* * *

### ![Cell Object](images/CellObject.png)

### **TEXT - NUMBER - FUNCTION - BOOLEAN**

Now that we've gone as granular as looking at one single character's value, let's talk about how the cell object is actually storing your information. Excel contains up to 17,179,869,184 cell objects per worksheet, with each cell being able to store any **one** of the four data types shown above. **This is a lot when considered all at once, so take it one cell at a time.**

Understanding what each data type means will eventually tie into your ability to manipulate data to meet your needs. For right now, it's less important for you to know every type structure and more about understanding what I like to call **"The Big Four"**. Especially as you expand your knowledge base in other languages you may find that more data types and structures exist and that some may even contradict what you're learning now.

| **Data Type** | **Type Structures** |
| --- | --- |
| **TEXT** | String |
| **NUMBER** | Integer  Long  Single  Double  Currency  Date  Date/Time |
| **FUNCTION** | Built-In Excel Functions  User Defined Functions |
| **BOOLEAN** |  |

Confused yet?... **Good** - that means you've stepped into that 50% of the program that most people dare not traverse. I know you have an idea of what text is as you read this and I'm positive you know what a number is, but what is a function? A function is a group of statements that together perform a task.

Functions are comprised of four parts:

- **Name**
    - A predefined name to invoke a function
- **Arguments**
    - The values (parameters) passed through a functions procedures.
        - Additionally the formula helper lists the number of arguments that must be completed to successfully return a value
- **Return Type**
    - The data type a function returns
- **Function Body**
    - A procedural list of statements that must be performed to return a value in accordance with the return type

I believe not enough emphasis is placed on the return type of a function when learning Excel, instead we've been conditioned to simply insert the parameters necessary to complete the function body's syntax, cross our fingers and hope that a value is returned.

* * *

Let's compare two functions using the same variables:

- "Die Hard ", 3

Function: **CONCATENATE**

**Describe It**:

- Joins several text strings into one text string

**Syntax**:

- \=CONCATENATE(text1, \[text2\], ...)

**Return Type:** Text

**Formula:** 

- \=CONCATENATE("Die Hard ", 3)

 

Function: **SUM**

**Describe It**:

- Adds all the numbers in a range of cells

**Syntax**:

- \=SUM(number1, \[number2\], ...)

**Return Type:** Number

**Syntax**:

- \=SUM("Die Hard ", 3)

* * *

**Just spit-balling right now:**

- The **CONCATENATE** function's return type is text - it will convert any data type into text and return as text for example "Die Hard 3"

- The **SUM** function's return type is a number - it requires the functions parameters to be any of the number data type structures - if you try to add the data types Text and Number together you will receive the error handling message of [#VALUE!](http://itsnotaboutthecell.com/2015/09/20/to-err-is-computational/) due to incompatible information.

You already know these things in the real world, all we are doing now is understanding how your computer interprets them.

* * *

Let's go ahead and bring it on home now by discussing what's going on each time you pass a formula through an Excel function. First off you call the function by typing "=" then the function **name** EXACT whose **parameters** are text1 as the text data structure string and text2 as the text data structure string with an expected **return type** of Boolean (TRUE | FALSE). The Excel engine will now evaluate the **function's body** to determine **if** text1 is the same as text2 and **then** return a **boolean** ( TRUE | FALSE) datatype value that either satisfies the requirements of the **return type** or results in an [error message](http://itsnotaboutthecell.com/2015/09/20/to-err-is-computational/) upon completion.

![Exact Function](images/Exact.png)

* * *

All this time you've been writing code and you didn't even know it. Telling yourself you are too far into your career, don't have enough time, or that programming is just too intimidating - are all now thrown out the window. You've done it. You are doing it. You can continue to do it.
