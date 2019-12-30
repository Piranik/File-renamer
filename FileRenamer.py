import os

folder = input(
    "Write in the path of the folder where you want to rename the files: ")

num = 1
for file in os.listdir(folder):
    x, whatkind = os.path.splitext(file)
    name = "file" + str(num) + whatkind  # the name of the new files

    os.rename(os.path.join(folder, file), os.path.join(folder, name))

    num = num + 1
