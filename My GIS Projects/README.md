
# My GIS Projects

The jupyter notebook files for each projects containing all the Python scripts and end-to-end pipelines are attached to this repo and they are named consistently with the names of the projects in the following:

## 1. Drinking fountains distribution - Vancouver, BC, Canada

In this project, I am investigating the drinking fountains accessibility (with 80 m as buffer distance) along the green pathwyas in Vancouver, BC, Canada. The shape files data were obtained from the City of Vancouver public data portal (https://opendata.vancouver.ca/pages/home/). I initially did this project in QGIS through its Python functionality but in order to provide all the details and workflows I am leveraging GeoPandas spatial functionalities (please see the jupyter notebook file named "Drinking fountains distribution - Vancouver, BC, Canada.ipynb", attached to this repo). 


The followings are some notes and explanations:

First, I need to see what the coordinate reference system (CRS) of the data presented in the City of Vancouver public data portal is. I need this when buffering the pathways:


    import geopandas as gpd
    import matplotlib.pyplot as plt

    path_to_df_shape_file = 'data/1.Drinking-fountains/drinking-fountains.shp'
    path_to_df_greenways_file = 'data/2.greenways/greenways.shp'

    greenways = gpd.read_file(path_to_df_greenways_file)
    drinking_fountains = gpd.read_file(path_to_df_shape_file)

    crs_name = greenways.crs.name

    print("The CRS Name for the greenways data is:", crs_name)

which returns:

        The CRS Name for the greenways data is: WGS 84

S**ome notes on CRS:**

A CRS defines how spatial data, such as maps or geographical features, are represented on a two-dimensional surface. The CRS of "WGS 84," typically indicates that the coordinates in the shapefile are based on the World Geodetic System 1984 (WGS 84) reference ellipsoid. In this CRS, the units are indeed **in degrees for both latitude and longitude.**

So in order to be able to generate buffer around
 greenways I need to convert the desired buffer distance in meter to degrees:

        buffer_distance_meters = 80

        buffer_distance_degrees = buffer_distance_meters / (111319.9 * 1)  # Approximate conversion factor for WGS 84
        print(f"The buffer distance of 80 m is equivalent to {buffer_distance_degrees:.8f} degrees")

which returns

        The buffer distance of 80 m is equivalent to 0.00071865 degrees


