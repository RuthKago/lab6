#What would be the final value of i for the cases where you
#decrement i by 2, 4, 5, and 10 (instead of 3)?

def finalval():
    i = 25
    while i > 12:
        print(i)
        i = i - 2  #Try using 2,4,5,10
    print(f"Final Value: {i}")  #Final Value is less than 12
    print()


finalval()





#In the following program, what is the value of x after the loop finishes (final
#value)? What would be the final value of x for the cases where the initial value
#of x is 6, 5, and 8?


def finalval2():
    x = 7
    while x >= 5 and x<=8:
        print(x)
        if x%2 ==0:
            x=x+1
        else:
            x=x-2
    print("Final value: ", x)


finalval2()
