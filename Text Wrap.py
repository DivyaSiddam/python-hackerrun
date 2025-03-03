import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)  # Wrap text to specified width

  # Print wrapped text

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
