from random import random, randint, choice

def all_fruits():
    fruits = [
        "Ackee",
        "Apple",
        "Apricot",
        "Avocado",
        "Açaí",
        "Banana",
        "Bell pepper",
        "Bilberry",
        "Black sapote",
        "Blackberry",
        "Blackcurrant",
        "Blood orange",
        "Blueberry",
        "Boysenberry",
        "Breadfruit",
        "Buddha's hand",
        "Cactus pear",
        "Cantaloupe",
        "Cherimoya",
        "Cherry",
        "Chico fruit",
        "Chile pepper",
        "Clementine",
        "Cloudberry",
        "Coconut",
        "Corn kernel",
        "Crab apple",
        "Cranberry",
        "Cucumber",
        "Currant",
        "Damson",
        "Date",
        "Dragonfruit",
        "Durian",
        "Eggplant",
        "Elderberry",
        "Feijoa",
        "Fig",
        "Galia melon",
        "Goji berry",
        "Gooseberry",
        "Grape",
        "Grapefruit",
        "Guava",
        "Hala Fruit",
        "Honeyberry",
        "Honeydew",
        "Huckleberry",
        "Jabuticaba",
        "Jackfruit",
        "Jalapeño",
        "Jambul",
        "Japanese plum",
        "Jostaberry",
        "Jujube",
        "Juniper berry",
        "Kiwano",
        "Kiwifruit",
        "Kumquat",
        "Lemon",
        "Lime",
        "Loganberry",
        "Longan",
        "Loquat",
        "Lychee",
        "Mandarine",
        "Mango",
        "Mangosteen",
        "Marionberry",
        "Melon",
        "Miracle fruit",
        "Mulberry",
        "Nance",
        "Nectarine",
        "Olive",
        "Orange",
        "Papaya",
        "Passionfruit",
        "Pea",
        "Peach",
        "Pear",
        "Persimmon",
        "Pineapple",
        "Pineberry",
        "Plantain",
        "Plum",
        "Pluot",
        "Pomegranate",
        "Pomelo",
        "Pumpkin",
        "Purple mangosteen",
        "Quince",
        "Rambutan",
        "Raspberry",
        "Redcurrant",
        "Salak",
        "Salal berry",
        "Salmonberry",
        "Satsuma",
        "Soursop",
        "Squash",
        "Star apple",
        "Star fruit",
        "Strawberry",
        "Surinam cherry",
        "Tamarillo",
        "Tamarind",
        "Tangelo",
        "Tangerine",
        "Tayberry",
        "Tomato",
        "Ugli fruit",
        "Watermelon",
        "White currant",
        "White sapote",
        "Yuzu",
        "Zucchini",
    ]
    return fruits

def shopping_list(n = 1):
    '''
    Returns a list of n randomly selected fruits. 
    If no value for n is passed, a single fruit is selected
    '''

    try: 
        fruits = all_fruits()

        if n == 1:
            return choice(fruits)
        
        fruit_list = []
        for i in range(n):
            fruit = choice(fruits)
            
            while fruit in fruit_list: 
                fruit = choice(fruits)

            fruit_list.append(fruit)

    except TypeError:
        print(f"'{type(n)}' object '{n}' cannot be interpreted as an integer")
        return None
        
    return fruit_list

def fruit_prices(n):
    '''
    Returns a dictionary of random fruits and a random
    price between 0.0 and 1.0
    '''
    try:
        fruits = all_fruits()

        inventory = {}
        for i in range(n):
            fruit = choice(fruits)
            while fruit in inventory:
                fruit = choice(fruits)

            inventory[fruit] = round(random(), 2)    
    
    except TypeError:
        print(f"'{type(n)}' object '{n}' cannot be interpreted as an integer")
        return None

    return inventory

    
def fill_basket(n):
    '''
    Returns a dictionary of fruits, their quantity, 
    price_per item and the running total for each item
    '''
    try:
        fruits = all_fruits()

        basket = {}
        for i in range(n):
            fruit = choice(fruits)
            while fruit in basket:
                fruit = choice(fruits)
            
            basket[fruit] = {}
            basket[fruit]['quantity'] = randint(1, 10)
            basket[fruit]['price_per'] = round(random(), 2)
            basket[fruit]['item_total'] = round(basket[fruit]['quantity'] * basket[fruit]['price_per'], 2)
    
    except TypeError:
        print(f"'{type(n)}' object '{n}' cannot be interpreted as an integer")
        return None

    return basket


