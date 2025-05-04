import string

def is_palindrome(teststr):
    nopunc = ""
    for char in teststr:
        if char not in string.punctuation:
            nopunc += char
    x = nopunc.upper()

    left = 0
    right = len(teststr) - 1
    while left < right:
        if teststr[left] != teststr[right]:
            return False
        
        left += 1
        right -= 1
    

    return True

test = input("Give me a sentence and I will check if this is a palindrome:   ")

result = is_palindrome(test)

print("Palindrome?", result)