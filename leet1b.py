#gegeben: [3,2,4]
#output: [0,1]
target=5
nums=[2,8,1,5,6,4,7,3]
def twoSums(nums,target ):
    for iindex,ival in enumerate(nums):
        diff=target-ival
        for jindex, jval in enumerate(nums[iindex+1:], start=iindex+1):
            if jval==diff:
                return [iindex, jindex]

    return []
print(twoSums(nums, target))
