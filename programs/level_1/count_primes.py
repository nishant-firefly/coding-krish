def count_primes(n):
    """
    Counts the number of prime numbers less than a non-negative number, n.

    Example:
    Input: 10
    Output: 4

    Input: 0
    Output: 0
    """
    # Krish's code here
    pass

if __name__ == "__main__":
    # Test cases
    assert count_primes(10) == 4  # Primes less than 10 are 2, 3, 5, 7
    assert count_primes(0) == 0
    assert count_primes(1) == 0
    assert count_primes(20) == 8  # Primes less than 20 are 2, 3, 5, 7, 11, 13, 17, 19
    assert count_primes(100) == 25
    print("All test cases passed for count_primes!")
