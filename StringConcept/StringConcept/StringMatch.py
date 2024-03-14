# def common_characters(str1, str2):
#     # Initialize an empty set to store common characters
#     common_chars = set()
#
#     # Iterate over each character in the first string
#     for char in str1:
#         # Check if the character exists in the second string
#         if char in str2:
#             # Add the common character to the set
#             common_chars.add(char)
#
#     # Return the set of common characters
#     return common_chars
#
# # Example usage
# string1 = "hello"
# string2 = "world"
# common = common_characters(string1, string2)
# print("Common characters:", common)
string1="abhishek"
string2="sanjay"
output=''
for chr in string1:
    if chr in string2:
        output+=chr
print(output)        