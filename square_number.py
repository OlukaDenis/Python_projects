def square_number(a):
    return a** 2
print(square_number(16))

def test_square_number():
    assert square_number(2)==4
    assert square_number(3)==9
    assert square_number(4)==16
    assert square_number(5)==25
    assert square_number(6)==36
    assert square_number(7)==49
    print("YOUR CODE IS CORRECT!")
test_square_number()
