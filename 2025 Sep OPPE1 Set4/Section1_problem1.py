def is_divisible_by_last_two_digits(num: int):
    """
    Checks if the given number is divisible by both of its last two digits.

    Return False if any of the last two digits is 0.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if divisible by both last two digits, False otherwise.
    """
    num_str = str(num)
    if int(num_str[-1]) == 0 or int(num_str[-2]) == 0:
      return False
    
    return num % int(num_str[-1]) == 0 and num % int(num_str[-2]) == 0