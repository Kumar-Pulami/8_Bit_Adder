def decimal_To_binary(decimalNo):
    #bit list used to store the reminder
    bit=[]
    counter=0
    #This loop is continue till counter is not equals to 8
    while counter !=8:
        reminder=decimalNo%2
        bit.append(reminder)
        #quotient is stored in decimalNo Variable
        decimalNo=decimalNo//2
        counter+=1
    #reversing the bit list values
    binaryNo=list(reversed(bit))
    return binaryNo


def binary_To_decimal(num):
    #Converting string list into int list
    l=list(map(int,num))
    newlist=[]
    decimal=0
    #inseting the the reversed values fo l in newlist
    for i in range(len(l)-1,-1,-1):
        newlist.append(l[i])
    #USING LOOP FOR THE DECIMAL CALCULATION
    for j in range(len(newlist)):
        result=(newlist[j])*(2**j)
        decimal=decimal+result
    return decimal
