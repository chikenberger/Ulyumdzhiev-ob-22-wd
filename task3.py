num = float(input())

if num % 2 == 0:
    print('{:.4f} - четное'.format(num))
else:
    print('{:.4f} нечетное'.format(num))


for i in range(1, 11):
    if i != 4 and i != 7:
        print(i)

