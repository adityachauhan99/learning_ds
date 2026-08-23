import string
test1="HackerRank.com presents Pythonist 2."
result=""
for i in range(0,len(test1)):
    if test1[i].isupper():
        result=result+test1[i].lower()
    if test1[i].islower():
        result=result+test1[i].upper()
    if test1[i].isdigit():
        result=result+test1[i]
    if test1[i].isspace():
        result=result+test1[i]
    if test1[i] in string.punctuation:
        result=result+test1[i]


print(result)
