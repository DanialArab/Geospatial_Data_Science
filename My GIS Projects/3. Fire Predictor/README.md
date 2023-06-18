
# 3. Fire Predictor

In this project, I studied the ML ideas, which are suggested based on the previous project I did on <a href="https://github.com/DanialArab/Geospatial_Data_Science/tree/main/My%20GIS%20Projects/2.%20Exploratory%20Data%20Analysis%20on%20US%20Wildfires
" target="_blank" rel="noopener">EDA on 1.88 Million US Wildfires</a>. In that project the followings ML ideas have been suggested:

+ Given the state, county, cause, and date of the fire, is it possible to predict the fire size class (classes A to G)? (the problem is classification)
+ Given the time, location, and size of the fire, is it possible to predict the cause of the fire? is it a function of seasons? (the problem is classification)
+ Given the state, county, cause, and date of the fire, is it possible to predict the fire size in acres? (the problem is regression)

In this project, I trained various ML models to investigate the above ideas. The structure of this project is as follows:

# Table of content

1. [Classification problem to predict the size class of the wildfire](#1)
   1. [Checking the balance of the dataset](#2)
   2. [Data cleaning](#3)
3. [Classification problem to predict the cause of the wildfire](#2)
4. [Regression problem to predict the size of the wildfire in acres](#2)
 
<a name="1"></b>
### Classification problem to predict the fire size class

The US wildfire sizes have been classified into seven different classes as follows:

Table 3. 1: Seven different fire size classes in the US wildfire data (1992 - 2015)

|**number of acres within the final fire perimeter expenditures**|**Fire Size Class ID** |
| -- | --| 
|0 - 0.25|A|
|0.26-9.9|B|
|10.0-99.9|C|
|100-299|D|
|300 to 999|E|
|1000 to 4999|F|
|5000 +|G|

So the problem is a multiclass classification and in this section, I will train an ML model to predict the fire size class based on the available features. The balance of data needs to be checked first:

<a name="2"></b>
### Checking the balance of the dataset

Table 3. 2: The counts of each fire size class in the US wildfire data (1992 - 2015)

|**FIRE_SIZE_CLASS**|**count** | **normalized count (%)**|
| -- | --| --|
|              B|939376|49.95|
|              A|666919|35.46|
|              C|220077|11.703329|
|              D| 28427|1.511701|
|              E| 14107|0.750187|
|              F|  7786|0.414047|
|              G|  3773|0.200642|

As shown in Table 3. 2, the data is so imbalanced, which greatly affects the accuracy of the classification algorithm. In these cases, we have to either rely on metrics other than accuracy, which are based on the confusion matrix like f1 score, recall, and precision, or resort to the sampling techniques. But for now, let's try the former approach i.e., working with the data as it is and measuring its performance via the confusion matrix.

<a name="2"></b>
### Data cleaning

side note:
I could have approached the problem like a regression task because the data also includes, in addition to the fire size class, the fire size in acres.

Here are some notes:

+ I used Spark 
+ ...


<a name="2"></b>
### Classification problem to predict the cause of the wildfire


|**STAT_CAUSE_CODE**|**count** | **normalized count (%)**|
| -- | --| --|
|            5.0|429028|22.81|
|            9.0|323805|17.21|
|            7.0|281455|14.96|
|            1.0|278468|14.80|
|           13.0|166723|8.86|
|            2.0|147612|7.84|
|            4.0| 76139|4.04|
|            8.0| 61167|3.25|
|            3.0| 52869|2.81|
|            6.0| 33455|1.77|
|           11.0| 14448|0.76|
|           10.0| 11500| 0.61|
|           12.0|  3796|0.20


<a name="3"></b>
### Regression problem to predict the size of the wildfire in acres 
