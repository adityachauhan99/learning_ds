n = int(input())
arr = list(map(int, input().split()))
sorted_list=sorted(set(arr))                
print(sorted_list[len(sorted_list)-2])