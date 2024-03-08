lower = "MAYUR"
lower_case = ""
for char in lower:
    # Check if the character is within uppercase range
    if ord('A') <= ord(char) <= ord('Z'):
        # Convert uppercase to lowercase by adding 32 to ASCII value
        lower_case += chr(ord(char) + 32)
    else:
        # If the character is already lowercase, just append it
        lower_case += char

print(lower_case)