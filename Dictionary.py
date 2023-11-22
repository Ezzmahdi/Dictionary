from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input('Enter your word: ')
    if word == '':
        break
    else:
        print(dictionary.meaning(word))