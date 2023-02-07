# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:50:26 2023

@author: vogel
"""


import re


# Dummies for testing purposes
dummydict = {"FriedEgg": 3,
             "Omelet": 6,
             "StrangeBun": 1,
             "VegetableStew": 7,
             "ParsnipSoup": 7,
             "PinkCake": 2,
             "Tortilla": 3,
             "StirFry": 3,
             "TripleShotEspresso": 5,
             "DishO'TheSea": 2,
             "Miner'sTreat": 1}

dummylist = ["FriedEgg",
             "Omelet",
             "StrangeBun",
             "VegetableStew",
             "ParsnipSoup",
             "PinkCake",
             "Tortilla",
             "StirFry",
             "TripleShotEspresso",
             "DishO'TheSea",
             "Miner'sTreat",
             "Bread",
             "Pizza",
             "FishTaco",
             "Pancakes",
             "MakiRoll"]

# Dict with all possible recipes
ALL_RECIPES = {"FriedEgg": {"Egg": 1},
               "Omelet": {"Egg": 1,
                          "Milk": 1},
               "Salad": {"Leek": 1,
                         "Dandelion": 1,
                         "Vinegar": 1},
               "CheeseCauli.": {"Cauliflower": 1,
                                "Cheese": 1},
               "BakedFish": {"Sunfish": 1,
                             "Bream": 1,
                             "WheatFlour": 1},
               "ParsnipSoup": {"Parsnip": 1,
                               "Milk": 1,
                               "Vinegar": 1},
               "VegetableStew": {"Tomato": 1,
                                 "Beet": 1},
               "CompleteBreakfast": {"FriedEgg": 1,
                                     "Milk": 1,
                                     "Hashbrowns": 1,
                                     "Pancakes": 1},
               "FriedCalamari": {"Squid": 1,
                                 "WheatFlour": 1,
                                 "Oil": 1},
               "Pizza": {"WheatFlour": 1,
                         "Tomato": 1,
                         "Cheese": 1},
               "BeanHotpot": {"GreenBean": 2},
               "GlazedYams": {"Yam": 1,
                              "Sugar": 1},
               "CarpSurprise": {"Carp": 4},
               "Hashbrowns": {"Potato": 1,
                              "Oil": 1},
               "Pancakes": {"WheatFlour": 1,
                            "Egg": 1},
               "SalmonDinner": {"Salmon": 1,
                                "Amaranth": 1,
                                "Kale": 1},
               "FishTaco": {"Tuna": 1,
                            "Tortilla": 1,
                            "RedCabbage": 1,
                            "Mayonnaise": 1},
               "CrispyBass": {"LargemouthBass": 1,
                              "WheatFlour": 1,
                              "Oil": 1},
               "PepperPoppers": {"HotPepper": 1,
                                 "Cheese": 1},
               "Bread": {"WheatFlour": 1},
               "TomKhaSoup": {"Coconut": 1,
                              "Shrimp": 1,
                              "CommonMushroom": 1},
               "TroutSoup": {"RainbowTrout": 1,
                             "GreenAlgae": 1},
               "ChocolateCake": {"WheatFlour": 1,
                                 "Sugar": 1,
                                 "Egg": 1},
               "PinkCake": {"Melon": 1,
                            "WheatFlour": 1,
                            "Sugar": 1,
                            "Egg": 1},
               "RhubarbPie": {"Rhubarb": 1,
                              "WheatFlour": 1,
                              "Sugar": 1},
               "Cookies": {"WheatFlour": 1,
                           "Sugar": 1,
                           "Egg": 1},
               "Spaghetti": {"WheatFlour": 1,
                             "Tomato": 1},
               "FriedEel": {"Eel": 1,
                            "Oil": 1},
               "SpicyEel": {"Eel": 1,
                            "HotPepper": 1},
               "Sashimi": {"AnyFish": 1},
               "MakiRoll": {"AnyFish": 1,
                            "Seaweed": 1,
                            "Rice": 1},
               "Tortilla": {"Corn": 1},
               "RedPlate": {"RedCabbage": 1,
                            "Radish": 1},
               "EggplantParm.": {"Eggplant": 1,
                                 "Tomato": 1},
               "RicePudding": {"Milk": 1,
                               "Sugar": 1,
                               "Rice": 1},
               "IceCream": {"Milk": 1,
                            "Sugar": 1},
               "BlueberryTart": {"Blueberry": 1,
                                 "WheatFlour": 1,
                                 "Sugar": 1,
                                 "Egg": 1},
               "Autumn'sBounty": {"Yam": 1,
                                  "Pumpkin": 1},
               "PumpkinSoup": {"Pumpkin": 1,
                               "Milk": 1},
               "SuperMeal": {"BokChoy": 1,
                             "Cranberries": 1,
                             "Artichoke": 1},
               "Cran.Sauce": {"Cranberries": 1,
                              "Sugar": 1},
               "Stuffing": {"Bread": 1,
                            "Cranberries": 1,
                            "Hazelnut": 1},
               "Farmer'sLunch": {"Omelet": 1,
                                 "Parsnip": 1},
               "SurvivalBurger": {"Bread": 1,
                                  "CaveCarrot": 1,
                                  "Eggplant": 1},
               "Disho'TheSea": {"Sardine": 2,
                                "Hashbrowns": 1},
               "Miner'sTreat": {"CaveCarrot": 2,
                                "Sugar": 1,
                                "Milk": 1},
               "RootsPlatter": {"CaveCarrot": 1,
                                "WinterRoot": 1},
               "TripleShotEspresso": {"Coffee": 3},
               "SeafoamPudding": {"Flounder": 1,
                                  "MidnightCarp": 1,
                                  "SquidInk": 1},
               "AlgaeSoup": {"GreenAlgae": 4},
               "PaleBroth": {"WhiteAlgae": 2},
               "PlumPudding": {"WildPlum": 2,
                               "WheatFlour": 1,
                               "Sugar": 1},
               "ArtichokeDip": {"Artichoke": 1,
                                "Milk": 1},
               "StirFry": {"CaveCarrot": 1,
                           "CommonMushroom": 1,
                           "Kale": 1,
                           "Oil": 1},
               "RoastedHazelnuts": {"Hazelnut": 3},
               "PumpkinPie": {"Pumpkin": 1,
                              "WheatFlour": 1,
                              "Milk": 1,
                              "Sugar": 1},
               "RadishSalad": {"Oil": 1,
                               "Vinegar": 1,
                               "Radish": 1},
               "FruitSalad": {"Blueberry": 1,
                              "Melon": 1,
                              "Apricot": 1},
               "BlackberryCobbler": {"Blackberry": 2,
                                     "Sugar": 1,
                                     "WheatFlour": 1},
               "CranberryCandy": {"Cranberries": 1,
                                  "Apple": 1,
                                  "Sugar": 1},
               "Bruschetta": {"Bread": 1,
                              "Oil": 1,
                              "Tomato": 1},
               "Coleslaw": {"RedCabbage": 1,
                            "Vinegar": 1,
                            "Mayonnaise": 1},
               "FiddleheadRisotto": {"Oil": 1,
                                     "FiddleheadFern": 1,
                                     "Garlic": 1},
               "PoppyseedMuffin": {"Poppy": 1,
                                   "WheatFlour": 1,
                                   "Sugar": 1},
               "Chowder": {"Clam": 1,
                           "Milk": 1},
               "FishStew": {"Crayfish": 1,
                            "Mussel": 1,
                            "Periwinkle": 1,
                            "Tomato": 1},
               "Escargot": {"Snail": 1,
                            "Garlic": 1},
               "LobsterBisque": {"Lobster": 1,
                                 "Milk": 1},
               "MapleBar": {"MapleSyrup": 1,
                            "Sugar": 1,
                            "WheatFlour": 1},
               "CrabCakes": {"Crab": 1,
                             "WheatFlour": 1,
                             "Egg": 1,
                             "Oil": 1},
               "ShrimpCocktail": {"Tomato": 1,
                                  "Shrimp": 1,
                                  "WildHorseradish": 1},
               "GingerAle": {"Ginger": 1,
                             "Sugar": 1},
               "BananaPudding": {"Banana": 1,
                                 "Milk": 1,
                                 "Sugar": 1},
               "MangoStickyRice": {"Mango": 1,
                                   "Coconut": 1,
                                   "Rice": 1},
               "Poi": {"TaroRoot": 4},
               "TropicalCurry": {"Coconut": 1,
                                 "Pineapple": 1,
                                 "HotPepper": 1},
               "SquidInkRavioli": {"SquidInk": 1,
                                   "WheatFlour": 1,
                                   "Tomato": 1},
               "StrangeBun": {"WheatFlour": 1,
                              "Periwinkle": 1,
                              "VoidMayonnaise": 1},
               "LuckyLunch": {"SeaCucumber": 1,
                              "Tortilla": 1,
                              "BlueJazz": 1},
               "FriedMushroom": {"CommonMushroom": 1,
                                 "Morel": 1,
                                 "Oil": 1}}


def import_File(path):
    file = open(path, "rt")
    text = file.readline()
    return text


def token_Search(token_name, text):
    liste = text.split(f"{token_name}")
    return liste


def clean_List(liste):
    listClean = []
    for i in range(1, len(liste), 2):
        listClean.append(liste[i])
    return listClean


def make_Player_Food_Dict(text):
    tkRecipes = token_Search("cookingRecipes", text)

    tkRecipesClean = re.sub('[<>/ ]', '', tkRecipes[1])

    tkString = token_Search("string", tkRecipesClean)
    tkInt = token_Search("int", tkRecipesClean)


    tkStringClean = clean_List(tkString)
    tkIntClean = clean_List(tkInt)

    player_food_dict = dict(zip(tkStringClean,tkIntClean))
    return player_food_dict


def print_meal(meal, style=2):

    """ Transforms strings from one string to multiple strings """

    # Re searches for a capital letter ([A-Z]) followed by anything but capital letters ([^A-Z])
    splitted_food = re.findall('[A-Z][^A-Z]*', meal)

    # Prints out the food's name in the same line, whitespace after the last one
    if style == 1:
        for parts in splitted_food:
            print(parts, end=" ")

    elif style == 2:
        for parts in splitted_food:
            # Prints out the food's name in the same line, no whitespace after the last one
            if splitted_food.index(parts) != len(splitted_food)-1:
                print(parts, end=" ")
            else:
                print(parts, end="")


def write_meal(meal, style=1):

    """ Transforms strings from one string to multiple strings """

    # Re searches for a capital letter ([A-Z]) followed by anything but capital letters ([^A-Z])
    splitted_food = re.findall('[A-Z][^A-Z]*', meal)
    
    new_string = []
    
    # Prints out the food's name in the same line, whitespace after the last one
    if style == 1:
        for parts in splitted_food:
            new_string.append(parts)
            new_string.append(" ")

    elif style == 2:
        for parts in splitted_food:
            # Prints out the food's name in the same line, no whitespace after the last one
            if splitted_food.index(parts) != len(splitted_food)-1:
                new_string.append(parts)
                new_string.append(" ")
            else:
                new_string.append(parts)

    string = "".join(new_string)

    return string


def already_cooked(player_food_dict, style=2, amount_per_line=5):

    """ Prints out wich meals have been cooked how often """

    # Prints everything in a new line with description
    if style == 1:
        for food, amount_cooked in player_food_dict.items():
            print("Player has cooked", end=" ")
            print_meal(food)
            print(f"{amount_cooked} times.")

    # Prints out foods as a list
    if style == 2:

        printed_in_line = 1
        counted_foods = 0

        print("Player has cooked following meals that often:\n")

        for food, amount_cooked in player_food_dict.items():

            # Breaks after the last recipe without the comma
            if counted_foods == len(player_food_dict)-1:
                print_meal(food, 2)
                print(f": {amount_cooked}")
                break

            # Prints the recipes in the same line
            if printed_in_line != amount_per_line:
                print_meal(food, 2)
                print(f": {amount_cooked},", end=" ")

                printed_in_line += 1
                counted_foods += 1

            # Prints recipe in the same line as the one before, then goes to a new line, n = recipes per line
            elif printed_in_line == amount_per_line:
                print_meal(food, 2)
                print(f": {amount_cooked},")

                printed_in_line = 1
                counted_foods += 1


def still_missing(player_food_dict, all_foods):

    """ checks wich foods from ALL_RECIPES have not yet been cooked (aka are not in player_food_dict) """

    missing_foods = []

    for foodies in all_foods:
        if foodies not in player_food_dict:
            missing_foods.append(foodies)

    # Returns list with all not yet cooked meals
    return missing_foods


def print_missing_food(player_food_dict, all_foods, style=2, amount_per_line=5):

    """ prints out all missing foods """

    # Creates a list with all not yet cooked meals
    missing_foods = still_missing(player_food_dict, all_foods)

    # Prints out missing food in new line with description
    if style == 1:

        for foodsers in missing_foods:
            print_meal(foodsers)
            print("has not yet been cooked")

    # Prints out missing food as list
    elif style == 2:

        print(f"The following meals have not yet been cooked: (Total: {len(missing_foods)})\n")

        printed_in_line = 1

        for foodsers in missing_foods:

            # Breaks after the last meal without the comma
            if missing_foods.index(foodsers) == len(missing_foods)-1:
                print_meal(foodsers, 2)
                break

            # Prints the meals in the same line
            if printed_in_line != amount_per_line:
                print_meal(foodsers, 2)
                print(",", end=" ")

                printed_in_line += 1

            # Prints the meal in the same line as the one before, then goes to a new line, n = meals in one line
            elif printed_in_line == amount_per_line:
                print_meal(foodsers, 2)
                print(",")

                printed_in_line = 1


def owned_recipes(player_recipes_list, style=2, amount_per_line=5):

    """" Prints all obtained recipes """

    # Prints out recipes in new line with description
    if style == 1:

        for recipe in player_recipes_list:
            print("Player has already obtained ", end=" ")
            print_meal(recipe)
            print(".")

    # Prints out recipes as list
    if style == 2:

        printed_in_line = 1

        print("Player has obtained the following recipes:\n")

        for recipe in player_recipes_list:

            # Breaks after the last recipe without the comma
            if player_recipes_list.index(recipe) == len(player_recipes_list)-1:
                print_meal(recipe, 2)
                break

            # Prints the recipes in the same line
            if printed_in_line != amount_per_line:
                print_meal(recipe, 2)
                print(",", end=" ")

                printed_in_line += 1

            # Prints recipe in the same line as the one before, then goes to a new line, n = recipes per line
            elif printed_in_line == amount_per_line:
                print_meal(recipe, 2)
                print(",")

                printed_in_line = 1


def print_missing_recipes(player_recipes_list, all_foods, style=2, amount_per_line=5):

    """" Prints out all missing recipes """

    # Creates a list with all missing recipes
    missing_recipes = still_missing(player_recipes_list, all_foods)

    # Prints out recipes in new line with description
    if style == 1:

        for recipe in missing_recipes:
            print_meal(recipe)
            print("has not yet been obtained.")

    # Prints out recipes as list
    elif style == 2:

        print(f"The following recipes have not yet been obtained: (Total: {len(missing_recipes)})\n")

        printed_in_line = 1

        for recipe in missing_recipes:

            # Breaks after the last meal without the comma
            if missing_recipes.index(recipe) == len(missing_recipes)-1:
                print_meal(recipe, 2)
                break

            # Prints the meals in the same line
            if printed_in_line != amount_per_line:
                print_meal(recipe, 2)
                print(",", end=" ")

                printed_in_line += 1

            # Prints meal in the same line as the one before, then goes to a new line, n = meals per line
            elif printed_in_line == amount_per_line:
                print_meal(recipe, 2)
                print(",")

                printed_in_line = 1


# if __name__ == "__main__":
#     # Call the functions to test them
#     print("the already_cooked() function in Style 1 (everything in a new line)\n")
#     already_cooked(dummydict, 1)
#     print("\n\nthe already_cooked() function in Style 2 (everything in one long list)\n")
#     already_cooked(dummydict)
#     print("\n\nthe print_missing_food() function in Style 1 (everything in a new line)\n")
#     print_missing_food(dummydict, ALL_RECIPES.keys(), 1)
#     print("\n\nthe print_missing_food() function in Style 2 (everything in one long list)\n")
#     print_missing_food(dummydict, ALL_RECIPES.keys())
#     print("\n\nthe owned_recipes() function in Style 1 (everything in a new line)\n")
#     owned_recipes(dummylist, 1)
#     print("\n\nthe owned_recipes() function in Style 2 (everything in one long list)\n")
#     owned_recipes(dummylist)
#     print("\n\nthe print_missing_recipes() function in Style 1 (everything in a new line)\n")
#     print_missing_recipes(dummylist, ALL_RECIPES.keys(), 1)
#     print("\n\nthe print_missing_recipes() function in Style 2 (everything in one long list)\n")
#     print_missing_recipes(dummylist, ALL_RECIPES.keys())


#%%
from io import StringIO
import streamlit as st


file = st.file_uploader("Please           upload Save file!")

if file is not None:
    text = StringIO(file.getvalue().decode("utf-8")).readline()

    recipeDict = make_Player_Food_Dict(text)
    
    cooking_help = False

    if len(still_missing(recipeDict, ALL_RECIPES.keys())) != 0:
        if st.button("cooking helper", help="shows needed ingredients for not yet cooked meals"):
            cooking_help = True

    if len(still_missing(recipeDict, ALL_RECIPES.keys())) == 0:
        st.subheader("All recipies have been cooked!")
        st.balloons()
        done = True

    with st.expander(f"Expand to see all recipes you own: [{len(make_Player_Food_Dict(text))}]"):

        for elements in recipeDict.keys():
            st.write("- " + write_meal(elements))
        
    with st.expander(f"Expand to see missing recipes: [{len(still_missing(recipeDict, ALL_RECIPES.keys()))}]"):
        missing_recipes = still_missing(recipeDict, ALL_RECIPES.keys())
        for elements in missing_recipes:
            st.write("- " + write_meal(elements))

    if cooking_help == True:
        if st.button("close", help="close needed ingredients for not yet cooked meals"):
            cooking_help = False

        choice = st.selectbox("choose meal to show recipe", still_missing(recipeDict, ALL_RECIPES.keys()))

        if choice is not None:
            st.write(choice + ":")
            temp = ALL_RECIPES[choice].keys()
            for i in temp:
                st.write("- " + i + " (" + str(ALL_RECIPES[choice][i]) + ")")
            
            