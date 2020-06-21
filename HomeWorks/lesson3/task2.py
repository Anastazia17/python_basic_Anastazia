# Add task2.py

def user_data_func():

    name = input('Введите Ваше имя: ')
    surname = input('Введите Вашу фамилию: ')
    year_of_birth = input('Введите год Вашего рождения: ')
    city = input('Введите Ваш город проживания: ')
    email = input('Введите Ваш e-mail: ')
    telephone = input('Введите Ваш телефон: ')

    print (f'{surname} {name} {year_of_birth} года рождения из города {city}. Контакты для связи: {email} {telephone}')

user_data_func()