#METHOD FOR TAKING FIRST NUMBER AND CHECK FOR THE VALIDIDTY
def input_a():
    print("********************************************************************************")
    a=input("Please,Enter The First Number:")
    flag=False
    while (flag==False):
        if(a==""):
            print("********************************************************************************")
            print("Opps!, Please Make Sure That You Have Entered Value.")        
            a=input("Could You Please, Enter The First Number Again?:")
        else:
            try:
                number1=int(a)
                if(int(a)<0 or int(a)>255):
                    print("********************************************************************************")
                    print("Opps!, Please Make Sure That Your Entered Value Ranges From 0 To 255.")
                    a=input("Could You Please, Enter The First Number Again?:")
                else:
                    return int(a)
                    flag=True
                    break
            except:
                print("********************************************************************************")
                print("Opps!, Please Make Sure That Your Entered Value Doesn't Enclude Character.")
                a=input("Could You Please, Enter The First Number Again?:")



#METHOD FOR TAKING SECOND NUMBER AND CHECK FOR THE VALIDIDTY
def input_b():
    print("********************************************************************************")
    b=input("Please,Enter The Second Number:")
    flag=False
    while (flag==False):
        if(b==""):
            print("********************************************************************************")
            print("Opps!, Please Make Sure That You Have Entered Value.")        
            b=input("Could You Please, Enter The Second Number Again?:")
        else:
            try:
                number1=int(b)
                if(int(b)<0 or int(b)>255):
                    print("********************************************************************************")
                    print("Opps!, Please Make Sure That Your Entered Value Ranges From 0 To 255.")
                    b=input("Could You Please, Enter The Second Number Again?:")
                
                else:
                    return int(b)
                    flag=True
                    break
            except:
                print("********************************************************************************")
                print("Opps!, Please Make Sure That Your Entered Value Doesn't Enclude Character.")
                b=input("Could You Please, Enter The Second Number Again?:")
