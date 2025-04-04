def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    lines = []
    for i in range(size):
        left = alpha[size-1:i:-1]
        center = alpha[i]
        right = alpha[i+1:size]
        line = '-'.join(left + center + right)
        lines.append(line.center(4 * size - 3, '-'))

    # Print top (excluding middle), then middle, then bottom (mirror of top)
    print('\n'.join(lines[::-1] + lines[1:]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
