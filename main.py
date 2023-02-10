import random

def select_random_from_list(list):
    return list[random(0, len(list) - 1)]

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

def get_entertainment_list():
    list = []
    list.append("Magic Show")
    list.append("Movie")
    list.append("Live Show")
    list.append("Concert")
    list.append("Football Game")


destinations = get_destinations_list()
restaurants = get_restaurants_list()
transporation_modes = get_transportation_modes_list()
entertainments = get_entertainment_list()

