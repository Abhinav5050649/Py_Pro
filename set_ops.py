def armstrongNumber(x, y):
    
    for i in range(x, y + 1, 1):
        temp, orgInt, newInt = i, i, 0 
        digits = len(str(temp))
        while temp != 0:
            digit = temp % 10
            newInt += (digit **digits)
            temp = temp //10

        if newInt == orgInt:
            print(newInt, end = " ")
        else:
            continue

def main():
    x = int(input("Enter lower limit: "))
    y = int(input("Enter upper limit: "))

    armstrongNumber(x, y)

main()