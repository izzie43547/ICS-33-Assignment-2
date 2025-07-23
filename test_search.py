import unittest
from bubble_search import bubble_search
from quick_search import quick_search

class TestSearchAlgorithms(unittest.TestCase):
    def test_search_existing_element(self):
        """Test searching for an element that exists in the array."""
        test_list = [5, 3, 8, 4, 2]
        target = 4
        
        # Both functions should find the target at the same index after sorting
        bubble_result = bubble_search(test_list, target)
        quick_result = quick_search(test_list, target)
        
        # The actual index might be different, but both should find the element
        self.assertIsNotNone(bubble_result)
        self.assertIsNotNone(quick_result)
        
        # Verify the element at the returned index is indeed the target
        sorted_list = sorted(test_list)
        self.assertEqual(sorted_list[bubble_result], target)
        self.assertEqual(sorted_list[quick_result], target)
    
    def test_search_non_existing_element(self):
        """Test searching for an element that doesn't exist in the array."""
        test_list = [9, 1, 6, 3]
        target = 7  # Not in the list
        
        # Both functions should return None for non-existing element
        self.assertIsNone(bubble_search(test_list, target))
        self.assertIsNone(quick_search(test_list, target))

if __name__ == '__main__':
    unittest.main()
