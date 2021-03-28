def ban():
    global jjang
    jjang = '07'
    print('jjang =', jjang)


jjang = 'pig dad'
ban()

print(jjang)


def hap(a, b):
    print(a + b)


def gop(a, b):
    print(a * b)


def hap_gop(a, b):
    hap(a, b)
    gop(a, b)


hap_gop(5, 10)


def countdown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)


countdown(2)


def sum_of_digits(num):
    if num < 1:
        return 0
    return num % 10 + sum_of_digits(num // 10)


print('Sum of digits = ', sum_of_digits(643))


def compound_interest_amount_without_n(p, r, t, n):
    if t <= 0:
        return p
    return compound_interest_amount_without_n(p, r, t - 1 / n, n) * (1 + r / n)


print(compound_interest_amount_without_n(3600000, 0.058, 2, 1))
print(compound_interest_amount_without_n(10000000, 0.05 / 12, 12, 1))

print(compound_interest_amount_without_n(1500000, 0.043, 6, 4))
print(compound_interest_amount_without_n(1500000, 0.043, 6, 1 / 2))

sum_result = (lambda x, y: x + y)(10, 20)
print(sum_result)

# map(함수, 리스트)
map_list = list(map(lambda x: x ** 2, range(5)))
print(map_list)

# reduce(함수, 순서형 자료)
from functools import reduce

reduce1 = reduce(lambda x, y: y + x, 'abcdefg')
print(reduce1)

# filter(함수, 리스트)
l = list(filter(lambda x: x < 5, range(10)))
print(l)
l = list(filter(lambda x: x % 2, range(10)))
print(l)