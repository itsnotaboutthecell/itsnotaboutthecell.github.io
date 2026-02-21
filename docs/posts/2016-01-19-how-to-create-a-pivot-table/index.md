---
title: "That Pivotal Moment"
date: 2016-01-19
categories: 
  - "excel"
tags: 
  - "carl-orff"
  - "carmina-burana"
  - "columns"
  - "community"
  - "count"
  - "countifs"
  - "excel-girl"
  - "excel-guy"
  - "field-list"
  - "filters"
  - "group"
  - "oz-d-du-soleil"
  - "pierce-hawthorne"
  - "pivot-table"
  - "pivotal"
  - "pivottable"
  - "refresh"
  - "refresh-all"
  - "rock-the-vote"
  - "rows"
  - "streets-ahead"
  - "streets-behind"
  - "subtotal"
  - "sum"
  - "sumifs"
  - "values"
comments: true
---

## piv·ot·al

<!-- more -->

##### ˈpivədl/

Of crucial importance in relation to the development or success of something else. Synonyms: central, crucial, vital, critical, focal, essential, key, decisive

* * *

There is no such thing as "**the right time**" when it comes to developing your talents in Excel. You are always on call as the swiss-army-knife of information. Today a financial analyst, tomorrow a visualization specialist... within each role you are consistently relied upon to evolve your talents at a moment's notice. So, throw away your abacus because you're about to learn one of the best tools for your arsenal.

* * *

## ![PivotTable](images/PivotTable.png)

##   

<iframe src="https://www.youtube.com/embed/AdIpoE2LEps?rel=0&amp;autoplay=1" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

* * *

### Download Workbook

* * *

### Let's Get Pivotal, Pivotal!

- Go to the Data worksheet and select a cell (**A1**) within your table object
- Go to the **Insert** tab and select **PivotTable**
- Within the Create PivotTable options dialog box
    - Select a table or range
        - Table/Range: **tblData**
    - Choose where you want the PivotTable report to be placed
        - - **New Worksheet**

* * *

Before you start dragging and dropping, let's first learn what goes on within each area.

![Pivot Areas](images/Pivot-Areas.png)

**Filters:** Display information that meets a specified criteria

**Columns:** Display fields horizontally

**Rows:** Display fields vertically

**Values:** Summarize numeric or text information

You can control the visibility of the **PivotTable Fields** sidebar by selecting your PivotTable and going to the **Analyze** tab on your ribbon. From there you can select or deselect the **Field List** button.

* * *

### Watch Then Learn

<iframe src="https://www.youtube.com/embed/SLhsEvMcBbs" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

* * *

### Ask the Question:

**"What are the total sales by name and date?"**

##### **Make It:**

- Drag the Name field into the Rows area
- Drag the Date field into Rows area positioned beneath Name
    - Rows and columns within a lower position are nested within the area immediately above
- Drag the Sales field into the Values area

##### **Describe It:**

You've completely bypassed multiple **SUM** or **SUMIFS** functions in order to get total sales figures using the Name and Date fields.

* * *

### Ask the Next Question:

**"What are the total sales counts by name and date?"**

##### **Make It:**

- Once again, drag the Sales field into the Values area beneath Sum of Sales
- Select Sum of Sales2 to display the options and select Value Field Settings...
- Within the Summarize Values By tab, select the Count option and then OK

##### **Describe It:**

You've completely bypassed multiple **COUNT** or **COUNTIFS** functions in order to get total sales figures using the Name and Date fields.

* * *

### And The Next Question:

**"What are the total sales figures by item?"**

##### **Make It:**

- Drag the Item field into the Columns area positioned above the Values field

##### **Describe It:**

- The count will now appear adjacent to each Items Sum of Sales total, if you were to position the Item field beneath Values, the items would be placed to the right of all Sum of Sales totals.

* * *

You've just made a PivotTable **by simply dragging and dropping**. In many respects, you might be considered an advanced Excel user by possessing this ability alone. But my [mission](http://itsnotaboutthecell.com/about/) isn't to make you good at Excel; it's to make you **great** at it. As an Excel developer, being as efficient and effective as possible in delivering interactive solutions to your end users will make you [streets ahead](https://www.youtube.com/watch?v=rf1GSjo4zSY&feature=youtu.be&t=17).

* * *

![DisclaimerNotice](images/DisclaimerNotice.png)

There will be a **TON** of information to juggle as we head into the more advanced concepts. Slow down and take one thing at a time as you work through each section.

<iframe src="https://www.youtube.com/embed/kLNTVrqHSvs" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

* * *

### **Column Naming**

Change Sum of Sales to: **"Sales "**

- Because the field Sales already exists, you can add an additional space after the field name to create a common workaround

Change Count of Sales2 to: "**Item Count**"

- Because the field Item Count does not already exist, you can create a custom name

* * *

### PivotTable Options

Right click the PivotTable and select **PivotTable Options...**

**Tab:** Layout & Format

- Autofit column widths on update: **Deselect**
- For empty cells show: **0** (Zero)

**Tab:** Display

- Field List: **Sort A to Z**

**Tab:** Data

- Number of items to retain per field: **None**
    - This is an interesting option, if you were to leave as automatic, because as data is removed from your record source the PivotTable would treat the deleted information as if it still exists. There may be some professions where this is necessary, but I'm estimating that is only about 1% of Excel users. For the majority of us, we want information to correlate so we can validate it at a moments notice in the event of discrepancies.

* * *

### Date Fields

Right click a date record within the PivotTable and select **Group...**

- By: **Days, Months, Years**

Right click a month record within the PivotTable and select the following:

- Subtotal "Months"
- Expand/Collapse: **Collapse Entire Field**

Right click a year record within the PivotTable and select the following:

- Subtotal "Years"

For Excel 2016 users, the Microsoft Office team has made time grouping automatic.

* * *

### **Slicer**

Select the PivotTable and go to the **Analyze** tab

- Select: **Insert Slicer**
- Select: **Name** & **State**
- Right click the Name Slicer and select: **Slicer Settings...**
    - Select: **Hide items with no data**

###### See the Difference of No Data:

Select "Brian" within the Name slicer and you will notice all States are still visible except for those without values, which are now greyed out. Clear the Name slicer and now select the state "AR" within the State slicer, you will notice that only the names "Brett" and "Ralph" appear within the Name slicer now.

* * *

### **Timeline**

For Excel 2013 users and beyond...

Select the PivotTable and go to the **Analyze** tab

- Select: **Insert Timeline**
- Select: **Date**

###### **Opinion on Time Level**

While I think the Timeline slicer is a great addition to Excel 2013 and on, I rarely use it because it restricts editing and disables its best assetthe Time Level selector whenever the worksheet is protected. The only workarounds that I have found thus far are to create four separate slicers.

![Timeline](images/Timeline.gif)

#### Do me a favor and [rock the vote](http://excel.uservoice.com/forums/304921-excel-for-windows-desktop-application/suggestions/10765209-enable-the-time-level-functionality-of-the-timelin) for time level to be fixed.

* * *

### **Refresh Data**

Select The PivotTable, right click and select: **Refresh**

or

Go to the **Data** tab

- Select: **Refresh All**

Last but certainly not least, when it comes to working with a PivotTable, refresh your worksheet objects to ensure new records are added and obsolete information is removed.

* * *

#### "We didn't wait for Excel before we went to the moon."

##### \-Oz D Du Soleil

* * *

There are certain moments in working with Excel where your major breakthroughs happen not because something was challenging but because it was so incredibly simple all this time. The PivotTable is **EXACTLY** that: an easy-to-start tool that is also incredibly powerful for seasoned developers. Don't wait to start trying out some of Excel's most robust features (**[Power Pivot](https://support.office.com/en-us/article/Power-Pivot-Add-in-a9c2c6e2-cc49-4976-a7d7-40896795d045), [Power Query](https://support.office.com/en-US/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605), [Power View](https://support.office.com/en-US/article/Power-View-Explore-visualize-and-present-your-data-98268D31-97E2-42AA-A52B-A68CF460472E)**), because in the age of big data the time is **NOW** for you to make your presence known and become the office professional you were meant to be....

## **The Excel Girl |** **The Excel Guy**
