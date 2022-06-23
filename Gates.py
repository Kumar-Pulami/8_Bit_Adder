#Method for AND gate
def andGate(a, b):
     if a == 1 and b == 1:
        return 1
     else:
        return 0

#METHOD FOR OR GATE.
def orGate(a, b):
    if a == 1:
        return 1
    elif b == 1:
        return 1
    else:
        return 0

#METHOD FOR NOT GATE
def notGate(a):
    if(a == 0):
        return 1
    else:
        return 0

#METHOD FOR XOR GATE
def xorGate(a , b):
    if a != b:
        return 1
    else:
        return 0

#METHOD FOR NAND GATE
def nandGate(a, b):
    if a == 1 and b == 1:
        return 0
    else:
        return 1

#METHOD FOR NOR GATE
def norGate(a,b):
    if(a == 0) and (b == 0):
        return 1
    else:
        return 0

