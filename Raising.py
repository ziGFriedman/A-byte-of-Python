'''Вызов исключения'''
class ShortInputException(Exception):
    '''Пользовательский класс исключения.'''
    def __init__(self, lenght, atleast):
        Exception.__init__(self)
        self.lenght = lenght
        self.atleast = atleast

try:
    text = input('Введите что-нибудь --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
        # Здесь может происходить обычная работа
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except ShortInputException as ex:
    print('ShortInputException: Длина введённой строки -- {0}; \
           ожидалось, как минимум, {1}'.format(ex.lenght, ex.atleast))
else:
    print('Не было исключений.')
