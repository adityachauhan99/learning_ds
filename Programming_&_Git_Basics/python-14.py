N,M= map(int,input().split())
pattern=".|."
for i in range(1,N):
    if i<=N//2:
        pattern_count=(2*i)-1
        print("-"*int((M-pattern_count*3)/2),pattern*pattern_count,"-"*int((M-pattern_count*3)/2),sep="")
    if i==N//2:
        print("-"*int(((M-7)/2)),"WELCOME","-"*int(((M-7)/2)),sep="")
        break

for i in range(1,N):
    if i<=N//2:
        pattern_count= (M-(6*i))/3
        print("-"*int(3*i),pattern*int(pattern_count),"-"*int(3*i),sep="")
        
        