class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Remove duplicates
        nums = list(set(nums))

        # Sort the distinct elements
        nums.sort()

        # If there are at least 3 distinct elements
        if len(nums) >= 3:
            return nums[-3]

        # Otherwise return the maximum element
        return nums[-1]