
# My GIS Projects

The jupyter notebook files for each projects containing all the Python scripts and end-to-end pipelines are attached to this repo and they are named consistently with the names of the projects in the following:

## 1. Drinking fountains distribution along green pathways in Vancouver, BC, Canada.

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
![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/80_m_buffered_greenways_plus_df.png)
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

Table 1: Location and coordinates (longitude and latitude) of the highly accessible drinking fountains (the ones which are at most 80 m depart from the green pathways) along the green pathways

![](https://raw.githubusercontent.com/DanialArab/Geospatial_Data_Science/main/My%20GIS%20Projects/plots/fountains_within_buffer_dataframe.PNG)

In total there are 111 highly accessible drinking fountains out of the 278 total fountins along the green pathways in Vancouver. 

Now I'd like to use this info to generate an interactive map of the highly accessible drinking fountains in Vancouver. I use **folium** library:

    import folium
    m = folium.Map(location = [df.Latitude.mean(), df.Longitude.mean()], zoom_start = 12)

    for i in range(0, len(df)):
        folium.Marker([df.iloc[i]['Latitude'], df.iloc[i]['Longitude']], popup = df.iloc[i]['name']).add_to(m)


    # Convert the buffered pathways to GeoJSON format
    buffered_pathways_geojson = greenways_buffer.__geo_interface__

    # Create a GeoJson layer for the buffered pathways
    buffered_pathways_layer = GeoJson(buffered_pathways_geojson, name='Buffered Pathways')

    # Define the style function to adjust the color
    def style_function(feature):
        return {
            'fillColor': 'green',  # Specify the desired color
            'color': 'green',      # Specify the border color
            'weight': 2,           # Specify the border width
            'fillOpacity': 0.5     # Specify the fill opacity
        }

    # Create a GeoJson layer for the buffered pathways with the defined style
    buffered_pathways_layer = GeoJson(
        buffered_pathways_geojson,
        name='Buffered Pathways',
        style_function=style_function
    )

    # Add the buffered pathways layer to the map
    buffered_pathways_layer.add_to(m)

    m.save('plots/interactive_map.html')

The screenshot of the interactive map is presented Fig. 3:

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/interactive_map_screenshot_2.png)

Fig. 3: Screenshot of the highly accessible drinking fountains along the green pathways in Vancouver, BC 

To generate the heatmap:

        import folium
        from folium import plugins

        locations = df
        # Calculate the mean latitude and longitude
        center_lat = locations['Latitude'].mean()
        center_lon = locations['Longitude'].mean()

        # Create a map object
        map_heatmap = folium.Map(location=[center_lat, center_lon], zoom_start=12)

        # Create a HeatMap object
        heat_data = locations[['Latitude', 'Longitude']].values.tolist()
        heatmap = plugins.HeatMap(heat_data)

        # Add HeatMap layer to the map
        map_heatmap.add_child(heatmap)

        # Display the map
        map_heatmap

which returns: 

![](https://github.com/DanialArab/Geospatial_Data_Science/blob/main/My%20GIS%20Projects/plots/heatmap_screenshot.png)
Fig. 4: Heatmap of the highly accessible drinking fountains along the green pathways in Vancouver, BC 

The interactive map provides various features such as panning, zooming, and browsing the map. Click on the link below to access and explore the map interactively:

[Vancouver highly accessible fountains along green pathways - interactive map](https://danialarab.github.io/interactive_map_drinking_fountain_Vancouver/)

## 2. Exploratory Data Analysis on US Wildfires 

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

+ The followings are useful attributes on which I will be focusing:

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
|-105.720555560000...|33.44083333000000...|0.100000000000000000|              A|
+--------------------+--------------------+--------------------+---------------+
only showing top 20 rows

+-----+--------------------+--------------------+--------------------+----------------+
|STATE|           FIRE_YEAR|       DISCOVERY_DOY|            CONT_DOY|STAT_CAUSE_DESCR|
+-----+--------------------+--------------------+--------------------+----------------+
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
+-----+--------------------+--------------------+--------------------+----------------+
only showing top 20 rows



Data reference: Short, Karen C. 2017. Spatial wildfire occurrence data for the United States, 1992-2015 [FPA_FOD_20170508]. 4th Edition. Fort Collins, CO: Forest Service Research Data Archive. https://doi.org/10.2737/RDS-2013-0009.4




