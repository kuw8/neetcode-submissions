class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        while val in nums:
            for i in range(len(nums)):
                if nums[i] == val:
                    del nums[i]
                    break

        return len(nums)