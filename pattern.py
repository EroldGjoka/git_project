''' Make a string count variable called "star_count'''

StarCount = ""

# for i in every number of range(9)
for i in range(9):

    # if i is less than or equal to 4 then:
    if i <= 4:

        # Add "*" to StarCount and store it in StarCount
        StarCount += "*"

        # Display StarCount
        print(StarCount)
    # Otherwise
    else:

        # Remove the last character from "StarCount"
        StarCount = StarCount[:-1]

        # Display StarCount
        print(StarCount)
