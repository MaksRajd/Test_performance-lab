import sys;


def ArrayFileRead(link):
    with open(link, 'r') as file:
        lst = file.readlines()
    lst = [int(line.rstrip()) for line in lst]
    return lst
numbers = "".join(sys.argv[1:])
a = ArrayFileRead(numbers)
m = sorted(a)[len(a) // 2]
print(sum(abs(v - m) for v in a))