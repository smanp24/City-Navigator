"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the class Country.

@file country.py
"""
from tabulate import tabulate
from city import City, create_example_cities


class Country():
    """
    Represents a country.
    """
    name_to_countries = dict() # a dict that associates country names to instances.

    city_names = []

    def __init__(self, name: str, iso3: str) -> None:
        """
        Creates an instance with a country name and a country ISO code with 3 characters.

        :param country_name: The name of the country
        :param country_iso3: The unique 3-letter identifier of this country
        :return: None
        """
        self.name = name
        self.iso3 = iso3
        cities = []
        self.cities = cities
        Country.name_to_countries[self.name] = self

    def add_city(self, city: City) -> None:
        """
        Adds a city to the country.

        :param city: The city to add to this country
        :return: None
        """
        self.cities.append(city)
        self.city_names.append(city.name)

    def get_cities(self, city_type: list[str] = None) -> list[City]:
        """
        Returns a list of cities of this country.

        The argument city_type can be given to specify a subset of
        the city types that must be returned.
        Cities that do not correspond to these city types are not returned.
        If None is given, all cities are returned.

        :param city_type: None, or a list of strings, each of which describes the type of city.
        :return: a list of cities in this country that have the specified city types.
        """
        if city_type is None:
            return self.cities
        else:
            city_list = []
            for instance in self.cities:
                if instance.city_type == city_type:
                    city_list.append(instance)
            return city_list

    def print_cities(self) -> None:
        """
        Prints a table of the cities in the country, from most populous at the top
        to least populous. Use the tabulate module to print the table, with row headers:
        "Order", "Name", "Coordinates", "City type", "Population", "City ID".
        Order should start at 0 for the most populous city, and increase by 1 for each city.
        """
        table =[]
        i = 1
        headers = ["Order","Name","Coordinates","City type", "Population", "City ID"]
        for instance in self.cities:
            table.append([i, instance.name,instance.coordinates, instance.city_type, instance.population, instance.city_id])
            i += 1

        sorted_table = (sorted(table, key=lambda x:x[4], reverse=True))
        
        sorted_number = 0

        for row in range(len(sorted_table)):
            sorted_table[row][0] = sorted_number
            sorted_number += 1
        
        print(tabulate(sorted_table, headers))

    def __str__(self) -> str:
        """
        Returns the name of the country.
        """
        return (f"{self.name}")


def add_city_to_country(city: City, country_name: str, country_iso3: str) -> None:
    """
    Adds a City to a country.
    If the country does not exist, create it.

    :param country_name: The name of the country
    :param country_iso3: The unique 3-letter identifier of this country
    :return: None
    """
    for instance in Country.name_to_countries:
        if country_name == Country.name_to_countries[instance].name and country_iso3 == Country.name_to_countries[instance].iso3:
            Country.add_city(Country.name_to_countries[instance], city)
            return 0

    Country(country_name, country_iso3)
    Country.add_city(Country.name_to_countries[country_name], city)


def find_country_of_city(city: City) -> Country:
    """
    Returns the Country this city belongs to.
    We assume there is exactly one country containing this city.

    :param city: The city.
    :return: The country where the city is.
    """
    for instance in Country.name_to_countries:
        if city in Country.name_to_countries[instance].cities:
            return Country.name_to_countries[instance]


def create_example_countries() -> None:
    """
    Creates a few countries for testing purposes.
    Adds some cities to it.
    """
    create_example_cities()
    malaysia = Country("Malaysia", "MAS")
    kuala_lumpur = City.name_to_cities["Kuala Lumpur"][0]
    malaysia.add_city(kuala_lumpur)
    add_city_to_country(kuala_lumpur, 'Malaysia', 'YES')
    print(Country.name_to_countries['Malaysia'].city_names)

    for city_name in ["Melbourne", "Canberra", "Sydney"]:
        add_city_to_country(City.name_to_cities[city_name][0], "Australia", "AUS")

def test_example_countries() -> None:
    """
    Assuming the correct countries have been created, runs a small test.
    """
    Country.name_to_countries["Australia"].print_cities()


if __name__ == "__main__":
    #create_example_countries()
    create_example_cities()
    australia = Country("Australia", "AUS")
    melbourne = City('Melbourne', (-37.8136, 144.9631), 'primary', 1000000, 1)
    sydney = City('Sydney', (-33.8688, 151.2093), 'admin', 500000, 2)
    brisbane = City('Brisbane', (-27.4698, 153.0251), 'minor', 200000, 3)
    australia.add_city(sydney)
    australia.add_city(melbourne)
    australia.add_city(brisbane)
    australia.print_cities()


    #test_example_countries()

