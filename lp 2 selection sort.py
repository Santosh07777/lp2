def selectionSort(array): 
    size = len(array) 
    for ind in range(size): 
        min_index = ind 
        for j in range(ind + 1, size): 
            if array[j] < array[min_index]: 
                min_index = j 
        array[ind], array[min_index] = array[min_index], array[ind]

arr = input("Enter the elements of the array separated by spaces: ").split() 
arr = [int(x) for x in arr]  
selectionSort(arr) 
print('The array after sorting in Ascending Order by selection sort is:') 
print(arr)
