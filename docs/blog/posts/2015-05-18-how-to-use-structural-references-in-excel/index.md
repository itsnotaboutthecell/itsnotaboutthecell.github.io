---
title: "The Million Dollar Bracket"
date: 2015-05-18
categories: 
  - "excel"
tags: 
  - "auto-fill"
  - "data-table"
  - "dynamic-data"
  - "excel"
  - "flo-rida"
  - "microsoft-excel"
  - "million-dollar-bracket"
  - "object"
  - "silicon-valley"
  - "spreadsheet"
  - "structure-reference"
  - "workbook"
comments: true
---

In our [last lesson](http://itsnotaboutthecell.com/2015/05/18/fivestardinner/) we talked about following the laws of fields and records. Now is the time to expand on that thought process because everything you knew about cell ranges and formulas is about to get turned upside down with two simple keyboard strokes.

<!-- more -->

* * *

Right now is your [come-to-Jesus moment](http://www.urbandictionary.com/define.php?term=come-to-Jesus+moment). You have been abusing yourself managing cell ranges manually for far too long and it has to stop. From this day forth you will be reborn again as a devout believer in the Excel table object.

**What is a table object?**

Great question. A table object is a collection of fields and records whose dynamic properties automatically adjust as data manipulation occurs.

**Ok, I’m not following you…**

Imagine this - your worksheet is setup with a formula to look at a defined range from 1 to 1000 exclusively.

> **Example: =Sum(A1:A1000)**

There is no humanly possible way you will ever need to look at that 1001th row you told yourself when you originally designed the spreadsheet. Judgement day is upon you and the boss keeps asking for more and more of that spreadsheet that he/she loves. In a nervous sweat you realize that with the 200+ formulas in one spreadsheet, you will have to go back and manually edit each one to expand your cell range. Smack dab in the middle of a late-night-infomercial-come-to-life, you tell yourself, **“[there has got to be a better way.](https://www.youtube.com/watch?v=lYpKYxozJ7c)”**

[Thank you Florida](https://www.youtube.com/watch?v=KLoYVjDTYsM). Here's how to fix it:

1. Someone put a name on that table!

- With the table selected go to the **Design** tab of your ribbon
- Within the Properties section will be the option **Table Name:**
    - No -
        - Spacing
        - Special Characters (An underscore being the only exception)

2\. Venture into dynamic data

- - As you add and remove data the tables range properties will expand and contrast according to the data records both vertically or horizontally

<iframe src="https://www.youtube.com/embed/3--HkBIgcoo" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

3\. Use the Million Dollar Bracket - \[  \]

> Relative Formulas - **\=\[@Field\]**

- Advantages -
    - Easily select table object fields
    - Auto Fill fields

<iframe src="https://www.youtube.com/embed/lJDk6kKIX8Y" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

> Dynamic Formulas - **\=tableName\[Field\]**

- Advantages -
    - Easily read formulas by referencing field titles
- Master It -
    - As you type you can utilize the "Tab" key to auto complete table or field names

<iframe src="https://www.youtube.com/embed/vXl7x7PFXSc" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

4\. Start managing your workbook using Dynamic Formulas

Count to 17,179,869,184 **(1,048,576 rows \* 16,384 columns)**

### **No. Because that's a waste of your time.**

When referencing table objects in your formulas it only looks within the table objects boundaries - no more, no less. Too often people are forcing the Excel application to review large ranges of empty cells to determine if values exist thereby killing your workbook's overall potential. That is why I place such a strong emphasis on managing your system's resources  and your end user's experience appropriately.

* * *

> If you or someone you know, is suffering from resource limiting formulas like the one below please download the [sample workbook](http://itsnotaboutthecell.com/wp-content/uploads/2015/05/MillionDollarTable.xlsx) now -
> 
> **Example: =SUM(A:A)**
