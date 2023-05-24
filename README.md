# Geospatial Data Science

This repo documents my understanding of GIS and application of ML in it. The structure of the repo is as follows, and more details on each topic is presented in the files in each directory, named consistently with the first-level headings below, attached to this repo.


### 1. GIS Fundamentals
This directory contains the following Markdown files detailing my understanding of GIS theory and programming using Python, PostgreSQL, and PostGIS. 

1. GIS Basics
2. Open Source GIS Stack: Python for Geospatial, Udemy course, instructor: Arthur Lembo

### 2. My GIS Projects
This directory contains the details of the GIS project I have done so far, whcih include the jupyter notebook files containing all the Python codes and end-to-end pipelines. For my projects, I work on jupyter notebook and although I installed QGIS in my ubuntu VM to be able to play with qgis package, geopandas works fabulously in a much simpler term. It allows me to access great spatial functions and operations. A brief summary of each project along with some visualizations are presented in the following. 

#### 1. Drinking fountains distribution along green pathways in Vancouver, BC, Canada. 

In this project, I am investigating the drinking fountains accessibility (with 80 m as buffer distance) along the green pathwyas in Vancouver, BC, Canada. The shape files data were obtained from the City of Vancouver public data portal (https://opendata.vancouver.ca/pages/home/). I initially did this project in QGIS through its Python functionality but in order to provide all the details and workflows I am leveraging GeoPandas spatial functionalities (please see the jupyter notebook file named "Drinking fountains distribution - Vancouver, BC, Canada.ipynb", presented in the directory called "My GIS Projects"). 


![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/80_m_buffered_greenways_plus_df.png)
Fig. 1: The buffered green pathways (with 80 m buffere distance) and the drinking fountains in Vancouver, BC


![](https://raw.githubusercontent.com/DanialArab/Geospatial_Data_Science/main/My%20GIS%20Projects/plots/80_m_buffered_greenways_plus_df_with_osm.png)

Fig. 2: The OpenStreetMap underlaid the spatial data of the buffered green pathways (with 80 m buffere distance) and the drinking fountains in Vancouver, BC

The location and coordinates (longitude and latitude) of the highly accessible drinking fountains (the ones which are at most 80 m depart from the green pathways) along the green pathways are summarized as a dataframe whose screenshot of the first 15 records is depicted in the following:

Table 1: Location and coordinates (longitude and latitude) of the highly accessible drinking fountains (the ones which are at most 80 m depart from the green pathways) along the green pathways

![](https://raw.githubusercontent.com/DanialArab/Geospatial_Data_Science/main/My%20GIS%20Projects/plots/fountains_within_buffer_dataframe.PNG)

In total there are 111 highly accessible drinking fountains out of the 278 total fountins along the green pathways in Vancouver. 

The screenshot of the interactive map of the highly accessible drinking fountains in Vancouver is depicted in Fig. 3:

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/interactive_map_screenshot_2.png)
Fig. 3: Screenshot of the highly accessible drinking fountains along the green pathways in Vancouver, BC


The interactive map provides various features such as panning, zooming, and browsing the map. Click on the link below to access and explore the map interactively:

[Vancouver highly accessible fountains along green pathways - interactive map](https://danialarab.github.io/map/)

#### Geopandas:

GeoPandas is a Python library that extends the capabilities of the popular data manipulation library, pandas, by adding **geospatial data processing and analysis functionalities**. It builds upon other powerful geospatial libraries such as Shapely, Fiona, and pyproj to provide a convenient and efficient way to work with geospatial data in Python. Some key benefits: 

Geometric Operations: GeoPandas provides a wide range of spatial operations and transformations. It allows us to perform operations such as overlaying geometries, buffering, simplifying, and finding intersections or unions between geometries. These operations are made possible by the underlying Shapely library.

Integration with Visualization Libraries: GeoPandas seamlessly integrates with popular data visualization libraries like Matplotlib and seaborn. It provides built-in plotting functions to create maps, scatter plots, choropleth maps, and more.

The main purpose of GeoPandas is to handle two-dimensional geospatial data, which consists of geometries (points, lines, polygons) and associated attribute data. It allows us to read, write, manipulate, analyze, and visualize geospatial datasets.



