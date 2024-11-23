class my_with(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        print(self.count)
        self.file = open(self.file_name, "w")
        return self.file    

    def __exit__(self, exception_type, exception_value, traceback):
        self.file.close()