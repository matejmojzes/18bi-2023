# Lecture #5: Pivot Tables (Special topic)

_November 15 2023_

## Pivo tables, you say?

Czech translation is: _kontingenční tabulka_. See e.g. [Wikipedia](https://en.wikipedia.org/wiki/Pivot_table) for reference and more information. 

Actually, this translation (at least in MS Excel) might not be ideal, because it seems to be referring to _contingency table_, a different concept.

> A pivot table is a versatile tool for summarizing and analyzing data in a spreadsheet, while a contingency table is specifically designed for analyzing the relationship between two categorical variables. They serve different purposes and are used in different contexts within the field of data analysis and statistics.


## What are they good for?

Ad-hoc inspection of a reasonably small data set.
* Either raw data, or already some statistics obtained by aggregation of a larger data set (e.g. on a cluster).
* Data set is typically a denormalized table (i.e. result of a join in a traditional normalized data base).

Pros: 
* Quick data exploration and validation of hypotheses via eyeballing (heatmaps, charts),
* Intuitive [slicing and dicing](https://en.wikipedia.org/wiki/OLAP_cube) of the data.

Cons: 
* They look maybe too trivial for some people (typically hard-core programmers), so they do not bother to learn about them.
* If they are GUI-based (e.g.: MS Excel, Google Sheets), they need to be manually re-configured for each question/hypothesis. Also, it might not be clear how one arrived to an output, and what was his/her reasoning.  This does not help with reproducibility, but can be solved using by a bit of coding e.g. in Python or R and development in a [lab notebook](https://en.wikipedia.org/wiki/Lab_notebook), e.g. [Jupyter](https://jupyter.org/).

## Let's try them out

### 1. Via a straightforward tutorial

[Pivot Tables in Spreadsheets from DataCamp](https://www.datacamp.com/tutorial/pivot-tables-spreadsheets).


### 2. Be careful with missing data in what you aggregate, eg. in the time dimension

Imagine the following data set:

```
Date,Dimension,Value
01/10/2023,Foo,10
02/10/2023,Foo,20
03/10/2023,Foo,30
04/10/2023,Foo,40
05/10/2023,Foo,50
06/10/2023,Foo,40
07/10/2023,Foo,30
08/10/2023,Foo,45
09/10/2023,Foo,70
10/10/2023,Foo,80
01/10/2023,Bar,20
02/10/2023,Bar,25
03/10/2023,Bar,40
04/10/2023,Bar,70
06/10/2023,Bar,25
07/10/2023,Bar,35
08/10/2023,Bar,30
09/10/2023,Bar,45
10/10/2023,Bar,50
```

See the problem?

### 3. Perform a pivot table analysis on your own data set

If you do not have nothing ready available, take a look at the following collection of data sets: [UCI ML repo data sets](https://archive.ics.uci.edu/ml/datasets.php), e.g. [Auto MPG](https://archive.ics.uci.edu/ml/datasets/Auto+MPG).
