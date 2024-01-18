"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the class Itinerary.

@file itinerary.py
"""
import math
from city import City, create_example_cities, get_cities_by_name


class Itinerary():
    """
    A sequence of cities.
    """

    def __init__(self, cities: list[City]) -> None:
        """
        Creates an itinerary with the provided sequence of cities,
        conserving order.
        :param cities: a sequence of cities, possibly empty.
        :return: None
        """
        # Initialise instance variables.
        self.cities = cities

    def total_distance(self) -> int:
        """
        Returns the total distance (in km) of the itinerary, which is
        the sum of the distances between successive cities.
        :return: the total distance.
        """
        # Initialise a distance variable to represent total distance.
        distance = 0

        # Loop through cities within the itinerary, add distance between them(using distance method from City) to distance variable.
        for city in range(len(self.cities)-1):
            distance += City.distance(self.cities[city], self.cities[city+1])
        return distance

    def append_city(self, city: City) -> None:
        """
        Adds a city at the end of the sequence of cities to visit.
        :param city: the city to append
        :return: None.
        """
        self.cities.append(city)

    def min_distance_insert_city(self, city: City) -> None:
        """
        Inserts a city in the itinerary so that the resulting
        total distance of the itinerary is minimised.
        :param city: the city to insert
        :return: None.
        """
        # Initialise two variables for best distance and best itinerary
        best_distance = math.inf    # Set to infinity, as ideally best distance (found later) will be shortest distance.
        best_itinerary = 0

        # Loop over all possible positions that the city can be inserted into the itinerary.
        for insert_position in range(len(self.cities)+1):

            # Create a new itinerary by inserting city into the current position.
            # Compute total distance of this itinerary 
            new_itinerary = self.cities[:insert_position] + [city] + self.cities[insert_position:]
            new_distance = Itinerary(new_itinerary).total_distance()

            # If new itinerary has a shorter total distance, make it the new best_itinerary
            if new_distance < best_distance:
                best_distance = new_distance
                best_itinerary = new_itinerary

        # Update the intinerary to follow the order of best itinerary.
        self.cities = best_itinerary

    def __str__(self) -> str:
        """
        Returns the sequence of cities and the distance in parentheses
        For example, "Melbourne -> Kuala Lumpur (6368 km)"

        :return: a string representing the itinerary.
        """
        # Create a list of city names and append all city name's in the itinerary to it.
        city_names = []
        for city in self.cities:
            city_names.append(city.name)

        # Create a string including all city names seperated by ' -> '
        cities_name = ' -> '.join(city_names)
        return(f"{cities_name} ({self.total_distance()} km)")


if __name__ == "__main__":
    create_example_cities()
    test_itin = Itinerary([get_cities_by_name("Melbourne")[0],get_cities_by_name("Kuala Lumpur")[0]])
    print(test_itin)

    #we try adding a city
    test_itin.append_city(get_cities_by_name("Baoding")[0])
    print(test_itin)

    #we try inserting a city
    test_itin.min_distance_insert_city(get_cities_by_name("Sydney")[0])
    print(test_itin)

    #we try inserting another city
    test_itin.min_distance_insert_city(get_cities_by_name("Canberra")[0])
    print(test_itin) 
