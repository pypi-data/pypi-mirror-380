"""
generator.py

Provides the core function to generate random names using vowels and consonants.
"""

import random


def generate_name():
    """
    Generates a random name string.

    The name is constructed using a mix of uppercase and lowercase vowels and consonants.
    It may include spaces and apostrophes to create more natural or fantasy-like names.

    Returns:
        str: A randomly generated name.
    """
    bloc_1 = "aeiou"
    bloc_2 = "bcdfghjklmnpqrstvwxyz"
    bloc_3 = "AEIOU"
    bloc_4 = "BCDFGHJKLMNPQRSTVWXYZ"
    name = ""

    option = random.randint(0, 5)
    if option < 2:
        name += random.choice(bloc_3)
    elif option < 5:
        name += random.choice(bloc_4) + random.choice(bloc_1)
    else:
        name += random.choice(bloc_4) + random.choice(bloc_1) + random.choice(bloc_2)

    name_long = random.randint(2, 4)
    for i in range(name_long):
        option = random.randint(0, 5)
        if option < 2:
            name += random.choice(["'", "", "", ""]) + random.choice(bloc_1)
        elif option < 5:
            name += random.choice(bloc_2) + random.choice(bloc_1)
        else:
            name += (
                random.choice(bloc_2) + random.choice(bloc_1) + random.choice(bloc_2)
            )

    if random.randint(0, 1):
        if random.randint(0, 1):
            option = random.randint(0, 2)
            if option == 0:
                name += " " + random.choice(bloc_3)
            elif option == 1:
                name += " " + random.choice(bloc_4) + random.choice(bloc_1)
            elif option == 2:
                name += " " + (
                    random.choice(bloc_4)
                    + random.choice(bloc_1)
                    + random.choice(bloc_2)
                )
        name += " "
        option = random.randint(0, 2)
        if option == 0:
            name += random.choice(bloc_3)
        elif option == 1:
            name += random.choice(bloc_4) + random.choice(bloc_1)
        elif option == 2:
            name += (
                random.choice(bloc_4) + random.choice(bloc_1) + random.choice(bloc_2)
            )
        name_long = random.randint(2, 4)
        for i in range(name_long):
            option = random.randint(0, 5)
            if option < 2:
                name += random.choice(["'", "", "", ""]) + random.choice(bloc_1)
            elif option < 5:
                name += random.choice(bloc_2) + random.choice(bloc_1)
            else:
                name += (
                    random.choice(bloc_2)
                    + random.choice(bloc_1)
                    + random.choice(bloc_2)
                )
    return name
