#Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#    *Примеры:*
    
#    - 6,78 -> 7
#    - 5 -> нет
#    - 0,34 -> 3


n = float(input('Enter number '))

if (int(n) == n):
    print('no')
else:
    print(int(abs(n) * 10) % 10)


number = float(input('Введите вещественное число: '))

if number != int(number):
    print(f'Первая цифра дробной части числа {number} -> {int(abs(number*10))%10}')
else:
    print(f'У числа {int(number)} нет дробной части')


number = input('Введите вещественное число: ')

number = number.split('.')
print(number[1][0])



number = input('Введите вещественное число: ')

number = number.split('.')
if len(number) > 1:
    print(number[1][0])
else:
    print('Целое число')
    # some comment