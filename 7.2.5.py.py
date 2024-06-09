def sort_string(s):
    """Sorts a string in alphabetical order."""
    return ''.join(sorted(s))

if __name__ == "__main__":
    a= input("Enter the input string: ")

    b= sort_string(a)

    print(f"\nThe output string: {b}")
