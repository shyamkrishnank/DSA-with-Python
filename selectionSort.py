def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i   # selecting i as the min
        for j in range(i+1,len(arr)):
             if arr[min] > arr[j]: # comparing min with each elements
                 min = j #changing the min value
        arr[i],arr[min] = arr[min],arr[i] #swapping
    return arr
arr=[9,6,6,5,6,7,78]
print(selection_sort(arr))