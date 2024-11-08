first = int(input('Введите первое число: '))
second = int(input('Введите второе  число: '))
third = int(input('Введите третье число: '))

if first == second == third:
    print('Равных чисел: ' '3')
elif first == second or first == third:
    print('Равных чисел: ' '2')
else:
    print(first != second != third, 'Равных чисел: 0')
