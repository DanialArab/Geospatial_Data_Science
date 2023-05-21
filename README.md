# Geospatial Data Science

This repo documents my understanding of GIS and application of ML in it. The structure of the repo is as follows, and more details on each topic is presented in the Markdown files, named consistently with the first-level headings below, attached to this repo.


### 1. GIS Fundamentals
This directory contains the following Markdown files detailing my understanding of GIS theory and programming using Python, PostgreSQL, and PostGIS. 

1. GIS Basics
2. Open Source GIS Stack: Python for Geospatial, Udemy course, instructor: Arthur Lembo

### 2. My GIS Projects
This directory contains the details of the GIS project I have done so far, whcih include the jupyter notebook files containing all the Python codes and end-to-end pipelines. For my projects, I work on jupyter notebook and although I installed QGIS in my ubuntu VM to be able to play with qgis package, geopandas works fabulously in a much simpler term. It allows me to access great spatial functions and operations. A brief summary of each project along with some visualizations are presented in the following. 

#### 1. Drinking fountains distribution along greenways and bikeways in Vancouver, BC, Canada. 

buffer distance = 80 m
df = drinking fountain
![](https://github.com/DanialArab/images/blob/main/GIS/1.PNG)

![](https://github.com/DanialArab/images/blob/main/GIS/2.PNG)

![](https://github.com/DanialArab/images/blob/main/GIS/3.PNG)


#### Geopandas:

GeoPandas is a Python library that extends the capabilities of the popular data manipulation library, pandas, by adding **geospatial data processing and analysis functionalities**. It builds upon other powerful geospatial libraries such as Shapely, Fiona, and pyproj to provide a convenient and efficient way to work with geospatial data in Python. Some key benefits: 

Geometric Operations: GeoPandas provides a wide range of spatial operations and transformations. It allows us to perform operations such as overlaying geometries, buffering, simplifying, and finding intersections or unions between geometries. These operations are made possible by the underlying Shapely library.

Integration with Visualization Libraries: GeoPandas seamlessly integrates with popular data visualization libraries like Matplotlib and seaborn. It provides built-in plotting functions to create maps, scatter plots, choropleth maps, and more.

The main purpose of GeoPandas is to handle two-dimensional geospatial data, which consists of geometries (points, lines, polygons) and associated attribute data. It allows us to read, write, manipulate, analyze, and visualize geospatial datasets.



