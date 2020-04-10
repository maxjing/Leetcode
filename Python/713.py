class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        product = 1
        left = 0
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left < len(nums):
                product /= nums[left]
                left += 1
            # case [1, 2, 3] k = 0, without right > left count will be negative
            if right > left:
                count += right - left + 1
        return count
