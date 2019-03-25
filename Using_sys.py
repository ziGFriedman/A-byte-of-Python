'''Модуль sys'''
import sys  #импортируем модуль sys

print('Аргумент командной строки:')
for i in sys.argv:
    print(i)

    print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')
