class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # values of nums[i],nums[j], nums[k] must add up to 0
        # -i = j + k
        # output does not have any duplicate triplets

        # -4,-1,-1,0,1,2
        # i = -4, 4 = j + k
        # j = -1, k = 2, 1 < 4
        # j = -1, k = 2, 1 < 4
        # j = 0, k = 2, 2 < 4
        # j = 1, k = 2, 3 < 4
        # Stop 
        # i = -1, 1 = j +k
        # j = -1, k = 2, 1 = 1, add them to a set containing lists (removes duplicates)
        # Stop
        # i = -1, 1 = j +k
        # j = 0, k = 2 , 2 > 1
        # j = 0, k = 1, 1 = 1, add them to the set containing lists which removes duplicates

        # sort the array
        nums.sort()
        answer = set()
        i = 0
        n = len(nums)
        print(nums)

        while i < n:
            target = -nums[i]
            j = i + 1
            k = n - 1

            while j < k:
                result = nums[j] + nums[k]

                if result > target:
                    k -= 1
                elif result < target: 
                    j += 1
                else: # equals target 
                    answer.add((nums[i], nums[j], nums[k]))
                    
                    # continue with the code to continue checking until j and k overlap 
                    j += 1
                    k -= 1


            
            i += 1

        
        return [list(t) for t in answer]
        