---
title: "We Need To Talk"
date: 2015-08-11
categories: 
  - "excel"
tags: 
  - "combin"
  - "combination"
  - "comparison-operators"
  - "do-it"
  - "excel"
  - "gambler"
  - "if"
  - "kenny-rogers"
  - "microsoft"
  - "office"
  - "shia-labeouf"
comments: true
---

### We all have problems.

<!-- more -->

Excel is an executable. No more or less than 1's and 0's interpreted by your operating system. To its unsuspecting users it is perceived as a daunting application full of things that you keep meaning to learn more about. Just stop.

<iframe src="https://www.youtube.com/embed/ZXsQAXx_ao0" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

 

#### Excel is not the solution to your problems, you are.

Without an answer you are merely left with questions. Stop and ask yourself - What is the story I'm trying to tell? What information will I need to tell this story? The wheels should be turning at this point as you start to assess the possibilities. The introduction of comparison operators and IF statements will transition you from just being a recreational user to a true power user of Excel.

| **Description** | **Comparison Operator** |
| --- | --- |
| **Equal to** | **\=** |
| **Not Equal to** | **<>** |
| **Less Than** | **<** |
| **Less Than or Equal To** | **<=** |
| **Greater Than** | **\>** |
| **Greater Than or Equal To** | **\>=** |

Let's use a simple question to review the total possibilities that exist by using the various comparison operators.

##### I want to know the number of kittens \_\_ 10 years of age,

##### adopted from the dates \_\_ June 1st 2015 and \_\_ August 31th 2015.

* * *

Function: **COMBIN**

**Describe It**:

- The number of combinations for a given number of items.

**Synatx**:

- \=COMBIN(number,number\_chosen)
    - The number can be any numerical value
    - The number\_chosen can be any numerical value

**Make It:**

- \=COMBIN(18,3)
    - number: 18 operators - (6 for each variable)
    - number\_chosen: 3 variables available

## **816 Combinations**

##### **(1 Story to Tell / 816 Possible Stories = 0.1225% Guess Rate)**

###### Even [Kenny Rogers](https://www.youtube.com/watch?v=Jj4nJ1YEAp4) wouldn't take those odds.

 

* * *

Data is full of possibilities, always ask the questions first -

#### **Who? What? When? Where? Why?**

* * *

 

### That's a bunch of Boolean and you know it!

You're right, nothing comes easy when telling your story. **IF** this happens count this, **IF** that happens sum that. Constantly developing your cognitive skills in relation to logic, reasoning, memory and processing can undoubtedly lead to more meaningful data analysis on your part. The cognitive reasoning used when determining if something is **TRUE** and if something is **FALSE** is known as [BOOLEAN](https://en.wikipedia.org/wiki/Boolean_data_type) when it comes to computer science.

* * *

Function: **IF**

**Describe It**:

- Return one value if a condition is true, another value if false

**Synatx**:

- \=IF(logical\_test,\[value\_if\_true\],\[value\_if\_false\])
    - logical\_test is the condition for argument
    - value\_if\_true is the result if true, can be both text or numerical
    - value\_if\_false is the result if false, can be both text or numerical

**Example:** =IF(10=11,TRUE,FALSE)

- We can easily determine that 10 does not equal 11 so this would be **FALSE**

**Example:** =IF(10=11,"Dogs","Cats")

- Nothing has changed from our logical\_test, our boolean values are now: "Dogs" = \[value\_if\_true\] and "Cats" = \[value\_if\_false\].

* * *

> ##### "If you're going through hell, keep going."
> 
> Winston Churchill

Practice, practice, practice. That feeling of being somewhat overwhelmed is called being on the verge of a breakthrough. Start building your own formulas using the comparison operators above with this lessons [test workbook](http://itsnotaboutthecell.com/wp-content/uploads/2015/08/We-Need-to-Talk.xlsx). If you want, you can get real crazy with it and research how to build even more advanced [nested if formulas](https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=nested+if+formulas).
