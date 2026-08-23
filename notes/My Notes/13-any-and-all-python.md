
python has built in functions named "any" and "all"

any : it takes an iterable of True and False values and if any one of them satisfies , it gives True
all : all needs to satisfy

eg :
print(any(c.islower() for c in s))             :                  s is the string name and c are the characters