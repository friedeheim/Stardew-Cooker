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
             "VegetableMedley": 7,
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
             "VegetableMedley",
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

# List with all possible meals
ALL_FOODS = ["FriedEgg",
            "Omelet",
            "Salad",
            "CheeseCauliflower",
            "BakedFish",
            "ParsnipSoup",
            "VegetableMedley",
            "CompleteBreakfast",
            "FriedCalamari",
            "Pizza",
            "BeanHotpot",
            "GlazedYams",
            "CarpSurprise",
            "Hashbrowns",
            "Pancakes",
            "SalmonDinner",
            "FishTaco",
            "CrispyBass",
            "PepperPoppers",
            "Bread",
            "TomKhaSoup",
            "TroutSoup",
            "ChocolateCake",
            "PinkCake",
            "RhubarbPie",
            "Cookie",
            "Spaghetti",
            "FriedEel",
            "SpicyEel",
            "Sashimi",
            "MakiRoll",
            "Tortilla",
            "RedPlate",
            "EggplantParmesan",
            "RicePudding",
            "IceCream",
            "BlueberryTart",
            "Autumn'sBounty",
            "PumpkinSoup",
            "SuperMeal",
            "CranberrySauce",
            "Stuffing",
            "Farmer'sLunch",
            "SurvivalBurger",
            "DishO'TheSea",
            "Miner'sTreat",
            "RootsPlatter",
            "TripleShotEspresso",
            "SeafoamPudding",
            "AlgaeSoup",
            "PaleBroth",
            "PlumPudding",
            "ArtichokeDip",
            "StirFry",
            "RoastedHazelnuts",
            "PumpkinPie",
            "RadishSalad",
            "FruitSalad",
            "BlackberryCobbler",
            "CranberryCandy",
            "Bruschetta",
            "Coleslaw",
            "FiddleheadRisotto",
            "PoppyseedMuffin",
            "Chowder",
            "FishStew",
            "Escargot",
            "LobsterBisque",
            "MapleBar",
            "CrabCakes",
            "ShrimpCocktail",
            "GingerAle",
            "BananaPudding",
            "MangoStickyRice",
            "Poi",
            "TropicalCurry",
            "SquidInkRavioli",
            "StrangeBun",
            "LuckyLunch",
            "FriedMushroom"]


def print_meal(meal, style=1):

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

    """ checks wich foods from ALL_FOODS have not yet been cooked (aka are not in player_food_dict) """

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


if __name__ == "__main__":
    # Call the functions to test them
    print("the already_cooked() function in Style 1 (everything in a new line)\n")
    already_cooked(dummydict, 1)
    print("\n\nthe already_cooked() function in Style 2 (everything in one long list)\n")
    already_cooked(dummydict)
    print("\n\nthe print_missing_food() function in Style 1 (everything in a new line)\n")
    print_missing_food(dummydict, ALL_FOODS, 1)
    print("\n\nthe print_missing_food() function in Style 2 (everything in one long list)\n")
    print_missing_food(dummydict, ALL_FOODS)
    print("\n\nthe owned_recipes() function in Style 1 (everything in a new line)\n")
    owned_recipes(dummylist, 1)
    print("\n\nthe owned_recipes() function in Style 2 (everything in one long list)\n")
    owned_recipes(dummylist)
    print("\n\nthe print_missing_recipes() function in Style 1 (everything in a new line)\n")
    print_missing_recipes(dummylist, ALL_FOODS, 1)
    print("\n\nthe print_missing_recipes() function in Style 2 (everything in one long list)\n")
    print_missing_recipes(dummylist, ALL_FOODS)
