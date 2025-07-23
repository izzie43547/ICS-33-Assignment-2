def quick_search(arr, target):
    """
    Sorts the input array using quick sort and then performs binary search for the target.
    
    Args:
        arr (list): The input list to search in
        target: The value to search for
        
    Returns:
        int or None: Index of target if found, None otherwise
    """
    def quick_sort(lst):
        """Sorts a list using quick sort algorithm."""
        if len(lst) <= 1:
            return lst
        
        pivot = lst[0]
        left = [x for x in lst[1:] if x <= pivot]
        right = [x for x in lst[1:] if x > pivot]
        
        return quick_sort(left) + [pivot] + quick_sort(right)

    def binary_search(sorted_arr, target):
        """
        Performs binary search on a sorted array.
        
        Args:
            sorted_arr (list): A sorted list to search in
            target: The value to search for
            
        Returns:
            int or None: Index of target if found, None otherwise
        """
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
