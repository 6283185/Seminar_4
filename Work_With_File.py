# file_path = r'C:\Users\Home\Desktop\GeekBrains\python\Seminar_4\test.txt'
# f = open(file_path, 'w')
# f.write('Hello world!')
# f.close()

file_path = r'C:\Users\Home\Desktop\GeekBrains\python\Seminar_4\test_2.txt'
with open(file_path, 'w') as f_data:
    # print(f_data.read())
    f_data.write('Hello world!')