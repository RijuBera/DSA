# 287. Find the Duplicate Number
# Solved
# Medium
# Topics
# Companies
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
 

# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.



# c++ Solution
#   int findDuplicate(vector<int>& nums) {
#     //   sort(nums.begin(),nums.end());
#     //   int ans;
#     //     for(int i=0;i<nums.size()-1;i++){
#     //         if(nums[i]==nums[i+1]){
              
#     //             ans=nums[i];
#     //         }
#     //     }
#     while(nums[0]!=nums[nums[0]]){
#         swap(nums[0],nums[nums[0]]);
#     }
#         return nums[0];
#     }
# };

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            index=abs(nums[i])
            if( nums[index]<0):
                ans=index
            else:
                nums[index]=nums[index]*(-1)
        return ans

    
        
     