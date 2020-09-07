#1
def div(*args):
    try:
        arg1 = int(input('Введите первое число '))
        arg2 = int(input('Введите второе число '))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка значения '
    except ZeroDivisionError:
        return 'Ошибка. Нельзя делить на ноль! '
    return res
print(f'result  {div()}')

#2
name = input('enter name')
surname = input('enter surname')
year = input('enter year')
city = input('enter city')
email = input('enter email')
telephone = input('input telephone')
def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(name, surname, year, city, email,telephone))

#3
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("Введите первый аргумент ")), int(input("Введите второй аргумент ")), int(input("Введите третий аргумент ")))}')

#4


#5
def my_sum():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите числа или Q для выхода - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Верная сумма равна {sum_res}')
    print(f'Ваша конечная сумма равна {sum_res}')

my_sum()

#6
def int_func (*args):
    word = input("Введите слово из маленьких латинских букв ")
    print(word.title())
    return
int_func()



