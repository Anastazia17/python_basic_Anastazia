# Add task6.py

with open('test6.txt', 'r+', encoding='UTF-8') as my_f:
    subjects = []
    hours = []

    for line in my_f:
        line_list = line.split()
        subj_name = line_list[0]
        subj_name = subj_name[0:subj_name.index(':')]
        subjects.append(subj_name)
        result = 0

        for el in line_list[1:]:
            if '(' in el:
                el = el[0:el.index('(')]
                result += int(el)
        hours.append(result)

education_dict = {subjects[i]:hours[i] for i in range(len(subjects))}
print(education_dict)