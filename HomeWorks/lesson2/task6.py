# Add task6.py

products = []

while True:
    name = input('Введите название товара: ')
    cost = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    unit = input('Введите единицу измерения товара: ')

    new_product = {}

    new_product['name'] = name
    new_product['cost'] = cost
    new_product['quantity'] = quantity
    new_product['unit'] = unit

    products.append(new_product)
    reply = input('Добавить еще один товар? Да/Нет (д/н): ')
    if reply == 'н':
        break
    else:
        continue

products = list(enumerate(products, 1))
print('Полный список: ', products)

analytics = {}
names, costs, quantityes, unites = [], [], [], []

for i in range(len(products)):
    names.append(products[i][1].get('name'))
    costs.append(products[i][1].get('cost'))
    quantityes.append(products[i][1].get('quantity'))
    unites.append(products[i][1].get('unit'))

analytics['Наименование'] = names
analytics['Цена'] = costs
analytics['Количество'] = quantityes
analytics['Единицы измерений'] = list(set(unites))

print('Аналитика по товарам: ', analytics)