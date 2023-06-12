
## 2. Exploratory Data Analysis on US Wildfires 

### Introduction

In this project, I use Spark to play with Sqlite data of 1.88 Million US Wildfires, data obtained from Kaggle (https://www.kaggle.com/datasets/rtatman/188-million-us-wildfires). My primary goal was to explore the data and find out any potential room for application of Machine Learning to see if we can predict the cause, location, or size of fire. So based on this exploratory data analysis, I will suggest different ML ideas, which could potentially be worth of more exploration. 

Some quick notes on the data:
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

|**STATE**|**FIRE_YEAR** | **DISCOVERY_DOY**|  **CONT_DOY**| **STAT_CAUSE_DESCR**|
| -- | --|  -- | -- | -- |
|   CA|2005.000000000000...|33.00000000000000...|33.00000000000000...|   Miscellaneous|
|   CA|2004.000000000000...|133.0000000000000...|133.0000000000000...|       Lightning|
|   CA|2004.000000000000...|152.0000000000000...|152.0000000000000...|  Debris Burning|
|   CA|2004.000000000000...|180.0000000000000...|185.0000000000000...|       Lightning|
|   CA|2004.000000000000...|180.0000000000000...|185.0000000000000...|       Lightning|
|   CA|2004.000000000000...|182.0000000000000...|183.0000000000000...|       Lightning|
|   CA|2004.000000000000...|183.0000000000000...|184.0000000000000...|       Lightning|
|   CA|2005.000000000000...|67.00000000000000...|67.00000000000000...|  Debris Burning|
|   CA|2005.000000000000...|74.00000000000000...|74.00000000000000...|  Debris Burning|
|   CA|2004.000000000000...|183.0000000000000...|184.0000000000000...|       Lightning|
|   CA|2004.000000000000...|184.0000000000000...|185.0000000000000...|       Lightning|
|   CA|2004.000000000000...|184.0000000000000...|185.0000000000000...|       Lightning|
|   CA|2004.000000000000...|247.0000000000000...|247.0000000000000...|   Miscellaneous|
|   CA|2004.000000000000...|272.0000000000000...|272.0000000000000...|        Campfire|
|   CA|2004.000000000000...|277.0000000000000...|277.0000000000000...|       Lightning|
|   CA|2004.000000000000...|277.0000000000000...|277.0000000000000...|       Lightning|
|   CA|2004.000000000000...|280.0000000000000...|295.0000000000000...|   Equipment Use|
|   CA|2004.000000000000...|287.0000000000000...|291.0000000000000...|   Equipment Use|
|   CA|2004.000000000000...|325.0000000000000...|326.0000000000000...|  Debris Burning|
|   NM|2004.000000000000...|156.0000000000000...|156.0000000000000...|       Lightning|

only showing top 20 rows



|**LONGITUDE**|**LATITUDE** | **FIRE_SIZE**|  **FIRE_SIZE_CLASS**|
| -- | --|  -- | -- |
|-121.005833330000...|40.03694444000000...|0.100000000000000000|              A|
|-120.404444440000...|38.93305556000000...|0.250000000000000000|              A|
|-120.735555560000...|38.98416667000000...|0.100000000000000000|              A|
|-119.913333330000...|38.55916667000000...|0.100000000000000000|              A|
|-119.933055560000...|38.55916667000000...|0.100000000000000000|              A|
|-120.103611110000...|38.63527778000000...|0.100000000000000000|              A|
|-120.153333330000...|38.68833333000000...|0.100000000000000000|              A|
|-122.433888890000...|40.96805556000000...|0.800000000000000000|              B|
|-122.283333330000...|41.23361111000000...|1.000000000000000000|              B|
|-120.149166670000...|38.54833333000000...|0.100000000000000000|              A|
|-120.159722220000...|38.69166667000000...|0.100000000000000000|              A|
|-120.106111110000...|38.52750000000000...|0.100000000000000000|              A|
|-120.193333330000...|38.78666667000000...|0.100000000000000000|              A|
|-120.510000000000...|38.43333333000000...|6.000000000000000000|              B|
|-120.279722220000...|38.67583333000000...|0.200000000000000000|              A|
|-120.542222220000...|38.56416667000000...|0.100000000000000000|              A|
|-120.211666670000...|38.52333333000000...|16823.00000000000...|              G|
|-120.260000000000...|38.78000000000000...|7700.000000000000...|              G|
|-120.411666670000...|38.94500000000000...|0.100000000000000000|              A|

only showing top 20 rows

Based on the above info we can:

+ map the fire using geospatial info (long and lat), 
+ see how long each fire took place which could provide some insight on each state capability to deal with fires, of course some parameters should be taken into account like the size of fire
+ calculate fire frequency in US in total or per state
+ investigate fire occurance per eason
+ size of fire in each state
+ investigate the main root cause of fire and see if this is region dependent 
+ ...


![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/US_Wildfire_locations_1992_2015.png)

Fig. 2. 1: Locations of US Wildfires (1992 - 2015)

Although 7 different fire size classes reported, it is good to know the average size of fire in each class:

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Average_Fire_Size_per_each_Class.png)

Fig. 2. 2: Average US Wildfires Size per each Class (1992 - 2015)

The number of wildfires per state is shown in Fig. 2. 3. As shown in this figure, California had the maximum number of fires during 1992 - 2015 followed by Georgia and Texas.

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Wildfire_counts_per_US_state_sorted.png)

Fig. 2. 3: The US Wildfires counts per state (1992 - 2015)

Other than the frequency of wildfires, it could be insightful to see how big the fire was in each state (see Fig. 2. 4 and 2. 5).

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Average_fire_size_per_US_state.png)
Fig. 2. 4: The average size of US Wildfires per state (1992 - 2015)

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_fire_size_per_US_state.png)
Fig. 2. 5: The total size of US Wildfires per state (1992 - 2015)

As Fig. 2. 5 suggests, Alaska with only around 700,000 total population (https://en.wikipedia.org/wiki/Alaska) has the largest wildfire in US between 1992 adn 2015. The number of wildfires for each class size per state is shown in Fig. 2. 6.

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

Comparing the plots for different states in Fig. 2. 6 shows that the number of wildfires generally decreases as the size of the fire incraeses. However, Alaska does not follow this trend and as shown in Fig. 2. 6 - 47, the number of wildfires increases as the size of fire incraeses from around 100 acres (class D) up to more than 5000 acres (class G). To further understand the wildfire occurence in different states, the fire cause in each state is investigated int he following.

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


![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Fire_Size_vs_date_1992_2000.png)

Fig. 2. 9: Size of US wildfire vs date (1992 - 2000)


![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Fire_Size_vs_date_2000_2008.png)

Fig. 2. 10: Size of US wildfire vs date (2000 - 2008)

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Fire_Size_vs_date_2008_2016.png)

Fig. 2. 11: Size of US wildfire vs date (2008 - 2016)

Data reference: Short, Karen C. 2017. Spatial wildfire occurrence data for the United States, 1992-2015 [FPA_FOD_20170508]. 4th Edition. Fort Collins, CO: Forest Service Research Data Archive. https://doi.org/10.2737/RDS-2013-0009.4

References:

Short, K. C. 2014. A spatial database of wildfires in the United States, 1992-2011. Earth System Science Data. 6:1-27. https://doi.org/10.5194/essd-6-1-2014


