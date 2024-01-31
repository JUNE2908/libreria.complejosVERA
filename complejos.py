import math
def sumac(c1,c2):
    sum1 = c1[0] + c2[0]
    sum2 = c1[1] + c2[1]
    return (sum1,sum2)

def multic(c1,c2):
    multi1= c1[0] * c2[0] - c1[1] * c2[1]
    multi2 = c1[0] * c2[1] + c2[0] * c1[1]
    return (multi1, multi2)

def restc(c1,c2):
    rest1 = c1[0] - c2[0]
    rest2 = c1[1] - c2[1]
    return (rest1,rest2)

def divic(c1,c2):
    numer = multic(c1,(c2[0],-c2[1]))
    denom = multic(c2,(c2[0],-c2[1]))
    divi1 = numer[0]/denom[0]
    divi2 = numer[1]/denom[0]
    return (divi1,divi2)

def moduc(c):
    a = c[0]**2
    b = c[1]**2
    modulo = math.sqrt(a+b)
    return (modulo)

def conjuc(c):
    conj1 = c[0]
    conj2 = -c[1]
    return (conj1,conj2)

def fasec(c):
    x = c[1] / c[0]
    fase = math.atan(x)
    return (fase)

def geomc(c):
    p = moduc(c)
    ang = fasec(c)
    geo1 = p * math.cos(ang)
    geo2 = p * math.sin(ang)
    return (geo1,geo2)
