x_coord = float(input('Введите координату X: '))
y_coord = float(input('Введите коордианту Y: '))
if x_coord == 0 or y_coord == 0:
    print('Точка находится на оси координат.')
elif x_coord > 0 and y_coord > 0:
    print('точка лежит в первой четверти.')
elif x_coord < 0 and y_coord > 0:
    print('точка лежит во второй четверти.')
elif x_coord < 0 and y_coord < 0:
    print('точка лежит в третьей четверти.')
elif x_coord > 0 and y_coord < 0 :
    print('точка лежит в четвертой четверти.')
    