def factorial(val):
    output = 1
    for i in range(1,val+1):
        output = output*i
    return output

while True:
    integer = int(input("Enter an integer: "))
    try:
        if integer < 0:  
            print("Sorry, input must be a positive integer, try again")
            continue
        break
    except ValueError:
        print("That's not an integer!")     

output = factorial(integer)
print(output)