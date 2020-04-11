# 4)    Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.



def my_func(file):
    while True:
        line = file.readline() # перебираем, пока есть сроки
        if line:
            line_list = line.split()  # переведем строку в список
            for key in numbering.keys():
                if key in line: # если в строке есть английские числительные
                    line_list[0] = numbering[key] # заменить на русские, по словарю
                    new_line = ' '.join(line_list) # переводим в строку
                    print(new_line)
                    with open('my_file_3.txt', 'a', encoding='utf-8') as f:  # запись срок с русскими числит.в нов.файл
                        f.write(new_line + '\n')
        else:
            break

numbering = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('my_file_2.txt', 'r', encoding='utf-8') as f:
    my_func(f)