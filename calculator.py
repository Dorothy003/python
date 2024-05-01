class Calculator:
    def sum(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def division(self,x,y):
        if(y==0):
            print("Cannot be divide\n")
        else:
            return x/y
#main program
cal = Calculator();
print("Enter the operation:\n")
print("1.Summation\n")
print("2.Substraction\n")
print("3.Division\n")
print("4.Multiplication\n")
choice = input("Enter your choice:\n")
if choice in ('1','2','3','4'):
    print("Enter the numbers\n")
    num1 = float(input("First number:\n"))
    num2 = float(input("Second number:\n"))
    if choice =='1':
        print("The sum of two numbers is " , cal.sum(num1,num2))
    elif choice =='2':
        print("The difference of two numbers is  " , cal.sub(num1,num2))
    elif choice =='3':
        print("The division of two numbers is  " , cal.division(num1,num2))
    elif choice =='4':
        print("The multiplication of two numbers is  " , cal.multiply(num1,num2))
else:
    print("Invalid input")
    
    

    
