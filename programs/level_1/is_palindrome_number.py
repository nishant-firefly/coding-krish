def is_palindrome_number(x):
    """
    Determines if an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

    Example:
    Input: 121
    Output: True

    Input: -121
    Output: False
    """
    # Krish's code here
    pass

if __name__ == "__main__":
    # Test cases
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(-121) == False
    assert is_palindrome_number(10) == False
    assert is_palindrome_number(12321) == True
    assert is_palindrome_number(0) == True
    print("All test cases passed for is_palindrome_number!")
