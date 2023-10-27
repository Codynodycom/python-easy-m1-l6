'''
Задача 5

Оптимизируй код программы

Бо решил посмотреть один из вебинаров по программированию и улучшить свои навыки. Однако он заметил что сайт для просмотра вебинаров недоступен, даже учитывая то что у него уже был аккаунт на этом сайте.
Данные пользователей записаны в формате логин : пароль.
Бо залез в код программы и нашел в нем сложный для чтения код, оптимизируй работу программы упростив код.

'''

accaunt1 = "superAccaunt : superPassword"
accaunt2 = "notHere : NotHere"
accaunt3 = "dreamer444 : 4645212"
accaunt4 = "BO : MySuperPassword"

login = input("Введи свой логин: ")
password = input("Введи свой пароль: ")

if (login in accaunt1 and password in accaunt1) or (login in accaunt2 and password in accaunt2) or (login in accaunt3 and password in accaunt3) or (login in accaunt4 and password in accaunt4):
    print("Вы вошли!")
else:
    print("Доступ закрыт!")

