def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique=[]
        t=int()
        i=0
        while(i<len(nums)):
            if(nums[i] in unique):
                nums.remove(nums[i])
                
            else:
                unique.append(nums[i])
                i+=1