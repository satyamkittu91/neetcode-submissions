class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for arr in matrix:
            if len(arr) == 0:
                continue
            left = 0
            right = len(arr)-1

            while left <= right:
                mid = int(left + (right - left)/2)
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
        return False