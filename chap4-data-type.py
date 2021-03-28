print(type(100000000000000))

print(100000000000000 + 100000000000000)

# for x in 'for-loop-string': print(x)

# 수치형: int, float, complex
# 순서형: str, list, tuple
# 매핑형: dict
print(type({'one': 1, 'two': 2, 'three': 3}))

# 불: bool
# 세트: set
fruits = {'apple', 'banana', 'orange'}
companies = {'apple', 'microsoft', 'google'}
alphabet = {'g', 'o', 'o', 'g', 'l', 'e'}
print(type(fruits))

print(fruits & companies)
print(fruits | companies)
print(alphabet)

# 문자열 슬라이싱(slicing)
p = 'Python'
print(p[0:2])
print(p[:2])
print(p[-2:])
print(p[:])
print(p[::-1])
print(p.lower())
print(p.replace('P', 'J'))


def palindrome(s):
    s = s.replace(' ','').lower()
    return s == s[::-1]


print(palindrome('anna'))
print(palindrome('banana'))
print(palindrome('Anna'))
print(palindrome('My gym'))

prime = [3, 7, 11]
prime.append(5)
print(prime)
prime.sort()
print(prime)
prime.insert(0, 2)
print(prime)
del prime[4]
print(prime)
prime[0] = 1
print(prime)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

characters = []
sentence = 'Be happy!'

for char in sentence:
    characters.append(char)

print(characters)
print(list(sentence))

one_to_ten = sum(list(range(1, 11)))
print(one_to_ten)

import operator
from functools import reduce

chulsu = [90, 85, 70]
younghee = [88, 79, 92]
yong = [100, 100, 100]
minsu = [90, 60, 70]

students = [chulsu, younghee, yong, minsu]

for scores in students:
    total = reduce(operator.add, scores)
    average = round(total / len(scores), 1)
    print(scores, total, average)


def sum_digits(num):
    return sum(map(int, list(str(num))))


print(sum_digits(999))


# 줄기와 잎 그림
score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]

stem_leaf = [[], [], []]
for s in score:
    d, m = divmod(s, 10)
    stem_leaf[d].append(m)

for i in range(len(stem_leaf)):
    print(f'{i}: {stem_leaf[i]}')


# 소수 구하기
limit = 30
L = list(range(2, limit + 1))
for i in L:
    for j in range(2, limit // i + 1):
        if i * j in L:
            L.remove(i * j)

print(L)


# 튜플
c = 10
d = 20
c, d = d, c
print(c, d)

p = (1, 2, 3)
q = p[:1] + (5,) + p[2:]
print(q)
print(list(q))
print(tuple(list(q)))

input_arr = '2018 10 2'.split(' ')

year, month, day = tuple(map(int, input_arr))
print('%02d/%02d/%04d' % (month, day, year))

# 진법 변환
# 2진: bin(i), 8진: oct(i), 16진: hex(i)
print(bin(13))
print(list(map(int, list(bin(13))[2:])))

d = 13
b = []
while True:
    d, m = divmod(d, 2)
    b.insert(0, m)
    if (d == 0):
        break

print(b)


# 딕셔너리(dict)
family = {'boy': 'choi', 'girl': 'kim', 'baby': 'choi'}
print(family)
print(family.keys())
print(family.values())
print('boy' in family)
print('sister' in family)

# ascii - ord(), chr()
print(ord('A'))
print(chr(65))
print(chr(55197))

love = '''L is for the way you look at me
O is for the only one I see
V is very, very extraordinary
E is even more than anyone that you adore can'''
print(love.split("\n"))

txt = '''신경발달장애 Neurodevelopmental Disorders
조현병 스펙트럼 및 기타 정신병적 장애 Schizophrenia Spectrum and Other Psychotic Disorders
양극성 및 관련 장애 Bipolar and Related Disorders
우울장애 Depressive Disorders
불안장애 Anxiety Disorder
강박 및 관련 장애 Obsessive－Compulsive and Related Disorders
외상 및 스트레스 관련 장애 Trauma－and Stressor－Related Disorders
해리장애 Dissociative Disorders
신체증상 및 관련 장애 Somatic Symptom and Related Disorders
급식 및 섭식장애 Feeding and Eating Disorders
배설장애 Elimination Disorders
수면－각성 장애 Sleep－Wake Disorders
성기능부전 Sexual Dysfunctions
성별 불쾌감 Gender Dysphoria
파괴적, 충동조절 및 품행 장애 Disruptive, Impulse－Control, and Conduct Disorders
물질관련 및 중독 장애 Substance－Related and Addictive Disorders
신경인지장애 Neurocognitive Disorders
성격장애 Personality Disorders
변태성욕장애 Paraphilic Disorders
기타 정신질환 Other Mental Disorders'''

disorders = dict()

is_eng = lambda x: 65 <= ord(x) <= 90 or 97 <= ord(x) <= 122

for l in txt.split('\n'):
    i = 0
    while not is_eng(l[i]):
        i += 1
    else:
        ko, en = l[:i-1], l[i:]
        disorders[ko] = en

print(disorders)

import copy

def sol2(inlist, coms):
    outlist = []
    sumout = []
    _inlist = copy.deepcopy(inlist)
    _inlist.sort(reverse=True)
    for i in range(coms):
        outlist.append([])
        sumout.append(0)

    for bread in _inlist:
        lowbasket = sumout.index(min(sumout))
        outlist[lowbasket].append(bread)
        sumout[lowbasket] += bread

    return outlist


print(sol2)