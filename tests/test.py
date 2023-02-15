
from . import main


def test_chest_parser():

    """ test the chest_Content_Dict() function """

    pass


def test_recipe_parser():

    """ test the make_Player_Food_Dict() function """

    pass


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
