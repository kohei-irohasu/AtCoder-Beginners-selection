#Product
a, b = map(int, input().split())
print('Even') if (a * b) % 2 ==0 else print('Odd')


#Placing Marbles
n = input()
total = sum(int(i) for i in n)
print(total)


#Shift only
n = int(input())
A = list(map(int, input().split()))
res = 0
while True:
    exist_odd = any(i % 2 != 0 for i in A)
    
    if exist_odd:
        break
    
    A = [i // 2 for i in A]
    res += 1
print(res)


#Coins
A = [int(input()) for _ in range(4)]
res = 0

for i in range(A[0] + 1):
    for j in range(A[1] + 1):
        for k in range(A[2] + 1):
            if 500 * i + 100 * j + 50 * k == A[3]:
                res += 1

print(res)
