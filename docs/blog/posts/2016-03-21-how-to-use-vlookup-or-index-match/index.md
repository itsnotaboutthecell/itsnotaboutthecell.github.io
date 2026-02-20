---
title: "Defining The Great Divide"
date: 2016-03-21
categories: 
  - "excel"
tags: 
  - "teamindexmatch"
  - "teamvlookup"
  - "7-eleven"
  - "ambiturner"
  - "area_num"
  - "array"
  - "black-knight"
  - "col_index_num"
  - "column_num"
  - "excel"
  - "great-divide"
  - "holy-grail"
  - "index"
  - "indexmatch"
  - "match"
  - "match-type"
  - "monty-python"
  - "quiktrip"
  - "range_lookup"
  - "row_num"
  - "vlookup"
  - "zoolander"
comments: true
---

Not since the great territory battles of [7-Eleven Vs. Quiktrip](http://www.city-data.com/forum/oklahoma-city/801662-quik-trip.html), has there been such an unparalleled rivalry: "**VLOOKUP or INDEX/MATCH?**"A seemingly innocent question, when asked among Excel users, gives you a general perception of one another. There is one function's inability to [turn left](https://youtu.be/8hJ1HDcMowk?t=13) and the others reliance on multiple functions for use. One's perceived simplicity vs. the others perceived complexity. Are we so divided, though that we are unable to recognize the benefits found within each function? I'm unsure.. but I know neither function is willing to surrender their position without a [fight](https://www.youtube.com/watch?v=mjEcj8KpuJw&feature=youtu.be&t=122).

<!-- more -->

### [Download Workbook](http://itsnotaboutthecell.com/wp-content/uploads/2016/03/GreatDivide.xlsx)

 

## #TEAMVLOOKUP

* * *

Function: **VLOOKUP**

**Describe It**:

- A reference lookup for vertical information retrieval.

**Syntax**:

- \=VLOOKUP((lookup\_value, table\_array, col\_index\_num, \[range\_lookup\])
    - lookup\_value is the value in which you want to reference for lookup
    - table\_array is the range of cells in which you will search for the lookup\_value
    - col\_index\_num is the column in which to return a value (left most column starts at 1)
    - \[range\_lookup\]
        - TRUE is an approximate match indicating return a value that is similar to the lookup\_value
        - FALSE is an exact match indicating return a value that is exact to the lookup\_value (not case sensitive)

**Ask The Question: What state are fictional products being sold in?**

**Make It False:**

\=VLOOKUP("Fictional",tblProduct\[\[Product Type\]:\[State\]\],3,FALSE) ![VLOOKUP - False](images/VLOOKUP-False.png)

**Talk It Out:** Even though there are four columns possible the table\_array you specified is only Product Type thru State. For this example the left most column Product Type will begin your column count at 1, the State category is found two columns away so the column in which we wish to return information is that of col\_index\_num 3. If multiple items of the same type are found, it will return the first corresponding matched value from top to bottom.

* * *

**Ask The Question: What is the total commission percentage for a sale of $61.50?**

**Requirements:**

Values will need to be sorted in Ascending order for the function to work correctly.

**Make It True:**

\=VLOOKUP(61.5,tblSales\[#All\],2,TRUE)

![VLOOKUP - True](images/VLOOKUP-True.png)

**Talk It Out:** The formula will review each item within the left most column until the lookup\_value returns a value that is equal to or less than the item within the lookup column. If the item is less than the current value it will return the index position to that of the previous value's position. As shown in the example above - $61.50 is greater than $50.00 so it evaluates the next item $75.00 and determines that it is less than $75.00, at this point it returns to the previous value and it's corresponding index position.

 

## #TEAMINDEXMATCH

* * *

Function: **INDEX**

**Describe It**:

- A reference lookup for the intersection of a row and or column retrieval.

**Syntax**:

- \=INDEX(array,row\_num,\[column\_num\])
    - array is the range of cells or an array constant
    - row\_num is the row number in your array in which you want to reference
    - \[column\_num\] is the column number in your array in which you want to reference (optional)
    - \[area\_num\] is the array number if multiple ranges used (optional)

**Make It:**

\=INDEX(tblRegion\[#All\],10,4)

![INDEX](images/INDEX.png)

**Talk It Out:** The formula will create an index of the left most column, at which point it will search for the item in the 10th position. Once located, it will then return the value from the column\_num 4.

* * *

## Caution

The position of the row\_num does not reference the worksheet but the array selected. For example, if you were to use a formula similar to the one below, the 1st indexed position would start on the 4th row.

### **\=INDEX($A$4:$C$9,2,3)**

* * *

Function: **MATCH**

**Describe It**:

- A reference lookup for the intersection of a row and or column retrieval.

**Syntax**:

- \=MATCH(lookup\_value,lookup\_array,\[match\_type\])
    - lookup\_value is the value in which you want to reference for lookup
    - lookup\_array is the range of cells in which you will search for the lookup\_value
    - \[match\_type\]
        - **\-1 - "Less Than":**
        - **0 - "Exact Match":**
        - **1 - "Greater Than":**

* * *

**Requirements:**

Values must be sorted in Descending order for the function to work correctly.

**Make It (Less Than):**

\=MATCH(3600,tblRegion\[Amount\],-1)

![Match - Less Than](images/Match-Less-Than.png)

**Talk It Out:** The -1 match type finds the smallest value within the lookup\_array that is greater than or equal to the lookup\_value. In the example above, the item $3,527.83 is less than our lookup\_value of $3600.00. So, the smallest value that is greater than $3600.00 is $3,809.88, which will return an index position of 16.

* * *

**Make It (Exact):**

\=MATCH("Speakers",tblRegion\[Product Type\],0)

![Match - Exact](images/Match-Exact.png)

**Talk It Out:** The 0 match type finds the exact matched lookup\_value within the lookup\_array. As shown in the example above, it will return the index position of the first exact match found even though multiple values exist.

* * *

**Requirements:**

Values must be sorted in Ascending order for the function to work correctly.

**Make It (Greater Than):**

\=MATCH(3600,tblRegion\[Amount\],1)

![Match - Greater Than](images/Match-Greater-Than.png)

**Talk It Out:** The 1 match type finds the largest value within the lookup\_array that is less than or equal to the lookup\_value. In the example above, the item $3,527.83 is less than our lookup\_value of $3600.00. So, the largest value less than $3600.00 is $3,527.83, which will return an index position of 2.

 

* * *

#### We're not out of the woods yet with INDEX and MATCH.

* * *

 

Nested Function: **INDEX(MATCH())**

**Ask The Question:** **What Product Type is sold in the State of CA?**

**Make It:**

\=INDEX(tblRegion\[Product Type\],MATCH("CA",tblRegion\[State\],0))

![INDEX MATCH](images/INDEX-MATCH.png)

**Talk It Out:** The INDEX function uses the Product Type column as the functions array index. We then nest the MATCH function to review the State column and return the row\_num when a specified lookup\_value condition is met.

* * *

### If it sounds confusing reading it.

### It felt confusing writing it.

* * *

**ELI5:** We know the MATCH function allows us to search a column to find where a conditions criteria is met, whereas the index function only uses numerical return positions. So in the above scenario, let's read the formula from the inside out. We first find the MATCH of the state "CA" at the indexed position of 6. We then tell our INDEX function to review the Product Type column and return the 6th indexed item. I would mark the -1 and 1 match types as NICE-TO-KNOW, but the majority of your time will be spent using **EXACT** match type when it comes to data. Trust me.
