def find_least_common_multiple(a, b):
    def find_gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    gcd = find_gcd(a, b)
    lcm = (a * b) // gcd
    return lcm

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

lcm = find_least_common_multiple(num1, num2)

print("Наименьший общий множитель:", lcm)
