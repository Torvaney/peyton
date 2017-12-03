PLAY_DISTRIBUTION = {
    0: "Handoff. Not much gain. [2 YARDS]",
    1: "SACK! [-5 YARDS]",
    2: "Short pass [3 YARDS]",
    3: "FUMBLE [PATRIOTS TOUCHDOWN] :(",
    4: "Medium pass [7 YARDS]",
    5: "THROWS DEEP... [COLTS TOUCHDOWN] ^_^"
}



def random_play(x):
    """
    Generates a play after an Omaha audible

    Parameters
    --------
    x - int
        A "random" number generated by the football Gods

    Returns
    --------
    str - commentary on the play
    """
    return PLAY_DISTRIBUTION[x]


