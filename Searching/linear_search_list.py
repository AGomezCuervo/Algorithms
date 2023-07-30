"""Linear search algorithm"""

def linear_search(haystack, needle):
    """
    Busca el valor 'needle' en el array 'haystack'.
    Devuelve True si se encuentra el valor y False en caso contrario.
    """
    for i in haystack:
        if haystack[i] == needle:
            return True
    return False


print(linear_search([1,2,3,4,5,6,7,8,9,10], 10))
