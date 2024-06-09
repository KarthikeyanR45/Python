def compare(str1, str2):
    if str1 == str2:
        return f"{str1} is equal to {str2}"
    elif str1 < str2:
        return f"{str1} is not equal to {str2}\n{str2} is greater than {str1}"
    else:
        return f"{str1} is not equal to {str2}\n{str1} is greater than {str2}"

if __name__ == "__main__":
    str1 = input("Enter the first string: ")
    str2 = input("\nEnter the second string: ")

    result = compare(str1, str2)
    print(result)
    
