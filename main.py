import random

#Return an item from a supplied list at random
def select_random_from_list(list):
    return list[random.randint(0, len(list) - 1)]

#Returns a list of predefined desinationa
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

#Returns a list of predefined restaurants
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

#Returns a list of predefined transportation modes
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

#Returns a list of predefined types of entertainment 
def get_entertainment_list():
    list = []
    list.append("Magic Show")
    list.append("Movie")
    list.append("Live Show")
    list.append("Concert")
    list.append("Football Game")
    return list

def print_selections(destination, restaurant, transportation_mode, entertainment):
    print(f"Desitnation: {destination}")
    print(f"Restaurant: {restaurant}")
    print(f"Entertainment: {entertainment}")
    print(f"Transportation: {transportation_mode}")

#Begin main program execution
destinations = get_destinations_list()
restaurants = get_restaurants_list()
transporation_modes = get_transportation_modes_list()
entertainments = get_entertainment_list()

satisfied_with_selections = False
while(not satisfied_with_selections):
    destination = select_random_from_list(destinations)
    restaurant = select_random_from_list(restaurants)
    transportation_mode = select_random_from_list(transporation_modes)
    entertainment = select_random_from_list(entertainments)

    print_selections(destination, restaurant, transportation_mode, entertainment)
    selection = input("Are you satisfied with your trip? Y or N: ") #Assuming nother other than Y or N will be entered
    if selection == "Y":
        satisfied_with_selections = True
