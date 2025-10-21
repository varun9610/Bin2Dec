def bin2dec(binaryinfunction):
    decimalinfunction = 0
    for digit in binaryinfunction:
        decimalinfunction = decimalinfunction * 2 + int(digit)
    return decimalinfunction


def check_num_valid(binarynumber):
    for digit in binarynumber:
        if int(digit) != 0 and int(digit) != 1:
            return 0
    return 1


if __name__ == '__main__':
    binary = input("Enter Binary Number")
    result = check_num_valid(binary)
    if result == 0:
        print("invalid binary number")
    else:
        decimal = bin2dec(binary)
        print("Decimal Number is: ", decimal)
