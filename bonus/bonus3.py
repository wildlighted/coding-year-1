line = input('Введите фразу на английском: ')
words = line.split(' ')
vowels = set('aeiouyAEIOUY')
pig = ''
for word in words:
    k = 0
    for letter in word:
        if letter in vowels:
            pword = word[k:] + word[:k] + 'ay'
            break
        k += 1
    pig = pig + ' ' + pword
print(pig)

# я пока не разобралась с капитализацией (чтобы в выводе фразы первая буква была заглавная
# и если ввод начинается с заглавной то не было ее в середине слова
# надеюсь это не критично, я разберусь
# еще я пробовала вывод строить объединением списка, все получалось, но терялись смайлики в конце через пробел :)
# так что пока я оставила конкатенацию
