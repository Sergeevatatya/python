#6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#Примеры строк файла:
#Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —

#Пример словаря:
#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def count_lessons(lesson):
    if lesson != '-':
        return int(lesson.split('(')[0])
    return 0

def sum_lessons(lessons):
    return sum([count_lessons(lesson) for lesson in lessons])

with open('files6/txt6', 'r') as f:
    lines = f.readlines()
    subj = {}
    for line in f:
        subject, *lessons = line.strip().split()
        subj[subject.split(':')[0]] = sum_lessons(lessons)
    print(subj)








