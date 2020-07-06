# Add task3.py

with open('test4.txt', encoding='UTF-8') as my_f, open('test4_new.txt', 'w', encoding='UTF-8') as new_file:

    for el in my_f:
        if 'One' in el:
            el = el.replace('One', 'Один')
        elif 'Two' in el:
            el = el.replace('Two', 'Два')
        elif 'Three' in el:
            el = el.replace('Three', 'Три')
        elif 'Four' in el:
            el = el.replace('Four', 'Четыре')
        print(el, end='', file=new_file)