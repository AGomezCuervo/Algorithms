"""Binary search algorithm"""

import math
def bs_list(haystack, needle):
    """
    Realiza una búsqueda binaria en una lista ordenada.
    
    Busca el valor 'needle' en el array 'haystack'.
    Devuelve True si se encuentra el valor y False en caso contrario.
    """
    lower = 0
    higher = len(haystack)

    while lower < higher:
        medium = math.floor(lower + (higher - lower) / 2)
        value = haystack[medium]
        if value == needle:
            return True
        if value > needle:
            higher = medium
        else:
            lower = medium + 1
    return False

print(bs_list([1,2,3,4,5,6,7,8,9,10], 3))
