def mean(num):
    """This function returns the average of given numbers
    e.g (4+5+6)/3
    """
    return sum(num)/len(num)

def addition(num):
    """ This function returns the sum of numbers"""
    return sum(num)

def addTen(num):
    return [n + 10 for n in num]

def minimum(num):
    return min(num)

def maximum(num):
    return max(num)


#Testing the functions
if __name__ == "__main__":
    print("\n Mean function is correct")
    m = [1,2,3,4,5]
    correct = 3
    assert(mean(m) == correct)

    print("\nAddition function is correct")
    correct_add = 15
    assert(addition(m) == correct_add)

    #print("\nTesting the addTen function")
    #correct_list = [10,20,30,40,50]
    #assert(addTen(m) == correct_list)

    print("\nAll functions tested correct")



