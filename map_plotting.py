"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It allows plotting an Itinerary as the picture of a map.

@file map_plotting.py
"""
from mpl_toolkits.basemap import Basemap    # have to do 'pip install basemap'
import matplotlib.pyplot as plt
from itinerary import Itinerary
from city import City


def plot_itinerary(itinerary: Itinerary, projection = 'robin', line_width=2, colour='b') -> None:
    """
    Plots an itinerary on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    The name of the file is map_city1_city2_city3_..._cityX.png.

    :param itinerary: The itinerary to plot.
    :param projection: The map projection to use.
    :param line_width: The width of the line to draw.
    :param colour: The colour of the line to draw.
    """
    # Checks if an itinerary is provided.
    if itinerary is None:
        print("Sorry. No such path exists.")
        exit()

    # Initialise the basemap so that it looks pretty.
    map = Basemap(projection=projection, lon_0=0, lat_0=0)
    map.fillcontinents(color='lightgreen', lake_color='white')
    map.drawmapboundary(fill_color='lightblue')
    map.drawcoastlines()
    map.drawcountries()

    # Obtain the longitude and latitude of each city within the itinerary.
    itinerary_lon = []
    itinerary_lat = []
    for city in itinerary.cities:
        itinerary_lon.append(city.coordinates[1])
        itinerary_lat.append(city.coordinates[0])

    # Convert the lon and lat into map coordinates.
    x, y = map(itinerary_lon, itinerary_lat)

    # Plot the itinerary on the map with provided colour and line width.
    map.plot(x, y, color=colour, linewidth=line_width)

    # Create the name of the savefile by joining the city names of the itinerary with a _ in between cities.
    city_name = []
    for city in itinerary.cities:
        city_name.append(city.name)
    name = 'map_'+'_'.join(city_name)

    # Save the file as a PNG with the created name.
    plt.savefig(f'{name}.png')


if __name__ == "__main__":
    # create some cities
    city_list = list()

    city_list.append(City("Melbourne", (-37.8136, 144.9631), "primary", 4529500, 1036533631))
    city_list.append(City("Sydney", (-33.8688, 151.2093), "primary", 4840600, 1036074917))
    city_list.append(City("Brisbane", (-27.4698, 153.0251), "primary", 2314000, 1036192929))
    city_list.append(City("Perth", (-31.9505, 115.8605), "1992000", 2039200, 1036178956))

    # plot itinerary

    plot_itinerary(Itinerary(city_list))

