import os

os.chdir("D:\PythonFileTrials")
print(os.getcwd())

file = open('our_python.txt') #wont work if the file doest not exist
file.close()

fr = open('our_python.txt', 'r')
print(fr.read())
fr.close()

fw = open('our_python.txt', 'w')
fw.write('lalalala')
fw.close()

fa = open('our_python.txt', 'a')
fa.write('dadada222')
fa.close()

ft = open('our_python.txt', 'rt') # open as text
print(ft.read())
ft.close()

fb = open('our_python.txt', 'rb')  # open as bytes
print(fb.read())
fb.close()

file = open('many_lines.txt', 'r')

for line in file.readlines():
    print(line.strip('\n')) # removes line spaces

file.close()

#------------------------------------------------------
print('#------------------------------------------------------')


directory = input('enter directory')
directory = directory.strip('\n')

os.chdir(directory)

file_name = input('enter file name')

content = 'Hello!\nGo To Hell\nYoYoYo\n'

with open(file_name, 'w') as fn: #closes file at the end of block
    fn.write(content)

with open(file_name, 'r+') as fn: # r+ =  read and write
    for line in fn.readlines():
        line = line.strip('\n')
        line = line[::-1] + '\n'
        fn.writelines(line)







