students=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
sorted_students=sorted(students, key = lambda students : students[1])
for i in range (1,len(sorted_students)):
    if sorted_students[i][1]!=sorted_students[0][1]:
        second_lowest_score=sorted_students[i][1]
        break

names=[]
for i in range(0,len(sorted_students)):
    if sorted_students[i][1]==second_lowest_score:
        names.append(sorted_students[i][0])
final_names=sorted(names)
for name in final_names:
    print(name)


