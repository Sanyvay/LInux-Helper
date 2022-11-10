import os
import string
import webbrowser
import secrets
print("Select your Language\nВыберите ваш язык\n1.English\n2.Русский\n3.Azərbaycanca\n4.Україньска\nСделано с <3 от WinslerStudio\nMade with <3 by WinslerStudio\nWinslerStudio tərəfindən <3 hazirlanib\nЗроблено з <3 від WinslerStudio")
language=int(input())
if language == 1:
    print("Welcome to Linux Helper!\nWhat you want to do?\n1.Show information about your OS and computer\n2.Full upgrade your system\n3.Free up disk space\n4.Visit developer's channel\n5.Generate strong passowrd(beta)\n6.Exit")
elif language == 2:
    print("Добро пожаловать в Linux Helper!\nЧто вы хотите сделать?\n1.Показать информацию вашей ОС и компьютера\n2.Полностью обновить вашу систему\n3.Освободить место на диске\n4.Посетить канал разработчика\n5.Сгенерировать надёжный пароль(бета)\n6.Выход")
elif language == 3:
    print("Linux köməkçi-yə xoş gəlmisiniz!\nNə etmək istəyirsiniz?\n1.Sistem və kompüter məlumatlarinizi göstərin\n2.Sisteminizi tamamilə yeniləyin\n3.Disk yerini boşaltin\n4.Developer kanalına baş çəkin\n5.Güclü parol yaradın(beta)\n6.Çixiş")
elif language == 4:
    print("Вітаємо в Linux Helper!\nЩо ви хочете зробити?\n1.Показати інформацію про ПЗ та компьютера\n2.Повністью оновити вашу систему\n3.Звільнити місце на дискі\n4.Відвідати канал розробника\n5.Згенерувати надійний пароль(бета)\n6.Вихід")
action = int(input())
while action != 5:
        if action == 6 and language == 1:
            print("Goodbye!")
            break
        if action == 6 and language == 2:
            print("Пока!")
            break
        elif action == 6 and language == 3:
            print("Gulə gulə!")
            break
        elif action == 6 and language == 4:
            print("До побачення!")
            break
        if action == 1:
            os.system("neofetch")
        if action == 2:
            os.system("apk update && apk upgrade")
        if action == 3 and language == 1:
            print("Sorry, but this function no avable for Alpine Linux!")
        if action == 3 and language == 2:
            print("Извините, но эта функция недоступна для Alpine Linux")
        elif action == 3 and language == 3:
            print("Üzr istəyirik, lakin bu funksiya Alpine Linux üçün mövcud deyil")
        elif action == 3 and language == 4:
            print("Вибачте, але ця функція недоступна для Alpine Linux")
        if action == 4:
            webbrowser.open_new("https://t.me/WinslerStudio")
        if action == 656345:
          try:
             os.system("curl parrot.live") 
          except:
             print ("Установите curl (apk add curl)")
        if action == 145673:
            webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        if language == 1:
            print("What you want to do?\n1.Show information about your OS and computer\n2.Full upgrade your system\n3.Free up disk space\n4.Visit developer's channel\n5.Generate strong passowrd(beta)\n6.Exit")
        if language == 2:
            print("Что вы хотите сделать?\n1.Показать информацию вашей ОС и компьютера\n2.Полностью обновить вашу систему\n3.Освободить место на диске\n4.Посетить канал разработчика\n5.Сгенерировать надёжный пароль(бета)\n6.Выход")
        if language == 3:
            print("Nə etmək istəyirsiniz?\n1.Sistem və kompüter məlumatlarinizi göstərin\n2.Sisteminizi tamamilə yeniləyin\n3.Disk yerini boşaltin\n4.Developer kanalına baş çəkin\n5.Güclü parol yaradın(beta)\n6.Çixiş")
        if language == 4:
            print("Що ви хочете зробити?\n1.Показати інформацію про ПЗ та компьютера\n2.Повністью оновити вашу систему\n3.Звільнити місце на дискі\n4.Відвідати канал розробника\n5.Згенерувати надійний пароль(бета)\n6.Вихід")
        action = int(input()) 
if action == 5:
    letters = string.hexdigits
    digits = string.digits
    special_chars = string.ascii_uppercase
    alphabet = letters + digits + special_chars
    pwd_length = 12
    pwd = ''
    for i in range(pwd_length):
      pwd += ''.join(secrets.choice(alphabet))
    print("Password:",pwd)
    if language == 1:
        print("Please restart Linux Helper")
    if language == 2:
        print("Пожалуйста перезагрузите Linux Helper")
    if language == 3:
        print("helpaurora komanda ilə Linux Helper-i yenidən başladın!")
    if language == 4:
        print("Будь ласка перезавантажте Linux Helper")