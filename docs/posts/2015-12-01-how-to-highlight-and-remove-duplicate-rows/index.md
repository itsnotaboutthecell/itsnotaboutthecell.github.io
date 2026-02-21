---
title: "The Best Truth Is Data"
date: 2015-12-01
categories: 
  - "excel"
tags: 
  - "absolute"
  - "bear-down"
  - "cell-reference"
  - "chicago-bears"
  - "data"
  - "excel-expert"
  - "highlight-duplicates"
  - "jim-barksdale"
  - "microsoft-office-specialist"
  - "mixed"
  - "mos"
  - "netscape"
  - "relative"
  - "remove-duplicates"
  - "teddy-roosevelt"
  - "theodore-roosevelt"
  - "waynes-world"
  - "waynes-world-2"
comments: true
---

Information is not an argument, it's a conversation.  As a developer, having the ability to remove personal feelings about what you think a workbook should be will take you far in you career.  Always be mindful that your end users may simply want the freedom to drive their own story in an easy-to-use format. **And that's perfectly fine.** Not everyone is going to dedicate the time that is needed to be an [Excel expert](https://www.microsoft.com/en-us/learning/mos-expert-certification.aspx) like you. But when they start asking questions about inconsistencies within the data, speak softly and carry a big data validation stick. You're going to need it.

<!-- more -->

* * *

### “If we have data, let’s look at data. If all we have are opinions, let’s go with mine.”

\-Jim Barksdale

* * *

#### Download Workbook

* * *

In this post, we're going to start out very easy and then work our way towards some more advanced concepts. [Bear with me](https://www.youtube.com/watch?v=rqFf-0eROUA).

<iframe src="https://www.youtube.com/embed/zQZARjckpn8" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

### **Remove Duplicates**

- Select a cell range within your table object
- Go to the **Data** Tab and select **Remove Duplicates**
- Press **OK** to accept the default options

### **Highlight Range Duplicates**

- Select column C
- Go to the **Home** Tab and select **Conditional Formatting**
    - Highlight Cells Rules
        - **Duplicate Values...**
- Press **OK** to accept the default options

**Pro Tip:**

- Put this in the "**Nice To Know**" category, but keep in mind that Excel's duplicate values function is very limited because it can only compare the values in a single column or row.

### **Highlight Row Duplicates**

This is where things get interesting as you start comparing multiple [fields and records](http://itsnotaboutthecell.com/2015/05/18/fivestardinneronatable/). Unfortunately Excel does not yet have a built-in feature to highlight these instances. You'll need to get creative with a mix of functions and conditional formatting formulas. Let's start with creating a single record.

Function: **CONCATENATE**

**Describe It**:

- Joins multiple values into a single string.

**Syntax**:

- \=CONCATENATE(text1,text2,...)
    - text1 is the first positioned text - can be a text value, number, or cell reference.
    - text2 is you guessed it the second positioned text

**Make It:**

- \=CONCATENATE(\[@Date\],\[@Name\],\[@Item\],\[@\[Purchase Amount\]\])

* * *

**All of the values here were combined to create a record within a single field. You can now leverage Excel's duplicate values limitation and turn it into your strength.**

* * *

- Select columns A:D
- Go to the **Home** Tab and select **Conditional Formatting**
    - New Rule...
        - **Use a formula to determine which cells to format**
- Format values where this formula is true:
    - \=COUNTIF($E:$E,$E1)>1
- Select Format...
    - Go to the **Fill** tab and select a fill color
- Press **OK**

![DataValidation](images/DataValidation.png)

* * *

**What in the world were all of those dollar signs in =COUNTIF($E:$E,$E1)>1 ?**

* * *

I knew at some point you would [ask this question](http://i.imgur.com/LpRSE.jpg). Your ability to control Excel's cell referencing is extremely important. Especially in some fields where an entire workbook is driven off of a single cell's value. Within the formula bar, type **\=A1** and press the **F4** button on your keyboard to cycle through the different types of references that exist. Excel will automatically adjust if you insert or delete rows and columns so don't worry that what you write is final.

### Absolute

**Cell Reference:** $A$1

**Describe It**:

- The absolute position of a cell whose row and column reference will not change regardless of movement
- A function will always reference cell A1 no matter what position you are in within a worksheet

### Relative

**Cell Reference:** G5

**Table Reference:** \[@Date\]

**Describe It**:

- The relative positioning of a cell whose row and column reference changes dependent upon movement.
- If you move this function left it will turn into F5. If you move this function up it will turn into G4.

### Mixed

**Cell Reference:** $B2

**Describe It**:

- The relative positioning of a cell whose row reference changes dependent upon movement and whose column reference remains the same
- If you move this function left it will remain $B2. If you move this function down it will turn into $B3

**Cell Reference:** B$5

**Describe It**:

- The relative positioning of a cell whose column reference changes dependent upon movement and whose row reference remains the same
- If you move this function right it will turn into C$5. If you move this function down it will remain B$5.

* * *

Now that we got that out of the way let's get back to that formula...

### **\=COUNTIF($E:$E,$E1)>1**

You have programmed Excel to count whether the value in the mixed cell reference of $E:1 occurs within the absolute column reference of $E:$E more than 1 time. If it does, this returns a Boolean expression (**TRUE | FALSE**) and the row will be marked as having a duplicate record if **TRUE**. With what you now know about cell references you can determine that Excel will automatically create the following conditional formatting rules based upon the cells positioning:

**\=COUNTIF($E:$E,$E2)>1**

**\=COUNTIF($E:$E,$E3)>1**

**[and so on and so on and so on...](https://www.youtube.com/watch?v=JA7CKvoKEmE)**

* * *

Presenting validated information clearly and confidently is more important than that [pretty bar chart](http://itsnotaboutthecell.com/2015/10/10/you-dont-owe-anyone-an-explanation/). Remember that you have moved mountains of data and conquered spreadsheets that others dared not touch. You are the Ayatollah of Spreadsheet-Rolla. But, keep that ego in check as nobody wants to work with someone who makes a situation difficult or tries to make them feel technologically inferior. Find ways to use Excel to elevate those around you to make them better. Remember:

### **Excel is your platform, not your purpose.**
