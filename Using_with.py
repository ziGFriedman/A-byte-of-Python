'''Действиие оператора with'''
with open('poem.txt') as f:
    for line in f:
        print(line, end='')
