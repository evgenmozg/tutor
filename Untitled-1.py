a = 'A'
b = 'B'
c = 'C'

def one(a):
    res1 = a + '1'
    return res1    


def two(b):
    res2 = b + '2'      
    return res2


def three(c):
    res3 = c + '3'
    return res3  


get1 = one(a)
get2 = two(b)
get3 = three(c)
print(get1, get2, get3, sep='\n')
lst = [get1, get2, get3]

for i in lst:
    print i
    