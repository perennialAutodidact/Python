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

def pick_fruit(n = 1):
    '''
    Returns a list of n randomly selected fruits. 
    If no value for n is passed, a single fruit is selected
    '''
    fruits = all_fruits()
    
    if n == 1:
        return choice(fruits)
    
    return [choice(fruits) for i in range(n)]

def fruit_prices(n):
    fruits = all_fruits()

    return {choice(fruits):round(random(), 2) for i in range(n)}

def fill_basket(n):
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
    return basket

