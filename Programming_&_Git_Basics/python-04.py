for i in range(1,20,2):
    print(i)

j=1
while j<=10:
    print(j*57)
    j+=1

for k in range (3,50,3):
    if k==15:
        continue
    print(k)

fnum=int(input("Enter First Number: "))
snum=int(input("Enter Second Number: "))

for l in range(1,1000):
    if l%fnum==0 and l%snum==0:
        print(l)
        break



    