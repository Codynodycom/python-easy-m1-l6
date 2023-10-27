# m1l2t2.py
import os


def create_lessons(part):
  global lesson_counter, path, path_2, folder_name

  if part == 1:
    for i in range(1, lesson_counter+1):
      absolute_path = f'{path}/{folder_name}{i}'
      os.mkdir(absolute_path)
    print('part 1 folders created')

  elif part == 2:
    for i in range(1, lesson_counter+1):
      absolute_path = f'{path_2}/{folder_name}{i}'
      os.mkdir(absolute_path)
    print('part 2 folders created')


def part_1():
  global module, lesson, task, lesson_counter
  
  # part 1
  for i in range(1, lesson_counter+1):
    file_name = f'm{module}l{lesson}t{task}.py'
    full_path = f'{path}/{folder_name}{i}/{file_name}'
    md_path = f'{path}/{folder_name}{i}/task.md'
    
    with open(full_path, 'w', encoding='utf-8') as f:
      f.write(text.format(task))

    with open(md_path, 'w', encoding='utf-8') as f:
      f.write('')

    task += 1
    
  print('part 1 created')


def part_2():
  global module, lesson, task, lesson_counter, text

  # part 2
  for i in range(1, lesson_counter+1):
    file_name = f'm{module}l{lesson}t{task}.py'
    full_path = f'{path_2}/{folder_name}{i}/{file_name}'
    md_path = f'{path_2}/{folder_name}{i}/task.md'

    with open(full_path, 'w', encoding='utf-8') as f:
      f.write(text.format(task))

    with open(md_path, 'w', encoding='utf-8') as f:
      f.write('')
      
    task += 1
    
  print('part 2 created')


path = 'tasks. part 1'
path_2 = 'tasks. part 2'
folder_name = 'task '

task = 1
lesson_counter = 1

text = """'''
Задача {}



'''



"""

module = int(input('Номер модуля: '))
lesson = int(input('Номер урока: '))
user = input('part 1/2 ?\n')

if user == '1':
  lesson_counter = int(input('количество задач: '))
  create_lessons(1)
  part_1()
elif user == '2':
  lesson_counter = int(input('количество задач: '))
  create_lessons(2)
  part_2()

input()
