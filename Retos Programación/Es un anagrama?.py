"Estas palabras son un anagrama?"

def anagram(first_word, second_word):
    if first_word.lower() == second_word.lower():
        return False
    return sorted(first_word.lower()) == sorted(second_word.lower())

print(anagram("hola", "aloh"))