def single_root_words(root_word, *other_words):
    some_words = []
    for w in other_words:
        if root_word.lower() in w.lower() or w.lower() in root_word.lower():
            some_words.append(w)
    return some_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
