while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please, this is not a valid number")
    except KeyboardInterrupt:
        print("No input!")
    finally :
        print("This is an attempt!")
