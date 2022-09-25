print("Программа для зашифровки и расшифровки методом Цезаря на русском или английском языках")
alpha1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
alpha2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
while True:
    a = int(input("Напишите 1 для зашифровки, напишите 2 для расшифровки, напишите 3 чтобы закончить: "))
    if a == 1:
        word = input("Введиде слово для зашифровки: ")
        word = word.lower()
        if word[0] in alpha1:
            step = int(input("Введите шаг шифровки: "))
            if step > 25:
                step %= 25
            newword = ""
            for i in word:
                pos = alpha1.find(i)
                newpos = pos + step
                newword += alpha1[newpos]
            print("Ваше зашифрованное слово: " + newword)
        elif word[0] in alpha2:
            step = int(input("Введите шаг шифровки: "))
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
        if word[0] in alpha1:
            step = int(input("Введите шаг шифровки: "))
            if step > 25:
                step %= 25
            newword = ""
            for i in word:
                pos = alpha1.find(i)
                newpos = pos - step
                newword += alpha1[newpos]
            print("Ваше расшифрованное слово: " + newword)
        elif word[0] in alpha2:
            step = int(input("Введите шаг шифровки: "))
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