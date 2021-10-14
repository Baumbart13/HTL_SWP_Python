def empty(x,y):
    return x,y

def emptyZwoa(x,y=3): # y=optionaler Parameter
    return x,y

def emptyDrei(x=3,y=5):
    return x,y

print(emptyZwoa(5))
print(emptyZwoa(5,8))

print(emptyDrei(6))
peter = emptyDrei

print(peter())

