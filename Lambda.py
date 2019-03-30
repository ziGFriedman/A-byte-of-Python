'''Lambda - формы'''
points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)
# Сортировка по собственному признаку, через lambda, которая
# используется только в этом месте 
