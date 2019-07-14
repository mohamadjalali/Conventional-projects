class FileIO:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = open(filename, mode)

    def write(self, text):
        if self.mode == 'w':
            self.file.writelines(text)
        else:
            print("File is open in read mode!")

    def read(self):
        if self.mode == 'r' or self.mode == '':
            return self.file.readlines()
        else:
            return ''

    def close(self):
        self.file.close()

    def __del__(self):
        self.close()


class CSVIO(FileIO):
    def __init__(self, filename, mode):
        super().__init__(filename, mode)
    def write(self, data):
        s = ""
        for row in data:
            for d in row:
                s += str(d)+","
            s += '\n'
        self.file.writelines(s)

data = [
        ["mohamad", 22, 183],
        ["sara", 20, 170]
]

csv = CSVIO("myfile.csv", "w")
csv.write(data)

