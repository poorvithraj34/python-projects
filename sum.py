def first_duplicate(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

    return -1

print(first_duplicate([2,3,4,2,5,6]))
    