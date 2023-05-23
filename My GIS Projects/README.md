
# My GIS Projects

The jupyter notebook files for each projects containing all the Python scripts and end-to-end pipelines are attached to this repo and they are named consistently with the names of the projects in the following:

## 1. Drinking fountains distribution - Vancouver, BC, Canada

In this project, I am investigating the drinking fountains accessibility along the green pathwyas in Vancouver, BC, Canada. The shape files data were obtained from the City of Vancouver public data portal (https://opendata.vancouver.ca/pages/home/). I initially did this project in QGIS through its Python functionality but in order to provide all the details and workflows I am leveraging GeoPandas spatial functionalities (please see the jupyter notebook file named "Drinking fountains distribution - Vancouver, BC, Canada.ipynb", attached to this repo). 

The followings are some notes and explanations:

The coordinate reference system (CRS) of the data presented in the City of Vancouver public data portal is 

    import geopandas as gpd
    import matplotlib.pyplot as plt

    path_to_df_shape_file = 'data/1.Drinking-fountains/drinking-fountains.shp'
    path_to_df_greenways_file = 'data/2.greenways/greenways.shp'

    greenways = gpd.read_file(path_to_df_greenways_file)
    drinking_fountains = gpd.read_file(path_to_df_shape_file)

    crs_name = greenways.crs.name

    print("The CRS Name for the greenways data is:", crs_name)



A CRS defines how spatial data, such as maps or geographical features, are represented on a two-dimensional surface. The crs.name property retrieves the name of the CRS associated with the "greenways" data.


ChatGPT
Yes, when the CRS name is "WGS 84," it typically indicates that the coordinates in the shapefile are based on the World Geodetic System 1984 (WGS 84) reference ellipsoid. In this CRS, the units are indeed in degrees for both latitude and longitude.

WGS 84 is a widely used geographic coordinate system and is often used as the default CRS for global or worldwide datasets. It provides a consistent and standardized way to represent locations on the Earth's surface using latitude and longitude measurements.

Therefore, if your shapefile has a CRS name of "WGS 84," you can assume that the units are in degrees for both the X (longitude) and Y (latitude) coordinates.
