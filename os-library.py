import os
import subprocess

print("current directory = " + os.getcwd())

# change directory
os.chdir('/home/albert/Learning')
print("current directory = " + os.getcwd())

# os.makedirs('shampoo') # creates new folder
# os.makedirs('/home/albert/GIT/zazaza') # creates new folder

print(os.path.abspath('/home/albert/GIT/zazaza'))
print(os.path.abspath('../'))

print(os.path.isabs('../')) # is absolute path
print(os.path.isabs('/home/albert/GIT/zazaza'))

file_path = '/home/albert/Learning/shampoo/blabla.txt'
print(os.path.basename(file_path))
print(os.path.dirname(file_path))
print(os.path.split(file_path))

print(os.path.getsize(file_path)) # file size in bytes
print(os.path.exists(file_path))

os.system('dir') # executes the command provided
subprocess.check_output('dir')








