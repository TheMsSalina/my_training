def single_root_words(root_word, *other_words):
    same_words = []
    word = list(other_words) #перебираем other_words и вписываем элементы в список word
    for i in range(len(word)): #перебираем символы в word до конца строки
        if root_word.lower() in word[i].lower() or word[i].lower() in root_word.lower(): #убрираем зависимость от регистра
            same_words.append(word[i]) #добавляем найденное однокоренное в список
    return (same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)