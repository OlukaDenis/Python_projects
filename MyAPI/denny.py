import myFunctions

marks = [20, 68, 84, 36,92, 73,49, 12, 47, 98]

avg = myFunctions.mean(marks)

min_mark = myFunctions.minimum(marks)
max_mark = myFunctions.maximum(marks)

total = myFunctions.addition(marks)

print("Average mark: ", avg)
print("Total mark: ", total)
print("Lowest mark: ", min_mark)
print("Highest mark: ", max_mark)