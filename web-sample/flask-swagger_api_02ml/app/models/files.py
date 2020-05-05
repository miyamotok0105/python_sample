

class files():
    def __init__(self):
        self.file_array = []

    def add_file(self, name, file):
        file = {"file_name": name, "file": file}
        self.file_array.append(file)

if __name__ == '__main__':
    files = files()
    files.add_file("n1", "f1")
    files.add_file("n2", "f2")

    print(files.file_array)

    results = files.file_array
    for result in results:
        print(result["file_name"])
        print(result["file"])

