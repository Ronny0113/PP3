print("Программа для зашифровки и расшифровки методом Цезаря на русском или английском языках")
alpha1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"  # английский алфавит
alpha2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # русский алфавит


def chek_eng(b):  # функции для проверки на принадлежность всех слов к одному из алфавитов
    for m in range(0, len(b)):
        if b[m] not in alpha1:
            return False
    return True


def chek_ru(b):
    for m in range(0, len(b)):
        if b[m] not in alpha2:
            return False
    return True


def step_chek():  # обработчик ошибки ввода шага шифровки
    while True:
        try:
            b = int(input("Введите шаг шифровки: "))
            return b
        except ValueError:
            print("Шаг должен быть циферками")


while True:  # цикл, который не позволяет программе завершиться до решения пользователя
    try:  # обработка ошибки ввода
        a = int(input("Напишите 1 для зашифровки, напишите 2 для расшифровки, напишите 3 чтобы закончить: "))
    except ValueError:
        print("Вы ввели не ту цифру")
        continue
    if a == 1:  # если надо шифровать
        word = input("Введиде слово для зашифровки: ")
        word = word.lower()  # если ввели заглавными буквами
        if chek_eng(word):  # если слово на английском
            step = step_chek()
            if step > 25:  # если шаг больше алфавита (дальше аналогично)
                step %= 25
            newword = ""
            for i in word:
                pos = alpha1.find(i)  # ищем нужную буковку
                newpos = pos + step  # прибавляем к буковке шаг шифровки
                newword += alpha1[newpos]  # записываем новую букву в новое слово (дальше аналогично)
            print("Ваше зашифрованное слово: " + newword)
        elif chek_ru(word):  # если слово на русском
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
            print("Вы ввели не слово")  # если буков нет в русском алфавите, или в слове есть цифры
    elif a == 2:  # если надо расшифровать
        word = input("Введиде слово для расшифровки: ")
        word = word.lower()
        if chek_eng(word):
            step = step_chek()
            if step > 25:
                step %= 25
            newword = ""
            for i in word:
                pos = alpha1.find(i)
                newpos = pos - step  # в этом случае вычитаем шаг
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
    elif a == 3:  # если пользователь решил закончить
        break
    else:
        print("Вы ввели не ту цифру")
