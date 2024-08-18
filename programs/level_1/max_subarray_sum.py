def max_subarray_sum(nums):
    """
    Finds the contiguous subarray (containing at least one number) which has the largest sum and returns that sum.

    Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6

    Input: [1]
    Output: 1
    """
    # Krish's code here
    pass

if __name__ == "__main__":
    # Test cases
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray_sum([1]) == 1
    assert max_subarray_sum([5,4,-1,7,8]) == 23
    assert max_subarray_sum([-1,-2,-3,-4]) == -1
    print("All test cases passed for max_subarray_sum!")
