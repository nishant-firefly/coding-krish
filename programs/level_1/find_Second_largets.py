def find_second_largest(numbers):
    """
    Returns the second largest number in a list of integers.

    Example:
    Input: [10, 5, 20, 8, 12]
    Output: 12

    Input: [3, 3, 3, 3]
    Output: None (since there is no second largest unique number)
    """
    # Krish's code here
    pass

if __name__ == "__main__":
    # Test cases
    assert find_second_largest([10, 5, 20, 8, 12]) == 12
    assert find_second_largest([3, 3, 3, 3]) == None
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 5, 5, 4, 4, 3]) == 4
    assert find_second_largest([10]) == None
    # Only one element, no second largest
    print("All test cases passed for find_second_largest!")
