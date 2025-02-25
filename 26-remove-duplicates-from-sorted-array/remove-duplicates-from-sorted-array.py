from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []  # Naya list banane ki zaroorat nahi hai
        
        for i in nums:
            if i not in result:
                result.append(i)
        
        nums[:len(result)] = result  # nums ko modify karna zaroori hai
        return len(result) 

        # result = [] #, nums = [1, 1, 2]
        # for i in nums:
        #     if i not in result:
        #         result.append(i)
        
        # return result