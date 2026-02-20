---
title: "The Illusion of Movement"
date: 2015-07-01
categories: 
  - "excel"
tags: 
  - "active-x"
  - "customize-ribbon"
  - "developer"
  - "eomonth"
  - "event-handler"
  - "form-object"
  - "gui"
  - "input"
  - "max"
  - "microsoft-excel"
  - "min"
  - "onclick"
  - "output"
  - "pro-tip"
  - "spin-button"
  - "spreadsheet"
comments: true
---

> ##### Until you've tasted the sour you can never truly enjoy the sweet.

<!-- more -->

* * *

Let's look at two varying statements objectively -

**Excel is a great application because of its incredible ease of use.**

**Excel is a terrible application because of its incredible ease of use.**

Getting started is as easy as clicking in a square box and typing away on your keyboard. It's likely that you can create a workbook that "**gets the job done**." You can also create a lifetime's worth of bad habits that will cost you time in the long run. _**Remember the cost of time = money.**_ But it's because we have struggled that we can now appreciate the complexity of what is placed in front of us in these tiny little squares.

**\* Insert infomercial speech about how easy Excel is and how to master in a weekend.**

* * *

Often we learn by emulating the practices we see in the environment around us. Those in well developed and nurtured environments thrive. Those without available resources, well... they often "**get the job done.**"

# That mentality ends now.

I'm preparing you for this as your skills are about to distance you from the environment around you. There is no going back once you've been to the other side. From this day forward you are a developer.

**Enable the Developer Tab**

- File
- Options
- Customize Ribbon
- Select Developer

![Developer](images/Developer.png)

**Code?! Add-Ins?! Controls?! XML?!**

Calm down. I'm not throwing you to the wolves (that comes later). I want you to start playing around with the form controls - it's really going to tie into the last couple of lessons.

**Put a Little Spin On Your Worksheet**

- Developer Tab
- Insert
- Under Form Controls - select "Spin Button (Form Control)"
    - Stay out of those ActiveX Controls for now

![SpinButton](images/SpinButton.png)

**Every Click Counts**

- Right-click the spin button and select "Format Control"
- Under the cell tab go to "Cell Link" and click the "Cell Selector"
- Select any single cell and press OK when complete
    - **Pro Tip**: I always use cell A1 - find a habit and stick to it
- Click click click away

![CellLink](images/CellLink.png)

* * *

> **Counting numbers by pressing a button? Really?**

I knew I was going to have some skeptics after this big reveal so let's talk about what just happened.

- You created a graphical user interface (GUI) with the Spin Button.
    - The form object allows you to interact with your worksheet

- You established an event - OnClick
    - Every time the Spin Button is pressed, the program is going to respond by changing the incremental value up or down onto your spreadsheet.

The whole process that occurs as you press up and down is known as an [event handler](http://searchsoa.techtarget.com/definition/event-handler). In layman's terms, how the application Excel receives and responds to events.

> **Input -> Output**

Take some time and explore the different form objects. Don't get frustrated if some things are over your head right now. Simply knowing what exists will improve your long term development. The rest will come in time as you continue use.

* * *

Now that we're done nerding out on the technical jargon for a bit, let's bring all the time traveling, MIN, MAX, and EOMONTH talk full-circle.

We're going to go back to our [last lesson](http://itsnotaboutthecell.com/2015/06/10/mad-maximum-value/) with the Mad Maximum [workbook](http://itsnotaboutthecell.com/wp-content/uploads/2015/06/Illusion-of-Movement.xlsx) and invoke some [time travel](http://itsnotaboutthecell.com/2015/06/01/wait-a-minute-doc-are-you-telling-me-that-you-built-a-time-machine-out-of-a-spreadsheet/) logic along the way.

**Describe It - Nested Function:**

- \=EOMONTH(MAX(Sales\[Date\]),-1)+1
    - **Talk it Out:** We know it's a past event (negative) and it's a static value of 1 in the current formula.

Let's change this static value into something a bit more interactive with our form object.

**Make It User-Controlled:**

- Add your spin button and set the cell link to A1
    - **Pro-Tip**: Minimum Value set to 0 is going to return you to the present in accordance with our time travel logic, change this to 1
- Change the Nested Function formula to include the cell link output
    - \=EOMONTH(MAX(Sales\[Date\]),-A1)+1
    - **Pro-Tip:** Placing a minus sign in front of your cell references will return them as negative values (We want to look at the past)
- Add the EDATE formula with negative 1 as your number of months
    - **Talk it Out:** Negative values indicate the past
- Use relational reference Auto Fill to create a cascading month over month view
    - **Talk it Out:** Relational reference will allow you to utilize adjacent cell values

**Click Away!**

<iframe src="https://www.youtube.com/embed/YLsBelD7ztw" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

* * *

## ["It is not the spoon that bends, it is only yourself."](https://www.youtube.com/watch?v=7n5UBrTGdxo)

Getting past the limiting idea that Excel is just a bunch of square boxes is the ultimate key to your success. People use Excel to create [beautiful artwork](http://www.spoon-tamago.com/2013/05/28/tatsuo-horiuchi-excel-spreadsheet-artist/), [role-playing games](http://carywalkin.ca/2013/03/17/arena-xlsm-released/) and financial modeling that drives our economies. It's Not About The Cell is not just a funny title. It's about changing your mindset and leveraging basic, everyday concepts to help you build your talents and take over the world. Thank you for taking this journey with me.
