def bold_nth_character(text: str, n: int) -> str:
    '''
    Returns a string where the nth character is wrapped in <b></b> tags.
    If n is invalid, returns the original string unchanged.
    '''
    if n < 1 or len(text) < n:
      return text
    else:
      return text[:n-1] + "<b>" + text[n-1] + "</b>" + text[n:]