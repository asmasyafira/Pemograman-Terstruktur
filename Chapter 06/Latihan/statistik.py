def sum(*number):
    i=0
    for s in number:
        i+=s
        hasil=i
    return hasil

def avg(*number):
    i=0
    for a in number:
        i+=1
        average=sum(*number)/i
    return average

def maks(*number):
    maksimum = number[0]
    for x in (number):
        if(x>maksimum):
            maksimum=x
    return maksimum 

def min(*number):
    minimum = number[0]
    for i in (number):
        if(i<minimum):
            minimum=i
    return minimum


