import os
from os import system
import random
import time
name_inventory = [
    "matiMg05", "Heidihyu", "NontiSuker8", "w49171n0nd35cr197", "Wapitioff", "Wapitisan"
]

pss_inventory = [
    "g86jSMOq70!0", "JitLJ8K6O5*Lf$", "F6%19w", "w49171n0nd35cr197", "22R0%", "ws8OW33G8#"
]

weapons_inventory = [
    "vandal origin", "phanthon oni", "knife karambit reaver", "PHANTOM", " GLITCHPOP", "VANDAL PRIME ", "OPERATOR ION", "SINGULARIDAD DE ARES",
    "ODIN PRIME 2.0", "JUEZ ELDERFLAME", "SPECTRE FORSAKEN", "RUINA ", "FANTASMA", "SHERIFF ION", "MARSHALL MAGEPUNK", "BUCKY ION", "GUARDIAN", " INFANTERÍA", "BULLDOG CONVEXO", "STINGER SOVEREIGN", "FRENESÍ PRIME", "MELEE PRIME 2.0"]



def generate_pss():

    pss_generate = random.choice(pss_inventory)
    return pss_generate + " "




def generate_usr():

    usr_generate = random.choice(name_inventory)
    return usr_generate + " "

def generate_wp():

    wp_gn = random.choice(weapons_inventory)
    return wp_gn + " "


def generateAll():
    print()
    print("        User: " + generate_usr() + " Password: " +
        generate_pss() + " skin: " + generate_wp() + generate_wp() + generate_wp())
    print()
    time.sleep(1)

def generateAcc():
    time.sleep(1)
    generateAll()
    generateAll()
    generateAll()
    generateAll()
    generateAll()
    generateAll()
    generateAll()
    generateAll()
    generateAll()
    generateAll()
    generateAll()
    generateAll()
    generateAll()
