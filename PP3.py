print("Программа для зашифровки и расшифровки методом Цезаря на русском или английском языках")
alpha1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
alpha2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def chek_eng(b):
    for m in range(0, len(b)):
        if b[m] not in alpha1:
            return False
    return True


def chek_ru(b):
    for m in range(0, len(b)):
        if b[m] not in alpha2:
            return False
    return True


def step_chek():
    while True:
        try:
            b = int(input("Введите шаг шифровки: "))
            return b
        except ValueError:
            print("Шаг должен быть циферками")


while True:
    try:
        a = int(input("Напишите 1 для зашифровки, напишите 2 для расшифровки, напишите 3 чтобы закончить: "))
    except ValueError:
        print("Вы ввели не ту цифру")
        continue
    if a == 1:
        word = input("Введиде слово для зашифровки: ")
        word = word.lower()
        if chek_eng(word):
            step = step_chek()
            if step > 25:
                step %= 25
            newword = ""
            for i in word:
                pos = alpha1.find(i)
                newpos = pos + step
                newword += alpha1[newpos]
            print("Ваше зашифрованное слово: " + newword)
        elif chek_ru(word):
            step = step_chek()
            if step > 32:
                step %= 32
            newword = ""
            for i in word:
                pos = alpha2.find(i)
                newpos = pos + step
                newword += alpha2[newpos]
            print("Ваше зашифрованное слово: " + newword)
        else:
            print("Вы ввели не слово")
    elif a == 2:
        word = input("Введиде слово для расшифровки: ")
        word = word.lower()
        if chek_eng(word):
            step = step_chek()
            if step > 25:
                step %= 25
            newword = ""
            for i in word:
                pos = alpha1.find(i)
                newpos = pos - step
                newword += alpha1[newpos]
            print("Ваше расшифрованное слово: " + newword)
        elif chek_ru(word):
            step = step_chek()
            if step > 32:
                step %= 32
            newword = ""
            for i in word:
                pos = alpha2.find(i)
                newpos = pos - step
                newword += alpha2[newpos]
            print("Ваше расшифрованное слово: " + newword)
        else:
            print("Вы ввели не слово")
    elif a == 3:
        break
    else:
        print("Вы ввели не ту цифру")
