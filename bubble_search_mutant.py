def bubble_search(arr, target):
    """
    Mutant version of bubble_search with an intentional bug.
    The bug is in the bubble sort implementation where the comparison is changed from > to <,
    which will cause the list to be sorted in descending order instead of ascending order.
    This will make the binary search fail since it expects a sorted list in ascending order.
    """
    def bubble_sort(lst):
        """Buggy bubble sort that sorts in descending order."""
        n = len(lst)
        result = lst.copy()
        for i in range(n):
            for j in range(0, n - i - 1):
                # BUG: Changed > to < which will sort in descending order
                if result[j] < result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result

    def binary_search(sorted_arr, target):
        """Standard binary search that expects a sorted array in ascending order."""
        left, right = 0, len(sorted_arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_val = sorted_arr[mid]
            
            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return None
    
    sorted_arr = bubble_sort(arr)
    return binary_search(sorted_arr, target)
