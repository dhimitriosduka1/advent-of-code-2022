from day07.model.Directory import Directory
from day07.model.File import File

file = open("./input/input.txt")
lines = file.readlines()

ROOT_DIR_NAME = "/"
FILESYSTEM_SIZE = 70000000
REQUIRED_SPACE_FOR_UPDATE = 30000000

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

unused_space_currently = FILESYSTEM_SIZE - root_directory.dir_size
additional_requires_space = REQUIRED_SPACE_FOR_UPDATE - unused_space_currently

all_directories.sort(key=lambda x: x.dir_size)

for candidate_directory in all_directories:
    if candidate_directory.dir_size >= additional_requires_space:
        print(candidate_directory.dir_size)
        break
