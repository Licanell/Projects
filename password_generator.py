import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
non_ordinary = "il1Lo0O"
pool = [digits, lowercase_letters, uppercase_letters, punctuation, non_ordinary]
password_count = int(input("Укажите количество паролей "))
password_len = int(input("Укажите длину пароля "))
print("В следующих двух вопросах укажите 'да' либо оставьте пустым")
if input("Добавлять ли в пароль символы '!#$%&*+-=?@^_'? ") == "да":
    include_punctuation = True
else:
    include_punctuation = False

if input("Добавлять ли в пароль неординарные символы 'il1Lo0O'? ") == "да":
    include_non_ordinary = True
else:
    include_non_ordinary = False

def generator(length, count):
    passwords_to_return = []
    if include_non_ordinary == True and include_punctuation == False:
        pool.remove(punctuation)
    elif include_non_ordinary == False and include_punctuation == True:
        pool.remove(non_ordinary)
    elif include_non_ordinary == False and include_punctuation == False:
        pool.remove(non_ordinary)
        pool.remove(punctuation)

    for i in range(count):
        password = ""
        for i in range(length):
            password += random.choice(random.choice(pool))
        passwords_to_return.append(password)
    #return "\n".join([f'{i+1}: {passwords_to_return[i]}' for i in range(count)])
    return passwords_to_return

result = generator(password_len, password_count)

with open("passwords.txt", "w") as file:
    for item in result:
        file.write(item + '\n')