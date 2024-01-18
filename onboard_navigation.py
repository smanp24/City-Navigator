"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It puts together all parts of the assignment.

@file onboard_navigation.py
"""
from city import City
from country import find_country_of_city
from csv_parsing import create_cities_countries_from_csv
from vehicles import CrappyCrepeCar, TeleportingTarteTrolley, DiplomacyDonutDinghy, HastyHulaHorse
from path_finding import find_shortest_path
from map_plotting import plot_itinerary

# Creates vehicles that the user can choose from.
vehicles = [CrappyCrepeCar(100), DiplomacyDonutDinghy(200, 150), TeleportingTarteTrolley(3, 2000), HastyHulaHorse(10)]


def validate_input(user_input, valid_inputs, reprompt):
    """
    Validates user input is within a list of valid inputs. If not, reprompts the user until a valid input is received.

    :param user_input: Input from user.
    :param valid_inputs: The valid inputs which the user_input must be apart of.
    :param reprompt: The reprompt message to display if the user's input is invalid.
    :return: The validated user input.
    """
    # Initialises input valid variable as false until proven that input is valid.
    input_valid = False

    while input_valid is False:
        try:
            # Raises a ValueError (causing except code to run) if the user input is not in the valid inputs.
            if user_input not in valid_inputs:
                raise ValueError
            input_valid = True # Stops the while loop when a valid user input is given.
        except ValueError:
            print(reprompt)
            user_input = (input("Your input: "))
    return user_input


def main_menu():
    user_input = (input('''-----------------------------------------------------------------------------
Welcome to your personalised Navigation system.
Here you may plan your journey from one city to another with a given vehicle,
and we'll show you the most optimal way to get there (if it exists).
Choose one of the following:
1 - Start planning your journey
2 - Get more information on the different vehicles available
3 - Exit the program
Your input: '''))
    # Validates user input to ensure it is one of the given choices.
    user_input = validate_input(user_input, ['1','2','3'], "That is not a valid input. Please try again!")
    if user_input == '1':
        journey_plan()
    elif user_input == '2':
        vehicle_info()
    elif user_input == '3':
        exit()


def vehicle_info():
    user_input = input(('''
You have a choice of 4 vehicles, all of which have special conditions that they follow:

- CrappyCrepeCar - While slow, this vehicle can travel from any given city to another at a speed of 100 km/h.
- DiplomacyDonutDinghy - Can travel between any two cities in the same country at a speed of 200 km/h, and can travel between any two cities in other countries at a speed of 150 km/h,if they are both capitals.  
- TeleportingTarteTrolley - Can travel between any two cities in exactly 3 hours, but can only do so if the cities are less than 2000 km apart.
- HastyHulaHorse - An eco-friendly option that can travel between any two cities at a speed of 10 km/h, given they are within the same country.

Choose one of the following:
1 - Start planning your journey
2 - Go back to main menu
3 - Exit the program

Your input: '''))
    # Validates user input to ensure it is one of the given choices.
    user_input = validate_input(user_input, ['1','2','3'], "That is not a valid input. Please try again!")
    if user_input == '1':
        journey_plan()
    elif user_input == '2':
        main_menu()
    elif user_input == '3':
        exit()


def journey_plan():
    # Prompts the user for a starting city, and validates the input.
    starting_city = input('''Great! To get started, type in your starting city name.
Your response: ''')

    # Checks if the city exists, and if there are multiple cities with the given name (If so, prompts user to pick which one).
    starting_city = city_check(starting_city)
    starting_city = multiple_city_check(starting_city)

    # Prompts the user for an ending city, and validates the input.
    ending_city = input('''Now type in the city you would like to go to.
Your response: ''')

    # Checks if the city exists, and if there are multiple cities with the given name (If so, prompts user to pick which one).
    ending_city = city_check(ending_city)
    ending_city = multiple_city_check(ending_city)

    # Prompts user to pick a vehicle
    vehicle_input = int(journey_vehicle())

    # Finds shortest distance between two cities with given vehicle using find_shortest_path, and plots and saves a PNG of the map of the journey.
    shortest_itinerary = find_shortest_path(vehicles[vehicle_input - 1], starting_city, ending_city)
    plot_itinerary(shortest_itinerary)


# This function ensures that city exists within name_to_cities, and otherwise reprompts the user for a valid city.
def city_check(city):
    try:
        city = validate_input(city, City.name_to_cities[city][0].name, "That city doesn't exist, try again.")
        return city

    # When the city does not exist, a KeyError is raised, and in this case, a recursive call on city_check is done until user input is a valid city.
    except KeyError:
        print("That city doesn't exist, try again")
        city = input("Your input: ")
        return city_check(city)


# This function checks whether there are multiple cities with the inputted name, and asks user to pick which city they wanted.
def multiple_city_check(city):
    # Initialises city_number as a variable.
    city_number = 0

    # Checks whether there are multiple cities with the same name.
    if len(City.name_to_cities[city]) > 1:
        print('''
There seems to be more than 1 city with that name.
Which one is the one you were trying to pick:''')

        # Prints the cities, along with a number accompanying them, as well as their country and ID.
        for city_index in range(len(City.name_to_cities[city])):
            origin_country = find_country_of_city(City.name_to_cities[city][city_index]).name
            print(f"{city_index + 1} : {City.name_to_cities[city][city_index].name} located in {origin_country}, with City ID {City.name_to_cities[city][city_index].city_id}")

        # Prompts the user to choose one of the cities.
        city_number = int(input(("Your input: "))) - 1

    # Returns the city that corresponds to the chosen city_number, if only one city exists, then the first city ([0]) is chosen.
    return (City.name_to_cities[city][city_number])


# This function asks the user to pick the vehicle they would like to use.
def journey_vehicle():
    print('''
1 - CrappyCrepeCar - Speed 100 km/h, can travel to any city.
2 - DiplomacyDonutDinghy - Speed 200 km/h between cities in same country, 150 km/h between cities that are capitals of two different countries.
3 - TeleportingTarteTrolley - 3 hour trip, given cities are less than 2000 km apart.
4 - HastyHulaHorse - Speed 10 km/h - Can only travel between two cities within the same country.
''')

    # Asks and validates user input for vehicle choice.
    vehicle_input = input("Your choice: ")
    vehicle = validate_input(vehicle_input, ['1','2','3','4'], "That is not a valid input. Please try again!")
    return vehicle


create_cities_countries_from_csv('worldcities_truncated.csv')
main_menu()

