#Create a bubble sort function -> have the largest number 'bubble' up to the end of the list

def bubble_sort(ls):
    sort_state = False
    ordered = 0
    #keep going while the list is not ordered (use ordered to check if we have fun through the list and made no swaps)
    while not sort_state:
        i = 0
        #for loop going through the list
        for _ in ls:
            #put in a stop for i + 1
            if i+1 < len(ls):
                #check if i is greater than i + 1
                if ls[i] > ls[i+1]:
                    #then swap
                    holder = ls[i]
                    ls[i] = ls[i+1]
                    ls[i+1] = holder
                    i += 1
                    ordered = 0
                else:
                    #add a count to ordered and increase i
                    ordered += 1
                    i += 1
                    #if ordered is the same length as the list then it is sorted
                    if ordered == len(ls):
                        sort_state = True
    return ls

print(bubble_sort([3,1,1,2,9,6,5,7]))
