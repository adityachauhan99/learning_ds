[[08-lambda-functions-python]]


numbers = [1,2,3]
result = map(lambda a: a+2,numbers)
print(list(result))

map(function,iterable)
*Whenever you want to run a function on each item on the list , you use map*


filter : similar to map but it removes some of the items based on the filter function
result = filter(lambda a: a%2= =0, numbers)
print(list(result))
