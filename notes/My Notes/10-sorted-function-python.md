
sorted(list_name) : sorts any array
sorted(list_name, reverse=True) : Descending order
sorted(list_name, reverse=True, key=Function()) : runs that function on each element of the list and then sorts.


eg:

list = [puppy , appple , hey]
sorted(list_name, reverse=True, key=len) : this will run len function on each element at a time (not the full list) and then use the sort

