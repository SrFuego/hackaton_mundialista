# apps/players/utils.py
# Python imports


# Django imports


# Third party apps imports


# Local imports


# Create your routers here.
def get_val_fatigue(val):
    if val < 47:
        return -7
    elif val < 62:
        return -6
    elif val < 77:
        return -5
    else:
        return -3


def get_val_recover(val):
    return 1 if val <= 53 else 2


def get_val_card_yellow(val):
    if val <= 43:
        return -5
    elif val <= 75:
        return -10
    else:
        return -15


def get_val_serious_foul(val):
    return -10 if val <= 53 else -15


def get_new_points(points, tipo):
    if tipo == "fatiga":
        return get_val_fatigue(points)
    elif tipo == "recuperacion":
        return get_val_recover(points)
    elif tipo == "tarjeta_amarilla":
        return get_val_card_yellow(points)
    elif tipo == "falta_grave":
        return get_val_serious_foul(points)
    elif tipo == "tarjeta_roja":
        return -80
