def reverse(text):
    """
    This function reverses the text passed as argument.
    """
    result = ""
    str_len = len(text)
    for i in range(1,str_len+1):
        result += text[str_len - (i)]

    return result

def binaryToDecimal(binary):
        """
        Function convert Binary to Decimal
        """
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            temp = binary % 10
            decimal = decimal + temp * pow(2, i)
            binary = binary//10
            i += 1

        return decimal

def decimalToBinary(decimalValue):
    """
    Function convert decimal to Binary
    """
    dec = decimalValue
    decimal = ""
    while dec > 1:
        decimal += str(dec%2)
        dec //= 2
    decimal += str(dec)
    return int(reverse(decimal))