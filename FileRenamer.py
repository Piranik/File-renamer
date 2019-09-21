import os

folder = input("Write in the path of the folder where you want to rename the files: ")
whatkind = input("What kind of file is this: ")


num = 1

for file in os.listdir(folder):
    name = "file" + str(num) + "." + whatkind
    os.rename(os.path.join(folder, file), os.path.join(folder, name))
    num = num + 1