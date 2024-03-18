''' Ask user to input the minutes achived
in each sport respectively, "namely_swim", "cycling", and "running"'''

namely_swim = int(input("Type total minutes achived in namely swimming : "))

cycling = int(input("Type total mimutes achived in cycling : "))

running = int(input("Type total minutes achives in running : "))


# Find sum and store it in triat_sum
triat_sum = namely_swim + cycling + running

#  Display message "The triathlons total time achived is ", + triat_sum
print(f'The triathlons total time achived is {triat_sum} minutes.')


#  If triat_sum is greater than 0 and equal or less than 100 then
if triat_sum >= 0 and triat_sum <= 100:
    # Display message "Congratulations you won Provincial Colours!!!"
    print("Congratulations you won Provincial Colours!!!")


# Else if triat_sum is greater than 100 and equal or less than 105 then
elif triat_sum > 100 and triat_sum <= 105:
    # Display message "Congratulations you won Provincial Half Colours!!!"
    print("Congratulations you won Provincial Half Colours!!!")


# Else if triat_sum is greater than 105 and equal or less than 110 then
elif triat_sum > 105 and triat_sum <= 110:
    # Display message "Congratulations you won Provincial Scroll!!!"
    print("Congratulations you won Provincial Scroll!!!")

# Otherwise run this
else:
    # Display message "No Award Achived"
    print("No Award Achived")
print("End of the program")
