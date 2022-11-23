from functions.check_correct import check_correct
import random
from functions.get_kenmerk import get_kenmerk
from init import speler


def end_data():
    list_scores = {"Software Engineer": speler.punten_se, "Forensisch ICT": speler.punten_fict,
                   "Interactie-Technologie": speler.punten_iat + 2, "Data Engineer": speler.punten_de - 2}
    winner = [k for k, v in list_scores.items() if v == max(list_scores.values())]
    random_kenmerken_list = []
    while len(random_kenmerken_list) < 4:
        random_kenmerken = random.choice(tuple(speler.kenmerken))
        if (get_kenmerk(random_kenmerken) not in random_kenmerken_list) and check_correct(random_kenmerken, winner[0]):
            random_kenmerken_list.append(get_kenmerk(random_kenmerken))
    kenmerken_string = ', '.join(random_kenmerken_list)
    return winner, kenmerken_string
