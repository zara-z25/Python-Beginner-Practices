while True:
    number = int(input("Please enter a number: "))
    straight_bar = "|"
    hyphen = "-"
    difference = number - 2
    pattern = "+" + hyphen*difference + "+"
    if number == 1:
        print("+")
    elif number>1:
        print(pattern)
        for i in range(number-2):
            print(straight_bar, end = "")
            for j in range(difference):
                print(hyphen, end="")
            print(straight_bar)
        print(pattern)