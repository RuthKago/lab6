#In the beginning of the program, initialize a float variable to 1 (e.g. x=1.0 ).
#Then, in a while loop, continually divide x by 2 (x=x/2). When the loop 1
#finishes, the program should print an appropriate message. Do you think this
#loop will stop or will it run forever?

def main():
    y = 1.0
    counter = 0

    #There is no difference between using y>0 or y !=0
    while y != 0:
        divide = y/2
        print(divide)
        counter = counter + 1

    print(f"{counter} steps to get to 0.")

main()
        
