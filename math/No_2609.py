def gcd(a, b):
    r = a % b
    if(r == 0):
        return b
        
    return gcd(b, r)

a, b = map(int, input().split())
gcd_answer = gcd(a, b)
lcm_answer = (a * b) // gcd_answer

print(gcd_answer)
print(lcm_answer)