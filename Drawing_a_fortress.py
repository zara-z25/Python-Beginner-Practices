while True:
    number = int(input("Please, enter a number(3-1000): "))
    quotient = number//2
    difference = ((number*2)-(quotient*2)-4)
    pattern = "/" + "^" * quotient + "\\" + "_"*difference +"/" + "^" * quotient + "\\"
    last_digit = (number*2)-2
    expression = (((number*2)-difference)//2)-1
    # print(quotient)
    # print(last_digit)
    print (pattern)
    for i in range(number-3):
        print("|", end = "")
        for j in range(number*2):
            if j == last_digit:
                print("|")
                break
            else: 
                print(" ", end = "")
    print("|" +" "*expression + "_"*difference + " "*expression + "|")
    print("\\" + "_"*quotient + "/" +" "*difference+ "\\" + "_"*quotient + "/")