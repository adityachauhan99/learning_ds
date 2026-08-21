# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
pattern = r"^(7|8|9)\d{9}$"

def check_valid(num):
    valid="NO"
    if len(num)==10:
        if re.match(pattern,num):
            valid="YES"
    print(valid)     
   
N = int(input())
for i in range(1,N+1):
    num=input()
    check_valid(num)
