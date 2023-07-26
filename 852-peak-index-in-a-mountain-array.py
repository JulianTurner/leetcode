class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        minPeakIndex = 0
        maxPeakIndex = len(arr) - 1
        while minPeakIndex != maxPeakIndex:
            midArrIndex = int((minPeakIndex + maxPeakIndex) / 2) + 1
            if arr[midArrIndex-1] < arr[midArrIndex]:
                # links oder spitze
                minPeakIndex = midArrIndex
            else:
                # rechts oder spitze
                maxPeakIndex = midArrIndex - 1 

        return minPeakIndex

arr = [0,10,5,2]
print(Solution().peakIndexInMountainArray(arr))