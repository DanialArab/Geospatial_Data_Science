
## 2. Exploratory Data Analysis on US Wildfires 

The python (pyspark) scripts for all the results in this exploratory data analysis are included in the jupyter notebook file named <a href="https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/2.%20Exploratory%20Data%20Analysis%20on%20US%20Wildfires/EDA%20on%201.88%20Million%20US%20Wildfires.ipynb" target="_blank" rel="noopener">EDA on 1.88 Million US Wildfires</a>. 

# Table of content

1. [Introduction](#1)
    1. [Some quick notes on the data](#2)
    2. [Potential ideas/deliverables](#3)
2. [Statistical analysis of the US Wildfires](#4)
    1. [US wildfires count and size distribution vs. location](#5)
       1. [US wildfires count and size per year across the country or within each state](#6)
       2. [US wildfires count and size per fire size class across the country or within each state](#7)
       3. [US wildfires count and size per cause of the wildfire across the country or within each state](#8)  
    2. [US wildfires count and size distribution vs. time](#9)
       1. [US wildfires count and size distribution vs. time across the country](#10)
       2. [US wildfires count and size distribution vs. time per state](#11)
       3. [Average duration of wildfires](#12)
            1. [per state](#13)
            2. [across the country per month](#14)
            3. [across the country per fire class size](#15)
3. [Conclusion](#16)

<a name="1"></b>
### Introduction

In this project, I use Spark to play with Sqlite data of 1.88 Million US Wildfires, data obtained from Kaggle (<a href="https://www.kaggle.com/datasets/rtatman/188-million-us-wildfires/" target="_blank" rel="noopener">link to the Kaggle data source</a>). My primary goal was to explore the data and find out any potential room for application of Machine Learning to see if we can predict the cause, location, or size of fire. So based on this exploratory data analysis, I will experiment different ML ideas, which could potentially be worth of more exploration, in a separate project named "3. Fire Predictor" (<a href="https://github.com/DanialArab/Geospatial_Data_Science/tree/main/My%20GIS%20Projects/3.%20Fire%20Predictor/" target="_blank" rel="noopener">link to its repo</a>). 

<a name="2"></b>
#### Some quick notes on the data
+ Data belong to 1992 to 2015 
+ The fire sizes are classified as 7 different classes, as follow:

|**number of acres within the final fire perimeter expenditures**|**Class ID** |
| -- | --| 
|0 - 0.25|A|
|0.26-9.9|B|
|10.0-99.9|C|
|100-299|D|
|300 to 999|E|
|1000 to 4999|F|
|5000 +|G|

+ The followings are the useful attributes on which I will be focusing:

      root
       |-- STATE: string (nullable = true)
       |-- FIRE_YEAR: decimal(38,18) (nullable = true)
       |-- DISCOVERY_DOY: decimal(38,18) (nullable = true)
       |-- CONT_DOY: decimal(38,18) (nullable = true)
       |-- STAT_CAUSE_DESCR: string (nullable = true)
       |-- LONGITUDE: decimal(38,18) (nullable = true)
       |-- LATITUDE: decimal(38,18) (nullable = true)
       |-- FIRE_SIZE: decimal(38,18) (nullable = true)
       |-- FIRE_SIZE_CLASS: string (nullable = true)

The first four rows of the data containing the above attributes, out of 1,880,465 records, are presented in the following:

|**STATE**|**FIRE_YEAR** | **DISCOVERY_DOY**|  **CONT_DOY**| **STAT_CAUSE_DESCR**|**LONGITUDE**|**LATITUDE** | **FIRE_SIZE**|  **FIRE_SIZE_CLASS**|
| -- | --|  -- | -- | -- | -- | --|  -- | -- |
|   CA|2005.000000000000...|33.00000000000000...|33.00000000000000...|   Miscellaneous|-121.005833330000...|40.03694444000000...|0.100000000000000000|              A|
|   CA|2004.000000000000...|133.0000000000000...|133.0000000000000...|       Lightning|-121.005833330000...|40.03694444000000...|0.100000000000000000|              A|
|   CA|2004.000000000000...|152.0000000000000...|152.0000000000000...|  Debris Burning|-120.404444440000...|38.93305556000000...|0.250000000000000000|              A|
|   CA|2004.000000000000...|180.0000000000000...|185.0000000000000...|       Lightning|-120.735555560000...|38.98416667000000...|0.100000000000000000|              A|

+ The cause of the US wildfire is classified as 13 classes:

| **STAT_CAUSE_DESCR**|**STAT_CAUSE_CODE**|
| -- | -- |
|        Lightning|              1|
|    Equipment Use|              2|
|          Smoking|              3|
|         Campfire|              4|
|   Debris Burning|              5|
|         Railroad|              6|
|            Arson|              7|
|         Children|              8|
|    Miscellaneous|              9|
|        Fireworks|             10|
|        Powerline|             11|
|        Structure|             12|
|Missing/Undefined|             13|


<a name="3"></b>
#### Potential ideas/deliverables
Based on the above info we can:

+ map the fire using geospatial info (long and lat), 
+ see how long each fire took place which could provide some insight on each state capability to deal with fires, of course some other parameters should be taken into account like the size of fire
+ calculate fire frequency in US in total or per state
+ investigate fire occurance per season/month
+ size/frequency of fire in each state
+ investigate the main root cause of fire and see if this is state dependent 
+ apply ML to discover any potential patterns in the data 

<a name="4"></b>
### Statistical analysis of the US wildfires

<a name="5"></b>
#### UUS wildfires count and size distribution vs. location


The number of wildfires per state is shown in Fig. 2. 3. As shown in this figure, California had the maximum number of fires during 1992 - 2015 followed by Georgia and Texas.

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Wildfire_counts_per_US_state_sorted.png)

Fig. 2. 3: The US Wildfires counts per state (1992 - 2015)

Other than the frequency of wildfires, it could be insightful to see how big the fire was in each state (see Fig. 2. 4 and 2. 5).

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Average_fire_size_per_US_state.png)
Fig. 2. 4: The average size of US Wildfires per state (1992 - 2015)

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_fire_size_per_US_state.png)
Fig. 2. 5: The total size of US Wildfires per state (1992 - 2015)

As Fig. 2. 5 suggests, Alaska with only around 700,000 total population (https://en.wikipedia.org/wiki/Alaska) has the largest wildfire in US between 1992 adn 2015. The number of wildfires for each class size per state is discussed next.

<a name="6"></b>
##### US wildfires count and size per year across the country or within each state
       
The total number and size of the US Wildfires across the country are shown in Fig. 2. 1-1 and 2. 1-2, respectively. 

|**(1)**|**(2)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/US_Wildfire_counts_per_Year.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/US_total_Wildfire_size_per_Year.png)|

Fig. 2. 1: 1) US Wildfire counts across all the states per year, 2) US Wildfire size (acres) across all the states per year

As shown above, the minimum and maximum number of US Wildfires occured on 1997 and 2006 with total number of 61450 and 114004, respectively. The distributions of the the US wildfires in 1992, 1997, 2006, and 2015 are shown on the following maps.

|**(1)**|**(2)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_67975_Wildfires_in_US_1992.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_61450_Wildfires_in_US_1997.png)|


|**(3)**|**(4)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_114004_Wildfires_in_US_2006.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_74491_Wildfires_in_US_2015.png)|

Fig. 2. 2: Locations of US Wildfires across all states for 1) 1992, 2) 1997, 3) 2006, and 4) 2015 

It would be insightfull to also see where, within each state, the wildfires were formed. As an example, the wildfires' location in Texas state during 1992 to 2015 are shown in the following:


|**(1)**|**(2)** |
| -- | --|  
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_1168_Wildfires_in_TX_1992.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_1457_Wildfires_in_TX_1993.png)|

|**(3)**|**(4)** |
| -- | --|  
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_907_Wildfires_in_TX_1994.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_1648_Wildfires_in_TX_1995.png)|


|**(5)**|**(6)** |
| -- | --|  
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_2843_Wildfires_in_TX_1996.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_770_Wildfires_in_TX_1997.png)|


|**(7)**|**(8)** |
| -- | --|  
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_2026_Wildfires_in_TX_1998.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_1775_Wildfires_in_TX_1999.png)|


|**(9)**|**(10)** |
| -- | --|  
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_2627_Wildfires_in_TX_2000.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_771_Wildfires_in_TX_2001.png)|

|**(11)**|**(12)** |
| -- | --|  
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_1229_Wildfires_in_TX_2002.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_1147_Wildfires_in_TX_2003.png)|

|**(13)**|**(14)** |
| -- | --|  
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_1040_Wildfires_in_TX_2004.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_6901_Wildfires_in_TX_2005.png)|

|**(15)**|**(16)** |
| -- | --|  
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_15022_Wildfires_in_TX_2006.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_5477_Wildfires_in_TX_2007.png)|

|**(17)**|**(18)** |
| -- | --|  
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_18067_Wildfires_in_TX_2008.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_14142_Wildfires_in_TX_2009.png)|

|**(19)**|**(20)** |
| -- | --|  
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_9351_Wildfires_in_TX_2010.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_19453_Wildfires_in_TX_2011.png)|

|**(21)**|**(22)** |
| -- | --|  
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_7623_Wildfires_in_TX_2012.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_9735_Wildfires_in_TX_2013.png)|

|**(23)**|**(24)** |
| -- | --|  
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_8538_Wildfires_in_TX_2014.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_8304_Wildfires_in_TX_2015.png)|

Fig. 2. 3: Locations of the Texas wildfires from 1992 to 2015

As shown in Fig. 2. 3, east of Texas consistently experienced wildfire during the period of study. The wildfire center was shifted towards the Texas centre since 2005 (Fig. 2. 3-14) and the fire was propagated towards the north on around 2011 (Fig. 2. 3-20)

<a name="7"></b>
##### US wildfires count and size per fire size class across the country or within each state

Although 7 different fire size classes were reported, it is good to know the average size of the fire in each class:

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Average_Fire_Size_per_each_Class.png)

Fig. 2. 2: Average US Wildfires Size per each Class (1992 - 2015)


|**(1)**|**(2)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_AZ.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_SC.png)|


|**(3)**|**(4)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_LA.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_MN.png)|


|**(5)**|**(6)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_NJ.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_DC.png)|

|**(7)**|**(8)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_OR.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_VA.png)|

|**(9)**|**(10)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_RI.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_WY.png)|

|**(11)**|**(12)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_KY.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_NH.png)|

|**(13)**|**(14)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_MI.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_NV.png)|

|**(15)**|**(16)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_WI.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_ID.png)|

|**(17)**|**(18)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_CA.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_NE.png)|

|**(19)**|**(20)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_CT.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_MT.png)|

|**(21)**|**(22)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_NC.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_VT.png)|

|**(23)**|**(24)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_MD.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_DE.png)|

|**(25)**|**(26)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_MO.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_IL.png)|

|**(27)**|**(28)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_ME.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_WA.png)|

|**(29)**|**(30)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_ND.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_MS.png)|

|**(31)**|**(32)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_AL.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_IN.png)|

|**(33)**|**(34)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_OH.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_TN.png)|

|**(35)**|**(36)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_NM.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_IA.png)|

|**(37)**|**(38)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_PA.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_SD.png)|

|**(39)**|**(40)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_NY.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_TX.png)|

|**(41)**|**(42)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_WV.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_GA.png)|

|**(43)**|**(44)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_MA.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_KS.png)|

|**(45)**|**(46)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_CO.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_FL.png)|

|**(47)**|**(48)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_AK.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_AR.png)|

|**(49)**|**(50)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_OK.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_PR.png)|

|**(51)**|**(52)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_UT.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Number_of_Fires_per_size_class_in_HI.png)|

Fig. 2. 6: The US Wildfires counts of each fire size class per state (1992 - 2015)

<a name="8"></b>
##### US wildfires count and size per cause of the wildfire across the country or within each state


Comparing the plots for different states in Fig. 2. 6 shows that the number of wildfires generally decreases as the size of the fire increases. However, Alaska does not follow this trend and as shown in Fig. 2. 6 - 47, the number of wildfires increases as the size of fire increases from around 100 acres (class D) up to more than 5000 acres (class G). To further understand the wildfire occurrence in different states, the fire cause in each state is investigated in the following.

The fire cause codes and definitions, adapted from the USFS (United States Forest Service) 2003 classification, are as follow (Short, 2014):

1. Lightning: This code is used when a fire is caused by lightning strikes. Lightning is a common natural cause of wildfires.

2. Equipment Use: This code is assigned when a fire is ignited by the use of equipment or machinery, such as chainsaws, generators, or vehicles. It includes cases where sparks or heat generated by equipment result in fire.

3. Smoking: This code is used when a fire is started by the careless or improper disposal of smoking materials, such as cigarettes or cigars.

4. Campfire: This code is assigned when a fire originates from an improperly managed or unattended campfire. It includes cases where campfires spread beyond their intended area or are left burning without proper extinguishment.

5. Debris Burning: This code is used when a fire is caused by the burning of debris, such as vegetation or waste materials. It includes cases where the fire gets out of control during debris burning activities.

6. Railroad: This code is assigned when a fire is ignited by activities related to railroad operations, such as sparks from trains or maintenance activities.

7. Arson: This code is used when a fire is intentionally set with the purpose of causing damage or harm. Arson is a criminal act and is considered a significant cause of wildfires.

8. Children: This code is assigned when a fire is started by children engaging in fire-related activities, such as playing with matches or lighters without proper supervision.

9. Miscellaneous: This code is used when the cause of the fire does not fall into any of the specific categories mentioned above. It includes cases where the cause is known but does not fit within the established categories.

10. Fireworks: This code is assigned when a fire is caused by the use of fireworks. Fireworks can ignite vegetation or other combustible materials, resulting in fires.

11. Power line: This code is used when a fire originates from a malfunction, failure, or contact with power lines or electrical equipment.

12. Structure: This code is assigned when a fire starts in or around a structure, such as a building or a dwelling.

M13. issing/Undefined: This code is used when the cause of the fire is unknown or cannot be determined due to lack of information or evidence.

To get an idea on the main root cause of the wildfire in US, the percentage of the wildfires caused by each cause is shown in Fig. 2. 4. 

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_across_all_states_1992_2015.png)

Fig. 2. 7: Cause of the US Wildfires across all the states (1992 - 2015)

This information is useful in suggesting that the human activities play a crucial role as a main cause behind the US wildfires. To be able to provide a standardized way to classify and track the causes of wildfires per state the percentage of each cause per total number of wildfires per state are shown in Fig. 2. 8. These details can be helpful to agencies and organizations to analyze trends, develop prevention strategies, and allocate resources.


|**(1)**|**(2)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_AZ_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_SC_1992_2015.png)|


|**(3)**|**(4)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_LA_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_MN_1992_2015.png)|


|**(5)**|**(6)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_NJ_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_DC_1992_2015.png)|

|**(7)**|**(8)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_OR_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_VA_1992_2015.png)|

|**(9)**|**(10)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_RI_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_WY_1992_2015.png)|

|**(11)**|**(12)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_KY_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_NH_1992_2015.png)|

|**(13)**|**(14)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_MI_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_NV_1992_2015.png)|

|**(15)**|**(16)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_WI_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_ID_1992_2015.png)|

|**(17)**|**(18)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_CA_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_NE_1992_2015.png)|

|**(19)**|**(20)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_CT_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_MT_1992_2015.png)|

|**(21)**|**(22)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_NC_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_VT_1992_2015.png)|

|**(23)**|**(24)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_MD_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_DE_1992_2015.png)|

|**(25)**|**(26)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_MO_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_IL_1992_2015.png)|

|**(27)**|**(28)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_ME_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_WA_1992_2015.png)|

|**(29)**|**(30)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_ND_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_MS_1992_2015.png)|

|**(31)**|**(32)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_AL_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_IN_1992_2015.png)|

|**(33)**|**(34)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_OH_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_TN_1992_2015.png)|

|**(35)**|**(36)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_NM_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_IA_1992_2015.png)|

|**(37)**|**(38)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_PA_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_SD_1992_2015.png)|

|**(39)**|**(40)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_NY_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_TX_1992_2015.png)|

|**(41)**|**(42)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_WV_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_GA_1992_2015.png)|

|**(43)**|**(44)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_MA_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_KS_1992_2015.png)|

|**(45)**|**(46)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_CO_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_FL_1992_2015.png)|

|**(47)**|**(48)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_AK_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_AR_1992_2015.png)|

|**(49)**|**(50)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_OK_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_PR_1992_2015.png)|

|**(51)**|**(52)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_UT_1992_2015.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Cause_of_US_Wildfire_in_HI_1992_2015.png)|

Fig. 2. 8: Cause of the US Wildfires across different states: a) Alaska, b) California, c) Georgia, and d) Texas (1992 - 2015)

As shown in Fig. 2. 8 - 47, more than 30 % of the wildfires in Alaska is caused by the ligthing strikes.

Comparing Fig. 2. 8 and 2. 13 can lead to a coherent conclusion: the larger the weight of nature to cause the wildfire the more chance to shift the peak of fire size towards the hottest months i.e., June, July, and August. 

<a name="9"></b>
#### US wildfires count and size distribution vs. time

<a name="10"></b>
##### US wildfires count and size distribution vs. time across the country

To see if there is any trend in the wildfire occurance at different seasons/month during a year, the fire size is plotted vs. date of fire occurance (Fig. 

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Fire_Size_vs_date_1992_2000.png)

Fig. 2. 4: Size of US wildfire vs date (1992 - 2000)


![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Fire_Size_vs_date_2000_2008.png)

Fig. 2. 5: Size of US wildfire vs date (2000 - 2008)

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Fire_Size_vs_date_2008_2016.png)

Fig. 2. 6: Size of US wildfire vs date (2008 - 2016)

As expected, there is a clear cyclic trend in the size of fire in each year, which peaks between June to August. To more quantitatively investigate this observation, the fire size across all the US states vs months is plotted in Fig. 2. 7.

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Fire_counts_vs_date_1992_2000.png)

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Fire_counts_vs_date_2000_2008.png)

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Fire_counts_vs_date_2008_2016.png)

<a name="11"></b>
##### US wildfires count and size distribution vs. time per state
Average duration of wildfires
per state
across the country per month
across the country per fire class size

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Average_duration_of_US_wildfires_per_fire_size_class.png)

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Average_duration_of_US_wildfires_per_month.png)

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Average_duration_of_wildfires_in_US_1992_to_2015.png)





![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month.png)

Fig. 2. 7: Size of US wildfire vs month for all states (1992 - 2015)

The data plotted in Fig. 2. 4 - 2. 7 belong to all the states. It would be insightful to investigate the fire size per month per state (Fig. 2. 8).

|**(1)**|**(2)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_AZ.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_SC.png)|

|**(3)**|**(4)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_LA.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_MN.png)|

|**(5)**|**(6)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_NJ.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_DC.png)|

|**(7)**|**(8)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_OR.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_VA.png)|

|**(9)**|**(10)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_RI.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_WY.png)|

|**(11)**|**(12)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_KY.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_NH.png)|

|**(13)**|**(14)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_MI.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_NV.png)|

|**(15)**|**(16)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_WI.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_ID.png)|

|**(17)**|**(18)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_CA.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_NE.png)|

|**(19)**|**(20)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_CT.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_MT.png)|

|**(21)**|**(22)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_NC.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_VT.png)|

|**(23)**|**(24)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_MD.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_DE.png)|

|**(25)**|**(26)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_MO.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_IL.png)|

|**(27)**|**(28)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_ME.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_WA.png)|

|**(29)**|**(30)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_ND.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_MS.png)|

|**(31)**|**(32)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_AL.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_IN.png)|

|**(33)**|**(34)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_OH.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_TN.png)|

|**(35)**|**(36)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_NM.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_IA.png)|

|**(37)**|**(38)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_PA.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_SC.png)|

|**(39)**|**(40)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_NY.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_TX.png)|

|**(41)**|**(42)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_WV.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_GA.png)|

|**(43)**|**(44)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_MA.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_KS.png)|

|**(45)**|**(46)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_CO.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_FL.png)|

|**(47)**|**(48)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_AK.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_AR.png)|

|**(49)**|**(50)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_OK.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_PR.png)|

|**(51)**|**(52)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_UT.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_Fire_Size_vs_month_in_HI.png)|

Fig. 2. 8: Size of the US wildfire vs. month per state (1992 - 2015)




ML Ideas and some comments:

|**FIRE_SIZE_CLASS**|**count** | **normalized count (%)**|
| -- | --| --|
|              B|939376|49.95|
|              A|666919|35.46|
|              C|220077|11.703329|
|              D| 28427|1.511701|
|              E| 14107|0.750187|
|              F|  7786|0.414047|
|              G|  3773|0.200642|


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


ideas to consider for ML

1. Given state, county, cause of fire, date, can I predict the fire size class? (the problem is classification)
2. Given state, county, cause of fire, date, can I predict the fire size ? (the problem is regression)
3. Given time, location, and size can I predict the cause of the fire? is it a function of seasons? 
4. comparison of fire discovery date with cont_date in various years and various states may be useful like how many days took to control fire in various states and also in the same state as a function of time this also can be a function of fire size



Data reference: Short, Karen C. 2017. Spatial wildfire occurrence data for the United States, 1992-2015 [FPA_FOD_20170508]. 4th Edition. Fort Collins, CO: Forest Service Research Data Archive. https://doi.org/10.2737/RDS-2013-0009.4

Link to the Kaggle data source: https://www.kaggle.com/datasets/rtatman/188-million-us-wildfires

References:

Short, K. C. 2014. A spatial database of wildfires in the United States, 1992-2011. Earth System Science Data. 6:1-27. https://doi.org/10.5194/essd-6-1-2014


