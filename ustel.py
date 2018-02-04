a = int(input("enter first number:"))
b = int(input("enter second number:"))

def ustel(b):

    if ( a < 0 ):
        return ("a should be greater than zero")
    elif ( a == 0 ):
        return ("ERROR! a shouldn't be zero")
    elif ( b < 0 ):
        return ("b should be greater than or equal zero")
    elif ( b == 0 ):
        return 1
    else:
        return a*(ustel(b-1))

print (ustel(b))