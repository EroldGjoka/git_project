# Prompt user to input a number store & into number
number = int(input("Type a number : "))


# Create a count variable
sum_number = 0


# While "number" is different to -1 do this:
while number != -1:
    # Add number to sum_number store it to sum_number
    sum_number += number
    # Prompt user to input a number & store into number
    number = int(input("Type a number : "))

# Display message "The total sum is: {sum_number}"
print(f"The total sum is : {sum_number}")
