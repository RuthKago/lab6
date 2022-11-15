#Modify both functions such that the end value is not 100, but it is entered by
#the user. You can use either < or <= in the while condition. Consider both
#cases, how would the boundary value change for both cases?




def main():
    sum = 0
    start = int(input("Enter the start number equal to 5:"))
    end = int(input("Enter the end number:"))
    if start < 5:
              print("You have to enter a number equal to 5")
           

    
    else:
        for i in range (start, end + 1):
            sum= sum + i
            print(sum)
            print()
    print(f"The sum of the numbers between {start} and {end} is {sum}")
    print()


main()




print("Using while loop")
def main():
    sum = 0
    num = int(input("Enter the start number equal to 5:"))
    number = num
    end = int(input("Enter the end number:"))
    if num < 5:
           print("You have to enter a number equal to 5")

    else:
        while num <= end:
            sum = sum + num
            num = num + 1
            print(sum)
    print (f"The sum of the numbers between {number} and {end} is {sum}")

main()
