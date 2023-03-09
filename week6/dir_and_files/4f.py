def file_len(file):
        with open(file) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print(file_len("demofile.txt"))
