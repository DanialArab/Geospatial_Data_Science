# Geospatial Data Science

This repo documents my understanding of GIS and Geospatial Data Science. The structure of the repo is as follows, and more details on each topic are presented in the files in each directory, named consistently with the first-level headings below, attached to this repo.


### 1. GIS Fundamentals
This directory contains the following Markdown files detailing my understanding of GIS theory and programming using Geospatial Python libraries (GeoPandas, Shapely, Rasterio, GDAL, etc.), PostgreSQL, and PostGIS. 

1. GIS Basics
2. Open Source GIS Stack: Python for Geospatial, Udemy course, instructor: Arthur Lembo

### 2. My GIS Projects
This directory contains the details of the GIS project I have done so far, which include the Jupyter Notebook files containing all the Python codes and end-to-end pipelines. For my projects, I work on Jupyter Notebook using GeoPandas to more interactively experiment what I have done using QGIS installed in my Ubuntu VM. This allows me to access great spatial functions and operations in Python. A brief high-level overview/summary of each project along with some visualizations are presented in the following (please find more details in the **My GIS Projects** directory of this repo):

#### 1. Drinking fountains distribution along green pathways in Vancouver, BC, Canada. 

In this project, I am investigating the drinking fountains' accessibility (with 80 m as a buffer distance) along the green pathways in Vancouver, BC, Canada. The shape files were obtained from the City of Vancouver public data portal (https://opendata.vancouver.ca/pages/home/). I initially did this project in QGIS through its Python functionality but in order to provide all the details and workflows I am leveraging GeoPandas spatial functionalities in Jupyter Notebook (please see [the link to the Jupyter Notebook file](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/1.%20Drinking%20fountains%20distribution%20in%20Vancouver%2C%20BC/Drinking%20fountains%20distribution%20-%20Vancouver%2C%20BC%2C%20Canada.ipynb)). 


In total, there are 111 highly accessible drinking fountains out of the 278 total fountains along the green pathways in Vancouver. Click on the link below to access and explore the interactive map, which provides various features such as panning, zooming, and browsing the map:

[Vancouver highly accessible fountains along green pathways - interactive map](https://danialarab.github.io/interactive_map_drinking_fountain_Vancouver/)

The screenshot of the interactive map and heatmap of the highly accessible drinking fountains in Vancouver are depicted in Fig. 1. A and 1. B, respectively:

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/interactive_map_screenshot_2.png)
Fig. 1. A: Screenshot of the highly accessible drinking fountains along the green pathways in Vancouver, BC


![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/heatmap_screenshot.png)
Fig. 1. B: Heatmap of the highly accessible drinking fountains along the green pathways in Vancouver, BC 

#### 2. Exploratory Data Analysis on US Wildfires 

<a href="https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/2.%20Exploratory%20Data%20Analysis%20on%20US%20Wildfires/EDA%20on%201.88%20Million%20US%20Wildfires.ipynb" target="_blank" rel="noopener">EDA on 1.88 Million US Wildfires</a>. 

In this project, I used Spark to perform exploratory data analysis on the Sqlite data of 1.88 Million US Wildfires (<a href="https://www.kaggle.com/datasets/rtatman/188-million-us-wildfires/" target="_blank" rel="noopener">link to the Kaggle data source</a>). My primary goal was to explore the data and find out any potential room for the application of Machine Learning to see if I can predict the cause, location, or size of the fire. Founded upon this exploratory data analysis, I tested different ML ideas in a separate project named "3. Fire Predictor" (<a href="https://github.com/DanialArab/Geospatial_Data_Science/tree/main/My%20GIS%20Projects/3.%20Fire%20Predictor/" target="_blank" rel="noopener">link to its repo</a>). The followings are some brief visualizations, for more detailed results please visit <a href="https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/2.%20Exploratory%20Data%20Analysis%20on%20US%20Wildfires/README.md" target="_blank" rel="noopener">Exploratory Data Analysis on US Wildfires</a>.


|**(1)**|**(2)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Wildfire_counts_per_US_state_sorted.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Average_duration_of_wildfires_in_US_1992_to_2015.png)|

Fig. 2. A: 1) The US Wildfire counts per state, 2) Average duration of US wildfires per state (1992 - 2015) 


|**(1)**|**(2)** | 
| -- | --|
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_67975_Wildfires_in_US_1992.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_61450_Wildfires_in_US_1997.png)|


|**(3)**|**(4)** | 
| -- | --| 
|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_114004_Wildfires_in_US_2006.png)|![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/Total_74491_Wildfires_in_US_2015.png)|

Fig. 2. B: Locations of US Wildfires across all states in 1) 1992, 2) 1997, 3) 2006, and 4) 2015 

Based on this exploratory data analysis, we can make the following conclusions about the US wildfires that happened between 1992 and 2015:

+ The states California, Georgia, and Texas had the most counts of wildfires.
+ The states Alaska, Idaho, and California had the largest average fire size.
+ US experienced the minimum and maximum number of wildfires in 1997 and 2006, with total counts of 61,450 and 114,004, respectively. 
+ Although there is no clear correlation between the number of US wildfires with time, the size of fires generally tends to increase.
+ This analysis allows us to locate the wildfires within each state. For example, the east of Texas consistently experienced wildfire since 1992 and the wildfire center was shifted towards the Texas center in 2005 and the fire was propagated towards the north around 2011. This type of detail may provide the decision-makers with useful insights to better manage wildfires.
+ It is observed that the number of wildfires generally decreases as the size of the fire increases. However, the followings are some interesting observations:
    + Alaska does not follow this trend: the number of wildfires in Alaska increases as the size of the fire increases from around 100 acres (class D) up to more than 5,000 acres (class G).
    + The states of DC, RI, NH, and VT only experienced small fires within classes A, B, C, or D. 
+ It is observed that human activities such as **Debris Burning** and **Arson** play a crucial role as the main causes behind the US wildfires. To be able to provide a standardized way to classify and track the causes of wildfires per state the percentage of each cause per total number of wildfires per state is calculated. These details can be helpful to agencies and organizations to analyze trends, develop prevention strategies, and allocate resources.
+ A clear cyclic trend in the size and counts of fire per season was observed, which peaks between June to August across the country. This is correlated with the main cause of the fire, which makes this conclusion state-dependent. 
+ Combining the insights obtained from the wildfires size distribution vs. time and the wildfire count distribution per cause of fire within each state provides a coherent conclusion: the larger the weight of nature to cause the wildfire the more chance to shift the peak of fire size towards the hottest months i.e., June, July, and August. This is clearly observed in the state of Alaska where the main cause of fire is lightning (with more than 30%) with the largest size of fires in the hottest months of the year i.e., June and July. On the other hand, in the state of Texas where the first three most frequent causes of wildfires are due to human activities (Debris Burning, Equipment Use, and Arson) March and April are the months with the largest fires. The hottest months in Texas are reported to be July and August (<a href="https://spectrumlocalnews.com/tx/austin/weather/2022/06/30/the-hottest-part-of-the-year-across-texas#:~:text=The%20warmest%20month%20of%20the%20year%20is%20also%20August%2C%20with,daily%20high%20temperature%20of%2097" target="_blank" rel="noopener">reference</a>), which supports this argument.
+ The data contain the date of fire discovery and also the contained date, the date when the fire was reported to be under control. This data was used to calculate the fire duration per state, per month, and per fire class size. The following insights can potentially reveal the capability of each state to deal with wildfire and suggest practical strategies:
    + Hawaii had the largest fire duration, followed by Alaska and New Jersey. The partial explanation for the largest duration of wildfires in Hawaii and Alaska could be their remote location and difficult accessibility. 
    + The hottest months of June, July, and August had the largest wildfire duration of around 2 days. 
    + There is a clear, meaningful, and understandable trend in the average duration of wildfire across the country per each fire size class: the larger the size of the fire the harder to control it and so the larger the duration of wildfires.

+ Based on the aforementioned analysis, the following <a href="https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/3.%20Fire%20Predictor/README.md" target="_blank" rel="noopener">ML ideas</a> have been investigated:
    + Given the state, county, cause, and date of the fire, is it possible to predict the fire size class (classes A to G)? (the problem is classification)
    + Given the state, county, cause, and date of the fire, is it possible to predict the fire size in acres? (the problem is regression)
    + Given the time, location, and size of the fire, is it possible to predict the cause of the fire? is it a function of seasons? (the problem is classification)



