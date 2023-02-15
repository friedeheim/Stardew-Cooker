
from . import main


test_string = open("./saves/100CompletedSaveFile", "rt")
test_string = test_string.readline()


def test_chest_parser():

    """ test the chest_Content_Dict() function """

    pass


def test_recipe_parser():

    """ test the make_Player_Food_Dict() function """

    assert main.make_Player_Food_Dict(test_string) == {'FriedEgg': '0',
                                                       'SurvivalBurger': '0',
                                                       'StirFry': '0',
                                                       'Coleslaw': '0',
                                                       "Farmer'sLunch": '0',
                                                       'RadishSalad': '0',
                                                       'Omelet': '0',
                                                       "Miner'sTreat": '0',
                                                       "Disho'TheSea": '0',
                                                       'BakedFish': '0',
                                                       'Pancakes': '0',
                                                       'RootsPlatter': '0',
                                                       'MakiRoll': '0',
                                                       'Bread': '0',
                                                       'Tortilla': '0',
                                                       'TroutSoup': '0',
                                                       'GlazedYams': '0',
                                                       'ArtichokeDip': '0',
                                                       'PlumPudding': '0',
                                                       'ChocolateCake': '0',
                                                       'Sashimi': '0',
                                                       'PumpkinPie': '0',
                                                       'Hashbrowns': '0',
                                                       'Pizza': '0',
                                                       'CranberryCandy': '0',
                                                       'ParsnipSoup': '0',
                                                       'CheeseCauli.': '0',
                                                       'CompleteBreakfast': '0',
                                                       'TripleShotEspresso': '0',
                                                       'LuckyLunch': '0',
                                                       'CarpSurprise': '0',
                                                       'SeafoamPudding': '0',
                                                       'CrispyBass': '0',
                                                       'MapleBar': '0',
                                                       'FriedMushroom': '0',
                                                       'Salad': '0',
                                                       'FriedEel': '0',
                                                       'PinkCake': '0',
                                                       'AlgaeSoup': '0',
                                                       'Spaghetti': '0',
                                                       'Chowder': '0',
                                                       'Escargot': '0',
                                                       'RoastedHazelnuts': '0',
                                                       'PepperPoppers': '0',
                                                       'FishTaco': '0',
                                                       'FruitSalad': '0',
                                                       'SalmonDinner': '0',
                                                       'PaleBroth': '0',
                                                       'Cookies': '0',
                                                       'VegetableStew': '0',
                                                       'FriedCalamari': '0',
                                                       'BlackberryCobbler': '0',
                                                       'Stuffing': '0',
                                                       'EggplantParm.': '0',
                                                       'FishStew': '0',
                                                       'CrabCakes': '0',
                                                       'PumpkinSoup': '0',
                                                       "Autumn'sBounty": '0',
                                                       'RedPlate': '0',
                                                       'SuperMeal': '0',
                                                       'SpicyEel': '0',
                                                       'RicePudding': '0',
                                                       'IceCream': '0',
                                                       'BeanHotpot': '0',
                                                       'BlueberryTart': '0',
                                                       'RhubarbPie': '0',
                                                       'LobsterBisque': '0',
                                                       'FiddleheadRisotto': '0',
                                                       'PoppyseedMuffin': '0',
                                                       'StrangeBun': '0',
                                                       'TomKhaSoup': '0',
                                                       'Cran.Sauce': '0',
                                                       'Bruschetta': '0',
                                                       'ShrimpCocktail': '0',
                                                       'SquidInkRavioli': '0',
                                                       'GingerAle': '0',
                                                       'BananaPudding': '0',
                                                       'TropicalCurry': '0',
                                                       'Poi': '0',
                                                       'MangoStickyRice': '0'}


def test_recipe_comparer():

    """ test the still_missing() function """

    test_player = {"Stuff": 1,
                   "Things": 3,
                   "Objects": 5}
    test_archive = {"Stuff": {"Filled": 1,
                              "With": 5,
                              "Things": 8},
                    "Things": {"Very": 5,
                               "Important": 7,
                               "Text": 1},
                    "Objects": {"Shorter": 3},
                    "Different": {"Just": 2,
                                  "Two": 2},
                    "Unneeded": {"Some": 4,
                                 "More": 2,
                                 "Content": 3},
                    "Filler": {"AlmostDone": 1,
                               "It'sContent": 5,
                               "CoolStuffBoi": 6},
                    "Text": {"Its": 4,
                             "Even": 1,
                             "Moore": 23,
                             "IKnowItsSpelledWrongItsIntended": 18}}

    assert main.still_missing(test_player, test_archive) == ["Stuff", "Things", "Objects"]
