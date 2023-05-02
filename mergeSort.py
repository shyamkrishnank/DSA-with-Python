def merge(li1, li2):   # the main merge funtion that is used to merge two sorted array
    combain = []
    i = j = 0
    while i < len(li1) and j < len(li2):
        if li1[i] < li2[j]:
            combain.append(li1[i])
            i += 1
        else:
            combain.append(li2[j])
            j += 1
    while i < len(li1):
        combain.append(li1[i])
        i += 1
    while j < len(li2):
        combain.append(li2[j])
        j += 1
    return combain    # returns the sorted array as a new array named "combain"


def merge_sort(arr):
    if len(arr) == 1:  # recursion base case thats the length of the array became 1
        return arr   # returns the array with array size 1
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
