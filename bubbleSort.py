def bubbleSort(arr):
    for i in range(len(arr)-1,1,-1): #the outer loop that runs -1times after each iteration
        for j in range(i): #the inner loop that iterate according to the outer loop
            if arr[j] > arr[j+1]: # comparison
                arr[j],arr[j+1] = arr[j+1],arr[j]   #swapping when comparison is true
    return arr

