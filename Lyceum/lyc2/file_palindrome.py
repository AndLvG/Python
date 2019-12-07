def palindrome():
    with open('input.txt', 'rb') as f:
        data = f.read()
    return data == data[::-1]


print(palindrome())
