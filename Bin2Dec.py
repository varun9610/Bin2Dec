def bin2dec(binaryinfunction):
    decimalinfunction = 0
    for digit in binaryinfunction:
        decimalinfunction = decimalinfunction * 2 + int(digit)
    return decimalinfunction


if __name__ == '__main__':
    binary = input("Enter Binary Number")
    decimal = bin2dec(binary)
    print("Decimal Number is: ", decimal)
