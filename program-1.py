#class starts here
class calculator:
    #functions which perform addition,multiplicatin and etc
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

try: 
    #first input takes from user
    a=float(input("Enter first number "))
    #second input takes from user
    b=float(input("Enter second number "))
    #class object
    cal_obj=calculator()
    op=input("Enter first number\n1.add\n2.sub\n3.mul\n4.div\n")
    if(op=='1'):
        #function call
        x=str(cal_obj.add(a,b))
        print("Your answer is "+ x)
    elif(op=='2'):
        x=str(cal_obj.sub(a,b))
        print("Your answer is "+ x)
    elif(op=='3'):
        x=str(cal_obj.mul(a,b))
        print("Your answer is "+ x)
    elif(op=='4'):
        x=str(cal_obj.div(a,b))
        print("Your answer is "+ x)
    else:
        print("Invalid option")
#catch block
except ValueError:
    print("Enter a valid number")