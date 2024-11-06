# Однокоренные

def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for word in other_words:
        if root_word in word.lower():
            same_words.append(word)
    return same_words

result1 = single_root_words('dem', 'dEmon', 'dEMocracy', 'dimon', 'moDel')
result2 = single_root_words('un', 'uNpoPulaR', 'UnDying', 'dying', 'jUngle')

print(result1)
print(result2)