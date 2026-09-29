

def merge_sort(arr):

    if len(arr)<=1:
        return arr

    m=len(arr)//2

    left=arr[:m]
    right=arr[m:]

    left_sorted=merge_sort(left)
    right_sorted=merge_sort(right)

    return merge(left_sorted,right_sorted)


def merge(left_arr,right_arr):
    i=0
    j=0

    res=[]

    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i]<=right_arr[j]:
            res.append(left_arr[i])
            i+=1
        else:
            res.append(right_arr[j])
            j+=1

    res.extend(left_arr[i:])
    res.extend(right_arr[j:])

    return res

array=[1,2,5,3,4,9,0,3]

print(merge_sort(array))