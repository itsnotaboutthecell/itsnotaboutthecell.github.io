---
title: "Mad Maximum Value"
date: 2015-06-10
categories: 
  - "excel"
tags: 
  - "dystopia"
  - "eomonth"
  - "mad-max"
  - "max"
  - "maximum"
  - "min"
  - "minimum"
  - "seinfeld"
  - "serenity-now"
comments: true
---

### **"Without villains, there can be no heroes."**

<!-- more -->

Our society is suffering under the constant oppression of dystopian workbooks - riddled with mediocrity and confined to restrictive methods. We need a hero. Someone to _write_ the wrongs and be the protagonist in our story. We need a Mad Maximum Value.

Great workbooks stand the test of time. This is a fact. The more you continue to work in or around data, the more you will find that data dimensions follow similar patterns, generally revolving around names, dates, times and counts. Consistently finding inventive ways to show this information is what sets developers like yourself apart.

* * *

We're jumping right into some of that learning, so for now, [enjoy](https://www.youtube.com/watch?v=SHoNWwhzh3M) this lesson.

[Download Workbook](http://itsnotaboutthecell.com/wp-content/uploads/2015/06/Mad-Maximum-Value.xlsx)

Function: **EOMONTH**

**Describe It**:

- Returns the last date of a month.

**Synatx**:

- \=EOMONTH(start\_date, months)
    - The start\_date can be any serial date value (number)
    - The months can be any numerical value both past, present or future

**Make It:**

- \=EOMONTH(TODAY(),0)
- \=EOMONTH(TODAY(),1)
- \=EOMONTH(TODAY(),-1)

* * *

I hate to be the bearer of bad news but there is no BOMONTH (Beginning of Month) function.

> Don't do anything rash in light of this revelation. Step away from the computer. [Serenity now](https://www.youtube.com/watch?v=Ow_9MglZrhs).

Remember, you're an experienced [time traveler](http://itsnotaboutthecell.com/2015/06/01/wait-a-minute-doc-are-you-telling-me-that-you-built-a-time-machine-out-of-a-spreadsheet/) navigating the basic constructs of Excel. Let's evaluate this logically.

**Talk It Out:**

- EOMONTH returns the last day of the month, we could simply add one to this date value to return the next calendar date.

**Make It:**

- \=EOMONTH(TODAY(),-1) + 1

Take _that_ Microsoft.

**Quick Recap:**

- When we evaluate information, we are trying to answer a question as to who, what, and **when**. The EOMONTH function is great in establishing sound parameters for reviewing monthly (and/or yearly ranges). Strengthening our understanding of date functions (and how to manipulate them) will only make your worksheet that much stronger.

* * *

Function: **MAX**

**Describe It:** 

- Returns the largest value in a set of values
- Maximum Value

**Syntax:**

- \=MAX(number1)
    - The max function can be used to review multiple sets of values or just a single range

**Make It:**

- \=MAX(Sales\[Date\])

**Quick Tip:**

- The **MIN** (Minimum Value) function is the exact opposite of the **MAX**

* * *

Now, about that nesting. Excel can handle up to 255 arguments in a function. **TWO HUNDRED AND FIFTY FIVE**. If you are afraid of using nested functions because one of your formulas may be too large, you need to start confronting the demons of worksheets past. Using ten cells to calculate what could have been calculated using a single cell is a [waste of your computer's resources](https://msdn.microsoft.com/en-us/library/office/ff700515\(v=office.14\).aspx#Office2007excelPerf_UnderstandingCalculationMethodsExcel).

Recognizing what data is and understanding what data could be is what separates you from the rest of the crew. This is your Mad Maximum Value.

Nested Function: **EOMONTH(MAX(),-1))+1**

**Talk it Out:**

- Using the max function you can return the largest (think newest) date value anytime information is appended to your record source
- Using the EOMONTH function alongside a past value (negative one) plus one you can return the beginning of the most recent month of records

**Make It:**

- \=EOMONTH(MAX(Sales\[Date\]),-1)+1

<iframe src="https://www.youtube.com/embed/7tWIVrrmqSc" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

Things like this come in handy in a number of ways. Add a couple new dates to the table and see for yourself.

* * *

We're getting closer and closer to this stuff making sense - **TRUST ME**. In the next lesson, we'll go over the one magic trick that will help you defy conventional development using the illusion of movement.
