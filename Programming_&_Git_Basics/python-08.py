# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re 

pattern = r"^[a-zA-Z][a-zA-Z0-9_.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

def check_valid(email_addr):
    valid=False
    if re.match(pattern,email_addr):
        valid=True
    return valid
    


n=int(input())

for i in range(1,n+1):
    name_and_email=input()
    parsed_email= email.utils.parseaddr(name_and_email)
    email_addr=parsed_email[1]
    if check_valid(email_addr):
        print(name_and_email)