# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
pattern = r"(?<=.)#(([0-9a-fA-F]{6})|([0-9a-fA-F]{3}))"

def check_valid(line):
    if re.findall(pattern,line):
        hex_codes=re.findall(pattern,line)
        for i in range(0,len(hex_codes)):
            print("#"+hex_codes[i][0])


N=int(input())
for i in range(1,N+1):
    line = input()
    check_valid(line)
        