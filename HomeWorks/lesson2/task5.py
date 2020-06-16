# Add task5.py

rating = [7, 5, 3, 3, 2]
print(f'Начальный рейтинг: {rating}')
new_rating = int(input('Введите Вашу оценку рейтинга: '))

while True:
    for el in range(len(rating)):
        if rating[el] == new_rating:
            rating.insert(el + 1, new_rating)
            break
        elif rating[0] < new_rating:
            rating.insert(0, new_rating)
        elif rating[-1] > new_rating:
            rating.append(new_rating)
        elif rating[el] > new_rating and rating[el + 1] < new_rating:
            rating.insert(el + 1, new_rating)
    print(f'Текущий рейтинг: {rating}')
    new_rating = int(input('Введите следующую оценку рейтинга: '))