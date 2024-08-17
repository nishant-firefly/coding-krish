def is_anagram(str1, str2):
    """
    Determines if two strings are anagrams of each other.
    An anagram is a word or phrase formed by rearranging the letters of another, such as "listen" and "silent".

    Example:
    Input: "listen", "silent"
    Output: True

    Input: "hello", "world"
    Output: False
    """
    # Krish's code herepass

if __name__ == "__main__":
    # Test cases
    assert is_anagram("listen", "silent") == True
    assert is_anagram("triangle", "integral") == True
    assert is_anagram("apple", "pale") == False
    assert is_anagram("a gentleman", "elegant man") == True
    assert is_anagram("aabbcc", "abcabc") == True
    assert is_anagram("abcd", "dcba") == True
    print("All test cases passed for is_anagram!")
