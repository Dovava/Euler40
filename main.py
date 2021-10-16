chcon = "0."
l = 1000001
for n in range(1,l):
    chcon += str(n)
def d(n):
    return int(chcon[n+1])
print(d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000))