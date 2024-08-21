print('Basic Arithmetic Calculator using two inputs')
print('***********(Add,Sub,Mil.Div)***********')


a= int(input('Enter first number :'))
b= int(input('Enter second number :'))


print("\noperations available:- \n1.addition\n2.subtraction\n3.multiplication\n4.divide")  


choice=int(input("Enter your operation (1/2/3/4) : ")) 

if (choice==1):
    sum = a+b
    print("The addition of two numbers :",a+b)
    
elif (choice==2):
    sum = a-b
    print("The Subtraction  of two numbers :",a-b)

elif (choice==3):
    sum = a*b
    print("The Multiplication of two numbers :",a*b)

elif (choice==4):
    sum = a/b
    print("The Division of two numbers :",a/b)
     
else:
      print("invalid option\nplease try again")
      
      
print('********Operation successfully completed********')
 




