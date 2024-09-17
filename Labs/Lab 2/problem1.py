def compare(file1, file2):
    f1 = open(file1).read().split('\n')
    f2 = open(file2).read().split('\n')
    for i in range(max([len(f1), len(f2)])):
        if len(f1) <= i: f1.append('')
        if len(f2) <= i: f2.append('')
        if f1[i] != f2[i]:
            print(f"'{f1[i]}' is different from '{f2[i]}'")
compare('file1.txt', 'file2.txt')