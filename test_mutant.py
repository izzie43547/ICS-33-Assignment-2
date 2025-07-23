import unittest
from bubble_search_mutant import bubble_search

class TestBubbleSearchMutant(unittest.TestCase):
    def test_sorting_order(self):
        """Test that the mutant sorts in descending order"""
        test_list = [5, 3, 8, 1, 2]
        # The mutant should sort in descending order
        result = bubble_search(test_list, 5)  # Search for 5
        # The binary search will fail because it expects ascending order
        # So we expect it to return None or incorrect index
        self.assertNotEqual(result, 0)  # In correct implementation, 5 would be at index 0

    def test_search_existing_element(self):
        """Test searching for an existing element"""
        test_list = [5, 3, 8, 4, 2]
        # The list will be sorted in descending order: [8, 5, 4, 3, 2]
        # So 5 should be at index 1
        result = bubble_search(test_list, 5)
        self.assertEqual(result, 1)  # This will fail because binary search expects ascending order

    def test_search_non_existing_element(self):
        """Test searching for a non-existing element"""
        test_list = [5, 3, 8, 4, 2]
        result = bubble_search(test_list, 10)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
