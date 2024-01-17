# 75. sort color
# Given an array nums with n objects colored red, white, or blue, 
# sort them in-place so that objects of the same color are adjacent,
#  with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 


# c++ soluation


# class Solution {
# public:
#     void sortColors(vector<int>& nums) {
#        int l,m,h;
#         l=0;
#         m=0;
#         h=nums.size()-1;
#         while(m<=h){
#         if(nums[m]==0){
#             swap(nums[m],nums[l]);
#         l++;
#       m++;
#         }
#         else if(nums[m]==1){
#             m++;
#         }
#         else{
#             swap(nums[m],nums[h]);
#             h--;
#         }
#         }
#     }
# };

# python sol

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        m=0
        h=len(nums)-1
        while(m<=h):
            if(nums[m]==0):
                nums[m],nums[l]=nums[l],nums[m]
                m=m+1
                l=l+1
            elif(nums[m]==1):
                m=m+1
            else:
                nums[m],nums[h]=nums[h],nums[m]
                h=h-1

