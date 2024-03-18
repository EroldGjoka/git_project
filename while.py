# Ask user to input a number store in number
number = int(input("Type a number : "))


# Create a count variable
sum_number = 0


# While "number" different to -1 do this:
while number != -1:
    # Add number to sum_numbber store it to sum_numbber
    sum_number += number
    # Ask user to input a number store in number
    number = int(input("Type a number : "))

# Display message "The total sum is : {sum_number}"
print(f"The total sum is : {sum_number}")
