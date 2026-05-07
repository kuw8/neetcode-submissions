class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            cnt = 0

            for j in range(i, len(nums)):
                if nums[j] == 1:
                    cnt += 1
                else:
                    break
            
            res = cnt if cnt > res else res
        
        return res

                
            
            


            
            
