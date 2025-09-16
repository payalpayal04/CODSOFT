print("CALCULATOR\n")

#create a function for performing the given arithmetic operation
def calculator():
    while True:
        #input both first and second number on which you want to apply arithmetic operation
        num1= float(input("Enter first number : "))
        num2= float(input("Enter second number : "))

        #the selection entering must be easy and convinient for the user that's why the choices are integer
        print("\n")
        print("Select '1' for (+) addition")
        print("Select '2' for (-) subraction")
        print("Select '3' for (x) multiplication")
        print("Select '4' for (/) division")
        print("Select '5' for (^) exponential")

        #let the user choose operation to be applied from given options
        choice= int(input("\nEnter your choice : "))

        if (choice==1):
            operator="+"
            result= num1 + num2
        
        elif(choice==2):
            operator="-"
            result= num1 - num2
        
        elif(choice==3):
            operator="x"
            result= num1 * num2
        
        elif(choice==4):
            operator="/"
            result= num1 / num2
        
        elif(choice==5):
            operator="^"
            result= num1 ** num2
        
        else:
            print("Invalid operator choice")
    
        #print result 
        print(f"\nThe result of {num1} {operator} {num2} = {result}")
    
        nextcalculation=input("\nDo you want to do another calculation (y/n): ")
    
        if nextcalculation != 'y':
            print("\nYou have Exited the Calculator")
            break

#function call
calculator() 