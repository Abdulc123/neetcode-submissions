class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Return the median (middle) value of two arrays sorted in increasing order

        # If Odd length, then take the middle index
        # If Even length, take the middle index and the one to its right and add then divide by 2

        # Combine the two lists into one increasing order list
        combinedList = nums1 + nums2
        combinedList.sort()
        print(combinedList)

        # Determine its length and find the median based off of that
        lengthOfCombinedList = len(combinedList)
        mid = (lengthOfCombinedList - 1) // 2

        # Even length
        if lengthOfCombinedList % 2 == 0: 
            return (combinedList[mid] + combinedList[mid + 1]) / 2
        # Odd length
        else:
            return combinedList[mid]
        
