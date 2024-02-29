"""
Write a function that receive any word as param and return all 
unique his letters (without repeat) but in alphabetical order.
"""

def get_unique_letters(word):
    """
    Get unique letters of word in alphabetic order.
    """
    list_letters = []
    final_list = []
    aux = ""
    for i in word.lower():
        list_letters.append(i)
    list_letters.sort()
    for char in list_letters:    
        if aux != char :
            aux = char
            final_list.append(aux)
    return final_list


print(get_unique_letters("PERRITO"))
