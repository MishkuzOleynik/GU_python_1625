import os.path

my_project_dir = 'my_project'
paths = ['settings', 'mainapp', 'adminapp', 'authapp']

for directory in paths:
    os.makedirs(os.path.join(os.curdir, my_project_dir, directory), exist_ok=True)
print(os.getcwd(), os.listdir(os.getcwd()))