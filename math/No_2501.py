n, k = map(int, input().split())

divisor = []
for i in range(1, int(n**(1/2) + 1)):
    if(n % i == 0):
        divisor.append(i)
        if(i * i != n):
            divisor.append(n // i)

divisor.sort()

if(k > len(divisor)):
    print(0)
else:
    print(divisor[k - 1])