
def rotateAry(d,a):
    rotatedArray = []
    for d in range(0,d):
        rotatedArray = a[1:]
        rotatedArray.append(a[0])
        a = rotatedArray
    return rotatedArray

print(rotateAry(3,[1,2,3,4,5]))
