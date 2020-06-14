# Add task6.py

a = int(input('Введите результат пробежки за 1-й день в км: '))
b = int(input('Введите общий желаемый результат в км: '))
result_days = 1
result_km = a
while result_km < b:
        a = a + a // 10
        result_days += 1
        result_km = result_km + a
print(f'Вы достигнете желаемый результат на %.d' '-й день.' % result_days)