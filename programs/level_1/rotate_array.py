def rotate_array(nums, k):
    """
    Rotates an array to the right by k steps.

    Example:
    Input: [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]

    Input: [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    """
    # Krish's code here
    pass

if __name__ == "__main__":
    # Test cases
    assert rotate_array([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4]
    assert rotate_array([-1,-100,3,99], 2) == [3,99,-1,-100]
    assert rotate_array([1,2], 3) == [2,1]  # When k > len(nums), k = k % len(nums)
    assert rotate_array([1], 0) == [1]  # No rotation
    print("All test cases passed for rotate_array!")
