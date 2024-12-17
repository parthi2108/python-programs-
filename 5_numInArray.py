def array_sum(arr,sum):
    arr.sort()
    left = 0
    right = len(arr)-1

    while (left <= right):
        if (arr[left]+arr[right] > sum):
            right = right-1
        elif (arr[left]+arr[right] < sum):
            left = left+1
        elif (arr[left]+arr[right] == sum):
            print("The values of pair :", arr[left],"&",arr[right])
            right = right-1
            left = left+1

        

arr = [1,2,3,5,6,8,9]
sum = 17

array_sum(arr,sum)



    