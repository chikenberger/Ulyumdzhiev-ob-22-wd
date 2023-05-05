def my_sum(a, b):
    s = a + b
    return s

a = float(input('Введите a:'))
b = float(input('Введите b:'))

s = my_sum(a, b)

print('Сумма а и b = {:.4f}'.format(s))
