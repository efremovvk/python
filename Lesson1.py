# Lesson 01
# Task 01

name = 'Valeriy'
region = 77
age = 34
somefloat = 20.7765
surname = input ('Введите фамилию: ')
age = input ('Введите возраст: ')
print (f'Имя и фамилия: {name} {surname}. Возраст: {age}. Регион: {region}. Какое-то число : {somefloat} ')


# Task 02
seconds = int( input ('Введите время в секндах: ') )
minutes = seconds // 60
seconds = seconds - (minutes * 60)
hours = minutes // 60
minutes = minutes - (hours * 60)
seconds = "%02d" % (seconds) # Чтобы секунды и минуты до 10 печатались с 0. 01 02 03...
minutes = "%02d" % (minutes)
print (f'Форматированое время: {hours}:{minutes}:{seconds}')

# Task 03
n = input ('Введите число: ')
nn = n + n
nnn = n + n + n
n = int (n)
nn = int (nn)
nnn = int (nnn)
sum = n + nn + nnn
print (f'{n} + {nn} + {nnn} = {sum}')

# Task 04
big = 0
number = int(input('Введите целое положительное число: '))
while number > 0:
    left = (number // 10) * 10
    current = number - left
    if big < current :
        big = current
    number = number // 10
print(f'Самая большая цифра в числе:  {big}')

# Task 05
receipt = float(input('Введите размер выручки: '))
charge = float(input('Введите размер расходов: '))
profit = receipt - charge
if profit > 0:
    print('Прибыль — выручка больше издержек')
    workers = int(input('Какова численность сотрудников фирмы? :'))
    forone = profit / workers
    print(f'Прибыль фирмы в расчете на одного сотрудника: {forone:.2f}')
elif profit < 0:
    print('Убыток — издержки больше выручки')
else:
    print('Прибыль и выручка равны')

# Task 06
day = 1
first = float(input('Результат первого дня: '))
last  = float(input('Итоговый результат: '))
km = first
while km < last:
    print(f'{day}-й день: {km:.3f}')
    km = km * 1.1
    day = day + 1
print(f'{day}-й день: {km:.3f}')
print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {first} км.')