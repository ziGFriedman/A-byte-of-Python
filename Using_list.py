'''Работа со списками'''
shoplist = ['яблоки','манго','морковь','бананы']

print ('Я должен сделать ', len(shoplist), 'покупок.')

print ('Покупки:', end=' ')  #Выводит список через пробел, а не в новой строке
for item in shoplist:
    print (item, end=' ')

print ('\nТакже нужно купить риса.')
shoplist.append('рис')              #добавляет к концу списка элемент
print ('Теперь мой писок покупок таков:', shoplist)

print ('Отсортирую-ка я свой список')
shoplist.sort()
print ('Отсортированный список покупок выглядит так:', shoplist)

print ('Первое, что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]

print ('Я купил', olditem)
print ('Теперь мой список покупок:', shoplist)
