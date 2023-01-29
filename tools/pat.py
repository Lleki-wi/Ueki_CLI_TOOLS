from sys import argv
argc = len(argv)

out = []

if argc < 2:
    print("lpat [count( > 0)]")
    exit(1)

count = argv[1]
try:
    count = int(count)
    if count < 1:
        print("lpat [count( > 0)]")
        exit(1)
except TypeError:
    print("lpat [count( > 0)]")
    exit(1)

ALP = [chr(i) for i in range(65, 65+26)]
ALP.extend([chr(i) for i in range(97, 97+26)])
INTEGER = [chr(i) for i in range(48, 48+10)]

while count:
    for c in ALP:
        for i in INTEGER:
            out.append(c)
            count -= 1
            if not count:
                break
            out.append(i)
            count -= 1
            if not count:
                break
        if not count:
            break

print("".join(out))
exit(0)