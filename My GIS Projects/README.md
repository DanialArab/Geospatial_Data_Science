
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

To generate a buffer of 80 m around greenways:

        greenways_buffer = greenways.buffer(buffer_distance_degrees)
        fig, ax = plt.subplots(figsize=(12,12))
        greenways_buffer.plot(ax=ax, color='green')
        drinking_fountains.plot(ax=ax, color='blue', alpha=0.3)
        plt.show()

which returns:
![!](https://raw.githubusercontent.com/DanialArab/Geospatial_Data_Science/main/My%20GIS%20Projects/plots/80_m_buffered_greenways_plus_df.png)

Fig. 1: The buffered green pathways (with 80 m buffere distance) and the drinking fountains in Vancouver, BC

Now, I'd like to underlay the Vancouver map. For that I use **Contextily**, which is a Python library that provides a simple way to add web-based map tile layers to the geospatial visualizations and analysis. It allows to easily retrieve map tiles from various tile providers (such as OpenStreetMap, Stamen, and others) and underlay them on the spatial data:

        plot_extent = greenways_buffer.total_bounds

        fig, ax = plt.subplots(figsize=(12, 12)) 

        ax.set_xlim(plot_extent[0], plot_extent[2])
        ax.set_ylim(plot_extent[1], plot_extent[3])

        ctx.add_basemap(ax, crs=greenways_buffer.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik)

        greenways_buffer.plot(ax=ax, color='green')
        drinking_fountains.plot(ax=ax, color='blue', alpha=0.3)
        plt.show()


![](https://raw.githubusercontent.com/DanialArab/Geospatial_Data_Science/main/My%20GIS%20Projects/plots/80_m_buffered_greenways_plus_df_with_osm.png)

Fig. 2: The OpenStreetMap underlaid the spatial data of the buffered green pathways (with 80 m buffere distance) and the drinking fountains in Vancouver, BC


Now, I'd like to know the location and coordinates (longitude and latitude) of the highly accessible drinking fountains along the green pathways: these fountains are at most 80 m depart from the green pathways. To do this calculation:


        fountains_within_buffer = drinking_fountains[drinking_fountains.intersects(greenways_buffer.unary_union)]

These info is summarized as a dataframe whose screenshot of the first 15 records is depicted in the following:

![](https://raw.githubusercontent.com/DanialArab/Geospatial_Data_Science/main/My%20GIS%20Projects/plots/fountains_within_buffer_dataframe.PNG)

In total there are 111 highly accessible drinking fountains out of the 278 total fountins along the green pathways in Vancouver. 



