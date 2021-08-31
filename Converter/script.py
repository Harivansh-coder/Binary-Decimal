"""
Following script help to convert binary to decimal or vice-versa.
"""

def reverse(text):
    result = ""
    str_len = len(text)
    for i in range(1,str_len+1):
        result += text[str_len - (i)]

    return result

def binaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        temp = binary % 10
        decimal = decimal + temp * pow(2, i)
        binary = binary//10
        i += 1

    return decimal

def decimalToBinary(decimalValue):
    dec = decimalValue
    decimal = ""
    while dec > 1:
        decimal += str(dec%2)
        dec //= 2
    decimal += str(dec)
    return reverse(decimal)

if __name__ == "__main__"
    test = [66,255,69]
    for i in test:
        binary = decimalToBinary(i)
        print(binary)
        print(binaryToDecimal(int(binary)))


"""
#Output
    1000010
    66
    11111111
    255
    1000101
    69
"""
