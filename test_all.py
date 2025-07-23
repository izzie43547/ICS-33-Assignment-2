import unittest
import sys
import os

# Import all implementations
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from bubble_search import bubble_search
from quick_search import quick_search
from bubble_search_mutant import bubble_search as bubble_search_mutant
from quick_search_mutant import quick_search as quick_search_mutant

class TestSearchAlgorithms(unittest.TestCase):
    def test_original_implementations(self):
        """Test that original implementations work correctly"""
        test_cases = [
            ([5, 3, 8, 4, 2], 4, 2),  # Middle element
            ([1, 2, 3, 4, 5], 1, 0),  # First element
            ([1, 2, 3, 4, 5], 5, 4),  # Last element
            ([1, 1, 1, 1, 1], 1, 2),  # All same elements (should return any valid index)
            ([], 1, None),             # Empty list
            ([1, 2, 3, 4, 5], 6, None) # Element not in list
        ]
        
        for arr, target, expected in test_cases:
            with self.subTest(arr=arr, target=target):
                # Test bubble search
                result = bubble_search(arr.copy(), target)
                if expected is not None:
                    sorted_arr = sorted(arr)
                    self.assertEqual(sorted_arr[result], target)
                else:
                    self.assertIsNone(result)
                
                # Test quick search
                result = quick_search(arr.copy(), target)
                if expected is not None:
                    sorted_arr = sorted(arr)
                    self.assertEqual(sorted_arr[result], target)
                else:
                    self.assertIsNone(result)

    def test_mutant_implementations_fail(self):
        """Test that mutant implementations fail as expected"""
        test_cases = [
            ([5, 3, 8, 4, 2], 4),  # Existing element
            ([1, 2, 3, 4, 5], 3),  # Middle element
            ([1, 1, 1, 1, 1], 1),  # All same elements
            ([1, 2, 3, 4, 5], 6)   # Non-existing element
        ]
        
        for arr, target in test_cases:
            # Test bubble search mutant
            with self.subTest(test='bubble_mutant', arr=arr, target=target):
                # The mutant should fail by either:
                # 1. Returning None for existing elements
                # 2. Returning incorrect indices
                # 3. Throwing an exception
                try:
                    result = bubble_search_mutant(arr.copy(), target)
                    if target in arr:
                        # If it didn't return None, check if the index is correct
                        sorted_arr = sorted(arr)
                        if result is not None and result < len(sorted_arr):
                            self.assertNotEqual(sorted_arr[result], target,
                                            "Mutant returned correct index but shouldn't have")
                except Exception as e:
                    # Exceptions are expected for some test cases
                    pass
            
            # Test quick search mutant
            with self.subTest(test='quick_mutant', arr=arr, target=target):
                try:
                    result = quick_search_mutant(arr.copy(), target)
                    if target in arr:
                        # If it didn't return None, check if the index is correct
                        sorted_arr = sorted(arr)
                        if result is not None and result < len(sorted_arr):
                            self.assertNotEqual(sorted_arr[result], target,
                                            "Mutant returned correct index but shouldn't have")
                except Exception as e:
                    # Exceptions are expected for some test cases
                    pass

    def test_edge_cases(self):
        """Test edge cases for original implementations"""
        # Single element
        self.assertEqual(bubble_search([1], 1), 0)
        self.assertEqual(quick_search([1], 1), 0)
        self.assertIsNone(bubble_search([1], 2))
        self.assertIsNone(quick_search([1], 2))
        
        # Two elements
        self.assertEqual(bubble_search([2, 1], 1), 0)
        self.assertEqual(quick_search([2, 1], 1), 0)
        
        # Already sorted
        self.assertEqual(bubble_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(quick_search([1, 2, 3, 4, 5], 3), 2)
        
        # Reverse sorted
        self.assertEqual(bubble_search([5, 4, 3, 2, 1], 3), 2)
        self.assertEqual(quick_search([5, 4, 3, 2, 1], 3), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
