from sys import argv
argc = len(argv)

if argc == 1 or argc > 4:
    print("lec <enter(any char or str)> [strings] [count]")
    exit(1)
if argc == 4:
    enter = 1
    strings = argv[2]
else:
    enter = 0
    strings = argv[1]

try:
    count = int(argv[-1])
except TypeError:
    print("lec <enter(any char or str)> [strings] [count]")
    exit(1)

if enter:
    print(strings*count)
else:
    print(strings*count, end="")

exit(0)