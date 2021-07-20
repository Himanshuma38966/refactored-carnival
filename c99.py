import os
import shutil

des = "D:/Des"
fil = input("enter filename")



if os.path.exists:
    os.mkdir("backup")








   

############no. of lines and alphabets and words present inside a file#################





'''import os
import shutil

path = input("enter the folder name")
print(path)
list_of_files=os.listdir(path)

for file in list_of_files:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=="":
        continue
    if os.path.exists(path+'/'+ext):
       
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)'''



