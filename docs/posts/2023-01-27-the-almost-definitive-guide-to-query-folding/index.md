---
title: "The (Almost) Definitive Guide to Query Folding"
date: 2023-01-27
categories: 
  - "power-query"
tags: 
  - "power-query"
  - "query-folding"
comments: true
---

There's only one rule. Don't break the fold! Before we start enforcing all these rules, we should start with something like a solid foundation of what does and doesn't fold in Power Query and their SQL equivalents. Now, if you found this page and we're like "what in the world is query folding?" [read this incredible article, from this amazing author.](https://powerquery.microsoft.com/en-us/blog/introduction-to-practical-query-folding/)

<!-- more -->

**The disclaimer thing:** This is a personal list compiled through testing during the [30-day query folding challenge](https://aka.ms/30dquery) either done by myself or members of the community (❤️). Every scenario is different, and every situation is unique. The functionality described in this article is subject to change and may evolve over time. Please feel free to leave comments at the end of the article or find me via the social channels to let me know of revisions.

**About the data source:** The source utilized for these scenarios was an Azure SQL Database or SQL Server. There may not be equal folding functionality within other systems, and you should always test your own solutions to determine full functionality before production use.

| Name | Supports Folding | SQL Equivalent |
| --- | --- | --- |
| [Binary.Buffer](https://docs.microsoft.com/powerquery-m/binary-buffer) | FALSE |  |
| [Binary.Compress](https://docs.microsoft.com/powerquery-m/binary-compress) | FALSE |  |
| [Binary.ApproximateLength](https://docs.microsoft.com/powerquery-m/binary-approximatelength) | FALSE |  |
| [Binary.Decompress](https://docs.microsoft.com/powerquery-m/binary-decompress) | FALSE |  |
| [Binary.ViewError](https://docs.microsoft.com/powerquery-m/binary-viewerror) | FALSE |  |
| [Binary.ToText](https://docs.microsoft.com/powerquery-m/binary-totext) | FALSE |  |
| [Binary.Type](https://docs.microsoft.com/powerquery-m/binary-type) | FALSE |  |
| [Binary.View](https://docs.microsoft.com/powerquery-m/binary-view) | FALSE |  |
| [Binary.ViewFunction](https://docs.microsoft.com/powerquery-m/binary-viewfunction) | FALSE |  |
| [Binary.Combine](https://docs.microsoft.com/powerquery-m/binary-combine) | FALSE |  |
| [Binary.ToList](https://docs.microsoft.com/powerquery-m/binary-tolist) | FALSE |  |
| [Binary.Range](https://docs.microsoft.com/powerquery-m/binary-range) | FALSE |  |
| [Binary.FromList](https://docs.microsoft.com/powerquery-m/binary-fromlist) | FALSE |  |
| [Binary.Length](https://docs.microsoft.com/powerquery-m/binary-length) | FALSE |  |
| [Binary.InferContentType](https://docs.microsoft.com/powerquery-m/binary-infercontenttype) | FALSE |  |
| [Binary.From](https://docs.microsoft.com/powerquery-m/binary-from) | FALSE |  |
| [Binary.FromText](https://docs.microsoft.com/powerquery-m/binary-fromtext) | FALSE |  |
| [Byte.Type](https://docs.microsoft.com/powerquery-m/byte-type) | FALSE |  |
| [Byte.From](https://docs.microsoft.com/powerquery-m/byte-from) | FALSE |  |
| [Character.FromNumber](https://docs.microsoft.com/powerquery-m/character-fromnumber) | FALSE | [CHAR](https://learn.microsoft.com/sql/t-sql/functions/char-transact-sql) |
| [Character.ToNumber](https://docs.microsoft.com/powerquery-m/character-tonumber) | FALSE |  |
| [Currency.Type](https://docs.microsoft.com/powerquery-m/currency-type) | FALSE |  |
| [Currency.From](https://docs.microsoft.com/powerquery-m/currency-from) | FALSE |  |
| [Date.IsLeapYear](https://docs.microsoft.com/powerquery-m/date-isleapyear) | FALSE |  |
| [Date.From](https://docs.microsoft.com/powerquery-m/date-from) | FALSE |  |
| [Date.StartOfDay](https://docs.microsoft.com/powerquery-m/date-startofday) | FALSE |  |
| [Date.MonthName](https://docs.microsoft.com/powerquery-m/date-monthname) | FALSE |  |
| [Date.EndOfYear](https://docs.microsoft.com/powerquery-m/date-endofyear) | FALSE |  |
| [Date.EndOfDay](https://docs.microsoft.com/powerquery-m/date-endofday) | FALSE |  |
| [Date.DaysInMonth](https://docs.microsoft.com/powerquery-m/date-daysinmonth) | FALSE |  |
| [Date.EndOfWeek](https://docs.microsoft.com/powerquery-m/date-endofweek) | FALSE |  |
| [Date.EndOfQuarter](https://docs.microsoft.com/powerquery-m/date-endofquarter) | FALSE |  |
| [Date.WeekOfMonth](https://docs.microsoft.com/powerquery-m/date-weekofmonth) | FALSE |  |
| [Date.ToText](https://docs.microsoft.com/powerquery-m/date-totext) | FALSE |  |
| [Date.Type](https://docs.microsoft.com/powerquery-m/date-type) | FALSE |  |
| [Date.FromText](https://docs.microsoft.com/powerquery-m/date-fromtext) | FALSE |  |
| [Date.ToRecord](https://docs.microsoft.com/powerquery-m/date-torecord) | FALSE |  |
| [Date.StartOfQuarter](https://docs.microsoft.com/powerquery-m/date-startofquarter) | FALSE |  |
| [Date.StartOfMonth](https://docs.microsoft.com/powerquery-m/date-startofmonth) | FALSE |  |
| [Date.StartOfYear](https://docs.microsoft.com/powerquery-m/date-startofyear) | FALSE |  |
| [Date.StartOfWeek](https://docs.microsoft.com/powerquery-m/date-startofweek) | FALSE |  |
| [Date.DayOfWeekName](https://docs.microsoft.com/powerquery-m/date-dayofweekname) | FALSE | [DATENAME](https://learn.microsoft.com/sql/t-sql/functions/datename-transact-sql) |
| [Date.IsInCurrentDay](https://docs.microsoft.com/powerquery-m/date-isincurrentday) | TRUE |  |
| [Date.IsInCurrentMonth](https://docs.microsoft.com/powerquery-m/date-isincurrentmonth) | TRUE |  |
| [Date.EndOfMonth](https://docs.microsoft.com/powerquery-m/date-endofmonth) | TRUE | [EOMONTH](https://learn.microsoft.com/sql/t-sql/functions/eomonth-transact-sql) |
| [Date.WeekOfYear](https://docs.microsoft.com/powerquery-m/date-weekofyear) | TRUE | [DATEPART](https://learn.microsoft.com/sql/t-sql/functions/datepart-transact-sql) |
| [Date.Year](https://docs.microsoft.com/powerquery-m/date-year) | TRUE | [DATEPART](https://learn.microsoft.com/sql/t-sql/functions/datepart-transact-sql) |
| [Date.IsInNextDay](https://docs.microsoft.com/powerquery-m/date-isinnextday) | TRUE |  |
| [Date.IsInNextMonth](https://docs.microsoft.com/powerquery-m/date-isinnextmonth) | TRUE |  |
| [Date.IsInCurrentYear](https://docs.microsoft.com/powerquery-m/date-isincurrentyear) | TRUE |  |
| [Date.IsInCurrentQuarter](https://docs.microsoft.com/powerquery-m/date-isincurrentquarter) | TRUE |  |
| [Date.IsInCurrentWeek](https://docs.microsoft.com/powerquery-m/date-isincurrentweek) | TRUE |  |
| [Date.AddWeeks](https://docs.microsoft.com/powerquery-m/date-addweeks) | TRUE | [DATEADD](https://learn.microsoft.com/sql/t-sql/functions/dateadd-transact-sql) |
| [Date.AddYears](https://docs.microsoft.com/powerquery-m/date-addyears) | TRUE | [DATEADD](https://learn.microsoft.com/sql/t-sql/functions/dateadd-transact-sql) |
| [Date.AddQuarters](https://docs.microsoft.com/powerquery-m/date-addquarters) | TRUE | [DATEADD](https://learn.microsoft.com/sql/t-sql/functions/dateadd-transact-sql) |
| [Date.AddDays](https://docs.microsoft.com/powerquery-m/date-adddays) | TRUE | [DATEADD](https://learn.microsoft.com/sql/t-sql/functions/dateadd-transact-sql) |
| [Date.AddMonths](https://docs.microsoft.com/powerquery-m/date-addmonths) | TRUE | [DATEADD](https://learn.microsoft.com/sql/t-sql/functions/dateadd-transact-sql) |
| [Date.Month](https://docs.microsoft.com/powerquery-m/date-month) | TRUE | [DATEPART](https://learn.microsoft.com/sql/t-sql/functions/datepart-transact-sql) |
| [Date.QuarterOfYear](https://docs.microsoft.com/powerquery-m/date-quarterofyear) | TRUE | [DATEPART](https://learn.microsoft.com/sql/t-sql/functions/datepart-transact-sql) |
| [Date.DayOfYear](https://docs.microsoft.com/powerquery-m/date-dayofyear) | TRUE | [DATEPART](https://learn.microsoft.com/sql/t-sql/functions/datepart-transact-sql) |
| [Date.Day](https://docs.microsoft.com/powerquery-m/date-day) | TRUE | [DATEPART](https://learn.microsoft.com/sql/t-sql/functions/datepart-transact-sql) |
| [Date.DayOfWeek](https://docs.microsoft.com/powerquery-m/date-dayofweek) | TRUE | [DATEPART](https://learn.microsoft.com/sql/t-sql/functions/datepart-transact-sql) |
| [Date.IsInPreviousNQuarters](https://docs.microsoft.com/powerquery-m/date-isinpreviousnquarters) | TRUE |  |
| [Date.IsInPreviousNWeeks](https://docs.microsoft.com/powerquery-m/date-isinpreviousnweeks) | TRUE |  |
| [Date.IsInPreviousNMonths](https://docs.microsoft.com/powerquery-m/date-isinpreviousnmonths) | TRUE |  |
| [Date.IsInPreviousMonth](https://docs.microsoft.com/powerquery-m/date-isinpreviousmonth) | TRUE |  |
| [Date.IsInPreviousNDays](https://docs.microsoft.com/powerquery-m/date-isinpreviousndays) | TRUE |  |
| [Date.IsInPreviousYear](https://docs.microsoft.com/powerquery-m/date-isinpreviousyear) | TRUE |  |
| [Date.IsInYearToDate](https://docs.microsoft.com/powerquery-m/date-isinyeartodate) | TRUE |  |
| [Date.IsInPreviousWeek](https://docs.microsoft.com/powerquery-m/date-isinpreviousweek) | TRUE |  |
| [Date.IsInPreviousNYears](https://docs.microsoft.com/powerquery-m/date-isinpreviousnyears) | TRUE |  |
| [Date.IsInPreviousQuarter](https://docs.microsoft.com/powerquery-m/date-isinpreviousquarter) | TRUE |  |
| [Date.IsInNextNQuarters](https://docs.microsoft.com/powerquery-m/date-isinnextnquarters) | TRUE |  |
| [Date.IsInNextNWeeks](https://docs.microsoft.com/powerquery-m/date-isinnextnweeks) | TRUE |  |
| [Date.IsInNextNDays](https://docs.microsoft.com/powerquery-m/date-isinnextndays) | TRUE |  |
| [Date.IsInNextNMonths](https://docs.microsoft.com/powerquery-m/date-isinnextnmonths) | TRUE |  |
| [Date.IsInNextNYears](https://docs.microsoft.com/powerquery-m/date-isinnextnyears) | TRUE |  |
| [Date.IsInPreviousDay](https://docs.microsoft.com/powerquery-m/date-isinpreviousday) | TRUE |  |
| [Date.IsInNextYear](https://docs.microsoft.com/powerquery-m/date-isinnextyear) | TRUE |  |
| [Date.IsInNextQuarter](https://docs.microsoft.com/powerquery-m/date-isinnextquarter) | TRUE |  |
| [Date.IsInNextWeek](https://docs.microsoft.com/powerquery-m/date-isinnextweek) | TRUE |  |
| [DateTime.FromText](https://docs.microsoft.com/powerquery-m/datetime-fromtext) | FALSE |  |
| [DateTime.Type](https://docs.microsoft.com/powerquery-m/datetime-type) | FALSE |  |
| [DateTime.IsInPreviousNSeconds](https://docs.microsoft.com/powerquery-m/datetime-isinpreviousnseconds) | TRUE |  |
| [DateTime.IsInPreviousSecond](https://docs.microsoft.com/powerquery-m/datetime-isinprevioussecond) | TRUE |  |
| [DateTime.IsInPreviousNMinutes](https://docs.microsoft.com/powerquery-m/datetime-isinpreviousnminutes) | TRUE |  |
| [DateTime.IsInPreviousMinute](https://docs.microsoft.com/powerquery-m/datetime-isinpreviousminute) | TRUE |  |
| [DateTime.IsInPreviousNHours](https://docs.microsoft.com/powerquery-m/datetime-isinpreviousnhours) | TRUE |  |
| [DateTime.LocalNow](https://docs.microsoft.com/powerquery-m/datetime-localnow) | TRUE |  |
| [DateTime.Time](https://docs.microsoft.com/powerquery-m/datetime-time) | FALSE |  |
| [DateTime.ToRecord](https://docs.microsoft.com/powerquery-m/datetime-torecord) | FALSE |  |
| [DateTime.FixedLocalNow](https://docs.microsoft.com/powerquery-m/datetime-fixedlocalnow) | FALSE |  |
| [DateTime.AddZone](https://docs.microsoft.com/powerquery-m/datetime-addzone) | FALSE |  |
| [DateTime.Date](https://docs.microsoft.com/powerquery-m/datetime-date) | FALSE |  |
| [DateTime.IsInPreviousHour](https://docs.microsoft.com/powerquery-m/datetime-isinprevioushour) | TRUE |  |
| [DateTime.IsInCurrentMinute](https://docs.microsoft.com/powerquery-m/datetime-isincurrentminute) | TRUE |  |
| [DateTime.IsInCurrentSecond](https://docs.microsoft.com/powerquery-m/datetime-isincurrentsecond) | TRUE |  |
| [DateTime.IsInCurrentHour](https://docs.microsoft.com/powerquery-m/datetime-isincurrenthour) | TRUE |  |
| [DateTime.From](https://docs.microsoft.com/powerquery-m/datetime-from) | TRUE | [CONVERT](https://learn.microsoft.com/sql/t-sql/functions/convert-transact-sql) |
| [DateTime.FromFileTime](https://docs.microsoft.com/powerquery-m/datetime-fromfiletime) | TRUE |  |
| [DateTime.IsInNextHour](https://docs.microsoft.com/powerquery-m/datetime-isinnexthour) | TRUE |  |
| [DateTime.IsInNextNSeconds](https://docs.microsoft.com/powerquery-m/datetime-isinnextnseconds) | TRUE |  |
| [DateTime.IsInNextSecond](https://docs.microsoft.com/powerquery-m/datetime-isinnextsecond) | TRUE |  |
| [DateTime.IsInNextNMinutes](https://docs.microsoft.com/powerquery-m/datetime-isinnextnminutes) | TRUE |  |
| [DateTime.IsInNextMinute](https://docs.microsoft.com/powerquery-m/datetime-isinnextminute) | TRUE |  |
| [DateTime.IsInNextNHours](https://docs.microsoft.com/powerquery-m/datetime-isinnextnhours) | TRUE |  |
| [DateTime.ToText](https://docs.microsoft.com/powerquery-m/datetime-totext) | FALSE |  |
| [DateTimeZone.ToUtc](https://docs.microsoft.com/powerquery-m/datetimezone-toutc) | FALSE |  |
| [DateTimeZone.ToText](https://docs.microsoft.com/powerquery-m/datetimezone-totext) | FALSE |  |
| [DateTimeZone.ZoneHours](https://docs.microsoft.com/powerquery-m/datetimezone-zonehours) | FALSE |  |
| [DateTimeZone.ToRecord](https://docs.microsoft.com/powerquery-m/datetimezone-torecord) | FALSE |  |
| [DateTimeZone.ZoneMinutes](https://docs.microsoft.com/powerquery-m/datetimezone-zoneminutes) | FALSE |  |
| [DateTimeZone.RemoveZone](https://docs.microsoft.com/powerquery-m/datetimezone-removezone) | FALSE |  |
| [DateTimeZone.FromText](https://docs.microsoft.com/powerquery-m/datetimezone-fromtext) | FALSE |  |
| [DateTimeZone.SwitchZone](https://docs.microsoft.com/powerquery-m/datetimezone-switchzone) | FALSE |  |
| [DateTimeZone.From](https://docs.microsoft.com/powerquery-m/datetimezone-from) | FALSE |  |
| [DateTimeZone.ToLocal](https://docs.microsoft.com/powerquery-m/datetimezone-tolocal) | FALSE |  |
| [DateTimeZone.FixedUtcNow](https://docs.microsoft.com/powerquery-m/datetimezone-fixedutcnow) | TRUE |  |
| [DateTimeZone.FromFileTime](https://docs.microsoft.com/powerquery-m/datetimezone-fromfiletime) | TRUE |  |
| [DateTimeZone.Type](https://docs.microsoft.com/powerquery-m/datetimezone-type) | FALSE |  |
| [DateTimeZone.FixedLocalNow](https://docs.microsoft.com/powerquery-m/datetimezone-fixedlocalnow) | TRUE |  |
| [DateTimeZone.UtcNow](https://docs.microsoft.com/powerquery-m/datetimezone-utcnow) | TRUE |  |
| [DateTimeZone.LocalNow](https://docs.microsoft.com/powerquery-m/datetimezone-localnow) | TRUE |  |
| [Decimal.Type](https://docs.microsoft.com/powerquery-m/decimal-type) | FALSE |  |
| [Decimal.From](https://docs.microsoft.com/powerquery-m/decimal-from) | TRUE |  |
| [Double.Type](https://docs.microsoft.com/powerquery-m/double-type) | FALSE |  |
| [Double.From](https://docs.microsoft.com/powerquery-m/double-from) | TRUE | [CONVERT](https://learn.microsoft.com/sql/t-sql/functions/convert-transact-sql) |
| [Duration.Minutes](https://docs.microsoft.com/powerquery-m/duration-minutes) | FALSE |  |
| [Duration.Type](https://docs.microsoft.com/powerquery-m/duration-type) | FALSE |  |
| [Duration.TotalMinutes](https://docs.microsoft.com/powerquery-m/duration-totalminutes) | FALSE |  |
| [Duration.TotalSeconds](https://docs.microsoft.com/powerquery-m/duration-totalseconds) | FALSE |  |
| [Duration.TotalHours](https://docs.microsoft.com/powerquery-m/duration-totalhours) | FALSE |  |
| [Duration.Seconds](https://docs.microsoft.com/powerquery-m/duration-seconds) | FALSE |  |
| [Duration.ToRecord](https://docs.microsoft.com/powerquery-m/duration-torecord) | FALSE |  |
| [Duration.ToText](https://docs.microsoft.com/powerquery-m/duration-totext) | FALSE |  |
| [Duration.Days](https://docs.microsoft.com/powerquery-m/duration-days) | FALSE |  |
| [Duration.TotalDays](https://docs.microsoft.com/powerquery-m/duration-totaldays) | TRUE | [DATEDIFF](https://learn.microsoft.com/sql/t-sql/functions/datediff-transact-sql) |
| [Duration.From](https://docs.microsoft.com/powerquery-m/duration-from) | FALSE |  |
| [Duration.Hours](https://docs.microsoft.com/powerquery-m/duration-hours) | FALSE |  |
| [Duration.FromText](https://docs.microsoft.com/powerquery-m/duration-fromtext) | FALSE |  |
| [Guid.From](https://docs.microsoft.com/powerquery-m/guid-from) | FALSE |  |
| [Guid.Type](https://docs.microsoft.com/powerquery-m/guid-type) | FALSE |  |
| [Int16.From](https://docs.microsoft.com/powerquery-m/int16-from) | FALSE |  |
| [Int16.Type](https://docs.microsoft.com/powerquery-m/int16-type) | FALSE |  |
| [Int32.Type](https://docs.microsoft.com/powerquery-m/int32-type) | FALSE |  |
| [Int32.From](https://docs.microsoft.com/powerquery-m/int32-from) | FALSE |  |
| [Int64.Type](https://docs.microsoft.com/powerquery-m/int64-type) | FALSE |  |
| [Int64.From](https://docs.microsoft.com/powerquery-m/int64-from) | FALSE |  |
| [Int8.From](https://docs.microsoft.com/powerquery-m/int8-from) | FALSE |  |
| [Int8.Type](https://docs.microsoft.com/powerquery-m/int8-type) | FALSE |  |
| [Json.FromValue](https://docs.microsoft.com/powerquery-m/json-fromvalue) | FALSE |  |
| [Json.Document](https://docs.microsoft.com/powerquery-m/json-document) | FALSE |  |
| [List.SingleOrDefault](https://docs.microsoft.com/powerquery-m/list-singleordefault) | FALSE |  |
| [List.Skip](https://docs.microsoft.com/powerquery-m/list-skip) | FALSE |  |
| [List.Split](https://docs.microsoft.com/powerquery-m/list-split) | FALSE |  |
| [List.Single](https://docs.microsoft.com/powerquery-m/list-single) | FALSE |  |
| [List.ReplaceRange](https://docs.microsoft.com/powerquery-m/list-replacerange) | FALSE |  |
| [List.ReplaceValue](https://docs.microsoft.com/powerquery-m/list-replacevalue) | FALSE |  |
| [List.Reverse](https://docs.microsoft.com/powerquery-m/list-reverse) | FALSE |  |
| [List.StandardDeviation](https://docs.microsoft.com/powerquery-m/list-standarddeviation) | FALSE |  |
| [List.Type](https://docs.microsoft.com/powerquery-m/list-type) | FALSE |  |
| [List.Union](https://docs.microsoft.com/powerquery-m/list-union) | FALSE |  |
| [List.Zip](https://docs.microsoft.com/powerquery-m/list-zip) | FALSE |  |
| [List.TransformMany](https://docs.microsoft.com/powerquery-m/list-transformmany) | FALSE |  |
| [List.Sum](https://docs.microsoft.com/powerquery-m/list-sum) | FALSE |  |
| [List.Times](https://docs.microsoft.com/powerquery-m/list-times) | FALSE |  |
| [List.Transform](https://docs.microsoft.com/powerquery-m/list-transform) | FALSE |  |
| [List.ReplaceMatchingItems](https://docs.microsoft.com/powerquery-m/list-replacematchingitems) | FALSE |  |
| [List.Distinct](https://docs.microsoft.com/powerquery-m/list-distinct) | FALSE |  |
| [List.Durations](https://docs.microsoft.com/powerquery-m/list-durations) | FALSE |  |
| [List.FindText](https://docs.microsoft.com/powerquery-m/list-findtext) | FALSE |  |
| [List.Difference](https://docs.microsoft.com/powerquery-m/list-difference) | FALSE |  |
| [List.Dates](https://docs.microsoft.com/powerquery-m/list-dates) | FALSE |  |
| [List.DateTimes](https://docs.microsoft.com/powerquery-m/list-datetimes) | FALSE |  |
| [List.DateTimeZones](https://docs.microsoft.com/powerquery-m/list-datetimezones) | FALSE |  |
| [List.Intersect](https://docs.microsoft.com/powerquery-m/list-intersect) | FALSE |  |
| [List.IsDistinct](https://docs.microsoft.com/powerquery-m/list-isdistinct) | FALSE |  |
| [List.IsEmpty](https://docs.microsoft.com/powerquery-m/list-isempty) | FALSE |  |
| [List.InsertRange](https://docs.microsoft.com/powerquery-m/list-insertrange) | FALSE |  |
| [List.First](https://docs.microsoft.com/powerquery-m/list-first) | FALSE |  |
| [List.FirstN](https://docs.microsoft.com/powerquery-m/list-firstn) | FALSE |  |
| [List.Generate](https://docs.microsoft.com/powerquery-m/list-generate) | FALSE |  |
| [List.Covariance](https://docs.microsoft.com/powerquery-m/list-covariance) | FALSE |  |
| [List.Sort](https://docs.microsoft.com/powerquery-m/list-sort) | TRUE |  |
| [List.Accumulate](https://docs.microsoft.com/powerquery-m/list-accumulate) | FALSE |  |
| [List.AllTrue](https://docs.microsoft.com/powerquery-m/list-alltrue) | FALSE |  |
| [List.Select](https://docs.microsoft.com/powerquery-m/list-select) | TRUE |  |
| [List.Contains](https://docs.microsoft.com/powerquery-m/list-contains) | TRUE | [IN](https://learn.microsoft.com/sql/t-sql/functions/in-transact-sql) |
| [List.Combine](https://docs.microsoft.com/powerquery-m/list-combine) | TRUE |  |
| [List.RemoveItems](https://docs.microsoft.com/powerquery-m/list-removeitems) | TRUE |  |
| [List.ContainsAll](https://docs.microsoft.com/powerquery-m/list-containsall) | FALSE |  |
| [List.ContainsAny](https://docs.microsoft.com/powerquery-m/list-containsany) | FALSE |  |
| [List.Count](https://docs.microsoft.com/powerquery-m/list-count) | FALSE |  |
| [List.Buffer](https://docs.microsoft.com/powerquery-m/list-buffer) | FALSE |  |
| [List.Alternate](https://docs.microsoft.com/powerquery-m/list-alternate) | FALSE |  |
| [List.AnyTrue](https://docs.microsoft.com/powerquery-m/list-anytrue) | FALSE |  |
| [List.Average](https://docs.microsoft.com/powerquery-m/list-average) | FALSE |  |
| [List.Last](https://docs.microsoft.com/powerquery-m/list-last) | FALSE |  |
| [List.Positions](https://docs.microsoft.com/powerquery-m/list-positions) | FALSE |  |
| [List.Product](https://docs.microsoft.com/powerquery-m/list-product) | FALSE |  |
| [List.Random](https://docs.microsoft.com/powerquery-m/list-random) | FALSE |  |
| [List.PositionOfAny](https://docs.microsoft.com/powerquery-m/list-positionofany) | FALSE |  |
| [List.NonNullCount](https://docs.microsoft.com/powerquery-m/list-nonnullcount) | FALSE |  |
| [List.Numbers](https://docs.microsoft.com/powerquery-m/list-numbers) | FALSE |  |
| [List.PositionOf](https://docs.microsoft.com/powerquery-m/list-positionof) | FALSE |  |
| [List.RemoveNulls](https://docs.microsoft.com/powerquery-m/list-removenulls) | FALSE |  |
| [List.RemoveRange](https://docs.microsoft.com/powerquery-m/list-removerange) | FALSE |  |
| [List.Repeat](https://docs.microsoft.com/powerquery-m/list-repeat) | FALSE |  |
| [List.RemoveMatchingItems](https://docs.microsoft.com/powerquery-m/list-removematchingitems) | FALSE |  |
| [List.Range](https://docs.microsoft.com/powerquery-m/list-range) | FALSE |  |
| [List.RemoveFirstN](https://docs.microsoft.com/powerquery-m/list-removefirstn) | FALSE |  |
| [List.RemoveLastN](https://docs.microsoft.com/powerquery-m/list-removelastn) | FALSE |  |
| [List.Modes](https://docs.microsoft.com/powerquery-m/list-modes) | FALSE |  |
| [List.MinN](https://docs.microsoft.com/powerquery-m/list-minn) | FALSE |  |
| [List.Mode](https://docs.microsoft.com/powerquery-m/list-mode) | FALSE |  |
| [List.MaxN](https://docs.microsoft.com/powerquery-m/list-maxn) | FALSE |  |
| [List.Min](https://docs.microsoft.com/powerquery-m/list-min) | FALSE |  |
| [List.Max](https://docs.microsoft.com/powerquery-m/list-max) | FALSE |  |
| [List.LastN](https://docs.microsoft.com/powerquery-m/list-lastn) | FALSE |  |
| [List.Median](https://docs.microsoft.com/powerquery-m/list-median) | FALSE |  |
| [List.MatchesAny](https://docs.microsoft.com/powerquery-m/list-matchesany) | FALSE |  |
| [List.MatchesAll](https://docs.microsoft.com/powerquery-m/list-matchesall) | FALSE |  |
| [Logical.ToText](https://docs.microsoft.com/powerquery-m/logical-totext) | FALSE |  |
| [Logical.FromText](https://docs.microsoft.com/powerquery-m/logical-fromtext) | FALSE |  |
| [Logical.Type](https://docs.microsoft.com/powerquery-m/logical-type) | FALSE |  |
| [Logical.From](https://docs.microsoft.com/powerquery-m/logical-from) | FALSE |  |
| [Null.Type](https://docs.microsoft.com/powerquery-m/null-type) | FALSE |  |
| [Number.Sinh](https://docs.microsoft.com/powerquery-m/number-sinh) | FALSE |  |
| [Number.Sin](https://docs.microsoft.com/powerquery-m/number-sin) | FALSE |  |
| [Number.Type](https://docs.microsoft.com/powerquery-m/number-type) | FALSE |  |
| [Number.Tanh](https://docs.microsoft.com/powerquery-m/number-tanh) | FALSE |  |
| [Number.Exp](https://docs.microsoft.com/powerquery-m/number-exp) | TRUE | [EXP](https://learn.microsoft.com/sql/t-sql/functions/exp-transact-sql) |
| [Number.RoundDown](https://docs.microsoft.com/powerquery-m/number-rounddown) | TRUE | [FLOOR](https://learn.microsoft.com/sql/t-sql/functions/floor-transact-sql) |
| [Number.Cos](https://docs.microsoft.com/powerquery-m/number-cos) | TRUE | [COS](https://learn.microsoft.com/sql/t-sql/functions/cos-transact-sql) |
| [Number.From](https://docs.microsoft.com/powerquery-m/number-from) | TRUE | [CONVERT](https://learn.microsoft.com/sql/t-sql/functions/convert-transact-sql) |
| [Number.ToText](https://docs.microsoft.com/powerquery-m/number-totext) | TRUE | [CONVERT](https://learn.microsoft.com/sql/t-sql/functions/convert-transact-sql) |
| [Number.Power](https://docs.microsoft.com/powerquery-m/number-power) | TRUE | [POWER](https://learn.microsoft.com/sql/t-sql/functions/power-transact-sql) |
| [Number.Round](https://docs.microsoft.com/powerquery-m/number-round) | TRUE | [ROUND](https://learn.microsoft.com/sql/t-sql/functions/round-transact-sql) |
| [Number.Mod](https://docs.microsoft.com/powerquery-m/number-mod) | TRUE | [MOD](https://learn.microsoft.com/sql/t-sql/functions/mod-transact-sql) |
| [Number.Log](https://docs.microsoft.com/powerquery-m/number-log) | TRUE | [LOG](https://learn.microsoft.com/sql/t-sql/functions/log-transact-sql) |
| [Number.Log10](https://docs.microsoft.com/powerquery-m/number-log10) | TRUE | [LOG10](https://learn.microsoft.com/sql/t-sql/functions/log10-transact-sql) |
| [Number.Epsilon](https://docs.microsoft.com/powerquery-m/number-epsilon) | TRUE | [4.940656458412465E-324](https://learn.microsoft.com/sql/t-sql/functions/4.940656458412465e-324-transact-sql) |
| [Number.Abs](https://docs.microsoft.com/powerquery-m/number-abs) | TRUE | [ABS](https://learn.microsoft.com/sql/t-sql/functions/abs-transact-sql) |
| [Number.Pi](https://docs.microsoft.com/powerquery-m/number-pi) | TRUE |  |
| [Number.PositiveInfinity](https://docs.microsoft.com/powerquery-m/number-positiveinfinity) | FALSE |  |
| [Number.E](https://docs.microsoft.com/powerquery-m/number-e) | TRUE |  |
| [Number.Atan2](https://docs.microsoft.com/powerquery-m/number-atan2) | TRUE | [ATN2](https://learn.microsoft.com/sql/t-sql/functions/atn2-transact-sql) |
| [Number.RoundUp](https://docs.microsoft.com/powerquery-m/number-roundup) | TRUE | [CEILING](https://learn.microsoft.com/sql/t-sql/functions/ceiling-transact-sql) |
| [Number.Atan](https://docs.microsoft.com/powerquery-m/number-atan) | TRUE | [ATAN](https://learn.microsoft.com/sql/t-sql/functions/atan-transact-sql) |
| [Number.Acos](https://docs.microsoft.com/powerquery-m/number-acos) | TRUE | [ACOS](https://learn.microsoft.com/sql/t-sql/functions/acos-transact-sql) |
| [Number.Asin](https://docs.microsoft.com/powerquery-m/number-asin) | TRUE | [ASIN](https://learn.microsoft.com/sql/t-sql/functions/asin-transact-sql) |
| [Number.Sqrt](https://docs.microsoft.com/powerquery-m/number-sqrt) | TRUE | [SQRT](https://learn.microsoft.com/sql/t-sql/functions/sqrt-transact-sql) |
| [Number.IsEven](https://docs.microsoft.com/powerquery-m/number-iseven) | FALSE |  |
| [Number.IsNaN](https://docs.microsoft.com/powerquery-m/number-isnan) | FALSE |  |
| [Number.IntegerDivide](https://docs.microsoft.com/powerquery-m/number-integerdivide) | FALSE |  |
| [Number.Factorial](https://docs.microsoft.com/powerquery-m/number-factorial) | FALSE |  |
| [Number.FromText](https://docs.microsoft.com/powerquery-m/number-fromtext) | FALSE |  |
| [Number.NegativeInfinity](https://docs.microsoft.com/powerquery-m/number-negativeinfinity) | FALSE |  |
| [Number.Permutations](https://docs.microsoft.com/powerquery-m/number-permutations) | FALSE |  |
| [Number.NaN](https://docs.microsoft.com/powerquery-m/number-nan) | FALSE |  |
| [Number.IsOdd](https://docs.microsoft.com/powerquery-m/number-isodd) | FALSE |  |
| [Number.Ln](https://docs.microsoft.com/powerquery-m/number-ln) | FALSE |  |
| [Number.BitwiseNot](https://docs.microsoft.com/powerquery-m/number-bitwisenot) | FALSE |  |
| [Number.BitwiseOr](https://docs.microsoft.com/powerquery-m/number-bitwiseor) | FALSE |  |
| [Number.BitwiseAnd](https://docs.microsoft.com/powerquery-m/number-bitwiseand) | FALSE |  |
| [Number.Tan](https://docs.microsoft.com/powerquery-m/number-tan) | TRUE | [TAN](https://learn.microsoft.com/sql/t-sql/functions/tan-transact-sql) |
| [Number.Random](https://docs.microsoft.com/powerquery-m/number-random) | TRUE |  |
| [Number.Combinations](https://docs.microsoft.com/powerquery-m/number-combinations) | FALSE |  |
| [Number.Cosh](https://docs.microsoft.com/powerquery-m/number-cosh) | FALSE |  |
| [Number.BitwiseXor](https://docs.microsoft.com/powerquery-m/number-bitwisexor) | FALSE |  |
| [Number.BitwiseShiftLeft](https://docs.microsoft.com/powerquery-m/number-bitwiseshiftleft) | FALSE |  |
| [Number.BitwiseShiftRight](https://docs.microsoft.com/powerquery-m/number-bitwiseshiftright) | FALSE |  |
| [Number.RoundTowardZero](https://docs.microsoft.com/powerquery-m/number-roundtowardzero) | FALSE |  |
| [Number.RandomBetween](https://docs.microsoft.com/powerquery-m/number-randombetween) | FALSE |  |
| [Number.RoundAwayFromZero](https://docs.microsoft.com/powerquery-m/number-roundawayfromzero) | FALSE |  |
| [Number.Sign](https://docs.microsoft.com/powerquery-m/number-sign) | FALSE |  |
| [Percentage.Type](https://docs.microsoft.com/powerquery-m/percentage-type) | FALSE |  |
| [Percentage.From](https://docs.microsoft.com/powerquery-m/percentage-from) | FALSE |  |
| [Single.Type](https://docs.microsoft.com/powerquery-m/single-type) | FALSE |  |
| [Single.From](https://docs.microsoft.com/powerquery-m/single-from) | FALSE |  |
| [Table.Column](https://docs.microsoft.com/powerquery-m/table-column) | FALSE |  |
| [Table.Buffer](https://docs.microsoft.com/powerquery-m/table-buffer) | FALSE |  |
| [Table.Transpose](https://docs.microsoft.com/powerquery-m/table-transpose) | TRUE |  |
| [Table.UnpivotOtherColumns](https://docs.microsoft.com/powerquery-m/table-unpivotothercolumns) | TRUE |  |
| [Table.TransformColumnNames](https://docs.microsoft.com/powerquery-m/table-transformcolumnnames) | TRUE |  |
| [Table.AddIndexColumn](https://docs.microsoft.com/powerquery-m/table-addindexcolumn) | FALSE |  |
| [Table.Unpivot](https://docs.microsoft.com/powerquery-m/table-unpivot) | TRUE |  |
| [Table.AddKey](https://docs.microsoft.com/powerquery-m/table-addkey) | FALSE |  |
| [Table.AlternateRows](https://docs.microsoft.com/powerquery-m/table-alternaterows) | FALSE |  |
| [Table.AggregateTableColumn](https://docs.microsoft.com/powerquery-m/table-aggregatetablecolumn) | FALSE |  |
| [Table.ColumnCount](https://docs.microsoft.com/powerquery-m/table-columncount) | FALSE |  |
| [Table.ReplaceMatchingRows](https://docs.microsoft.com/powerquery-m/table-replacematchingrows) | FALSE |  |
| [Table.ReplaceRelationshipIdentity](https://docs.microsoft.com/powerquery-m/table-replacerelationshipidentity) | FALSE |  |
| [Table.ReplaceKeys](https://docs.microsoft.com/powerquery-m/table-replacekeys) | FALSE |  |
| [Table.AddJoinColumn](https://docs.microsoft.com/powerquery-m/table-addjoincolumn) | FALSE |  |
| [Table.ReplaceErrorValues](https://docs.microsoft.com/powerquery-m/table-replaceerrorvalues) | FALSE |  |
| [Table.TransformRows](https://docs.microsoft.com/powerquery-m/table-transformrows) | FALSE |  |
| [Table.ViewFunction](https://docs.microsoft.com/powerquery-m/table-viewfunction) | FALSE |  |
| [Table.TransformColumnTypes](https://docs.microsoft.com/powerquery-m/table-transformcolumntypes) | FALSE |  |
| [Table.ReplaceRows](https://docs.microsoft.com/powerquery-m/table-replacerows) | FALSE |  |
| [Table.ToColumns](https://docs.microsoft.com/powerquery-m/table-tocolumns) | FALSE |  |
| [Table.ReorderColumns](https://docs.microsoft.com/powerquery-m/table-reordercolumns) | TRUE |  |
| [Table.Range](https://docs.microsoft.com/powerquery-m/table-range) | TRUE | [TOP](https://learn.microsoft.com/sql/t-sql/functions/top-transact-sql) |
| [Table.FirstN](https://docs.microsoft.com/powerquery-m/table-firstn) | TRUE | [TOP](https://learn.microsoft.com/sql/t-sql/functions/top-transact-sql) |
| [Table.SelectColumns](https://docs.microsoft.com/powerquery-m/table-selectcolumns) | TRUE | [SELECT](https://learn.microsoft.com/sql/t-sql/functions/select-transact-sql) |
| [Table.SelectRows](https://docs.microsoft.com/powerquery-m/table-selectrows) | TRUE | [WHERE](https://learn.microsoft.com/sql/t-sql/functions/where-transact-sql) |
| [Table.Repeat](https://docs.microsoft.com/powerquery-m/table-repeat) | TRUE | [UNION ALL](https://learn.microsoft.com/sql/t-sql/functions/union-all-transact-sql) |
| [Table.Combine](https://docs.microsoft.com/powerquery-m/table-combine) | TRUE | [UNION ALL](https://learn.microsoft.com/sql/t-sql/functions/union-all-transact-sql) |
| [Table.Distinct](https://docs.microsoft.com/powerquery-m/table-distinct) | TRUE | [DISTINCT](https://learn.microsoft.com/sql/t-sql/functions/distinct-transact-sql) |
| [Table.ReplaceValue](https://docs.microsoft.com/powerquery-m/table-replacevalue) | TRUE | [CASE](https://learn.microsoft.com/sql/t-sql/functions/case-transact-sql) |
| [Table.PrefixColumns](https://docs.microsoft.com/powerquery-m/table-prefixcolumns) | FALSE |  |
| [Table.Pivot](https://docs.microsoft.com/powerquery-m/table-pivot) | TRUE | [PIVOT](https://learn.microsoft.com/sql/t-sql/functions/pivot-transact-sql) |
| [Table.Sort](https://docs.microsoft.com/powerquery-m/table-sort) | TRUE | [ORDER BY](https://learn.microsoft.com/sql/t-sql/functions/order-by-transact-sql) |
| [Table.Group](https://docs.microsoft.com/powerquery-m/table-group) | TRUE | [GROUP BY](https://learn.microsoft.com/sql/t-sql/functions/group-by-transact-sql) |
| [Table.AddColumn](https://docs.microsoft.com/powerquery-m/table-addcolumn) | TRUE |  |
| [Table.NestedJoin](https://docs.microsoft.com/powerquery-m/table-nestedjoin) | TRUE |  |
| [Table.Join](https://docs.microsoft.com/powerquery-m/table-join) | TRUE |  |
| [Table.FromPartitions](https://docs.microsoft.com/powerquery-m/table-frompartitions) | TRUE |  |
| [Table.RenameColumns](https://docs.microsoft.com/powerquery-m/table-renamecolumns) | TRUE |  |
| [Table.RemoveColumns](https://docs.microsoft.com/powerquery-m/table-removecolumns) | TRUE |  |
| [Table.Partition](https://docs.microsoft.com/powerquery-m/table-partition) | TRUE |  |
| [Table.DuplicateColumn](https://docs.microsoft.com/powerquery-m/table-duplicatecolumn) | TRUE |  |
| [Table.ColumnsOfType](https://docs.microsoft.com/powerquery-m/table-columnsoftype) | TRUE |  |
| [Table.ColumnNames](https://docs.microsoft.com/powerquery-m/table-columnnames) | TRUE |  |
| [Table.ExpandTableColumn](https://docs.microsoft.com/powerquery-m/table-expandtablecolumn) | TRUE |  |
| [Table.ExpandRecordColumn](https://docs.microsoft.com/powerquery-m/table-expandrecordcolumn) | TRUE |  |
| [Table.ExpandListColumn](https://docs.microsoft.com/powerquery-m/table-expandlistcolumn) | TRUE |  |
| [Table.FuzzyNestedJoin](https://docs.microsoft.com/powerquery-m/table-fuzzynestedjoin) | FALSE |  |
| [Table.HasColumns](https://docs.microsoft.com/powerquery-m/table-hascolumns) | FALSE |  |
| [Table.InsertRows](https://docs.microsoft.com/powerquery-m/table-insertrows) | FALSE |  |
| [Table.FromValue](https://docs.microsoft.com/powerquery-m/table-fromvalue) | FALSE |  |
| [Table.FuzzyGroup](https://docs.microsoft.com/powerquery-m/table-fuzzygroup) | FALSE |  |
| [Table.FuzzyJoin](https://docs.microsoft.com/powerquery-m/table-fuzzyjoin) | FALSE |  |
| [Table.IsDistinct](https://docs.microsoft.com/powerquery-m/table-isdistinct) | FALSE |  |
| [Table.LastN](https://docs.microsoft.com/powerquery-m/table-lastn) | FALSE |  |
| [Table.MatchesAllRows](https://docs.microsoft.com/powerquery-m/table-matchesallrows) | FALSE |  |
| [Table.MatchesAnyRows](https://docs.microsoft.com/powerquery-m/table-matchesanyrows) | FALSE |  |
| [Table.IsEmpty](https://docs.microsoft.com/powerquery-m/table-isempty) | FALSE |  |
| [Table.Keys](https://docs.microsoft.com/powerquery-m/table-keys) | FALSE |  |
| [Table.Last](https://docs.microsoft.com/powerquery-m/table-last) | FALSE |  |
| [Table.FromRows](https://docs.microsoft.com/powerquery-m/table-fromrows) | FALSE |  |
| [Table.DemoteHeaders](https://docs.microsoft.com/powerquery-m/table-demoteheaders) | FALSE |  |
| [Table.FillDown](https://docs.microsoft.com/powerquery-m/table-filldown) | FALSE |  |
| [Table.FillUp](https://docs.microsoft.com/powerquery-m/table-fillup) | FALSE |  |
| [Table.Contains](https://docs.microsoft.com/powerquery-m/table-contains) | FALSE |  |
| [Table.ContainsAll](https://docs.microsoft.com/powerquery-m/table-containsall) | FALSE |  |
| [Table.ContainsAny](https://docs.microsoft.com/powerquery-m/table-containsany) | FALSE |  |
| [Table.FilterWithDataTable](https://docs.microsoft.com/powerquery-m/table-filterwithdatatable) | FALSE |  |
| [Table.FromColumns](https://docs.microsoft.com/powerquery-m/table-fromcolumns) | FALSE |  |
| [Table.FromList](https://docs.microsoft.com/powerquery-m/table-fromlist) | FALSE |  |
| [Table.FromRecords](https://docs.microsoft.com/powerquery-m/table-fromrecords) | FALSE |  |
| [Table.FindText](https://docs.microsoft.com/powerquery-m/table-findtext) | FALSE |  |
| [Table.First](https://docs.microsoft.com/powerquery-m/table-first) | FALSE |  |
| [Table.FirstValue](https://docs.microsoft.com/powerquery-m/table-firstvalue) | FALSE |  |
| [Table.Max](https://docs.microsoft.com/powerquery-m/table-max) | TRUE | [TOP](https://learn.microsoft.com/sql/t-sql/functions/top-transact-sql) |
| [Table.SelectRowsWithErrors](https://docs.microsoft.com/powerquery-m/table-selectrowswitherrors) | FALSE |  |
| [Table.SingleRow](https://docs.microsoft.com/powerquery-m/table-singlerow) | FALSE |  |
| [Table.Skip](https://docs.microsoft.com/powerquery-m/table-skip) | FALSE |  |
| [Table.ReverseRows](https://docs.microsoft.com/powerquery-m/table-reverserows) | FALSE |  |
| [Table.RowCount](https://docs.microsoft.com/powerquery-m/table-rowcount) | FALSE |  |
| [Table.Schema](https://docs.microsoft.com/powerquery-m/table-schema) | FALSE |  |
| [Table.Split](https://docs.microsoft.com/powerquery-m/table-split) | FALSE |  |
| [Table.ToRows](https://docs.microsoft.com/powerquery-m/table-torows) | FALSE |  |
| [Table.TransformColumns](https://docs.microsoft.com/powerquery-m/table-transformcolumns) | FALSE |  |
| [Table.View](https://docs.microsoft.com/powerquery-m/table-view) | FALSE |  |
| [Table.SplitColumn](https://docs.microsoft.com/powerquery-m/table-splitcolumn) | FALSE |  |
| [Table.ToList](https://docs.microsoft.com/powerquery-m/table-tolist) | FALSE |  |
| [Table.ToRecords](https://docs.microsoft.com/powerquery-m/table-torecords) | FALSE |  |
| [Table.RemoveRowsWithErrors](https://docs.microsoft.com/powerquery-m/table-removerowswitherrors) | FALSE |  |
| [Table.PartitionValues](https://docs.microsoft.com/powerquery-m/table-partitionvalues) | FALSE |  |
| [Table.PositionOf](https://docs.microsoft.com/powerquery-m/table-positionof) | FALSE |  |
| [Table.PositionOfAny](https://docs.microsoft.com/powerquery-m/table-positionofany) | FALSE |  |
| [Table.MaxN](https://docs.microsoft.com/powerquery-m/table-maxn) | TRUE | [TOP](https://learn.microsoft.com/sql/t-sql/functions/top-transact-sql) |
| [Table.Min](https://docs.microsoft.com/powerquery-m/table-min) | TRUE | [TOP](https://learn.microsoft.com/sql/t-sql/functions/top-transact-sql) |
| [Table.MinN](https://docs.microsoft.com/powerquery-m/table-minn) | TRUE | [TOP](https://learn.microsoft.com/sql/t-sql/functions/top-transact-sql) |
| [Table.CombineColumns](https://docs.microsoft.com/powerquery-m/table-combinecolumns) | FALSE |  |
| [Table.RemoveLastN](https://docs.microsoft.com/powerquery-m/table-removelastn) | FALSE |  |
| [Table.RemoveMatchingRows](https://docs.microsoft.com/powerquery-m/table-removematchingrows) | FALSE |  |
| [Table.RemoveRows](https://docs.microsoft.com/powerquery-m/table-removerows) | FALSE |  |
| [Table.Profile](https://docs.microsoft.com/powerquery-m/table-profile) | FALSE |  |
| [Table.PromoteHeaders](https://docs.microsoft.com/powerquery-m/table-promoteheaders) | FALSE |  |
| [Table.RemoveFirstN](https://docs.microsoft.com/powerquery-m/table-removefirstn) | FALSE |  |
| [Text.ToBinary](https://docs.microsoft.com/powerquery-m/text-tobinary) | FALSE |  |
| [Text.ToList](https://docs.microsoft.com/powerquery-m/text-tolist) | FALSE |  |
| [Text.SplitAny](https://docs.microsoft.com/powerquery-m/text-splitany) | FALSE |  |
| [Text.Select](https://docs.microsoft.com/powerquery-m/text-select) | FALSE |  |
| [Text.Split](https://docs.microsoft.com/powerquery-m/text-split) | FALSE |  |
| [Text.AfterDelimiter](https://docs.microsoft.com/powerquery-m/text-afterdelimiter) | FALSE |  |
| [Text.Range](https://docs.microsoft.com/powerquery-m/text-range) | FALSE | [SUBSTRING](https://learn.microsoft.com/sql/t-sql/functions/substring-transact-sql) |
| [Text.BeforeDelimiter](https://docs.microsoft.com/powerquery-m/text-beforedelimiter) | FALSE |  |
| [Text.Type](https://docs.microsoft.com/powerquery-m/text-type) | FALSE |  |
| [Text.BetweenDelimiters](https://docs.microsoft.com/powerquery-m/text-betweendelimiters) | FALSE |  |
| [Text.RemoveRange](https://docs.microsoft.com/powerquery-m/text-removerange) | FALSE |  |
| [Text.Insert](https://docs.microsoft.com/powerquery-m/text-insert) | FALSE |  |
| [Text.Middle](https://docs.microsoft.com/powerquery-m/text-middle) | TRUE | [SUBSTRING](https://learn.microsoft.com/sql/t-sql/functions/substring-transact-sql) |
| [Text.InferNumberType](https://docs.microsoft.com/powerquery-m/text-infernumbertype) | FALSE |  |
| [Text.Format](https://docs.microsoft.com/powerquery-m/text-format) | FALSE |  |
| [Text.FromBinary](https://docs.microsoft.com/powerquery-m/text-frombinary) | FALSE |  |
| [Text.Clean](https://docs.microsoft.com/powerquery-m/text-clean) | FALSE |  |
| [Text.Remove](https://docs.microsoft.com/powerquery-m/text-remove) | FALSE |  |
| [Text.PositionOfAny](https://docs.microsoft.com/powerquery-m/text-positionofany) | FALSE |  |
| [Text.PadEnd](https://docs.microsoft.com/powerquery-m/text-padend) | FALSE |  |
| [Text.PadStart](https://docs.microsoft.com/powerquery-m/text-padstart) | FALSE |  |
| [Text.At](https://docs.microsoft.com/powerquery-m/text-at) | FALSE | [SUBSTRING](https://learn.microsoft.com/sql/t-sql/functions/substring-transact-sql) |
| [Text.Start](https://docs.microsoft.com/powerquery-m/text-start) | TRUE | [LEFT](https://learn.microsoft.com/sql/t-sql/functions/left-transact-sql) |
| [Text.From](https://docs.microsoft.com/powerquery-m/text-from) | TRUE | [CONVERT](https://learn.microsoft.com/sql/t-sql/functions/convert-transact-sql) |
| [Text.Length](https://docs.microsoft.com/powerquery-m/text-length) | TRUE | [LEN](https://learn.microsoft.com/sql/t-sql/functions/len-transact-sql) |
| [Text.TrimStart](https://docs.microsoft.com/powerquery-m/text-trimstart) | TRUE | [LTRIM](https://learn.microsoft.com/sql/t-sql/functions/ltrim-transact-sql) |
| [Text.Lower](https://docs.microsoft.com/powerquery-m/text-lower) | TRUE | [LOWER](https://learn.microsoft.com/sql/t-sql/functions/lower-transact-sql) |
| [Text.Contains](https://docs.microsoft.com/powerquery-m/text-contains) | TRUE | [CASE](https://learn.microsoft.com/sql/t-sql/functions/case-transact-sql) |
| [Text.Proper](https://docs.microsoft.com/powerquery-m/text-proper) | FALSE |  |
| [Text.EndsWith](https://docs.microsoft.com/powerquery-m/text-endswith) | TRUE | [CASE](https://learn.microsoft.com/sql/t-sql/functions/case-transact-sql) |
| [Text.Combine](https://docs.microsoft.com/powerquery-m/text-combine) | TRUE | [CONCAT](https://learn.microsoft.com/sql/t-sql/functions/concat-transact-sql) |
| [Text.StartsWith](https://docs.microsoft.com/powerquery-m/text-startswith) | TRUE | [CASE](https://learn.microsoft.com/sql/t-sql/functions/case-transact-sql) |
| [Text.PositionOf](https://docs.microsoft.com/powerquery-m/text-positionof) | FALSE | [CHARINDEX](https://learn.microsoft.com/sql/t-sql/functions/charindex-transact-sql) |
| [Text.NewGuid](https://docs.microsoft.com/powerquery-m/text-newguid) | TRUE |  |
| [Text.Repeat](https://docs.microsoft.com/powerquery-m/text-repeat) | FALSE | [REPLICATE](https://learn.microsoft.com/sql/t-sql/functions/replicate-transact-sql) |
| [Text.ReplaceRange](https://docs.microsoft.com/powerquery-m/text-replacerange) | FALSE | [STUFF](https://learn.microsoft.com/sql/t-sql/functions/stuff-transact-sql) |
| [Text.Reverse](https://docs.microsoft.com/powerquery-m/text-reverse) | FALSE | [REVERSE](https://learn.microsoft.com/sql/t-sql/functions/reverse-transact-sql) |
| [Text.End](https://docs.microsoft.com/powerquery-m/text-end) | TRUE | [RIGHT](https://learn.microsoft.com/sql/t-sql/functions/right-transact-sql) |
| [Text.Replace](https://docs.microsoft.com/powerquery-m/text-replace) | TRUE | [REPLACE](https://learn.microsoft.com/sql/t-sql/functions/replace-transact-sql) |
| [Text.TrimEnd](https://docs.microsoft.com/powerquery-m/text-trimend) | TRUE | [RTRIM](https://learn.microsoft.com/sql/t-sql/functions/rtrim-transact-sql) |
| [Text.Upper](https://docs.microsoft.com/powerquery-m/text-upper) | TRUE | [UPPER](https://learn.microsoft.com/sql/t-sql/functions/upper-transact-sql) |
| [Text.Trim](https://docs.microsoft.com/powerquery-m/text-trim) | TRUE | [TRIM](https://learn.microsoft.com/sql/t-sql/functions/trim-transact-sql) |
| [Time.Type](https://docs.microsoft.com/powerquery-m/time-type) | FALSE |  |
| [Time.ToText](https://docs.microsoft.com/powerquery-m/time-totext) | FALSE |  |
| [Time.Second](https://docs.microsoft.com/powerquery-m/time-second) | FALSE |  |
| [Time.ToRecord](https://docs.microsoft.com/powerquery-m/time-torecord) | FALSE |  |
| [Time.StartOfHour](https://docs.microsoft.com/powerquery-m/time-startofhour) | FALSE |  |
| [Time.FromText](https://docs.microsoft.com/powerquery-m/time-fromtext) | FALSE |  |
| [Time.EndOfHour](https://docs.microsoft.com/powerquery-m/time-endofhour) | FALSE |  |
| [Time.From](https://docs.microsoft.com/powerquery-m/time-from) | FALSE |  |
| [Time.Hour](https://docs.microsoft.com/powerquery-m/time-hour) | FALSE |  |
| [Time.Minute](https://docs.microsoft.com/powerquery-m/time-minute) | FALSE |  |
| [Value.Add](https://docs.microsoft.com/powerquery-m/value-add) | FALSE |  |
| [Value.Compare](https://docs.microsoft.com/powerquery-m/value-compare) | FALSE |  |
| [Value.Divide](https://docs.microsoft.com/powerquery-m/value-divide) | FALSE |  |
| [Value.Multiply](https://docs.microsoft.com/powerquery-m/value-multiply) | FALSE |  |
| [Value.Equals](https://docs.microsoft.com/powerquery-m/value-equals) | TRUE | [CASE](https://learn.microsoft.com/sql/t-sql/functions/case-transact-sql) |
| [Value.As](https://docs.microsoft.com/powerquery-m/value-as) | TRUE |  |
| [Value.FromText](https://docs.microsoft.com/powerquery-m/value-fromtext) | FALSE |  |
| [Value.NullableEquals](https://docs.microsoft.com/powerquery-m/value-nullableequals) | FALSE |  |
| [Value.Firewall](https://docs.microsoft.com/powerquery-m/value-firewall) | FALSE |  |
| [Value.RemoveMetadata](https://docs.microsoft.com/powerquery-m/value-removemetadata) | FALSE |  |
| [Value.ReplaceType](https://docs.microsoft.com/powerquery-m/value-replacetype) | FALSE |  |
| [Value.ReplaceMetadata](https://docs.microsoft.com/powerquery-m/value-replacemetadata) | FALSE |  |
| [Value.Metadata](https://docs.microsoft.com/powerquery-m/value-metadata) | FALSE |  |
| [Value.Is](https://docs.microsoft.com/powerquery-m/value-is) | FALSE |  |
| [Value.ResourceExpression](https://docs.microsoft.com/powerquery-m/value-resourceexpression) | FALSE |  |
| [Value.Subtract](https://docs.microsoft.com/powerquery-m/value-subtract) | FALSE |  |
| [Value.NativeQuery](https://docs.microsoft.com/powerquery-m/value-nativequery) | FALSE |  |
