---
title: "Introduction to practical Query folding"
date: 2025-08-16
categories: 
  - "power-query"
tags: 
  - "excel"
  - "microsoft-fabric"
  - "power-bi"
  - "power-query"
  - "query-folding"
comments: true
---

One of the most powerful capabilities of Power Query and the M Language is Query Folding (also referred to as query delegation, and predicate push-down). Query Folding allows the Power Query Mashup Engine to **push the transformations expressed in an M (mashup) query to the data source, in the data source’s query language**, resulting in more efficient data processing.

<!-- more -->

For inexperienced database technology users this ability to leverage the graphical user interface of Power Query to dynamically generate a query written in the data source’s query language unlocks enormous opportunities to find insights with any data, at any scale.

In this article we’ll explore how to:

- Configure Global options in Power Query Online to enrich our development experience.

- Ensure folding queries for efficient data processing.

- Leverage folding indicators and query plans in a development workflow.

See [Understanding query evaluation and folding](https://docs.microsoft.com/power-query/query-folding-basics) for more details. 

## Configure Global options in Power Query Online

Before we begin using the Power Query Online experience, let’s ensure that we’ve enabled some authoring settings to assist us in our work. As we proceed through this article, we’ll utilize several of these settings within our workflow where fortunately for us, they will also persist the next time we return for future projects within Power Query. 

1. Within the Power Query Online editor, select the **Home** tab and then the **Options** > **Global options** property. 

![Global options in the Options Submenu in the Home tab of the Power Query ribbon](images/image-2.png)

2. Within the **Global options** window ensure the following settings are enabled and select **OK** once complete. 

**Steps** 

1. Enable query folding indicators 

3. Show script in step callout 

![Global options view within Power Query Online, with Enable query folding indicators and Show script in step callout enabled](images/image-3.png)

See [query folding indicators](https://docs.microsoft.com/power-query/step-folding-indicators) for more details. 

## Ensure folding queries for efficient data processing

When connecting to various data sources within the Database, Azure, or Online services categories within Power Query, we often may need to extract large volumes of data and for this we should only extract the necessary columns and rows needed for our projects requirements.  

In this example, we’ll leverage the scale and computing power of an Azure SQL Database data source and the [AdventureWorksLT sample database](https://docs.microsoft.com/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms#deploy-to-azure-sql-database) to demonstrate how we can leverage our data source to process our transformations.  

1. From the **Home** tab, we’ll select the **Choose columns** option to deselect the unnecessary columns within our Customer table. This will ensure that we only bring in the necessary and check marked columns. 

![The Choose columns dialog box, with columns disabled.](images/image-4.png)

2. Within the **Query settings** pane and in our **Applied steps** list the **Choose columns** step includes the **Folding** indicator. If we were to hover above the individual step name we’d get some additional information, including:
    - The full description of the **Folding** icon “This step will be evaluated by the data source.”
    
    - Our **Choose columns** transformation formula displayed within the **Script** area. The **Script** details are especially useful when needing to understand our previously applied step formulas without the necessity of opening the **Advanced Editor** or waiting for the **Data preview** window to display results

![Step name, folding indicator and script step information displayed on hover from the Applied steps list](images/image-23.png)

3. From the **Transform** tab, we’ll select the **Merge columns** option to combine our customers’ name fields into a new column titled Full Name using the **Space** separator to make it easier for others to read. 

![Merge columns dialog box to concatenate multiple fields into a full name](images/image-5-1024x554.png)

4. With the CompanyName column selected from the **Home** tab, we’ll select the **Filter rows** option to only return the necessary rows within our Customer table. In the **Filter rows** window, we’ll update the filtering options to **contains** and **or** – and within the value fields enter “Bike” and “Cycle” as our filtering criteria. 

![Filter rows dialog box, to find rows where Bike or Cycle are present within text](images/image-6-1024x616.png)

5. In the **Query settings** pane’s **Applied steps** list, our **Folding** step indicator now includes the **Choose columns**, **Merged columns** and **Filtered rows** steps. If we were to right-click any of these steps, we can then navigate to the **View data source query** option to view our transformations written in the data source’s query language. 

![Folding indicator icon spanning multiple steps and the View data source query option](images/image-10.png)

6. In the **Data source query** window is a read-only view of the SQL statement that will be sent to our data source, including our transformation steps:
    - **Merged columns** as a [CASE](https://docs.microsoft.com/sql/t-sql/language-elements/case-transact-sql) statement. 
    
    - **Choose columns** to limit the returned columns in the [SELECT](https://docs.microsoft.com/sql/t-sql/queries/select-transact-sql) statement. 
    
    - **Filtered rows** as a [WHERE](https://docs.microsoft.com/sql/t-sql/queries/where-transact-sql) clause, as displayed in the image below to only return rows where our condition of CompanyName containing Bike or Cycle have been met. 

![Data source query window, displaying the generated SQL statement](images/image-9.png)

## Leverage folding indicators and query plans in a development workflow

As demonstrated above, we didn’t write a single line of code to query our Azure SQL database and our transformations were instantly translated into the data source’s querying language. To ensure that we can achieve optimal performance with our queries let’s continue to explore our data using some common transformation steps below. 

1. With the SalesPerson column selected, from the **Transform** tab, we’ll select the **Split column**, **By delimiter** option to extract only the sales person’s user name.  

![Split columns dialog window, separating a columns value by the backslash character](images/image-12-1024x689.png)

2. With the active selection of the SalesPerson.1 column, from the **Home** tab, we’ll select the **Remove columns** option to remove this unnecessary column from our table. 

![Remove columns option from the ribbon](images/image-13-1024x536.png)

3. We’ll now right click the SalesPerson.2 column and select the **Rename…** option to change the column’s name from SalesPerson.2 to SalesPerson. 

![Rename function as displayed when right-clicking a column header](images/image-14.png)

4. Within the **Query settings** pane and in our **Applied steps** list, our step indicator now displays the **Not Folding** icon for our **Split column by delimiter**, **Removed columns** and **Renamed columns** steps. This has resulted in our query being partially folded, with certain steps being completed by the remote data source and other steps being streamed into Power Query’s transformation engine. 

![A not folding indicator within the Applied steps list](images/image-20.png)

This process of partial folding ensures that as a citizen data integrator, you won’t be blocked from completing your work – though there could be downstream impacts such as increased refresh durations, which is why we’ll want to revisit our steps and find a more optimal and performant method to maintain our query folding. 

5. To learn more about which steps are being handled remotely and which are being streamed into Power Query, right click the **Renamed columns** step, and then select the **View query plan** option. 

![View query plan option when right clicking a step within the Applied steps window](images/image-21.png)

6. Within the **Query plan** window, from right to left we see the various stages of building our query with the labels **Remote** and **Streaming**, including the option to **View details** to review more information.
    - **Remote** are folded nodes, which are sent back to the data source.
    
    - **Streaming** are non-folded nodes, which must be loaded into Power Query for further processing.

See [Query plan for Power Query](https://docs.microsoft.com/power-query/query-plan#identify-folded-nodes-from-other-nodes) for more details.

![Query plan dialog window, displaying Remote and Streaming operations, including the ability to View details for more information](images/image-22.png)

7. Now that we have a better idea of our costly operations, we’ll return to the **Query settings** pane’s **Applied steps** section and right click the **Split column by delimiter** step and then the **Delete until end** option to remove all our non-foldable transformations.

![Delete until end option from the Applied steps window to remove multiple steps](images/image-16.png)

8. From the **Transform** tab, select the **Replace values** option and within the **Value to find** field we’ll enter the text “adventure-works\\”.

![Replace values option from the ribbon](images/image-17-1024x536.png)

9. In the **Query settings** pane’s **Applied steps** list, our step indicator now displays the **Folding** icon for all our steps, all while still achieving the same result that we attempted above.

![Folding indicator spanning multiple steps, including the description on hover that This step will be evaluated by the data source](images/image-18-1024x256.png)

10. If we were to right click the **Replaced value** step and select the **View query plan** option, all our operations are now being handled remotely once again and when selecting the **View details** below **Value.NativeQuery** our query now includes the [REPLACE](https://docs.microsoft.com/sql/t-sql/functions/replace-transact-sql) function.

![Query plan dialog window and the Native Query that has now been generated](images/image-19.png)

As project requirements change with time, it’s important that we maintain query folding for our most intense operations and aim to only break query folding when no other options may exist. For this reason, we should aim to achieve the above query plan with remote operations and understand that project requirements may dictate where we may need to deviate from this goal.

See [Best practices when working with Power Query](https://docs.microsoft.com/power-query/best-practices#do-expensive-operations-last) for more details.

**Important note:** Query folding capabilities rely on both the capabilities of the data source and the connector in use. Foldable operations from a given data source and connector might not translate directly to a different data source and/or different connector.

## Continue your journey

Thank you for taking the time to learn more about one of my favorite topics in Query folding, as a citizen data integrator myself – the trial and error of trying different methods to build performant queries and leveraging the modern development experiences within Power Query have unlocked many scenarios I once thought impossible. It all starts with one simple rule though – “Don’t break the fold!” – which is where if you’re in the initial stages of learning, I’d encourage you to check out the [30-Day Query Folding](https://www.youtube.com/playlist?list=PLKW7XPyNDgRCorKNS1bfZoAO3YSIAVz3N) challenge and use the hashtag #30DQUERY on social networks to share your own solutions and learn from others.
