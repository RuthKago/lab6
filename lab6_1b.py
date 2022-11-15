#Modify your functions such that summation starts from 5 instead of 1. Then
#further generalize such that the start value is entered by the user.



def main():
    sum = 0
    start = int(input("Enter the start number equal to 5:"))
    if start < 5:
           print("You have to enter a number equal to 5")

    else:
        for i in range (start, 101):
            sum= sum + i
            print(sum)
            print()

main()



print("Using while loop")
def main():
    sum = 0
    i = 100
    num = int(input("Enter the start number equal to 5:"))
    if num < 5:
           print("You have to enter a number equal to 5")

    else:
        while i >= 5:
            sum = sum + i
            i = i - 1 
            print (sum)

main()
