'''
Задача 7

Описание задачи в файле task.md

'''

candidate_name  = input("Ваше имя: ")
candidate_age = int(input("Ваш возраст: "))
candidate_rating = int(input("Ваш рейтинг в академии: "))

if candidate_age > 18 and candidate_rating > 150:
    print("Кандидат", candidate_name, "допускается к участию!")
else:
    print("Кандидат", candidate_name, "не допускается к участию!")

