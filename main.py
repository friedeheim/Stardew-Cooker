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


def still_missing(player_food_dict, all_foods):

    """ checks wich foods from ALL_RECIPES have not yet been cooked (aka are not in player_food_dict) """

    missing_foods = []

    for foodies in all_foods:
        if foodies not in player_food_dict:
            missing_foods.append(foodies)

    # Returns list with all not yet cooked meals
    return missing_foods


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
            
            