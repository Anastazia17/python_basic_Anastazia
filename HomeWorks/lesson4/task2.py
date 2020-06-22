# Add task2.py

my_list = [600, 2, 24, 12, 44, 1, 3, 899, 2, 1, 4, 10, 7, 1, 78, 123, 900, 69, 55, 117]
my_new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]

print(f'Исходный список: {my_list}')
print(f'Новый список: {my_new_list}')