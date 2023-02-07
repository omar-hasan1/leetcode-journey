'''
Given an array of distinct integers and an integer representing the target sum, 
we are asked to implement a function that is going to find out whether 
there's a pair of numbers in the array that adds up to the target sum. 
If such pair exists, return the pair in any order; otherwise return an empty array. 
We cannot add a number to itself to get the target sum.
Note: it is similar to Leetcode two sum problem but little bit complex
'''

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        nums = {}
        for num in array:
            if targetSum - num in nums:
                return [ targetSum - num, num ]
            else:
                nums[num] = True
        return []

x = Solution()
