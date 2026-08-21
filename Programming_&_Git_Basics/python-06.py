import re
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"

user_input=input("Enter Your Email")
if re.search(pattern,user_input):
    print("Correct")
else:
    print("Invalid")