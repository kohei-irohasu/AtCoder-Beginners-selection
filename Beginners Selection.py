#1 Product
a, b = map(int, input().split())
print('Even') if (a * b) % 2 ==0 else print('Odd')


#2 Placing Marbles
n = input()
total = sum(int(i) for i in n)
print(total)


#3 Shift only
N = int(input())
A = list(map(int, input().split()))

count = 0
while True:
    exist_odd = any(i % 2 != 0 for i in A)
    if exist_odd:
        break
    A = [i // 2 for i in A]
    count += 1

print(count)
        


#4 Coins
A = [int(input()) for _ in range(4)]
count = 0

for i in range(A[0] + 1):
    for j in range(A[1] + 1):
        for k in range(A[2] + 1):
            if 500 * i + 100 * j + 50 * k == A[3]:
                count += 1

print(count)


#5 Some Sums
def findSum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

N, A, B = map(int, input().split())
total = 0

for i in range(1, N + 1):
    sum = findSum(i)
    if sum >= A and sum <= B:
        total += i

print(total)


#6 Card Game for Two
N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
Alice = sum(a[i] for i in range(0, N, 2))
Bob = sum(a[i] for i in range(1, N, 2))
print(Alice - Bob)


#7 Kagami Mochi
N = int(input())
d = [int(input()) for _ in range(N)]

num = [0] * 110

for i in range(N):
    num[d[i]] += 1

res = 0
for i in range(1, 101):
    if num[i] > 0:
        res += 1

print(res)

#7 別解
N = int(input())
d = [int(input()) for _ in range(N)]

values = set()

for i in range(N):
    values.add(d[i])

print(len(values))


#8 Otoshidama
N, Y = map(int, input().split())
res10000, res5000, res1000 = -1, -1, -1

for a in range(N + 1):
    for b in range(N - a + 1):
        c = N - a - b
        total = 10000 * a + 5000 * b + 1000 * c
        if total == Y:
            res10000, res5000, res1000 = a, b, c

print(res10000, res5000, res1000)


#9 白昼夢
divide = ["dream", "dreamer", "erase", "eraser"]

S = input()
S = S[::-1]
divide = [d[::-1] for d in divide]

can = True
i = 0
while i < len(S):
    can2 = False
    for j in range(4):
        d = divide[j]
        if S.startswith(d, i):
            can2 = True
            i += len(d)
            break
    if not can2:
        can = False
        break

print('YES') if can else print('NO')


#10 Traveling
N = int(input())
t, x, y = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)
for i in range(N):
    t[i + 1], x[i + 1], y[i + 1] = map(int, input().split())

can = True
for i in range(1, N + 1):
    dt = t[i] - t[i - 1]
    dist = abs(x[i] - x[i - 1]) + abs(y[i] - y[i - 1])
    if dt < dist:
        can = False
    if dist % 2 != dt % 2:
        can = False

print('Yes') if can else print('No')