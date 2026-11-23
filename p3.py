print("to check whether the given string is pallindrome or not")

print ("*"*88)

text = input("Enter a string: ")
reverse = ""
index = len(text) - 1

while index >= 0:
    reverse += text[index]
    index -= 1

if text == reverse:
    print("The string is a palindrome")
elif text != reverse:
    print("The string is not a palindrome")
else:
    print("Invalid input")

