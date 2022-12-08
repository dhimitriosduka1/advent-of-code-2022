from day07.model.File import File


class Directory:
    def __init__(self, name):
        self.name = name
        self.files: [File] = []
        self.sub_directories: [Directory] = []
        self.parent = None
        self.dir_size = 0

    def get_parent(self):
        return self.parent
