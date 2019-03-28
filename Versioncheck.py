'''Проверяет версию Python'''
import sys, warnings
if sys.version_info[0] < 3:
    warnings.warn('Для выполнения программы необходима как минимум \
    вурсия Python 3.0', RuntimeWarning)
else:
    print('Нормальное продолжение')
