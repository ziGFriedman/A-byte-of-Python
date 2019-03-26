'''Сохранение объекта в файл'''
import pickle

# имя файла в котором мы сохраняем объект
shoplistfile = 'shoplist.data'
# список покупок
shoplist = ['Яблоко', 'манго','морковь']

# запиь в файла
f = open(shoplistfile, 'wb')   # 't' - текстовой ввод, 'b' - бинарный
pickle.dump(shoplist, f) # помещаем объект в файла
f.close()

del shoplist    # уничтожает переменную shoplist
# Считываем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)    # загружаем объект из файла
print(storedlist)
