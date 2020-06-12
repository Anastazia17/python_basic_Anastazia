# Add task2.py

var_time = int(input('Введите время в секундах: '))
var_hours = var_time // 3600
var_minutes = (var_time - var_hours * 3600) // 60
var_seconds = var_time - (var_hours * 3600 + var_minutes * 60)
print(f'Время в формате чч:мм:сс: {var_hours:02}:{var_minutes:02}:{var_seconds:02}')