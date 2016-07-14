import os
exes = []
master_path = "./Downloads/"
for root, dirs, files in os.walk(master_path):
    for names in files:
        path = os.path.join(root,names)
        filename, file_extension = os.path.splitext(path)
        if file_extension not in exes:
            exes.append(file_extension)
for exe in exes:
    if exe != '':
        path = master_path + exe[1:]
        os.makedirs(path)
for root, dirs, files in os.walk(master_path):
    for names in files:
        path = os.path.join(root,names)
        filename, file_extension = os.path.splitext(path)
        if file_extension != '':
        	new_path = master_path + file_extension[1:] + "/" + names
        	os.rename(path, new_path)