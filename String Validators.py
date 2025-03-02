if __name__ == '__main__':
    s = input().strip()  # Read input string
    
    # Print whether the string contains at least one alphanumeric character
    print(any(c.isalnum() for c in s))
    
    # Print whether the string contains at least one alphabetical character
    print(any(c.isalpha() for c in s))
    
    # Print whether the string contains at least one digit
    print(any(c.isdigit() for c in s))
    
    # Print whether the string contains at least one lowercase character
    print(any(c.islower() for c in s))
    
    # Print whether the string contains at least one uppercase character
    print(any(c.isupper() for c in s))
