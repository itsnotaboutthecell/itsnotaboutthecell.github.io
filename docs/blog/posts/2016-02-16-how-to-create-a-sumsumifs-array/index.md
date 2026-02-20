---
title: "500 Days of SUM(SUMIFS())"
date: 2016-02-16
categories: 
  - "excel"
tags: 
  - "500-days-of-summer"
  - "array"
  - "average"
  - "averageif"
  - "averageifs"
  - "count"
  - "counta"
  - "countif"
  - "countifs"
  - "eric-clapton"
  - "function"
  - "high-fidelity"
  - "index"
  - "its-in-the-way-that-you-use-it"
  - "john-cusack"
  - "joseph-gordon-levitt"
  - "office-365"
  - "round"
  - "salvador-dali"
  - "sum"
  - "sumif"
  - "sumifs"
  - "the-color-of-money"
  - "zooey-deschanel"
comments: true
---

#### This is not an Excel Lesson... This is a Lesson About Excel.

<!-- more -->

[![](images/500DaysOfSums.png)](https://society6.com/product/toms-favourite-spot-angels-knoll-park-la-500-days-of-summer_print#1=45)

#### **Let's start at the beginning...**

* * *

Download Workbook

* * *

# Day 1

* * *

Function: **SUM**

**Describe It**:

- Add all the numbers within a range of cells.

**Syntax**:

- \=SUM(number1,number2,…)
    - number1 can be anything from a single cell to a range of adjacent cells
    - number2 and so on can be anything from a single cell to a range of cells, that are non-adjacent to number1

**Make It:**

- \=SUM(tblData\[Sales\])

* * *

**Pro Tip:**

Keyboard Shortcut: **ALT =**

- Hold Alt and Press the Equal Sign

Similar processes can be applied to the following functions:

Function: **AVERAGE**

- **Describe It:** Average all the numbers within a range of cells
- **Syntax:** =AVERAGE(number1,number2,…)

Function: **COUNT**

- **Describe It:** Count all the number values within a range of cells
- **Syntax:** \=COUNT(value1,value2,…)

Function: **COUNTA**

- **Describe It:** Count all non-blank values within a range of cells. Can be text or numerical.
- **Syntax:** \=COUNTA(value1,value2,…)

* * *

# **Day 6.0**

* * *

Function: **SUMIF**

**Describe It**:

- Add all the numbers within a range of cells if they meet a specified criteria.

**Syntax**:

- \=SUMIF(range,criteria,\[sum\_range\])
    - Range can be anything from a single cell to a range of adjacent cells
    - Criteria is a user specified value
        - Any text or [logical](http://itsnotaboutthecell.com/2015/08/10/we-need-to-talk/) symbols must be enclosed within quotations
            - **Ex.** ">=45"
            - **Ex.** "North"

**Make It:**

- \=SUMIF(tblData\[Name\],"Tim",tblData\[Sales\])

Use of a sum range is optional when strictly evaluating numbers, though I would recommend always using it, especially if your workbook is going to grow in scope.

- **Ex.** =SUMIF(tblData\[Sales\],">=5000")

* * *

**Pro Tip:**

Similar processes can be applied to the following functions:

Function: **AVERAGEIF**

- **Describe It:** Average all the numbers within a range of cells
- **Syntax:** =AVERAGEIF(range,criteria,\[average range\])

Function: **COUNTIF**

- **Describe It:** Count all the number values within a range of cells
- **Syntax:** \=COUNTIF(range,criteria)
    - As you notice within the syntax above, the COUNTIF function only requires the initial range be defined, as the inclusion of a \[count range\] would be redundant

* * *

# **Day 365**

* * *

Function: **SUMIFS**

**Describe It**:

- Add all the numbers within a range of cells if they meet a multitude of specified criteria

**Syntax**:

- \=SUMIFS(sum\_range,criteria\_range1,criteria1,...)
    - Range can be anything from a single cell to a range of adjacent cells
    - Criteria is user-specified value
        - Any text or [logical](http://itsnotaboutthecell.com/2015/08/10/we-need-to-talk/) symbols must be enclosed within quotations
            - **Ex.** ">=45"
            - **Ex.** "North"
            - **Ex.** ">="&B5

**Make It:**

- \=SUMIFS(tblData\[Sales\],tblData\[Name\],"Mike",tblData\[State\],"MO")

* * *

The [ampersand](https://en.wikipedia.org/wiki/Ampersand) (&) as shown above in example **">="&B5** is an important tool for your arsenal: especially if you are passing cell values in conjunction with calculation operators into a formula. Otherwise, Excel will interpret this as a string of text read as:

**(">=B5") Greater Than or Equal To B5**

Instead of:

**(">="&B5) Greater Than or Equal to The Value of B5.**

* * *

**Pro Tip:**

Similar processes can be applied to the following syntaxes:

Function: **AVERAGEIFS**

- **Describe It:** Average all the numbers within a range of cells
- **Syntax:** =AVERAGEIFS(average\_range,criteria\_range1,criteria1,...)

Function: **COUNTIFS**

- **Describe It:** Count all the number values within a range of cells
- **Syntax:** \=COUNTIFS(criteria\_range1,criteria1,...)
    - As you notice within the syntax above, the COUNTIFS function only requires the initial range

* * *

## **MOAR!**

Consider this a bonus section for those out there in the modeling and analysis world. It's a good practice to use, instead of typing the criteria into the formula utilize cells, so that you can easily change information on the fly.

**Example:**

- Create the following text in the corresponding cells - **G1** Name | **G2** State | **G4** Total Sales
- Type a name into cell H1
- Type a name into cell H2

**Make It: (Cell H4)**

- \=SUMIFS(tblData\[Sales\],tblData\[Name\],$H$1,tblData\[State\],$H$2)

Let's expand some of these concepts into more modeling.

**Example:**

- Create the following text in the corresponding cells - **G3** Sales Target | **G5** Within Target
- Type a number into cell H3

**Make It:** **(Cell H4)**

\=SUMIFS(tblData\[Sales\],tblData\[Name\],$H$1,tblData\[State\],$H$2,tblData\[Sales\],">="&$H$3)

**Make It: (Cell H4)**

\=COUNTIFS(tblData\[Name\],$H$1,tblData\[State\],$H$2,tblData\[Sales\],">="&$H$3)

If you haven't picked up on it by now, the COUNTIFS function is very similar to the SUMIFS and AVERAGEIFS functions. Simply copy and paste, change the function, and remove the sum\_range or average\_range.

* * *

# **Day 500**

* * *

Now you've mastered multiple criteria like they're nobody's business. You adamantly swear by the statement "**[great formula lasts forever](http://itsnotaboutthecell.com/2015/06/01/wait-a-minute-doc-are-you-telling-me-that-you-built-a-time-machine-out-of-a-spreadsheet/)**", so why try and reinvent the wheel when you can simply copy and paste a formula and modify criteria here and there as needed?

**Ask The Question:** What are the total soap sales in IL, MO and IA?

**Formula:** \=SUMIFS(tblData\[Sales\],tblData\[State\],"IL",tblData\[Item\],"Soap")

**Talk It Out:** Great formulas last forever. Simply copy and paste the formula modifying the \[State\] criteria from "IL" to "MO" and "IA" and use the addition arithmetic operator to sum together.

**Example:**

\=SUMIFS(tblData\[Sales\],tblData\[State\],"IL",tblData\[Item\],"Soap")+ SUMIFS(tblData\[Sales\],tblData\[State\],"MO",tblData\[Item\],"Soap")+ SUMIFS(tblData\[Sales\],tblData\[State\],"IA",tblData\[Item\],"Soap")

* * *

Knowing what we now know about the different variations of the **SUM** function, what if we were to be a little bit more inventive with the use of an array?

* * *

Hold on... What in the world is an array? Well, in the simplest terms, an array is a data structure for storing information of the same type. Still not following?

**ELI5**: Think of your favorite musical artist. If you wanted to catalog every album they ever produced in [autobiographical](https://www.youtube.com/watch?v=AQvOnDlql5g) order, you would assign a value to index each individual event and then store this specific information to be easily recalled in the future.

_"All right, I get that,"_ you say. _"So how does an array formula work?"_

An array formula performs a calculation on each item within the collection and stores that information. Have I lost you again?

* * *

## **Let's Visualize This Instead.**

\=SUM(SUMIFS(tblData\[Sales\],tblData\[State\],

{

**"IL",**

**"MO",**

**"IA"**

}

))

* * *

To store an array's values, you must use open and closed [curly brackets](http://www.computerhope.com/jargon/c/curlybra.htm). In the example above, we are creating an index for our \[State\] criteria by using {"IL","MO","IA"}. Excel is interpreting this array as seen below and returning the values within the indexed argument positions of 0, 1 and 2. ([Computer Science Starts at Zero](https://en.wikipedia.org/wiki/Zero-based_numbering)) -

**See It:**

**$185,474.04** =SUMIFS(tblData\[Sales\],tblData\[State\],**"IL"**,tblData\[Item\],"Soap") **$278,378.15** =SUMIFS(tblData\[Sales\],tblData\[State\],**"MO"**,tblData\[Item\],"Soap") **$188,954.19** =SUMIFS(tblData\[Sales\],tblData\[State\],**"IA"**,tblData\[Item\],"Soap")

**Make It:**

\=SUMIFS(tblData\[Sales\],tblData\[State\],{"IL","MO","IA"},tblData\[Item\],"Soap")

* * *

But something isn't right... You're only getting $185,474.04. Why isn't it returning the total for all three states? Well, you've stored them but Excel doesn't know what you want to do with them, so it goes back to its default behavior: returning the information stored within the argument position 0. This is where we're going to get back to basics and use the **SUM** function to add together all stored array values.

**See It:**

\=SUM( **$185,474.04 , $278,378.15 , $188,954.19 )**

**Make It:**

\=SUM(SUMIFS(tblData\[Sales\],tblData\[State\],{"IL","MO","IA"},tblData\[Item\],"Soap"))

**ProTip:**

You can also adapt the above logic in conjunction with a SUM(COUNTIFS()).

* * *

## Wrap It Up!

**You turned the original formula:**

\=SUMIFS(tblData\[Sales\],tblData\[State\],"IL",tblData\[Item\],"Soap")+SUMIFS(tblData\[Sales\],tblData\[State\],"MO",tblData\[Item\],"Soap")+SUMIFS(tblData\[Sales\],tblData\[State\],"IA",tblData\[Item\],"Soap")

**Into this formula:**

\=SUM(SUMIFS(tblData\[Sales\],tblData\[State\],{"IL","MO","IA"},tblData\[Item\],"Soap"))

Just to be **100%** clear, there is absolutely **NO DIFFERENCE** in the final result. But, there is a difference between a 192-character formula and an 81-character formula. You've essentially eliminated **\=ROUND(0.578125,4)** of the original formula with no loss of integrity to your results.

* * *

# WORK SMARTER,

# NOT HARDER.

* * *

It's Not About The Cell is not a hotbed for the top Excel keyboard shortcuts; it's a dedication to the 50% of the program that you didn't even know existed and might never use. But you've seen it. **You now know it's POSSIBLE**. And knowing it's possible will help you bring more imagination to your workbooks. Sure, there are always going to be be more "**efficient**" methods out there, but as Eric Clapton always says, "[It's In The Way That **You** Use It](https://www.youtube.com/watch?v=l0XQwazkx10)." Creating an efficiency by using fewer characters, easy-to-read formulas and nested functions all sounds great to me, but at the end of the day do it in a way that makes sense for you.
