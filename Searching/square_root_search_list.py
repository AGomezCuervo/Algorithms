"""
squareroot search algorithm

Dadas dos bolas de cristal que se romperán si se dejan caer desde una distancia
lo suficientemente alta determinar el punto exacto en el que se romperá de la forma más
optimizada.
"""

import math
def two_crystal_balls (breaks):
    """
    Realiza una busqueda en un array de True and False
    
    """

    jmpAmount = math.floor(math.sqrt(len(breaks)))
    i = jmpAmount
    while i < len(breaks):
        if breaks[i]:
            break
        i += jmpAmount

    i -= jmpAmount
    for j in range(jmpAmount):
        if i < len(breaks) and breaks[i]:
            return i
        i += 1
    return -1   
