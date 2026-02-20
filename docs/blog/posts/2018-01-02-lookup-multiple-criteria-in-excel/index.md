---
title: "I Always Feel Like SUMPRODUCT()'s Watching Me"
date: 2018-01-02
categories: 
  - "excel"
tags: 
  - "array"
  - "boolean"
  - "cse"
  - "double-unary"
  - "index"
  - "indexmatch"
  - "match"
  - "nts"
  - "rows"
  - "sumproduct"
  - "table-objects"
  - "vlookup"
comments: true
---

As the war wages on between **#TEAMVLOOKUP** and **#TEAMINDEXMATCH,** a new challenger has arisen. #SUMPRODUCT, a function often associated with math and trig, has now taken on a new purpose - Boolean logic. But can it compete? Or, will it continue to lurk in the shadows, only to be utilized by Power Users...

<!-- more -->

#### Download Workbook

 

##  #TEAMSUMPRODUCT

* * *

Function: **SUMPRODUCT**

**Describe It**:

- Multiplies a corresponding range or array and returns the sum of all values.

**Syntax**:

- \=SUMPRODUCT(array1, \[array2\], \[array3\],....)
    - o array1 – it’s required and can be a single cell, a range or an array
    - o array2, array3, etc. – must be the same size of array1, if populated
        - **Reminder:** optional arguments are stored in square brackets
            - If no values in the optional arguments the **SUMPRODUCT** function will emulate the **SUM** function with the value(s) stored in array1.

**Make It:**

- Worksheet: Sales Data
- \=SUMPRODUCT(salesUnits\[Units\],salesUnits\[Cost Per Unit\])

* * *

**Talk It Out:** SUMPRODUCT requires that the size of the arrays are the same. For instance, if array1 contains 10 elements and array2 contains 10 elements - you're good to go. SUMPRODUCT then multiplies each item relative to their index position. For instance in our example above 30 Units \* $60.29 Cost Per Unit = $1,808.70. It performs this process for each item in the array and then sums the total of each result when complete.

| **Index Position** | **Units** | **Cost Per Unit** | **Result** |
| --- | --- | --- | --- |
| 1 | 21 | $58.93 | $1808.70 |
| 2 | 23 | $79.09 | $1819.07 |
| 3 | 16 | $78.85 | $1261.60 |
| ... | ... | ... | ... |
|  |  | **Total:** | $10282.83 |

“I thought you said this was going to be a lesson on LOOKUP functions?” I did! I swear this is one of those unsung heroes that is great to have in your arsenal. It's like a [secret sign](https://www.youtube.com/watch?v=qkpnOTr8k9I) that only Excel professionals like you and me will know about.

* * *

First we'll perform a multi lookup of an \[**Employee\]** and **\[Item\]** to return the current **\[State\]** where the product is sold.

**Make It - STATE:**

\=SUMPRODUCT((regionalSales\[Employee\]=$H$2)\*(regionalSales\[Item\]=$H$3),ROW(regionalSales\[State\])-1)

**Talk It Out: “**I've never heard of a state named 4.” You're right how could forget to mention - SUMPRODUCT's return type is a NUMBER, which is why we'll want to wrap an INDEX function to get the correct position in our array.

 

* * *

## **IMPORTANT NOTE**

Because we've used structural references in our formula, we will subtract 1 from the return value of ROW due to the header row. If our header row was to start on row 10, for example, we would need to subtract 11. I know. I know. **MATH**.

* * *

 

**Make It Again - STATE:**

\=INDEX(regionalSales\[State\],SUMPRODUCT((regionalSales\[Employee\]=$H$2)\*(regionalSales\[Item\]=$H$3),ROW(regionalSales\[State\])-1))

 

**Pro Tip:** You can also use the double unary operator "--" to turn text into numbers, or more importantly, to turn your BOOLEAN returns into 1's and 0's. Due to Wordpress formatting I had to add double spacing below "- -" it should be just a single space when in your Excel workbook.

\=INDEX(regionalSales\[State\],SUMPRODUCT(- -(regionalSales\[Employee\]=$H$2),- -(regionalSales\[Item\]=$H$3),ROW(regionalSales\[State\])-1))

* * *

**Hold up - Hold Up, [Double Unary](https://www.youtube.com/watch?v=MdMnW7rdOmU)?!**

A double unary turns numbers stored as text "those top left green triangles" back into numbers. The first "-" turns the value into a negative number, the second "-" turns a negative back into a positive.

**Try It (Double Unary):**

- Check to see if a value is stored as TEXT:
    - In 'Regional Sales' Range H8: =ISTEXT(G8)
        - **Pro Trip:** Text's default alignment is LEFT, while numbers are RIGHT
- Convert Text to Number:
    - In 'Regional Sales' Range I8: =- -G8

* * *

All of the above is COOL and all... but I'm really not a fan of that whole ROW() - 1 because we would need to account for movement if people were to edit where our table is located. Plus, I would much rather future-proof my work without having to solve all known mysteries of the universe. That’s why I think it's time we start talking about the big bad world of array formulas: why to love 'em and why to hate 'em.

* * *

 

 

 

![Control+Shift+Enter](images/CSE.png)

 

 

 

* * *

**What is an array formula?**

An array formula can perform multiple calculations on one or more items in an array.

**Ok... What does that mean?**

In a [past lesson](http://itsnotaboutthecell.com/2016/02/16/how-to-create-a-sumsumifs-array/), we learned about hard coding arrays by manually typing in values in order for our formulas to perform multiple calculations to return a value. A C+S+E formula is no different.

**Ok... What does C+S+E mean?**

Control+Shift+Enter is a secret combination to tap even further into the Excel calculation engine's potential.

* * *

**Make It (Again) - STATE:**

**Very Important Note:** Before pressing enter after completing the formula, press in combination Ctrl+Shift+Enter to force an array calculation. Once complete you should notice that your calculation is now surrounded with curly brackets { }. You cannot manually type these in to perform the calculation, they must be forced through C+S+E.

\=INDEX(regionalSales\[State\],MATCH(1,(regionalSales\[Employee\]=I2)\*(regionalSales\[Item\]=I3),0))

* * *

**Break It Down:**

| **Formula** | **Walk Through** |
| --- | --- |
| \=INDEX(regionalSales\[State\], | INDEX Function. |
|  MATCH(1, | In Excel Boolean values are 1 for TRUE and 0 for FALSE. We want to MATCH all conditions that are 1 = TRUE. |
|  (regionalSales\[Employee\]=I2)\*(regionalSales\[Item\]=I3) | We evaluate each column to see if each value in the column is equal to that of our value, TRUE or FALSE.  We then multiply our conditions which converts to 1's and 0's - 1 being a match per our condition above. |
|  ,0)) | MATCH type 0 being that of an Exact match. |

 

**Not Good Enough - ELI5 It:**

The real magic starts at MATCH. We set our lookup\_value to be 1 (a little strange I know but remember, 1 = TRUE, 0 = FALSE). Within our comparisons of the \[Employee\] and \[Item\] ranges, we’ve created an array containing TRUE/FALSE. We then multiply each array by the index of the other - Employee T/F \* Item T/F. This converts our TRUE / FALSE back to 1's and 0's which our MATCH lookup\_value is attempting to find.

|  **Employee** | **Item** | **Employee T/F** | **Item T/F** | **Value**  |
| --- | --- | --- | --- | --- |
|  Jack | Laptop | FALSE | TRUE | 0 \* 1 = 0 |
|  Jill | Tissue | TRUE | FALSE | 1 \* 0 = 0 |
|  Jack |  Notebook | FALSE | FALSE | 0 \* 0 = 0 |
|  Jill |  Laptop | TRUE |  TRUE | 1 \* 1 = 1 |

# N-T-S

Not Too Shabby.

* * *

That's cool for multiple-condition lookups, but didn't you talk about hard coding arrays in a [previous lesson](http://itsnotaboutthecell.com/2016/02/16/how-to-create-a-sumsumifs-array/)? Great catch! **Real talk, though**: Forced array calculations can eat up crazy amounts of memory and cause performance degradation if you are thinking about filling your worksheet with them. I would recommend using them sparingly to solve more complex problems or in returning a single value.

**Make It: (Remember to press CTRL+SHIFT+ENTER When Complete)**

\=SUM(SUMIF(regionalSales\[State\],stateList\[State\],regionalSales\[Price Per Unit\]))

**Pro Tip:**

Instead of hard-coding values we are now using the structural reference stateList\[State\] to create an array. Go ahead and add the state "MO" to the stateList table and notice how your array formula is now dynamically updating.

* * *

 

## **\*Drops The Mic\***

## **\*Throws The Bat\***

## **We're Done Here**

 

* * *

This was certainly a very cerebral lesson in some respects - but that's why you are here. Your brand is built on putting out the best product for others to use, and doing more with less is an approach that you’re already familiar with. Array formulas, while they certainly require a bit more forethought, can deliver powerful results in the long-term development of your outputs. Array formulas may represent a new strange world that you are entering into, but I know you've got this. Keep going.
