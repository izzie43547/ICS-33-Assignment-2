# Complexity and Mutation Analysis

## Bubble Sort Complexity

### Time Complexity Analysis

```python
def bubble_sort(lst):
    n = len(lst)                    # O(1)
    result = lst.copy()             # O(n)
    for i in range(n):              # O(n) iterations
        for j in range(0, n-i-1):   # O(n-i) iterations
            if result[j] > result[j+1]:  # O(1)
                result[j], result[j+1] = result[j+1], result[j]  # O(1)
    return result                   # O(1)

def binary_search(sorted_arr, target):
    left, right = 0, len(sorted_arr)-1  # O(1)
    while left <= right:                # O(log n) iterations
        mid = (left + right) // 2       # O(1)
        mid_val = sorted_arr[mid]       # O(1)
        if mid_val == target:           # O(1)
            return mid                  # O(1)
        elif mid_val < target:          # O(1)
            left = mid + 1              # O(1)
        else:                           # O(1)
            right = mid - 1             # O(1)
    return None                         # O(1)
```

### Complexity Breakdown
- Bubble Sort: O(n²) in worst and average case, O(n) in best case (already sorted)
- Binary Search: O(log n)
- **Total Complexity**: O(n²) + O(log n) = O(n²)

The bubble sort's quadratic time complexity dominates the logarithmic complexity of the binary search, making the overall time complexity O(n²).

## Quick Sort Complexity

### Time Complexity Analysis

```python
def quick_sort(lst):
    if len(lst) <= 1:                    # O(1)
        return lst                       # O(1)
    
    pivot = lst[0]                       # O(1)
    left = [x for x in lst[1:] if x <= pivot]  # O(n)
    right = [x for x in lst[1:] if x > pivot]  # O(n)
    
    return quick_sort(left) + [pivot] + quick_sort(right)  # T(n) = 2T(n/2) + O(n)

# Binary search is the same as above, O(log n)
```

### Complexity Breakdown
- Quick Sort: O(n log n) average case, O(n²) worst case (when already sorted or reverse sorted)
- Binary Search: O(log n)
- **Total Complexity**: O(n log n) + O(log n) = O(n log n) on average

In the average case, quick sort's O(n log n) dominates the binary search's O(log n). However, in the worst case (already sorted or reverse sorted input), quick sort degrades to O(n²).

## Worklist Algorithm Analysis

### Algorithm Description
The worklist algorithm processes a matrix by continuously updating its values based on the sum of elements in the same row and column. It uses a worklist to track which positions need to be updated.

### Time Complexity Analysis

```python
def worklist_algorithm(matrix):
    n = len(matrix)                                 # O(1)
    worklist = [(i, j) for i in range(n) for j in range(n)]  # O(n²)
    
    while worklist:                                  # O(n³) in worst case
        i, j = worklist.pop()                       # O(1)
        for k in range(n):                          # O(n)
            new_val = matrix[i][k] + matrix[k][j]    # O(1)
            if new_val < matrix[i][j]:               # O(1)
                matrix[i][j] = new_val               # O(1)
                for m in range(n):                   # O(n)
                    worklist.append((i, m))          # O(1)
                    worklist.append((m, j))          # O(1)
```

### Complexity Breakdown
1. Initialization of worklist: O(n²)
2. Outer while loop: Can run up to O(n³) times in the worst case
   - For each position (i,j), the value can be updated up to O(n) times
   - Each update can trigger O(n) new worklist entries
3. Inner loops: O(n) for each iteration of the while loop

**Total Complexity**: O(n³) in the worst case

### Formal Proof
We need to show that there exist constants c and n₀ such that for all n ≥ n₀, the running time T(n) ≤ c·n³.

1. Let's analyze the number of operations:
   - Initialization: c₁·n²
   - While loop iterations: Up to c₂·n³
   - Operations per iteration: c₃·n
   - Total operations: T(n) ≤ c₁·n² + c₂·n³·c₃·n = c₁·n² + c₂·c₃·n⁴

2. For n ≥ 1, n⁴ ≥ n³, so we can say T(n) ≤ (c₁ + c₂·c₃)·n⁴

3. Choose c = c₁ + c₂·c₃ and n₀ = 1, then for all n ≥ n₀, T(n) ≤ c·n⁴

Therefore, T(n) = O(n⁴)

## Mutation Explanation

### Bubble Search Mutant
**File**: bubble_search_mutant.py
**Bug**: Changed the comparison operator in bubble sort from `>` to `<`
**Effect**: Causes the list to be sorted in descending order instead of ascending order
**Why it fails**: The binary search function expects the input list to be sorted in ascending order. When given a descending list, the binary search will not work correctly and may return incorrect results or None even when the element exists in the list.

### Quick Search Mutant
**File**: quick_search_mutant.py
**Bug**: Changed the pivot selection to the last element but didn't adjust the list slicing
**Effect**: The pivot element is included in both left and right partitions, causing incorrect sorting
**Why it fails**: The quick sort implementation produces an incorrectly sorted list, which causes the binary search to fail since it relies on the list being properly sorted. The bug can lead to infinite recursion in some cases or incorrect search results.

## Verification of Mutants
To verify that the mutants fail the tests:

1. For bubble_search_mutant.py:
   - Input: [5, 3, 8, 4, 2], target=4
   - Correct behavior: Should return index 2 (after sorting: [2, 3, 4, 5, 8])
   - Mutant behavior: Sorts to [8, 5, 4, 3, 2], binary search fails to find 4

2. For quick_search_mutant.py:
   - Input: [9, 1, 6, 3], target=1
   - Correct behavior: Should return index 0 (after sorting: [1, 3, 6, 9])
   - Mutant behavior: Incorrect sorting causes binary search to fail
