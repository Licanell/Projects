eng_alpha = "abcdefghijklmnopqrstuvwxyz"
eng_alpha_up = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
rus_alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_alpha_up = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

string = input("Введите текст ")
split_string = string.split(" ")

def russian_alpha_caeaser(index, string, num):
    if string[index].isupper():
        if ord(string[index]) + num > 1071:
            return chr(ord(string[index]) + num - 32)
        else:
            return chr(ord(string[index]) + num)
    elif string[index].islower():
        if ord(string[index]) + num > 1103:
            return chr(ord(string[index]) + num - 32)
        else:
            return chr(ord(string[index]) + num)

def english_alpha_caesar(string, num):
    if string.isupper():
        if ord(string) + num > 90:
            return chr(ord(string) + num - 26)
        else:
            return chr(ord(string) + num)
    elif string.islower():
        if ord(string) + num > 122:
            return chr(ord(string) + num - 26)
        else:
            return chr(ord(string) + num)



def remove_punct_translate(s: str) -> str:
    PUNCT = '.,:;!?—«»…–-()[]}{"\'`«»…'
    return s.translate(str.maketrans('', '', PUNCT))

def caesar(string):
    result = ""
    for word in split_string:
        for letter in range(len(word)):
            num = len(remove_punct_translate(word))
            if word[letter].isalpha():
                if word[letter] in rus_alpha or word[letter] in rus_alpha_up:
                    num = num % 32
                    result += russian_alpha_caeaser(word[letter], num)
                elif word[letter] in eng_alpha or word[letter] in eng_alpha_up:
                    num = num % 26
                    result += english_alpha_caesar(word[letter], num)
            else:
                result += word[letter]
        result += " "
    return result[:-1]

print(caesar(string))