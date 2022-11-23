from functions.firebase import get_kenmerken


def get_kenmerk(kenmerk):
    dict_kenmerken = {}

    kenmerken = get_kenmerken()
    for i in kenmerken:
        dict_kenmerken.update({i["ID"]: i["Kenmerken"]})

    if kenmerk in dict_kenmerken.keys():
        return dict_kenmerken[kenmerk]
