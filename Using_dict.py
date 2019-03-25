'''Работа со словарём'''
# "ab" - сокращение от 'a'ddress 'b'ook
ab = {'Swaroop'  : 'swaroop@swaroopch.com',
      'Larry'    : 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer'  : 'spammer@hotmail.com'
      }         # Словарь

print ('Адрес Swaroop\'a:',ab['Swaroop'])

del ab['Spammer']
# Удаление пары ключ-значение

print ('\nВ адресной книге {0} контактов\n'.format(len(ab)))

for name, address in ab.items():
    print ('Контакт {0} с адресом {1}'.format(name, address))

ab['Guido'] = 'guido@python.org'
#Добавление пары ключ-значение

if 'Guido' in ab:
    print ('\nАдрес Guido:', ab['Guido'])
