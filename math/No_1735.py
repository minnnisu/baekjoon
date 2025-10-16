def gcd(a, b):
    r = a % b
    if(r == 0):
        return b
    
    return gcd(b, r)

a, b = map(int, input().split(" "))
c, d = map(int, input().split(" "))

e = (a * d) + (b * c)
f = b * d

gcd_result = 0
if(e > f):
    gcd_result = gcd(e, f)
else:
    gcd_result = gcd(f, e)

print(f"{e // gcd_result} {f // gcd_result}")