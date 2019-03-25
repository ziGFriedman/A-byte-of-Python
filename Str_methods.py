'''Методы строк'''
name = 'Swaroop'
#Это объект строки
if name.startswith('Swa'):
    print('Да, строка начинается на "Swa"')
# startswith - начинается ли строка с некоторой заданной подстройки
if 'a' in name:
    print('Да, она содержиит строку "а"')
# in - являетяс ли некоторая строка частью данной строки.
if name.find('war') != -1:
    print('Да, она содержит строку "war"')
# find - для определения позиции данной подстройки в строке, возвращает -1, если подстройка не обнаружена
delimiter='_*_'

mylist = ['Бразилия','Россия','Индия','Китай']
print(delimiter.join(mylist))
# join - метод объединения элементов последовательности с указанной в качестве
#разделителя между элементами, возвращяющий большую строку, сгенерированную таким образом