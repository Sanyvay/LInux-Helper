import os
import string
import webbrowser
import secrets
print("Select your Language\nВыберите ваш язык\n1.English\n2.Русский\n3.Azərbaycanca\n4.Україньска\nСделано с <3 от WinslerStudio\nMade with <3 by WinslerStudio\nWinslerStudio tərəfindən <3 hazirlanib\nЗроблено з <3 від WinslerStudio")
language=int(input())
if language == 1:
    print("Welcome to Linux Helper Lite!\nWhat you want to do?\n1.Show information about your OS and computer\n2.Visit developer's channel\n3.Generate strong passowrd(beta)\n4.Exit")
elif language == 2:
    print("Добро пожаловать в Linux Helper Lite!\nЧто вы хотите сделать?\n1.Показать информацию вашей ОС и компьютера\n2.Посетить канал разработчика\n3.Сгенерировать надёжный пароль(бета)\n4.Выход")
elif language == 3:
    print("Linux köməkçi-yə xoş gəlmisiniz!\nNə etmək istəyirsiniz?\n1.Sistem və kompüter məlumatlarinizi göstərin\n2.Developer kanalına baş çəkin\n3.Güclü parol yaradın(beta)\n4.Çixiş")
elif language == 4:
    print("Вітаємо в Linux Helper Lite!\nЩо ви хочете зробити?\n1.Показати інформацію про ПЗ та компьютера\n2.Відвідати канал розробника\n3.Згенерувати надійний пароль(бета)\n4.Вихід")
action = int(input())
while action != 3:
        if action == 4 and language == 1:
            print("Goodbye!")
            break
        if action == 4 and language == 2:
            print("Пока!")
            break
        elif action == 4 and language == 3:
            print("Gulə gulə!")
            break
        elif action == 4 and language == 4:
            print("До побачення!")
            break
        if action == 1:
            os.system("neofetch")
        if action == 2:
            webbrowser.open_new("https://t.me/WinslerStudio")
        if action == 656345:
            os.system("curl parrot.live")
        if action == 145673:
            webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        if language == 1:
            print("Welcome to Linux Helper!\nWhat you want to do?\n1.Show information about your OS and computer\n2.Visit developer's channel\n3.Generate strong passowrd(beta)\n4.Exit")
        if language == 2:
            print("Добро пожаловать в Linux Helper!\nЧто вы хотите сделать?\n1.Показать информацию вашей ОС и компьютера\n2.Посетить канал разработчика\n3.Сгенерировать надёжный пароль(бета)\n4.Выход")
        if language == 3:
            print("Linux köməkçi-yə xoş gəlmisiniz!\nNə etmək istəyirsiniz?\n1.Sistem və kompüter məlumatlarinizi göstərin\n2.Developer kanalına baş çəkin\n3.Güclü parol yaradın(beta)\n4.Çixiş")
        if language == 4:
            print("Вітаємо в Linux Helper!\nЩо ви хочете зробити?\n1.Показати інформацію про ПЗ та компьютера\n2.Відвідати канал розробника\n3.Згенерувати надійний пароль(бета)\n4.Вихід")
        action = int(input()) 
if action == 3:
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
        print("Please restart «Linux Helper»!")
    if language == 2:
        print("Пожалуйста перезагрузите «Linux Helper»!")
    if language == 3:
        print("«Linux Helper-i» yenidən baş!")
    if language == 4:
        print("Будь ласка перезавантажте «Linux Helper»") 