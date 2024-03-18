
# Ask user to input a text and store it in "str_manip"
str_manip = input("Type text here : ")


#                   (1 Line Code)
# Dsplay message "The leght of str_manip is : " + leght of str_manip
print("The leght of str_manip is : ", + len(str_manip))


# or


#            (Saved and easily retrieved)
# Create a variable "len_str_manip" and store the leght of str_manip
len_str_manip = len(str_manip)


# Display message "The leght of str_manip is : " + len_str_manip
print("The leght of str_manip is : ", + len_str_manip)


''' Take str_manip and replace every letter equal to last
with "@" and store in "replace_str_manip"'''
replace_str_manip = str_manip.replace(str_manip[-1], "@")

# Display message "The replaced text is : " + replace_str_manip
print("The replaced text is : ", replace_str_manip)


''' Take the last 3 characters of str_manip and
store it in "last_3_char_str_manip"'''
last_3_char_str_manip = str_manip[-3:]

''' Display message "The last three characters
of your text are : " + last_3_char_str_manip'''
print("The last three characters of your text are : ", last_3_char_str_manip)


''' Take first 2 and last 3 characters of str_manip add
them together and store them "five_letter_str_manip" '''
five_letter_str_manip = str_manip[:2] + str_manip[-3:]

# Display message "The 5 letter string is : " + the five_letter_str_manip
print("The 5 letter string is : ", five_letter_str_manip)
