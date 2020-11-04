
list1 = [11,2,5,10,3,15,1]

for i in range(len(list1)):
    for j in range(len(list1)):
        if list1[i] < list1[j]:
            temp = list1[i]
            list1[i]=list1[j]
            list1[j]=temp
        else:
            pass

print(list1)