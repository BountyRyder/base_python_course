# 1 exercise
number_1 = input('Введите число от 1 до 9: ')
word_1 = input('Введите букву: ')
print(word_1)
print(number_1)

# 2 exercise
time = int(input('Введите время в секундах: '))
time_hours = time // 3600
time_minutes = (time - time_hours * 3600) // 60
time_seconds = time - (time_hours * 3600 + time_minutes * 60)
print(f'Время в формате чч:мм:сс {time_hours} : {time_minutes} : {time_seconds}')

# 3 exercise
number_2 = int(input('Введите число от 0 до 9: '))
summ_numbers = (number_2 + int(str(number_2) + str(number_2)) + int(str(number_2) + str(number_2) + str(number_2)))
print('Сумма чисел равна: ' + str(summ_numbers))

# 4 exercise
number_3 = abs(int(input('Введите целое положительное число ')))
max = number_3 % 10
while number_3 >= 1:
    number_3 = number_3 // 10
    if number_3 % 10 > max:
        max = number_3 % 10
    if number_3 > 9:
        continue
    else:
        print('Максимальная цифра в числе ', max)
        break
# 5 exercise
profit = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержку фирмы: '))
if profit > costs:
    print(f'Фирма работает с прибылью. Рентабильность выручки составила {profit / costs:.2f}')
    workers = int(input('Введите количество сотрудников фирмы '))
    print(f'прибыль в расчёте на одного сотрудника составила {profit / workers:.2f}')
elif profit == costs:
    print('Фирма работает в ноль')
else:
    print('Фирма работает в убыток')

# 6 exersice
a = int(input('Введите результат пробежки первого дня в км: '))
b = int(input('Введите общий желаемый результат в км: '))
result_days = 1
result_km = a
while result_km < b:
    a = a + 0.1 * a
    result_days += 1
    result_km = result_km + a
print(f'Вы достигнете требуемых показателей на %.d день' % result_days)

