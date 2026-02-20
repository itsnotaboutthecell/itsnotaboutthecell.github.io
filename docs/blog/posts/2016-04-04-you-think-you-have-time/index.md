---
title: "You Think You Have Time"
date: 2016-04-04
categories: 
  - "excel"
tags: 
  - "86400"
  - "beat-the-clock"
  - "cedar-rapids"
  - "datevalue"
  - "decimal"
  - "int"
  - "mod"
  - "not-too-shabby"
  - "nts"
  - "pomodoro"
  - "taco-bout-it"
  - "timevalue"
  - "tomato-timer"
  - "whole-number"
comments: true
---

With every passing second of every minute, of every hour - you are in a constant race against time. Trying to find time to exercise, to spend time with friends or family, or read the latest [Excel TV](https://excel.tv/blogging-buddies-meet-alex-of-its-not-about-the-cell/) article. Managing your schedule becomes even more important in the age of information. More data means more analysis, which means more reports. Either you beat the clock, or the clock beats you. But not everything is what it seems when it comes to time...

<!-- more -->

* * *

#### [Download Workbook](http://itsnotaboutthecell.com/wp-content/uploads/2016/04/Time.xlsx)

* * *

Function: **INT**

**Describe It:**

- Round a number down to the nearest integer

**Syntax:**

- \=INT(number)
    - Number is the value in which to round down and return with no decimal places

**Make It:**

\=INT(B3)

* * *

## HOLD ON, I THOUGHT YOU SAID

## THIS LESSON WAS ABOUT TIME?

It is, we just need to be a little bit more inventive with our use of functions once again.

* * *

**[Taco Bout It:](https://www.youtube.com/watch?v=0A8nEfYmmtM)**

- Excel dates are any zero or whole number value ranging from 0 (1/0/1900) to 2958465 (12/31/9999)
- Excel times are any decimal value ranging from 0 (0:00:00) to 0.99988426 (23:59:59)

If the INT function removes decimal numbers (time values). To extract the time value we would want to take the (Date Time) minus (Date).

* * *

**Make It Again:**

\=B3-INT(B3)

* * *

**Make It Even Better: (Courtesy of Brian Canes)**

Function: **MOD**

**Describe It:**

- Returns the remaining amount after a number is divided by a divisor

**Syntax:**

- \=MOD(number, divisor)
    - Number is the value in which to divide
    - Divisor is the value in which to divide by the number

**Make It:**

\=MOD(B3,1)

**Talk It Out:**

With MOD (Modulo) the function wants to see how much of your value is remaining. For instance if you were to try something like =MOD(10,3) you would see that 3 can go into 10, 3 times before it can no longer be used. At this point you have ( 10 - ( 3 + 3 + 3) ) = 1. In the above instance you are using 1 as the divisor to remove whole numbers (Date) and all that remains are decimal places (Time).

* * *

# N-T-S

###### (NOT TOO SHABBY)

I know what you're thinking: if only data was that clean all the time, right? Sometimes what you think are dates and times are actually just one long string of text that is impossible to format properly.

* * *

## 23DEC2016 15:38:56

* * *

Function: **DATEVALUE**

**Describe It:**

- Returns a date value from a text string

**Syntax:**

- \=DATEVALUE(date\_text)
    - date\_text is the value in which to round down and return with no decimal places.

**Make It:**

\=DATEVALUE(B6)

* * *

Function: **TIMEVALUE**

**Describe It:**

- Returns a time value as a decimal number from a text string

**Syntax:**

- \=TIMEVALUE(time\_text)
    - time\_text are values ranging from 0:00:00 to 23:59:59

**Make It:**

\=TIMEVALUE(B6)

* * *

## **If you don't respect your time no one else will.**

* * *

You are the expert. You are the one that everyone comes to for help. You get people out of the last minute jams. People can respect your skills, but if they don't respect your time you will never truly get anything of value accomplished. Always set time aside for yourself. Use a [Tomato Timer](http://tomato-timer.com/) to break up the daily monotony. Don't be afraid to step away from a project to gain clarity. We only have a finite amount of time on this planet. Do not spend each passing second entertaining the distractions.

* * *

#### So what are you waiting for?

# 86400

<script type="text/javascript">// <![CDATA[ /*author Philip M. 2010*/ <div></div> var timeInSecs; var ticker; <div></div> function startTimer(secs){ timeInSecs = parseInt(secs)-1; ticker = setInterval("tick()",1000); // every second } <div></div> function tick() { var secs = timeInSecs; if (secs>0) { timeInSecs--; } else { clearInterval(ticker); // stop counting at zero // startTimer(86400); // remove forward slashes in front of startTimer to repeat if required } <div></div> document.getElementById("countdown").innerHTML = secs; } <div></div> startTimer(86400); // 60 seconds // ]]></script>
