# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:50:26 2023

@author: vogel & friedeheim
"""

from io import StringIO
import streamlit as st
import re


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


def clean_List(liste):

    """ simple function to make a new list with every second element of the old one,
        needed because of the open and close format of XML """

    listClean = []
    for i in range(1, len(liste), 2):
        listClean.append(liste[i])
    return listClean


def make_Player_Food_Dict(text):

    """ makes a dictionary of all recipes the player owns.
        keys is name of recipe, values are amount cooked """

    tkRecipes = text.split("cookingRecipes")

    # Removes unnecessary symbols
    tkRecipesClean = re.sub('[<>/ ]', '', tkRecipes[1])

    # makes list of all Recipenames
    tkString = tkRecipesClean.split("string")

    # makes list of Amount cooked
    tkInt = tkRecipesClean.split("int")

    # removes unnecessary elements in the list
    tkStringClean = clean_List(tkString)
    tkIntClean = clean_List(tkInt)

    player_food_dict = dict(zip(tkStringClean,tkIntClean))
    return player_food_dict


def chest_Content_Dict(text):

    """ makes a dictionary of all items the player has in chests.
        keys is name of item, values are amount owned """

    # makes one string element for all chest and saves them in a list
    tkChest = text.split("Object xsi:type=\"Chest\"")

    # makes one list with string element for all items
    # discards first element since its not needed
    allItems = []
    for element in tkChest[1:]:
        if "<Item xsi:type=\"" in element:
            allItems.extend(element.split("<Item xsi:type=\"")[1:])

    # cleans list of unnecessary symbols
    allItemsClean = []
    for element in allItems:
        allItemsClean.append(re.sub('[<>/ \']', '', element))

    # list of all item names
    allItemsName = []
    for element in allItemsClean:
        allItemsName.append(element.split("name")[1])

    # list of amount for each item
    allItemsStack = []
    for element in allItemsClean:
        allItemsStack.append(int(element.split("Stack")[1]))

    # since dict overwrites amount if item already exists, this makes a dict with all names and value = 0
    chest_Content_Dict = dict.fromkeys(allItemsName, 0)
    # then adds amount for each item in list
    for name, stack in zip(allItemsName, allItemsStack):
        chest_Content_Dict[name] = chest_Content_Dict[name] + stack

    return chest_Content_Dict


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


def has_cooked(player_food_dict):

    """checks which recipes have not yet been cooked"""

    allCooked = []

    for recipe, amount in player_food_dict.items():
        if amount != "0":
            allCooked.append(recipe)

    return allCooked


def still_missing(player_food_dict, all_foods):

    """ checks wich foods from ALL_RECIPES have not yet been gathered (aka are not in player_food_dict) """

    missing_foods = []

    for foodies in all_foods:
        if foodies not in player_food_dict:
            missing_foods.append(foodies)

    # Returns list with all not yet cooked dishes
    return missing_foods




# """    !!! START OF STREAMLIT IMPLEMENTATION !!!  """ #



st.header("Stardew Cooker")

st.write("This is a Stardew Valley Helper Tool! It is designed to help people get a simple overview of what recipes are still missing to achieve Perfection or the Gourmet Chef Achievment. For this Tool to work, its best to put all your items in chests! Otherwise those items will be missed. (Auto Grabber count as Chests :))")
st.write("WARNING: Mods that add recipes may break this tool and make it not function properly!")
st.write("") # aesthetic purposes


# save file upload
file = st.file_uploader("Please upload your Save file!")

#appears only after file is uploaded
if file is not None:
    # parses through Players recipes
    text = StringIO(file.getvalue().decode("utf-8")).readline()
    recipeDict = make_Player_Food_Dict(text)

    # Reward for cooking all recipes!
    if len(has_cooked(recipeDict)) == 80:
        st.subheader("All recipies have been gathered!")
        st.balloons()
        done = True


    # View Recipes
    # FIRST SECTION OF WEBSITE

    st.write("") # aesthetic purposes
    with st.expander("View Recipes:"):
        col1, col2, col3 = st.columns(3)

        # st.write("Missing: All recipes you cant make yet. Owned: All recipe")
        # st.write("")

        # Views all Missing Recipes i.e. not yet collected
        with col1:
            missing = st.checkbox("Missing")
            all_missing = still_missing(recipeDict, ALL_RECIPES)
            if missing:
                st.write("#### Missing:")
                if len(all_missing) != 0:
                    for element in all_missing:
                        st.write("- " + write_meal(element))
                else:
                    st.write("No missing recipes.")

        # views all collected but not cooked recipes
        with col2:
            owned = st.checkbox("Owned")
            all_owned = []

            for recipe, amount in recipeDict.items():
                if amount == "0":
                    all_owned.append(recipe)

            if owned:
                st.write("#### Owned:")
                if len(all_owned) != 0:
                    for element in all_owned:
                        st.write("- " + write_meal(element))
                else:
                    st.write("No owned recipes.")

        # views all cooked recipes
        with col3:
            cooked = st.checkbox("Cooked")
            all_cooked = has_cooked(recipeDict)

            if cooked:
                st.write("#### Cooked:")
                if len(all_cooked) != 0:
                    for element in all_cooked:
                        st.write("- " + write_meal(element))
                else:
                    st.write("No cooked recipes.")



    # cooking helper
    # SECOND SECTION OF WEBSITE
    with st.expander("What Items are missing:"):

        view = st.radio("Please choose one:", ("All Items", "All missing Items", "All Items in Chests"))

        # makes and displays Dict of all Items needed to cook all uncooked recipes
        neededItems = {}
        has_not_cooked = []
        has_cooked = has_cooked(recipeDict)

        for element in ALL_RECIPES.keys():
            if element not in has_cooked:
                has_not_cooked.append(element)

        for recipe in has_not_cooked:
            for ingredient in ALL_RECIPES[recipe]:
                if ingredient not in neededItems.keys():
                    neededItems[ingredient] = ALL_RECIPES[recipe][ingredient]
                elif ingredient in neededItems.keys():
                    neededItems[ingredient] = neededItems[ingredient] + ALL_RECIPES[recipe][ingredient]

        neededItems = dict(sorted(neededItems.items(), key=lambda x:x[1], reverse=True))


        # dictonary of all needed items stored in chests
        chestContent = chest_Content_Dict(text)
        chestItems = {}
        for item,amount in neededItems.items():
            if item in chestContent.keys():
                if chestContent[item] >= amount:
                    chestItems.update({item:amount})
                else:
                    chestItems.update({item:chestContent[item]})


        # makes all fully missing items (i.e. not in any chests)
        missingItems = dict.fromkeys(chestItems.keys(), 0)
        for item,amount in neededItems.items():
            if item in chestItems.keys():
                missingItems[item] = amount - chestItems[item]
            else:
                missingItems[item] = amount


        # visual function for streamlit overview
        # prints all items, all missing items or all items stored in chests
        if view == "All Items":
            st.write("#### All Items:")
            col1, col2 = st.columns(2)
            counter = 1
            for keys, values in neededItems.items():
                if  counter % 2 == 1:
                    with col1:
                        st.write("- " + write_meal(keys, 2) + ": " + str(values) + "x")
                        counter += 1
                else:
                    with col2:
                        st.write("- " + write_meal(keys, 2) + ": " + str(values) + "x")
                        counter += 1


        if view == "All missing Items":
            st.write("#### All missing Items:")
            col1, col2 = st.columns(2)
            counter = 1
            for keys, values in missingItems.items():
                if values != 0:
                    if  counter % 2 == 1:
                        with col1:
                            st.write("- " + write_meal(keys, 2) + ": " + str(values) + "x")
                            counter += 1
                    else:
                        with col2:
                            st.write("- " + write_meal(keys, 2) + ": " + str(values) + "x")
                            counter += 1


        if view == "All Items in Chests":
            st.write("#### All Items in Chests:")
            col1, col2 = st.columns(2)
            counter = 1
            for keys, values in chestItems.items():
                if  counter % 2 == 1:
                    with col1:
                        st.write("- " + write_meal(keys, 2) + ": " + str(values) + "x")
                        counter += 1
                else:
                    with col2:
                        st.write("- " + write_meal(keys, 2) + ": " + str(values) + "x")
                        counter += 1

st.write("")
st.write("**Follow us on GitHub: https://github.com/friedeheim/Stardew-Cooker.git")
