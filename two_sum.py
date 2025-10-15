# LeetCode Problem 1: Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/
# Author: Miriam Wepiya Gale

class Solution(object):
    def two_sum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# -------------------------------
# Run the code below this line
# -------------------------------
if __name__ == "__main__":
    solution = Solution()
    result = solution.two_sum([2, 7, 11, 15], 9)
    print(result)
