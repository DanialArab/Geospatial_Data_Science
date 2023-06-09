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
         1. [Resampling technique to deal with the imbalanced dataset](#7)
            1. [Oversampling](#8)
            2. [Undersampling](#9)
      2. [Random forest classifier](#10)
         1. [Resampling technique to deal with the imbalanced dataset](#11)
            1. [Oversampling](#12)
            2. [Undersampling](#13)
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

the attributes in the each record above are FIRE_YEAR, DISCOVERY_DOY, STAT_CAUSE_CODE, and STATE_Index. This spark dataframe will be used in different classification algorithms like Logistic Regression and Random Forest Classifier. But before moving forward, the range of features needs to be checked: 

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/distribution_of_features.png)

Fig.3. 1: Distribution of features

So since the range of features is remarkably different (Fig. 3. 1), I do need to scale the features, whose distributions are presented in the following figure:

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/distribution_of_scaled_features.png)

Fig.3. 2: Distribution of scaled features

<a name="5"></b>
#### ML results

<a name="6"></b>
##### Logistic regression

The metrics for the first trial of logistic regression with this very imbalanced data are as follows:

      Accuracy = 0.5051604681376763
      f1_score = 0.43094392943837395, 
      weighted_Precision = 0.4163392177660231, 
      weighted_Recall = 0.5051604681376762, 
      confusion Matrix: 
      prediction                0.0    1.0
      FIRE_SIZE_CLASS_index               
      0.0                    237439  44446
      1.0                    152441  47569
      2.0                     54899  11120
      3.0                      6612   1969
      4.0                      2980   1248
      5.0                      1436    864
      6.0                       558    612 

in this case, as shown in the confusion matrix above, the predicted classes were only 0 and 1. In the dataset, these classes dominate the distribution with 49.95 and 35.46 % normalized counts, respectively (Table 3. 2). So that is why the classifier is so biased towards the majority class, leading to poor performance on the minority class. As shown above, the accuracy is 50 %, which is almost similar to the dummy model which only predicts class 0. To improve the model's performance, the resampling techniques of oversampling the minority class or undersampling the majority class have been tested to balance the dataset.

<a name="7"></b>
###### Resampling technique to deal with the imbalanced dataset

The oversampling and undersampling should be applied only to the training data to avoid introducing bias into the testing or validation sets. Additionally, the choice between oversampling and undersampling depends on the specific problem and dataset, so I will experiment with both approaches and evaluate their impact on the model's performance.

<a name="8"></b>
###### Oversampling -- SMOTE (Synthetic Minority Over-sampling Technique)

After implementing SMOTE on the training dataset, the counts of each class in the FIRE_SIZE_CLASS_ENCODED are:

      FIRE_YEAR	DISCOVERY_DOY	STAT_CAUSE_CODE	STATE_ENCODED FIRE_SIZE_CLASS_ENCODED				
            0	      657818	      657818	            657818	      657818
            1	      657818	      657818	            657818	      657818
            2	      657818	      657818	            657818	      657818
            3	      657818	      657818	            657818	      657818
            4	      657818	      657818	            657818	      657818
            5	      657818	      657818	            657818	      657818
            6	      657818	      657818	            657818	      657818

The metrics for the Logistic regression model trained on the oversampled training dataset and evaluated on the testing data, not oversampled of course, are as follows:

      Accuracy = 0.1381483319743326
      f1_score = 0.1470281243963427, 
      precision = 0.3820880139959797, 
      recall = 0.1381483319743326, 
      confusion_matrix_df: 
             A      B       C      D      E      F      G
      A  33672  10690   47877  17608   8227  17707  64681
      B  44536  11284  118020  24195  10730  19944  52849
      C   9354   1835   31192   4667   2063   4111  12609
      D   1162    279    3205    709    296    590   2308
      E    507    238    1191    347    159    325   1539
      F    248    116     432    189     87    201   1064
      G     79     27     104     63     25     81    718

<a name="9"></b>
###### Undersampling 

After implementing undersampling on the training dataset, the counts of each class in the FIRE_SIZE_CLASS_ENCODED are:

      FIRE_YEAR	DISCOVERY_DOY	STAT_CAUSE_CODE	STATE_ENCODED FIRE_SIZE_CLASS_ENCODED				
      0	               2676	         2676	            2676	            2676
      1	               2676	         2676	            2676	            2676
      2	               2676	         2676	            2676	            2676
      3	               2676	         2676	            2676	            2676
      4	               2676	         2676	            2676	            2676
      5	               2676	         2676	            2676	            2676
      6	               2676	         2676	            2676	            2676

The metrics for the Logistic regression model trained on the undersampled training dataset and evaluated on the testing data, not undersampled of course, are as follows:

      Accuracy = 0.15093948310703018
      f1_score = 0.1798858106979777, 
      precision = 0.4343619572545453, 
      recall = 0.15093948310703018, 
      confusion_matrix_df: 
             A      B      C      D      E      F      G
      A  34396  11647  44572  17112  13059  16298  63378
      B  46794  22658  96321  31692  16364  16307  51422
      C   9909   4352  26044   6881   3107   3300  12238
      D   1221    506   2648    909    501    502   2262
      E    541    327    974    426    234    293   1511
      F    269    131    362    200    139    194   1042
      G     83     38     89     50     40     81    716

<a name="10"></b>
##### Random forest classifier

The metrics for the first trial of the random forest classifier with this very imbalanced data are as follows:

      Accuracy = 0.5768454379329395
      f1_score = 0.5266650612135855, 
      weighted_Precision = 0.491926070356712, 
      weighted_Recall = 0.5768454379329395, 
      confusion Matrix: 
      prediction                0.0     1.0
      FIRE_SIZE_CLASS_index                
      0.0                    220551   61801
      1.0                     94795  105219
      2.0                     55054   11115
      3.0                      6033    2504
      4.0                      2454    1800
      5.0                       940    1344
      6.0                       281     853 

The accuracy was improved by around 7 % compared to the logistic regression classifier, but still, only two dominant classes of 0 and 1 were predicted. 

<a name="11"></b>
###### Resampling technique to deal with the imbalanced dataset

<a name="12"></b>
###### Oversampling -- SMOTE (Synthetic Minority Over-sampling Technique)

The metrics for the random forest classifier model trained on the oversampled training dataset and evaluated on the testing data, not oversampled of course, are as follows:

      Accuracy = 0.5283316198106853
      f1_score = 0.5377056763298095, 
      weighted_Precision = 0.491926070356712, 
      weighted_Recall = 0.5768454379329395, 
      confusion Matrix: 
      prediction                0.0     1.0
      FIRE_SIZE_CLASS_index                
      0.0                    220551   61801
      1.0                     94795  105219
      2.0                     55054   11115
      3.0                      6033    2504
      4.0                      2454    1800
      5.0                       940    1344
      6.0                       281     853 

<a name="13"></b>
###### Undersampling 

The metrics for the random forest classifier model trained on the undersampled training dataset and evaluated on the testing data, not undersampled of course, are as follows:

      Accuracy = 0.31727053568263197
      f1_score = 0.38256458450575936, 
      weighted_Precision = 0.491926070356712, 
      weighted_Recall = 0.5768454379329395, 
      confusion Matrix: 
      prediction                0.0     1.0
      FIRE_SIZE_CLASS_index                
      0.0                    220551   61801
      1.0                     94795  105219
      2.0                     55054   11115
      3.0                      6033    2504
      4.0                      2454    1800
      5.0                       940    1344
      6.0                       281     853


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
