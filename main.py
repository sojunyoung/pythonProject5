num = -1
avg = 0
a = ()

while a != 0:
    a = int(input())
    num = num + 1
    avg = avg + a
    if a == 0:
        break

print(avg / num)
