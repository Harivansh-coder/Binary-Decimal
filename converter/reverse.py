def reverse(text):
    """
    This function reverses the text passed as argument.
    """
    result = ""
    str_len = len(text)
    for i in range(1,str_len+1):
        result += text[str_len - (i)]

    return result