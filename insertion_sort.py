# insertion sort , 
list1 = [ 1,4,2,6,3,99,12,43,54]
for i in range(1,len(list1)):
    j = i - 1
    temp =list1[i]
    print('i , j is : ', i,j)
    while j >= 0 and temp < list1[j]:
        list1[j+1] = list1[j]
        j = j - 1
        print(f'after {i},{j} temp is {temp}')
    list1[j+1] = temp
print(list1)
    
        
        
    
