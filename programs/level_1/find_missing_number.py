def find_missing_number(nums):
    """
    Finds the missing number in a list containing n distinct numbers taken from 0, 1, 2, ..., n.

    Example:
    Input: [3, 0, 1]
    Output: 2

    Input: [0, 1]
    Output: 2
    """
    # Krish's code here
    pass

if __name__ == "__main__":
    # Test cases
    assert find_missing_number([3, 0, 1]) == 2
    assert find_missing_number([0, 1]) == 2
    assert find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert find_missing_number([0]) == 1
    assert find_missing_number([1]) == 0
    print("All test cases passed for find_missing_number!")
