---
title: "To Err Is Computational"
date: 2015-09-21
categories: 
  - "excel"
tags: 
  - "div0"
  - "fml"
  - "na"
  - "name"
  - "null"
  - "num"
  - "ref"
  - "value"
  - "error"
  - "excel"
  - "formula-auditing"
  - "george-costanza"
  - "iferror"
  - "seinfeld"
  - "trace-dependents"
  - "trace-precedents"
comments: true
---

You will never learn more about Excel than on the day you inherit a broken workbook. You're tasked with uncovering the method to the original author's madness, and if you're not careful you can get lost trying to understand why the author did things the way they did instead of finding the solution.

<!-- more -->

| **Error Type** | **Description** |
| --- | --- |
| #NULL! | When a function returns an invalid result. |
| #DIV/0! | When a function attempts to divide by zero. |
| #VALUE! | When a function contains incompatible information. |
| #REF! | When a cell reference is moved or deleted. |
| #NAME? | When a cell reference or named range is unable to be located. |
| #NUM! | When an invalid number is encountered within a function. |
| #N/A! | When a function is unable to return an applicable result. |

I know what you're thinking, a bunch of confusing hashtags to try and remember, [#FML](https://twitter.com/search?q=%23FML&src=typd) right? Well they are actually a lot more helpful than they let on.

* * *

Error: **#NULL!**

**Make It:**

- \=Sum(A1 A10)

**Imagine It:**

- When a function is missing a range operator or when a range intersect does not exist.

* * *

Error: **#DIV/0!**

**Make It:**

- \=100 / 0

**Imagine It:**

- Attempting to divide a number by a number that contains no value.

* * *

Error: **#VALUE!**

**Make It:**

- \=10 + "Dog"

**Imagine It:**

- When a function attempts to add two different value types such as a number and a word.

* * *

Error: **#REF!**

**Make It:**

- \=A2 + A3
- Delete row 3

**Imagine It:**

- When a cell reference no longer exists.

* * *

Error: **#NAME?**

**Make It:**

- \=COUN(A1:A10)

**Imagine It:**

- When referencing an invalid function.

* * *

Error: **#NUM!**

**Make It:**

- \=SQRT(-10)

**Imagine It:**

- When using incompatible symbols or numbers within a function.

* * *

Error: **#N/A!**

**Make It:**

- \=VLOOKUP(20,A1:A6,1,FALSE)
    

**Imagine It:**

- When no applicable results can be found.

* * *

## When In Doubt, Trace It Out

I've been going on and on about these dang errors, so how about we find our sources using formula auditing to determine exactly where the disconnects are being made instead?

1. **Use The Formula (Auditing) Luke...**

- Go To The Formulas tab
- Within the Formula Auditing section are the options to:
    - Trace Precedents
    - Trace Dependents
    - Evaluate Formula

2\. **The Formula Trail (Dysentery Not Included)**

- Select a Cell and Click
    - **Trace Precedents** to view all cells that proceed the cell value.
        - **Pro Tip:** Ctrl + \[
    - **Trace Dependents** to view all cells that dependent upon the cell value.
        - **Pro Tip:** Ctrl + \]

[![TraceErrors](images/TraceErrors.png)](http://itsnotaboutthecell.com/wp-content/uploads/2015/09/TraceErrors.png)3\. **Leave No Trace**

- Once you are done auditing your workbook you can select **Remove Arrows** to eliminate all worksheet tracing elements.

4\. **See It To Believe It**

- Within the Formula Auditing section **Evaluate Formula** will take you step by step through your function as well as the operator order. This process is imperative to ensuring you have placed parenthesis appropriately throughout your function.

* * *

> ## **"It's Not You, It's Me"**
> 
> George Costanza

Sometimes we are just trying to make something out of nothing. It happens. No matter how hard we try we just can't tell our story with the information provided. Instead we are left with a worksheet riddled with ugly hashtags for all to see. The great thing about Excel is we are allowed to mask these shortcomings via error handling functions.

* * *

Function: **IFERROR**

**Describe It**:

- Return a value if valid or an alternate value if an error occurs.

**Synatx**:

- \=IFERROR(value,value\_if\_error)
    - The value can be any combination of text, numbers, functions or boolean.
    - The value if error can also be any combination of text, numbers, functions or boolean.

**Make It:**

- \=IFERROR(10/Cats,"HELP!")
- \=IFERROR(10/5),300)
- \=IFERROR(10/0),"DR WHO")

**Pro Tip: Double Quotations ""**

- The great thing about the **IFERROR** function is that it's very simple to start using and a game changer once you've mastered it. Often people will use strings such as "N/A" to let the end user know not applicable when value\_if\_error occurs. I agree that process "**WORKS,"** but I'm in that new school of thought and prefer to concentrate on functions devoid of noise.

**Make It:**

- \=IFERROR(10/Cats,"")
- \=IFERROR(10/5),"")
- \=IFERROR(10/0),"")

**Talk It Out:**

- The formulas still exist regardless of the empty visual on your worksheet. Once you start building in nested functions to deal with real world changes that occur you will be prepared to display information as soon as it's available.

* * *

I'll say it for the thousandth time, you will never learn more about Excel than on the day you inherit a broken workbook. I can shorten the blog and tell you where to click but honestly that information is everywhere on the internet. I want you to understand WHY we do things in Excel. Next up is data visualization, so let's move past the grind and into the reward.
