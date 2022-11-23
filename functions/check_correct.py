from functions.firebase import get_kenmerken


def check_correct(kenmerk, specialisatie):
    dict_se = {}
    dict_fict = {}
    dict_de = {}
    dict_iat = {}

    kenmerken = get_kenmerken()
    for i in kenmerken:
        if i["SE"] == "TRUE":
            dict_se.update({i["ID"]: i["Kenmerken"]})
        if i["FICT"] == "TRUE":
            dict_fict.update({i["ID"]: i["Kenmerken"]})
        if i["DE"] == "TRUE":
            dict_de.update({i["ID"]: i["Kenmerken"]})
        if i["IAT"] == "TRUE":
            dict_iat.update({i["ID"]: i["Kenmerken"]})

    if kenmerk in dict_se.keys() and specialisatie == "Software Engineer":
        return True
    elif kenmerk in dict_fict.keys() and specialisatie == "Forensisch ICT":
        return True
    elif kenmerk in dict_de.keys() and specialisatie == "Data Engineer":
        return True
    elif kenmerk in dict_iat.keys() and specialisatie == "Interactie-Technologie":
        return True
    else:
        return False
