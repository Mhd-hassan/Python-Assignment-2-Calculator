# Python calculator Method 1 using user-defined 
n1=float(input("Enter the value of number one : "))
n2=float(input("Enter the value of number two : "))
ans=n1+n2
print()
print("The addition of two number is :       ",ans)
ans=n1-n2
print("The subtraction of two number is :    ",ans)
ans=n1*n2
print("The multiplication of two number is : ",ans)
ans=n1/n2
print("The division of two number is :       ",ans)
"""
Output:
Enter the value of number one : 10
Enter the value of number two : 5

The addition of two number is :        15.0
The subtraction of two number is :     5.0
The multiplication of two number is :  50.0
The division of two number is :        2.0
"""
# Python calculator Method 2 using pre-defined
n1=20
n2=10
print("The value of number one is : ",n1)
print("The value of number two is : ",n2)
print()
ans=n1+n2
print("The addition of two number is : ",ans)
ans=n1-n2
print("The subtraction of two number is : ",ans)
ans=n1*n2
print("The multiplication of two number is : ",ans)
ans=n1/n2
print("The division of two number is : ",ans)
"""
Output:
The value of number one is :  20
The value of number two is :  10

The addition of two number is :  30
The subtraction of two number is :  10
The multiplication of two number is :  200
The division of two number is :  2.0
"""
# python calculator using while loop Method 1
ch=1
while ch==1:
    print("The menu for calculator : ")
    print(" 1. Press 1 to do addition. \n 2. Press 2 to do subtraction. \n 3. Press 3 to do multiplication. \n 4. Press 4 to do division")
    print()
    choice=int(input("Enter your choice : "))
    if choice==1:
        n1=float(input("Enter the value of number one : "))
        n2=float(input("Enter the value of number two : "))
        ans=n1+n2
        print("The addition of two number is : ",ans)
    elif choice==2:
        n1=float(input("Enter the value of number one : "))
        n2=float(input("Enter the value of number two : "))
        ans=n1-n2
        print("The subtraction of two number is : ",ans)
    elif choice==3:
        n1=float(input("Enter the value of number one : "))
        n2=float(input("Enter the value of number two : "))
        ans=n1*n2
        print("The multiplication of two number is : ",ans)
    elif choice==4:
        n1=float(input("Enter the value of number one : "))
        n2=float(input("Enter the value of number two : "))
        ans=n1/n2
        print("The division of two number is : ",ans)
    else:
        print("Wrong choice.................")
    n=input("If you want to continue ahead then press 1 otherwise press any key : ")
    if n!="1":
        exit()
    ch=int(n)
"""
Output:
The menu for calculator : 
 1. Press 1 to do addition. 
 2. Press 2 to do subtraction. 
 3. Press 3 to do multiplication. 
 4. Press 4 to do division

Enter your choice : 1
Enter the value of number one : 10
Enter the value of number two : 20
The addition of two number is :  30.0
If you want to continue ahead then press 1 otherwise press any key : 1
The menu for calculator : 
 1. Press 1 to do addition. 
 2. Press 2 to do subtraction. 
 3. Press 3 to do multiplication. 
 4. Press 4 to do division

Enter your choice : 2
Enter the value of number one : 20
Enter the value of number two : 10
The subtraction of two number is :  10.0
If you want to continue ahead then press 1 otherwise press any key : 1
The menu for calculator : 
 1. Press 1 to do addition. 
 2. Press 2 to do subtraction. 
 3. Press 3 to do multiplication. 
 4. Press 4 to do division

Enter your choice : 3
Enter the value of number one : 10
Enter the value of number two : 5
The multiplication of two number is :  50.0
If you want to continue ahead then press 1 otherwise press any key : 1
The menu for calculator : 
 1. Press 1 to do addition. 
 2. Press 2 to do subtraction. 
 3. Press 3 to do multiplication. 
 4. Press 4 to do division

Enter your choice : 4
Enter the value of number one : 20
Enter the value of number two : 5
The division of two number is :  4.0
If you want to continue ahead then press 1 otherwise press any key : 1
The menu for calculator :
 1. Press 1 to do addition.
 2. Press 2 to do subtraction.
 3. Press 3 to do multiplication.
 4. Press 4 to do division

Enter your choice : 6
Wrong choice.................
If you want to continue ahead then press 1 otherwise press any key : 0
"""