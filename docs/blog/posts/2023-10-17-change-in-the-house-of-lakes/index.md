---
title: "CHANGE (IN THE HOUSE OF LAKES)"
date: 2023-10-17
categories: 
  - "microsoft-fabric"
tags: 
  - "data-factory"
  - "data-pipeline"
  - "dataflow-gen2"
  - "microsoft-fabric"
  - "power-query"
comments: true
---

Data Factory in Microsoft Fabric is an AMAZING tool that allows us to combine the flexibility of Data pipelines and ease of a Dataflow Gen2 to create some nifty solutions with a **_tiny_** _**smidge**_ of code. One of the most common use cases is the ability to load new data into a destination for a select period (incrementally). Below is a high-level diagram that we’ll start breaking down to copy data from a SQL Database into a Lakehouse.

<!-- more -->

[![Picture of a completed pipeline used to incrementally load data using a Dataflow Gen2 and a Data pipeline.](images/IncrementalRefreshPipeline-1-1024x292.png)](https://itsnotaboutthecell.com/wp-content/uploads/2023/10/IncrementalRefreshPipeline-1.png)

To get started, create a new Warehouse item and execute the below SQL query to create a stored procedure. For the purposes of this example, I’m using date only but please feel free to adjust as needed for datetime. (I’ll be highlighting why I started with date only while leveraging the world’s most popular language Power Query M a bit later…)

```
CREATE PROCEDURE IncrementRefresh @DateValue DATE
AS

DROP TABLE dbo.IrDate;

CREATE TABLE dbo.IrDate (
    DateValue DATE
);

INSERT INTO dbo.IrDate (DateValue)
VALUES (@DateValue);

GO;
```

[![Creating a stored procedure within Synapse Engineering's datawarehouse.](images/StoredProcedure-1024x462.png)](https://itsnotaboutthecell.com/wp-content/uploads/2023/10/StoredProcedure.png)

We'll now execute our stored procedure to add a single date value into our table and view the results once complete.

```
EXEC IncrementRefresh @DateValue = '2018-06-01';

SELECT * FROM dbo.IrDate;
```

[![Executing a stored procedure within Synapse Engineering's datawarehouse.](images/ExecuProcedure-1024x512.png)](https://itsnotaboutthecell.com/wp-content/uploads/2023/10/ExecuProcedure.png)

Next, create a Dataflow Gen2 and a new query using **Get data > from Warehouse**. Connect to the table that contains our date value and select **Drill down** to convert the query into a scalar value.

Also, create another query using **Get data > from SQL Server** for the table you want to setup an incremental refresh with (this could be any data source in your case, preferably one that that supports [query folding](https://powerquery.microsoft.com/blog/introduction-to-practical-query-folding/)).

[![Setting a drill down value with Data Factory's Dataflow Gen2.](images/DrillDown-1011x1024.png)](https://itsnotaboutthecell.com/wp-content/uploads/2023/10/DrillDown.png)

To avoid refreshing fact tables that may take forever to complete with large volumes, we’ll go for a specific period using the date/datetime columns and set a static filter for **Equals**... and then jump into the formula bar for a small bit of Power Query M later.

[![Selecting equals to for a date range filter with Data Factory's Dataflow Gen2.](images/DateTimeFilter-1024x590.png)](https://itsnotaboutthecell.com/wp-content/uploads/2023/10/DateTimeFilter.png)

Now, let’s set up a static filter for **equals** on the date/datetime columns in the **Filter rows** window. Type in any static value and select **OK** \- we’ll update this using the scalar value from our Warehouse in the next portion.

[![Setting a date range filter with Data Factory's Dataflow Gen2.](images/EqualsDate-1024x605.png)](https://itsnotaboutthecell.com/wp-content/uploads/2023/10/EqualsDate.png)

To update the formula, we’ll replace the #datetime(yyyy,mm,dd,hh,mm,ss) value with the scalar value from our IrDate query and cast it to a datetime type using [DateTime.From](https://learn.microsoft.com/powerquery-m/datetime-from) function.

```
Table.SelectRows(#"Remove Columns", each [ModifiedDate] = DateTime.From(IrDate))
```

"I can hear you wondering why we didn’t cast it appropriately at the beginning?!" The reason is that I wanted to show you the full flexibility of adjusting your solution. If you ever need to modify this in the future, you can leverage Power Query M functions like ([Date.IsInCurrentMonth](https://learn.microsoft.com/powerquery-m/date-isincurrentmonth), [Date.Month,](https://learn.microsoft.com/powerquery-m/date-month) etc.)

[![Updating a formula with Data Factory's Dataflow Gen2.](images/UpdatedFormula-1024x614.png)](https://itsnotaboutthecell.com/wp-content/uploads/2023/10/UpdatedFormula.png)

Now that we’ve set up our filter, there are a few more important things to do. Right-click each query and deselect the “**Enable staging**” option. Why? Because both the sources Warehouse and SQL Database support [query fol](https://powerquery.microsoft.com/blog/introduction-to-practical-query-folding/)[d](https://powerquery.microsoft.com/en-us/blog/introduction-to-practical-query-folding/)[ing](https://powerquery.microsoft.com/en-us/blog/introduction-to-practical-query-folding/) - no need for all that Fabric compute to process heavy transformations since we're doing a simple WHERE equivalent, basically save them CUs! Make sure to set your destination to your Lakehouse / Warehouse (wherever you want!) by visiting **Home > Add data destination**, and setting the update method to **Append** and select **Publish**.

Of note, **Publish** will both publish the Dataflow and start the refresh activity, you may want to manually update the date within the Warehouse by executing the stored procedure once the dataflow refresh has completed to avoid duplication of results.

[![Disable staging with Data Factory's Dataflow Gen2.](images/PerfectScreenshot-1024x503.png)](https://itsnotaboutthecell.com/wp-content/uploads/2023/10/PerfectScreenshot.png)

Next, we’ll create a Data pipeline and in the bottom portion of the screen, we’ll select **Variables** and then **New** to create the three variables listed below.

| Name | Type | Default Value |
| --- | --- | --- |
| IncrementValue | Integer | 1 |
| DateValue | String | (leave as null) |
| MaxRange | Integer | 1 |

In our example, the **IncrementValue** will be used to set how many days we will incrementally count by, the **DateValue** will be used to store the date value from our Warehouse and **MaxRange** to set how many days we want this to run in a single instance. (For instance, if we want to increment by 1 day with a maximum period of up thirty times, we will grab 30 days’ worth of information on pipeline run.)

[![Creating variables within Data Factory's data pipeline.](images/CreateVariables-1024x632.png)](https://itsnotaboutthecell.com/wp-content/uploads/2023/10/CreateVariables.png)

Add a **Script activity** to the Data pipeline. In the **Settings** configuration, select the Warehouse name in the Data warehouse section and set the **Script** to **Query**. This will run the SQL query to obtain the date value that we previously inserted. Return to the **General** tab of the activity and update the title to **Get Date** before proceeding.

```
SELECT * FROM dbo.Irdate
```

[![Script activity within Data Factory's data pipeline.](images/ScriptActivity-1018x1024.png)](https://itsnotaboutthecell.com/wp-content/uploads/2023/10/ScriptActivity.png)

Using the **Activities** tab, insert a **Set variable activity**. Below the **Value** field, select **Add dynamic content** (click into the field well for it to become visible). Once in the expression builder, include the following expression which obtains the **DateValue** column’s first result (zero index) from our Get Date activity and select **OK** to close.

```
@activity('Get Date').output.resultSets[0].rows[0].DateValue
```

Return to the General menu and update the name of the activity to **Set DateValue** and drag and drop the **On success** conditional path from the **Get Date** activity to the **Set DateValue** activity.

[![Expression builder for set variable activity within Data Factory's data pipeline.](images/SetDateValue-1024x335.png)](https://itsnotaboutthecell.com/wp-content/uploads/2023/10/SetDateValue.png)

Using the Activities tab, add a **ForEach activity** to create a loop. With the activity selected in the Items field, select **Add dynamic content (**click into the field well for it to become visible**)**. Once in the expression builder, include the following expression below for range which will use the variable **MaxRange** to determine how many times we should increment through our activity and select **OK** to close.

```
@range(1,variables('MaxRange'))
```

[![Expression builder for the ForEach activity within Data Factory's data pipeline.](images/ForEachItem-1-1024x445.png)](https://itsnotaboutthecell.com/wp-content/uploads/2023/10/ForEachItem-1.png)

Select the pencil from the **ForEach** activity to move into the sub canvas editor and from the **Activities** menu add a **Dataflow** activity. Within the Settings we’ll add the Dataflow Gen2 that we created previously from the drop-down menu and update the name to **Incremental Dataflow**.

[![Dataflow Gen2 activity within Data Factory's data pipeline.](images/AddDataflow-1024x672.png)](https://itsnotaboutthecell.com/wp-content/uploads/2023/10/AddDataflow.png)

Using the Activities tab, add a **Stored procedure activity**. With the activity selected in the Settings configuration, select Workspace within the Data store type and choose your Warehouse from within the drop-down list. Select the **Stored procedure name** that we created earlier for **IncrementalRefresh**. Within the Stored procedure parameters section, select **Import** and for the **DateValue**'s **Value** select **Add dynamic content** (click into the field well for it to become visible).

Once in the expression builder, include this expression below to add a day to our current date based on our increment value of 1 (e.g., June 1st would then update to June 2nd and so on) and select **OK** to close.

```
@adddays(variables('DateValue'), variables('IncrementValue'))
```

Once complete, update the name of the Stored procedure activity to **Update date**, drag and drop the **On success** conditional path from the **Incremental Dataflow** activity to the **Update date** activity.

[![Expression builder for stored procedure activity within Data Factory's data pipeline.](images/Stored-procedure-1-1024x564.png)](https://itsnotaboutthecell.com/wp-content/uploads/2023/10/Stored-procedure-1.png)

To return to our **Pipeline**, select the **Main canvas** text from the top left. Next, navigate to the **Home** tab and click on **Run** to enjoy the beautiful incrementally loaded data! The right portion of the screenshot below shows that our original date has now been updated to June 2nd and is ready for our next run. Ideally, this should be scheduled through the **Scheduler** on the **Home** tab and in accordance with the data update cadence.

[![A picture of a data pipeline and warehouse upon successful completion](images/SuccessPipeline-1024x592.png)](https://itsnotaboutthecell.com/wp-content/uploads/2023/10/SuccessPipeline.png)

Ok, long~ish post with a lot of pictures and a few bits of text but honestly a couple lines of SQL, a couple of activities on the Data pipeline canvas and done. Easy peezy lemon squeezy. Let me know in the comments if you put this pattern into action and how you improved upon it too!
