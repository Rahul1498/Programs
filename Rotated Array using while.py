class Solution:
        
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        start=0
        end=len(nums)-1
        while(start<end):
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start=start+1
            end=end-1
        start=0
        end=k-1
        while(start<end):
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start=start+1
            end=end-1
        start=k
        end=len(nums)-1
        while(start<end):
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start=start+1
            end=end-1
    