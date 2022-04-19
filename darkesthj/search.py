def linearSearch(lista,target):
    for i in lista:
        if lista[i]==target:
            return i
    return None

def binarySearch(lista,target):
    first=0
    last=len(lista)-1
    while first <= last:
        midpoint=(first+last)//2
        if lista[midpoint] == target:
            return midpoint
        elif midpoint < target:
            first = midpoint+1
        elif midpoint > target:
            last = midpoint-1

def recursiveBinarySearch(lista,target):
    if len(lista)==0:
        return False
    else:
        midpoint=len(lista)//2
        if lista[midpoint]==target:
            return True
        elif lista[midpoint]<target:
            return recursiveBinarySearch(lista[midpoint+1:],target)
        elif lista[midpoint]>target:
            return recursiveBinarySearch(lista[:midpoint],target)

