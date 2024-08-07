def is_palindrome(input_str):
    input_str = input_str.lower()
    for i in range(len(input_str) // 2):
        if input_str[i] != input_str[-(i + 1)]:
            return False
    return True
input_string = "madam"
print(is_palindrome(input_string))