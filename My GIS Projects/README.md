
# My GIS Projects

The jupyter notebook files for each projects containing all the Python scripts and end-to-end pipelines are attached to this repo and they are named consistently with the names of the projects in the following:

## 1. Drinking fountains distribution - Vancouver, BC, Canada

In this project, I am investigating the drinking fountains accessibility along the green pathwyas in Vancouver, BC, Canada. The shape files data were obtained from the City of Vancouver public data portal (https://opendata.vancouver.ca/pages/home/). I initially did this project in QGIS through its Python functionality and here I am leveraging GeoPandas spatial functionalities. ALl the Python scripts are atatched as the jupyter notebook file names "Drinking fountains distribution - Vancouver, BC, Canada.ipynb". The followings are some notes and explanations:




ChatGPT
Yes, when the CRS name is "WGS 84," it typically indicates that the coordinates in the shapefile are based on the World Geodetic System 1984 (WGS 84) reference ellipsoid. In this CRS, the units are indeed in degrees for both latitude and longitude.

WGS 84 is a widely used geographic coordinate system and is often used as the default CRS for global or worldwide datasets. It provides a consistent and standardized way to represent locations on the Earth's surface using latitude and longitude measurements.

Therefore, if your shapefile has a CRS name of "WGS 84," you can assume that the units are in degrees for both the X (longitude) and Y (latitude) coordinates.
