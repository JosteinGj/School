def recursive_sum(n):
    if n==1:
        return 1
    return n+recursive_sum(n-1)

print(recursive_sum(3))

def find_smallest_elem(nums):
    minimum=nums[0]
    for i in nums:
        if i<minimum:
            minimum=i
    return minimum
print(find_smallest_elem([1,2,3,4,5,10,0,-123,7,124]))

def binary_search(nums,elem):
    nums=sorted(nums)
    mid=len(nums)//2-1
    if nums[mid]==elem:
        return mid
    elif len(nums)<=1:
        return -float("inf")
    elif nums[mid]<elem:
        return mid + binary_search(nums[mid:],elem)
    elif nums[mid]> elem:
        return mid + binary_search(nums[:mid],elem)

print(binary_search([1,2,3,3,3,3,3,3,3,5,7,56,74],1))





