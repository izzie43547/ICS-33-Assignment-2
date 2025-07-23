def bubble_search(arr, target):
    """
    Sorts the input array using bubble sort and then performs binary search for the target.
    
    Args:
        arr (list): The input list to search in
        target: The value to search for
        
    Returns:
        int or None: Index of target if found, None otherwise
    """
    def bubble_sort(lst):
        """Sorts a list using bubble sort algorithm."""
        n = len(lst)
        result = lst.copy()
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    # Swap if the element found is greater than the next element
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result

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
    
    sorted_arr = bubble_sort(arr)
    return binary_search(sorted_arr, target)
