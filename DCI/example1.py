def sum_of_list(list): 
    #import ipdb; ipdb.set_trace()
    print(list)
    flatten_list=[]
    for item in list: 
        print("Item value: " + str(item))
        flatten_list.append(item)
    return sum(flatten_list)

result = sum_of_list([1,2,3,4,5,6,7,8])
print("Final result: "  + str(result))