def sum_list(nums):
    result = 0
    for i in nums:
        try:
            result+= int(i)
        except ValueError:
            pass
    return result 




 
