def gcd(_a, _b):
    while(_b > 0):
        _r = _a % _b
        _a = _b
        _b = _r
    return _a
    
def lcm(_gcd_result, _a, _b):
   _a = _a // gcd_result 
   _b = _b // gcd_result 
   return gcd_result * _a * _b


a, b = map(int,(input().split(" ")))
r = 0

if a > b:
    a, b = b, a

gcd_result = gcd(a, b)
lcm_result = lcm(gcd_result, a, b)
print(gcd_result)
print(lcm_result)
# print("gcd: %d lcm: %d" % (gcd_result, lcm_result))

