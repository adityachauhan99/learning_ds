def get_average(a,b,c):
    value= (a+b+c)/3
    print(f"{value:.2f}")

my_dict={"name":[50,60,80]}
print(my_dict.get("name"))
get_average(*my_dict.get("name"))