number_of_quatro = int(input('Введите номер четверти: '))

if number_of_quatro == 1:
    print("X > 0 and Y > 0")
elif number_of_quatro == 2:
    print("X < 0 and Y > 0")
elif number_of_quatro == 3:
    print("X < 0 and Y < 0")
elif number_of_quatro == 4:
    print("X > 0 and Y > 0")
else:
    print('такой четверти нет.')