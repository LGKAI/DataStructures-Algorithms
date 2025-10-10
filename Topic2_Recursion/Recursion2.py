def groupSum(start, nums, target):
    if start >= len(nums):
        return target == 0
    return groupSum(start + 1, nums, target - nums[start]) or groupSum(start + 1, nums, target)

def groupSum6(start, nums, target):
    if start >= len(nums):
        return target == 0
    if nums[start] == 6:
        return groupSum6(start + 1, nums, target - nums[start])
    return groupSum6(start + 1, nums, target - nums[start]) or groupSum6(start + 1, nums, target)

def groupNoAdj(start, nums, target):
    if start >= len(nums):
        return target == 0
    return groupNoAdj(start + 2, nums, target - nums[start]) or groupNoAdj(start + 1, nums, target)

def groupSum5(start, nums, target):
    if start >= len(nums):
        return target == 0
    if nums[start] % 5 == 0:
        if start + 1 < len(nums) and nums[start + 1] == 1:
            return groupSum5(start + 2, nums, target - nums[start])
        return groupSum5(start + 1, nums, target - nums[start])
    return groupSum5(start + 1, nums, target - nums[start]) or groupSum5(start + 1, nums, target)

def groupSumClump(start, nums, target):
    if start >= len(nums):
        return target == 0
    i = start
    while i < len(nums) and nums[start] == nums[i]:
        i += 1
    return groupSumClump(i, nums, target - (i - start) * nums[start]) or groupSumClump(i, nums, target)

def splitArray(nums):
    def helper(index, sum1, sum2):
        if index >= len(nums):  
            return sum1 == sum2
        return helper(index + 1, sum1 + nums[index], sum2) or helper(index + 1, sum1, sum2 + nums[index])

    return helper(0, 0, 0)

def splitOdd10(nums):
    def helper(index, sum1, sum2):
        if index >= len(nums):
            return (sum1 % 10 == 0) and (sum2 % 2 == 1)
        return helper(index + 1, sum1 + nums[index], sum2) or helper(index + 1, sum1, sum2 + nums[index])

    return helper(0, 0, 0)

def split53(nums):
    def helper(index, sum1, sum2):
        if index >= len(nums):
            return sum1 == sum2
        if nums[index] % 5 == 0:
            return helper(index + 1, sum1 + nums[index], sum2)
        elif nums[index] % 3 == 0:
            return helper(index + 1, sum1, sum2 + nums[index])
        return helper(index + 1, sum1 + nums[index], sum2) or helper(index + 1, sum1, sum2 + nums[index])
    
    return helper(0, 0, 0)


if __name__ == "__main__":
    pass