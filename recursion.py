def Fibonnaci_Recursion(n):
    if n <= 1:
        return n
    else:
        return(Fibonnaci_Recursion(n-1)+ Fibonnaci_Recursion(n-2))

def PartI():
    while True:
        try:
            number = int(input("Please enter a positive integer\n"))
        except ValueError:
            print("Not a integer!")
            continue
        else:
            for i in range(number):
                print(Fibonnaci_Recursion(i))

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def PartII():
    while True:
        try:
            a = int(input("The first number is\n"))
            b = int(input("The second number is\n"))

        except ValueError:
            print("This is not a number!")
        else:
            print(gcd(a, b))

def String_Comparison(s1, s2):
    if s1 == s2:
        return 0


def PartIII():

        s1 = input("string1\n")
        s2 = input("string2\n")
        String_Comparison(s1, s2)


if __name__ == '__main__':

    selection = int(input("Fibonnaci Recursion select 1\n"
                          "GCD Recursion select 2\n"
                          "String Comparison select 3\n"))
    if selection == 1:
        PartI()
    elif selection == 2:
        PartII()
    elif selection == 3:
        PartIII()
    else:
        exit()
