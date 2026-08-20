import random

def clue(lucky_num,user_num):
    if lucky_num-user_num==0:
        print("Correct")
    elif lucky_num-user_num>=10:
        print("Too Low, Think Higher")
    elif lucky_num-user_num<=-10:
        print("Too High, Think Lower")
    elif lucky_num-user_num<0 and lucky_num-user_num>-10:
        print("High, Think Lower")
    else:
        print("Low, Think Higher")

    
    

lucky_num=random.randint(1,100)
user_num=int(input("Enter Your Number: "))

while user_num!=lucky_num:
    clue(lucky_num,user_num)
    user_num=int(input("Enter Your Number: "))

print("Correct")