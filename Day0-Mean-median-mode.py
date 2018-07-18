N = int(input())
str = input()
list = [int(i) for i in str.split()]
print('%.1f' %(sum(list)/len(list)))   #Mean 
sort_list = sorted(list)
n = len(sort_list)
if n%2==0:
    median = (sort_list[int(n/2-1)]+sort_list[int(n/2)])/2
    print('%.1f' %median)
else:
    median = sort_list[int(n/2)]
    print('%.1f' %median)
    
dict = {i : list.count(i) for i in list}
modes =[]
for key,value in dict.items():
    if max(dict.values())==value:
        modes.append(key)
        
print(min(modes))
    

    
