#Input validation


def valid_squareroot():
    x = int(input("Enter the number for SquareRoot: "))
    while x < 0 :
        print("Number cannot be negative...")
        x = int(input("Enter the number for Squareroot:"))
    print(f"The squareroot of {x} is {x**0.5}")


valid_squareroot()



def password():
    pwd = input("Enter your chosen password: ")
    while len (pwd) < 6 :
        print("Length of your password is less than 6 characters")
        pwd = input("Enter your chosen password:")
    print(f"Here is your password {pwd}")


password()

