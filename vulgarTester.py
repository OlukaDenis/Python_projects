while True:
    try:
        word = ["fuck", "sex", "fuck you", "shit", "dick", "pussy", "lick pussy", "two-some"]
        vulgar = input("Enter a word: ")
        if vulgar in word:
            print("This is a vulgar word!")
            break
        else:
            print("This is not a vulgar word")
            break
    except:
        break
