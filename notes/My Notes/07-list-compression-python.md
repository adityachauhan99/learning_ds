List compression - instead of loops, use a single line 

eg: 
	numbers = [1,2,3,4,5]
	 numbers_power = [n**2 for n in numbers]
this solves the problem in 1 line

result=[]
for i in range(3):
	result.append(i)

this becomes :
result=[i for i in range(3)]

result=[]
for i in range(3):
	for j in range(3):
		if i+j!=3:
			result.append([i,j])

this becomes:
result=[[i,j] for i in range(3) for j in range(3) if i+j!=3]