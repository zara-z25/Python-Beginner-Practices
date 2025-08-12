
def pattern(row):
    for i in range (row):
        spaces = " " * (row-i-1)
        print(spaces, end ="")
        for j in range(i+1):
            print("*", end = " ")
        print()

    for i in range (row-1,0,-1):
        spaces = " " * (row-i)
        print(spaces, end ="")
        for j in range(i):
            print("*", end = " ")
        print()

while True:
    num = input("Enter row or '/' to exit: ")
    if num == "/":
        print("Exiting...")
        break
    else:
        pattern(int(num))