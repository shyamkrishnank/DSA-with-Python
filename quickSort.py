def pivot(arr,pivot_index,end_index):
   swap_index = pivot_index
   for i in range(pivot_index+1,end_index+1):
       if arr[i] < arr[pivot_index]:
           swap_index += 1
           arr[i],arr[swap_index] = arr[swap_index],arr[i]
   arr[pivot_index],arr[swap_index] = arr[swap_index],arr[pivot_index]
   return swap_index
def quick(arr,left,right):
   if left < right:
       pivot_index = pivot(arr,left,right)
       left = quick(arr,left,pivot_index-1)
       right = quick(arr,pivot_index+1,right)
       return arr

def quick_sort(arr):
    return quick(arr,0,len(arr)-1)

def quick_sort(arr):
   return quick(arr,0,len(arr)-1)
