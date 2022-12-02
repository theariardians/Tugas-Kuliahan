def reverse_a_string(string: str) -> str:
    """
    This method is used to reverse a string.
    Args:
        string: a string to reverse

    Returns: a reversed string
    """
    if type(string) != str:
        raise TypeError("{0} This not a string, Please provide a string!".format(type(string)))
    string_place_holder = ""
    start = 0
    end = len(string) - 1
    if end >= 1:
        while start <= end:
            string_place_holder = string_place_holder + string[end]
            end -= 1
        return string_place_holder
    else:
        return string
    
a = "DINA"
rev = reverse_a_string(a)
print(rev)
