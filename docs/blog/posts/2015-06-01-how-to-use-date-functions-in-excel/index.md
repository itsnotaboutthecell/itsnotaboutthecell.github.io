---
title: "Wait a Minute Doc. Are You Telling Me That You Built a Time Machine Out of a Spreadsheet?"
date: 2015-06-01
categories: 
  - "excel"
tags: 
  - "back-to-the-future"
  - "dates"
  - "delorean"
  - "doc-brown"
  - "edate"
  - "excel"
  - "flux-capacitor"
  - "function"
  - "jiggawatt"
  - "kingpin"
  - "marty-mcfly"
  - "roy-munson"
  - "today"
comments: true
---

#### "**I don't know what you're making me do and** **I have no idea when I will ever use this.**"

<!-- more -->

Good. That means you're on the right track, because I need you to look past the obvious and start concentrating on the possibilities.

* * *

Let's consider this idea: **50%** of Excel's abilities have to do with inputting text and numbers. The other **50%** have to do with manipulating that text and those numbers. If you are having doubts about your skill level for this site I want you to know that you have already passed the typing test. My intent is to show you the dark corners of Excel - the other 50% - which will make you a better user overall. I want to show you the parts of Excel that most people do not even know exist. And that brings us to the discussion of time travel...

To understand the concept of time in Excel, we need to first establish a sequence of events - **The Past, The Present, The Future**

![RobotFace](images/RobotFace.png)

**The Past -** Negative Values

- Yesterday, last week , last month, last year - all events deriving a negative value from a mathematical standpoint - that's the past. If I were to ask you, "When was yesterday?" you could easily look at a calendar and subtract one day from the present to determine this value.

> Example: **\=Today() - 1**

**The Present -** Zero Value

- An un-manipulated value used to describe a current event.

> Example: **\=Today()**

**The Future -** Positive Values

- Tomorrow, next month, next year - all events deriving a positive value from a mathematical standpoint - that's the future. If I were to ask you, "When will it be one week from today?" you could easily look at a calendar and add seven days from the present to determine the value.

> Example: **\=Today() + 7**

Listen, I know you can figure [some things](https://www.youtube.com/watch?v=28vEFPAmGwU&feature=youtu.be&t=20) out for yourself, but these building blocks are important. They are what separate a usable spreadsheet from an indestructible spreadsheet - the kind that last for a lifetime without painstaking updates and revisions.

* * *

Let's make a little magic - download the sample [workbook](http://itsnotaboutthecell.com/wp-content/uploads/2016/01/DateValue.xlsx).

In both exercises below, we are going to look at the relative positioning of our cells and utilize "AutoFill" to create cascading values so that any time you update the "Date Value" cell, the spreadsheet will update accordingly.

**Weekly Results**

**Make It:**

- Create a formula to add / subtract 7 days from the present value
    - Something as simple as = Cell Range + 7 or  = Cell Range - 7

**Monthly Results**

**Function:** EDATE

**Describe It:**

- Effective Date of Change. Returns the same date value in past or future months (redundant for the present)

**Syntax:** =EDATE(start\_date,months)

- Use the present value as your start\_date
- Enter a numerical value for the number of months

**Make It:**

- Using the EDATE function create a formula to add / subtract 1 month from the present value

**Master It:**

- Use the "AutoFill" feature to easily drag formulas left or right to populate adjacent cells

<iframe src="https://www.youtube.com/embed/tm_8fwHd6L0" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

**Validate It**:

- Compare your outputted dates with their values to ensure accuracy from the present date value

* * *

Great formulas last forever. Let's say it all together now "**Great Formulas Last Forever.**" Excel is not about doing more - it's about doing more with less and finding consistencies that exist not only in your data but in the real world.
