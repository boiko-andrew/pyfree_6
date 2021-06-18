def count_letter(input_words, input_letter):
    letter_qty = 0
    for input_word in input_words:
        if input_word.find(input_letter) >= 0:
            letter_qty += 1
    return letter_qty


words = []
while True:
    word = input("Введите слово: ")
    if len(word) == 0:
        break
    word = word.lower()
    words.append(word)

letter = input("Введите букву для поиска: ")
if len(letter) > 1:
    letter = letter[0]
letter = letter.lower()

qty = count_letter(words, letter)
print("Буква {0} в списке {1} найдена в {2} слове(ах)".format(letter, words, qty))
input("Нажмите Enter для продолжения: ")
