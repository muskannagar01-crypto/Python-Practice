"""
Week 2 - Data Structures Practice
Topics:
- Strings
- Lists
- Tuples
- Sets
- Dictionaries
-Exception Handling
-File Handling
"""
#EXCEPTION HANDLING
n=5
try:
    ans=n/0
except ZeroDivisionError:
    print("Can't be divided by 0!")

n=8
try:    #error code
    ans=n/6
except ZeroDivisionError:     #handles error if occurs
    print("Can't be divided by 0!")
else:    # if no error then this is executed
    print(ans)
finally:     #runs always
    print("Execution complete!")

try:
    n=int("str")
    inverse= 1/n
except ZeroDivisionError:
    print("Zero has no inverse")
except ValueError:
    print("Not valid value!")

try :
    div="20"/20
except ArithmeticError:
    print("Arithmentic error")
except:
    print("something wrong!")

def set(age):
    if age<0:
        raise ValueError("Age cannot be negative!")
    print("Age set to",age)
try:
    set(-3)
except ValueError as e:
    print(e)

try:
    val=int(input("enter a no:"))
    result=100/val
except (ValueError,ArithmeticError,ZeroDivisionError) as error:
    print("An invalid mathematical input occured",error)
else:
    print(result)

#Calculator that doesn't crash on invalid input
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

def calculator():
    while True:
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")

        choice = int(input("Enter your choice:"))
        if choice==5:
            print("Goodbye!")
            break
        if choice in range(4):
            try:
                n1= int(input("Enter first no.:"))
                n2= int(input("Enter second no.:"))
            except:
                print("Invalid input!")
            if choice==1:
                print(f"Add:{n1+n2}")
            elif choice==2:
                print(f"Subtract:{n1-n2}")
            elif choice==3:
                print(f"Multiply:{n1*n2}")
            elif choice==4:
                print(f"Divide:{n1/n2}")
        else:
            print("Invalid. Choose from above mentioned options.")
calculator()