##while loop

english = [20, 60,72, 65,89,34,56,94]
score= [67,56,78,54,49,78,90, 45]
subject = ["History", "CRE", "Math", "Commerce", "Art", "Biology", "Chemistry", "Physics"]

result_eng = []


while sum(result_eng)<100:
    result_eng.append(english.pop())
print(sum(result_eng))

print(list(zip(subject, score)))
   
