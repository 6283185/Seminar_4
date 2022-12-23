# 1. Считать строку из набора чисел из файла.
#  Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел. 
# Результат заисать в конец исходного файла (х1 х2).

file_path = r'C:\Users\Home\Desktop\GeekBrains\python\Seminar_4\task_1.txt'
with open(file_path, 'w') as f_data:
    f_data.write('1 4 5 6 8 2 6 8\n')
with open(file_path, 'r') as f_data:
    lst = f_data.read()
new_lst = lst.split(" ")
lst_int = [int(i) for i in new_lst]
max_num = max(lst_int)
min_num = min(lst_int)


with open(file_path, 'a') as f_data:
    f_data.write(f'Max num is {max_num}\n')
    f_data.write(f'Min num is {min_num}')
