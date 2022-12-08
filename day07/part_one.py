from day07.model.Directory import Directory
from day07.model.File import File

ROOT_DIR_NAME = "/"

file = open("./input/input.txt")
lines = file.readlines()

root_directory = Directory(ROOT_DIR_NAME)
current_directory = root_directory

all_directories = []

for line in lines[1:]:
    tokens = line.removesuffix("\n").split(" ")

    if tokens[0].startswith("$"):
        if tokens[1].startswith("ls"):
            continue
        if tokens[1].startswith("cd"):
            if tokens[2].startswith(".."):
                current_directory = current_directory.parent
            else:
                for directory in current_directory.sub_directories:
                    if directory.name == tokens[2]:
                        current_directory = directory
                        break
    elif tokens[0].startswith("dir"):
        sub_directory = Directory(tokens[1])
        sub_directory.parent = current_directory
        current_directory.sub_directories.append(sub_directory)

        all_directories.append(sub_directory)
    else:
        current_directory.files.append(File(tokens[1], int(tokens[0])))

        itr_dir = current_directory
        while itr_dir is not None:
            itr_dir.dir_size += int(tokens[0])
            itr_dir = itr_dir.parent

filtered_directories = list(filter(lambda x: x.dir_size <= 100000, all_directories))
result = sum(x.dir_size for x in filtered_directories)

print(result)
