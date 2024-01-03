# Task_1

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

# Task_2

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []

for i in my_list:
    if i.isdigit():
        new_list.extend(['"', f'{int(i):02}', '"'])
    elif (i.startswith('+') or i.startswith('-')) and i[1].isdigit():
        new_list.extend(['"', f'{i[0]}{int(i[1]):02}', '"'])
    else:
        new_list.append(i)
result = ' '.join(new_list)
print(result)

# Task_4

people = [
    'инженер-конструктор Игорь', 
    'главный бухгалтер МАРИНА', 
    'токарь высшего разряда нИКОЛАй', 
    'директор аэлита'
]
for i in people:
    print(f'Привет, {i.split()[-1].capitalize()}!')

# Task_5
    
price = [25.07, 36.98, 12.35, 77, 49,99, 53,15, 92]
print(id(price))
print(price)
price.sort()
print(id(price))
print(price)

new_price = []
for x in price:
    rub = int(x)
    kop = (x - rub) * 100
    print(f'{rub} рублей {kop:02.0f} копеек', end=', ')


