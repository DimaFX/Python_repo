# Task_1

duration = int(input('enter seconds: '))
days = duration // 86400
hours = duration % 86400 // 3600
minutes = duration % 86400 % 3600 // 60
seconds = duration % 60

print(f'd:{days}, h:{hours}, m:{minutes}, s:{seconds}')

# Task_2
def s_digit(num):
    s = 0
    for i in str(num):
        s += int(i)
    return s


my_list = []
for n in range(1, 1001, 2):
    my_list.append(n ** 3)
total = 0
total_2 = 0
for x in my_list:
    if s_digit(x) % 7 == 0:
        total += x
for y in my_list:
    y += 17
    if s_digit(y) % 7 == 0:
        total_2 += y
print(total)
print(total_2)

# Task_3

for z in range(1, 101):
    if z % 10 == 1 and z != 11:
        r = 'процент'
    elif 1 < z < 5:
        r = 'процента'
    else:
        r = 'процентов'
    print(z, r)






