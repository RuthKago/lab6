#Write a function that finds the sum of numbers from 1 to 100 (both included)
#using a for loop. Write another function that does the same operation
#using a while loop.


def main():
    sum = 0
    for i in range (1, 101):
        sum= sum + i
        print(sum)
        print()

main()



print("Using while loop")
def main():
    sum = 0
    num = 1
    while num <= 100:
        sum = sum + num
        num = num + 1  #It increases num with 1
        print (sum)

main()
