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