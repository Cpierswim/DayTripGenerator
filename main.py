import random

# Returns and deletes item from a supplied list at random
#   -if there is only 1 item left, it does not delete the item, it picks that one
def select_random_from_list(list_to_pick_from):
    if len(list_to_pick_from) > 1:
        index = random.randint(0, len(list_to_pick_from) - 1)
        list_element = list_to_pick_from[index]
        list_to_pick_from.pop(index)
        return list_element
    else:
        return list_to_pick_from[0]

# Returns a list of predefined desinations
def get_destinations_list():
    list = []
    list.append("Perth, WA")
    list.append("Sandusky, OH")
    list.append("Atlanta, GA")
    list.append("New York, NY")
    list.append("London, ENG")
    list.append("London, CAN")
    list.append("San Diego, CA")
    list.append("Omaha, NE")
    list.append("San Franciso, CA")
    return list

# Returns a list of predefined restaurants
def get_restaurants_list():
    list = []
    list.append("Gino's  Pizza")
    list.append("McDonald's")
    list.append("Mancy's Steakhouse")
    list.append("Little Tokyo Sushi")
    list.append("Norifish")
    list.append("Empire State South")
    list.append("Southern Kitchen & Grille")
    list.append("Okiboru Tsukemen & Ramen")
    return list

# Returns a list of predefined transportation modes
def get_transportation_modes_list():
    list = []
    list.append("Car")
    list.append("Truck")
    list.append("Yacht")
    list.append("Bus")
    list.append("Plane")
    list.append("Cruise")
    list.append("Bicycle")
    list.append("Rickshaw")
    return list

# Returns a list of predefined types of entertainment
def get_entertainment_list():
    list = []
    list.append("Magic Show")
    list.append("Movie")
    list.append("Live Show")
    list.append("Concert")
    list.append("Football Game")
    return list

#Formats and prints the selections made
def print_selections(destination, restaurant, transportation_mode, entertainment):
    print(f"Desitnation: {destination}")
    print(f"Restaurant: {restaurant}")
    print(f"Entertainment: {entertainment}")
    print(f"Transportation: {transportation_mode}")

#Determines if there is only 1 option to pick from and displays a message if there is
def determine_if_no_more_options(list_to_check, option_string):
    if len(list_to_check) == 1:
        print(f"There are no more {option_string}s left to pick from. The the options will start over.")
        return True
    else:
        return False

#Get the selections that the user wants
#  - supply the lists to pick from and references to where to put the selections
def get_desired_selections(destinations_list, restaurant_list, transportation_mode_list, entertainment_list):
    satisfied_with_selections = False

    desired_destination = select_random_from_list(destinations_list)
    desired_restaurant = select_random_from_list(restaurant_list)
    desired_transportation_mode = select_random_from_list(transportation_mode_list)
    desired_entertainment = select_random_from_list(entertainment_list)
    while (not satisfied_with_selections):

        print_selections(desired_destination, desired_restaurant, desired_transportation_mode, desired_entertainment)
        selection = input("Are you satisfied with your trip? Y or N: ")
        if selection == "Y":
            satisfied_with_selections = True
        elif selection == "N":
            selection = input("Which option would you like to change? Destination, Restaurant, Entertainment, Transportation: ")
            if "Destination" in selection:
                desired_destination = select_random_from_list(destinations_list)
                if(determine_if_no_more_options(destinations_list, selection)):
                    destinations_list = get_destinations_list()
            elif "Restaurant" in selection:
                desired_restaurant = select_random_from_list(restaurant_list)
                if(determine_if_no_more_options(restaurant_list, selection)):
                    restaurant_list = get_restaurants_list()
            elif "Entertainment" in selection:
                desired_entertainment = select_random_from_list(entertainment_list)
                if(determine_if_no_more_options(entertainment_list, selection)):
                    entertainment_list = get_entertainment_list()
            elif "Transportation" in selection:
                desired_transportation_mode = select_random_from_list(transportation_mode_list)
                if(determine_if_no_more_options(transportation_mode_list, selection)):
                    transportation_mode_list = get_transportation_modes_list()
            else:
                print("Input misunderstood")
        else:
            print("Input misunderstood")

    print_final_selctions(desired_destination, desired_restaurant, desired_transportation_mode, desired_entertainment)

# Print the final selection message
def print_final_selctions(destination, restaurant, transportation_mode, entertainment):
    print("")
    print("Here is your final trip!")
    print_selections(destination, restaurant, transportation_mode, entertainment)

# Begin main program execution
destinations = get_destinations_list()
restaurants = get_restaurants_list()
transporation_modes = get_transportation_modes_list()
entertainments = get_entertainment_list()

get_desired_selections(destinations, restaurants, transporation_modes, entertainments)

