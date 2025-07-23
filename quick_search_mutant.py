def quick_search(arr, target):
    """
    Mutant version of quick_search with an intentional bug.
    The bug is in the quick sort implementation where the pivot is chosen as the last element
    but the list slicing still starts from index 1, causing the pivot to be included in the
    left or right partitions. This will lead to incorrect sorting and cause the binary search to fail.
    """
    def quick_sort(lst):
        """Buggy quick sort that incorrectly handles the pivot element."""
        if len(lst) <= 1:
            return lst
        
        # BUG: Choosing last element as pivot but still using lst[1:]
        pivot = lst[-1]
        left = [x for x in lst[1:] if x <= pivot]  # Should be lst[:-1]
        right = [x for x in lst[1:] if x > pivot]  # Should be lst[:-1]
        
        return quick_sort(left) + [pivot] + quick_sort(right)

    def binary_search(sorted_arr, target):
        """Standard binary search that expects a properly sorted array."""
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
    
    sorted_arr = quick_sort(arr)
    return binary_search(sorted_arr, target)
