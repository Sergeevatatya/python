#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран



with open('files5/txt5', 'w+') as f:
    line = input('Введите цифры через пробел: ')
    f.writelines(line)
    my_numb = line.split()
with open('files5/txt5', 'r') as f:
    line = f.read()
    print(sum(map(int, my_numb)))

