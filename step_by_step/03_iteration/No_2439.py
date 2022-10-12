stars = int(input())

for star in range(1, stars + 1):
    print(" " * (stars-star), end="")
    print("*" * star)