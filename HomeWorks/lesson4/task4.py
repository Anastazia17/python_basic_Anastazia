# Add task.4.py

my_list = [1, 1, 5, 2, 2, 6, 2, 7, 23, 1, 44, 56, 44, 3, 2, 9, 10, 10, 7, 4, 11, 77, 99, 99]
new_list = [el for el in my_list if my_list.count(el) < 2]

print(new_list)