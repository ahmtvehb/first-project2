n = int(input("enter number n = "))

def iki_uzeri(n):

    if ( n<0 ):
        return ("number is greater or equal zero")
    elif ( n==0 ):
        return 1
    else :
        return 2*iki_uzeri(n-1)

print (iki_uzeri(n))