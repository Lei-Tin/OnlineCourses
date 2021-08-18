def sum_of_odd():

    sum = 0
    myList = []
    
    for i in range(524, 10509, 2):
        
        sum += i
        myList.append(i)

    print(sum)
    print(len(myList))
