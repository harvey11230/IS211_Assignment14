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

result = []
def recur_string(s1, s2):

    len_string1 = len(s1)
    len_string2 = len(s2)


    if len_string1 == 0 or len_string2 == 0:
        return 0
    if s1[0] == s2[0]:
        result.append(0)
        return recur_string(s1[1:], s2[1:])
    if s1[0] < s2[0]:
        result.append(-1)
        return recur_string(s1[1:], s2[1:])
    if s1[0] > s2[0]:
        result.append(1)
        return recur_string(s1[1:], s2[1:])




def PartIII():

        s1 = input("string1\n")
        s2 = input("string2\n")
        recur_string(s1, s2)
        print(result)

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
