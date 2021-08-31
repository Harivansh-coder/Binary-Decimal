from .reverse import reverse

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