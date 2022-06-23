from Input import*
from Conversion import *
from Adder import *

#Creating Main Method.
def main():
    print("********************************************************************************")
    print("                            Welcome To The 8-Bit Adder Program.")
    # Using Loop. it will Loop the main method as long as we input 'yes' at the end of the program.
    answer="yes"
    while(answer=="Yes" or answer==("yes") or answer=='y' or answer=="Y" ):
        #Calling Input modules and storing values.
        number1=input_a()      
        number2=input_b()

        #looping using while loop until enter 2 number sum is <= 255.
        #Because our program works in 8-bit wheres above 255(11111111), its value has more than 8-bits i.e 256(100000000)
        #which cause faulty sum above 255.
        flag=False
        while (flag==False):            
            if(number1+number2>255):
                print("********************************************************************************")
                print("Opps!!, Please Make Sure That Sum of Your Entered Number isn't Greater Than 255.")
                number1=input_a()      
                number2=input_b()
            else:
                flag=True
                break
            
        #Converting decimal number into binary Number.
        #Calling decimal_To_binary method from conversion module.
        number1_binary=decimal_To_binary(number1) 
        number2_binary=decimal_To_binary(number2) 

        #creating the reversed list of binary number as adding process starts from right hand side.
        upper_bit=list(reversed(number1_binary))
        lower_bit=list(reversed(number2_binary))

        #calling resultCalculation method from adder module which adds the binary values.
        #and storing vaulue.
        result_in_binary= resultCalculation(upper_bit,lower_bit)

        #Converting  binary number into decimal number.
        decimal_result=binary_To_decimal(result_in_binary)

        #Displaying the result.
        print("********************************************************************************")
        print("Numbers            In Decimal              In Binary ")
        print("First Number          ",number1,"                ",number1_binary)
        print("Second Number         ",number2,"                ",number2_binary)
        print("             Sum:     ",decimal_result,"                ",result_in_binary)
        print("********************************************************************************")
        answer=input("Do You Want To Continue or Exit? (Type 'Yes' /'Y' To Continue Or Hit 'Enter' To Terminate):")
    print("Thank You For Using This Program.")

    
main()
