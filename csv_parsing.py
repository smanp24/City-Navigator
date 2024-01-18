"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a parser that reads a CSV file and creates instances
of the class City and the class Country.

@file city_country_csv_reader.py
"""
import csv
from city import City
from country import Country, add_city_to_country


def create_cities_countries_from_csv(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.

    :param path_to_csv: The path to the CSV file.
    """
    # Open csv file as file.
    with open(path_to_csv, 'r') as file:
        # Utilse DictReader to automatically create dictionaries based on the headers given in the first row of csv.
        csv_cities = csv.DictReader(file)

        # Create a new City object using the data from csv_cities.
        # Add city to country also given from the csv data.
        for row in csv_cities:
            row['city'] = City(row['city_ascii'], (float(row['lat']), float(row['lng'])), row['capital'], row['population'], row['id'])
            add_city_to_country(row['city'], row['country'], row['iso3'])


if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated_aus.csv")
    for country in Country.name_to_countries.values():
        country.print_cities()
