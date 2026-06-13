eng_alpha = "abcdefghijklmnopqrstuvwxyz"
eng_alpha_up = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
rus_alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_alpha_up = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

type = input("Введите 'encode' или 'decode' для шифровки и, соответственно расшифровки текста ")

sdvig = int(input("Введите длину сдвига "))

string = input("Введите текст ")

if type == 'decode':
    sdvig = -sdvig

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

def english_alpha_caesar(index, string, num):
    if string[index].isupper():
        if ord(string[index]) + num > 90:
            return chr(ord(string[index]) + num - 26)
        else:
            return chr(ord(string[index]) + num)
    elif string[index].islower():
        if ord(string[index]) + num > 122:
            return chr(ord(string[index]) + num - 26)
        else:
            return chr(ord(string[index]) + num)

def caesar(num, string):
    result = ""
    for i in range(len(string)):
        num = sdvig
        if string[i].isalpha():
            if string[i] in rus_alpha or string[i] in rus_alpha_up:
                num = num % 32
                result += russian_alpha_caeaser(i, string, num)
            elif string[i] in eng_alpha or string[i] in eng_alpha_up:
                num = num % 26
                result += english_alpha_caesar(i, string, num)
        else:
            result += string[i]
    return result

print(caesar(sdvig, string))