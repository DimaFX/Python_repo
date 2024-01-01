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
    elif i.endswith('+') or i.endswith('-'):
        new_list.extend(['"', f'{i[1]:02}', '"'])
    else:
        new_list.append(i)
print(new_list)

#new_list = ' '.join(my_list)
#print(new_list)

