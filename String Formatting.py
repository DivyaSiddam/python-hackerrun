def print_formatted(number):
    
    width = len(bin(number)) - 2  # Compute width based on binary length
    
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]  # Remove '0o' prefix
        hexadecimal = hex(i)[2:].upper()  # Remove '0x' prefix and capitalize
        binary = bin(i)[2:]  # Remove '0b' prefix
        
        # Print all values right-aligned with width
        print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
