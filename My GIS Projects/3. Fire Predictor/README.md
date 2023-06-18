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
   3. [Formatting data to be compatible with spark MLlib](#4)
   4. [ML results](#5)
      1. [Logistic regression](#6)
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

<a name="3"></b>
### Data cleaning

Let's see if there are any null values in the features:

|LONGITUDE|LATITUDE|FIRE_SIZE|FIRE_SIZE_CLASS|STATE|FIRE_YEAR|DISCOVERY_DOY|STAT_CAUSE_CODE|CONT_DOY|
|--|--|--|--|--|--|--|--|--|
|        0|       0|        0|              0|    0|        0|            0|              0|   891531|

so as a first trial, let's exclude CONT_DOY and work with the other features. 

<a name="4"></b>
#### Formatting data to be compatible with spark MLlib

The data after being processed and getting compatible with spart MLlib is shown in the following:

      +---------------+-----+---------+-------------+---------------+---------------------+-----------+--------------------+
      |FIRE_SIZE_CLASS|STATE|FIRE_YEAR|DISCOVERY_DOY|STAT_CAUSE_CODE|FIRE_SIZE_CLASS_index|STATE_Index|            features|
      +---------------+-----+---------+-------------+---------------+---------------------+-----------+--------------------+
      |              A|   CA|     2005|           33|              9|                  1.0|        0.0|[0.0,2005.0,33.0,...|
      |              A|   CA|     2004|          133|              1|                  1.0|        0.0|[0.0,2004.0,133.0...|
      |              A|   CA|     2004|          152|              5|                  1.0|        0.0|[0.0,2004.0,152.0...|
      |              A|   CA|     2004|          180|              1|                  1.0|        0.0|[0.0,2004.0,180.0...|
      |              A|   CA|     2004|          180|              1|                  1.0|        0.0|[0.0,2004.0,180.0...|
      |              A|   CA|     2004|          182|              1|                  1.0|        0.0|[0.0,2004.0,182.0...|
      |              A|   CA|     2004|          183|              1|                  1.0|        0.0|[0.0,2004.0,183.0...|


the columns need to be used in ML are **features** and **FIRE_SIZE_CLASS_index**, which are features and taget/label, respectively. The first five features are:

      Row(features=DenseVector([0.0, 2005.0, 33.0, 9.0]))
      Row(features=DenseVector([0.0, 2004.0, 133.0, 1.0]))
      Row(features=DenseVector([0.0, 2004.0, 152.0, 5.0]))
      Row(features=DenseVector([0.0, 2004.0, 180.0, 1.0]))
      Row(features=DenseVector([0.0, 2004.0, 180.0, 1.0]))

the attributes in the each record above are state_indexed, fire_year, discovery_doy, and fire_cause_indexed. This spark dataframe will be used in different classification algorithms like Logistic Regression and Random Forest Classifier. 

<a name="5"></b>
#### ML results

<a name="6"></b>
##### Logistic regression

      Acuuracy = 0.5053254563727341
      f1_score = 0.4312706891097169, 
      weighted_Precision = 0.416745785366686, 
      weighted_Recall = 0.5053254563727341, 
      confusionMatrix: 
      prediction                0.0    1.0
      FIRE_SIZE_CLASS_index               
      0.0                    237386  44540
      1.0                    152411  47707
      2.0                     55012  11031
      3.0                      6405   1955
      4.0                      2997   1211
      5.0                      1442    939
      6.0                       546    595





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
