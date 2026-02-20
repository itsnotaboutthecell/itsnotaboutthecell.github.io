---
title: "Love It Or List It"
date: 2016-04-20
categories: 
  - "excel"
tags: 
  - "canada"
  - "data"
  - "data-validation"
  - "drop-down"
  - "excel"
  - "excel-tables"
  - "hgtv"
  - "it-works"
  - "john-doe"
  - "kevin-jones"
  - "list"
  - "love-it-or-list-it"
  - "name-box"
  - "name-manager"
  - "new-york-times"
  - "table-object"
  - "zack-barresse"
comments: true
---

#### "What gets measured gets managed."

<!-- more -->

**Peter Drucker**

* * *

Analysts estimate anywhere from 50-80% of their time is dedicated to cleansing information (Source: [New York Times](http://www.nytimes.com/2014/08/18/technology/for-big-data-scientists-hurdle-to-insights-is-janitor-work.html?_r=0)). Making use of Excel's data validation controls can drastically reduce this necessary evil when developed properly. No longer will you spend hours trying to infer if "S" really means "Saturday" or "Sunday"; or trying to match "John Doe" with the employees actual name "Johnathan Doe". Because the time you invest now in planning what is truly important and creating a set of sound variables will pay off infinitely in the end. Not only in making data entry easier for others, but also when it comes time to analyzing the things that matter: **RESULTS.**

* * *

#### [Download Workbook](http://itsnotaboutthecell.com/wp-content/uploads/2016/04/Love-It-Or-List-It.xlsx)

* * *

### **Make It:**

- Select a cell from within your worksheet
- Navigate to the Data Tab
- Select Data Validation
- Allow: List
- Source: =$A$2:$A$10
    - Use the cell selector button on the right side to select the range
- Select OK to complete

![DataValidationRange](images/DataValidationRange.png)

* * *

This is great and "**it works,**" but let's say tomorrow you want to add an item to A11. Then, you have to go back to the data validation tab and edit the source to $A$2:$A$11. And then the next day, through range A12, and then A13 and then A14. You could always just change source to be A:A, ignore blank and be done with it all right? Well sure, if you are a big fan of forcing your computer to unnecessarily count to 1,048,576, or if you enjoy closing and reopening your workbook every time you make edits to see them reflected properly.

![ezGIF-ListAA](images/ezGIF-ListAA.gif)

* * *

### "Insanity Is Repeating The Same Mistakes and Expecting Different Results"

[Not Albert Einstein](https://www.quora.com/Did-Einstein-really-define-insanity-as-doing-the-same-thing-over-and-over-again-and-expecting-different-results)

* * *

### **WHAT'S YOUR NAME?!**

- Select Cells A2:A11
- To the left of the Formula Bar is the Name Box. Select the default value shown and replace with ProductList.
    - Note: this cannot contain spaces and must start with a letter or underscore
- You can also use the Name Box to easily navigate to the range locations. Select the drop down icon to view available selections.

![ProductList](images/ProductList.gif)

* * *

### I'D LIKE TO SPEAK TO A MANAGER...

- Navigate to the Formulas Tab
- Select Name Manager
    - **Name:** The named ranges and objects contained within your workbook. The ProductList displays a named range icon while the tblProducts displays the icon for a table object.
    - **Value:** From our [previous lesson](http://itsnotaboutthecell.com/2016/02/16/500-days-of-sumsumifs/) we recognize the curly braces surrounding each named range value as information stored within an array
    - **Refers To:** Information either stored locally or declared using a function

![NameManager](images/NameManager.png)

* * *

### **Make It Again:**

- Select a cell from within your worksheet
- Navigate to the Data Tab
- Select Data Validation
- Source: =ProductList
    - Note: this must include the = symbol, otherwise Excel will interpret the source as a string of text
- Select OK to complete

![DataValidation](images/DataValidation.png)

As you continue to add and remove items from the column titled Product within your table object, you will now notice that your drop down list is automatically updating without forcing you to make any changes to the cell range.

* * *

Honestly, I've stopped using cell ranges for some time now, and I want to make a strong argument that you should too. Even the lessons on this site were designed since day one specifically for tables and my use of cell ranges is rare unless absolutely necessary. If you're skeptical of their importance there's an entire book dedicated to **JUST** tables "[Excel Tables: A Complete Guide for Creating, Using and Automating Lists and Tables](http://www.amazon.com/Excel-Tables-Complete-Creating-Automating/dp/161547028X/ref=sr_1_1?ie=UTF8&qid=1461022246&sr=8-1&keywords=excel+table)." Ultimately, though if the majority of your time is spent cleansing unstructured information, you have two choices: either start loving it or start listing it.
