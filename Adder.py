from Gates import *


#method to add binary number
def resultCalculation(a,b):
    result=[]
    carry=0
    for i in range(len(a)):
        phase1=xorGate(a[i], b[i])
        phase2=nandGate(phase1, carry)
        phase3=orGate(phase1, carry)
        phase4=andGate(phase3, phase2)
        phase5=andGate(a[i], b[i])
        phase6=andGate(carry, phase1)
        phase7=norGate(phase5, phase6)
        phase8=notGate(phase7)
        result.append(phase4)
        carry=phase8
    return list(reversed(result))
