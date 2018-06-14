def biggest_guy():
    number1 = input("Number 1:  ")
    number2 = input("Number 2:  ")
    number3 = input("Number 3:  ")
    if (number1>number2) and (number1>number3):
        biggest_number = number1
        print("The biggest number among " +number1+"," +number2+"," +number3+","
              "is " +biggest_number)
    elif (number2>number1) and (number2>number3):
        biggest_number = number2
        print("The biggest number among " +number1+"," +number2+"," +number3+","
              "is " +biggest_number)
    else:
        biggest_number = number3
        print("The biggest number among " +number1+"," +number2+"," +number3+","
              "is " +biggest_number)
        
biggest_guy()
    
