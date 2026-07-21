class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        n=len(nums)
        k%=n
        x=nums[-k:]
        y=nums[:-k]
        nums[:]=x+y