numbers = list(input().strip())
numbers.sort(reverse=True)

for number in numbers:
    print(number, end="")