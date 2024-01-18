"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a function to create a path, encoded as an Itinerary, that is shortest for some Vehicle.

@file path_finding.py
"""
import math
import networkx
from city import City, get_city_by_id
from itinerary import Itinerary
from vehicles import Vehicle, create_example_vehicles
from csv_parsing import create_cities_countries_from_csv


def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Itinerary | None:
    """
    Returns a shortest path between two cities for a given vehicle as an Itinerary,
    or None if there is no path.

    :param vehicle: The vehicle to use.
    :param from_city: The departure city.
    :param to_city: The arrival city.
    :return: A shortest path from departure to arrival, or None if there is none.
    """
    # Create a graph for all the cities.
    paths = networkx.Graph()
    try:
        for city in City.id_to_cities.values():
            # Add all cities as nodes into the graph.
            paths.add_node(city)
            for other_city in City.id_to_cities.values():
                # Compute the travel time between each pair of cities stored in id_to_cities dictionary, and add an edge if possible.
                if city != other_city:
                    if vehicle.compute_travel_time(city, other_city) == math.inf:
                        continue    # Refrain from creating an edge if travel is not possible.
                    else:
                        paths.add_edge(city, other_city, weight = vehicle.compute_travel_time(city,other_city))

        # Note: Two for loops are used here, as we want to create edges from every city to every city (where possible). E.g city a to city b, city a to city c, then city b to city a etc.

        # Using networkx.shortest_path, create a list that provides the shortest path between two given cities.
        shortest_path_list = networkx.shortest_path(paths, from_city, to_city, weight = 'weight')
    except networkx.exception.NetworkXNoPath:
        shortest_path = None
        return shortest_path    # Return None if NoPath error is raised (no path is possible).

    # Create an Itinerary from the shortest path list, and return it.
    shortest_path = Itinerary(shortest_path_list)
    return (shortest_path)


if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")
    from_cities = set()
    for city_id in [1036533631, 1036142029, 1458988644]:
        from_cities.add(get_city_by_id(city_id))


    # we create some vehicles
    vehicles = create_example_vehicles()

    to_cities = set(from_cities)
    for from_city in from_cities:
        to_cities -= {from_city}
        for to_city in to_cities:
            print(f"{from_city} to {to_city}:")
            for test_vehicle in vehicles:
                shortest_path = find_shortest_path(test_vehicle, from_city, to_city)
                print(f"\t{test_vehicle.compute_itinerary_time(shortest_path)}"
                      f" hours with {test_vehicle} with path {shortest_path}.")

