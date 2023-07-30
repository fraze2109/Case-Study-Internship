# import json (for output)
import json


# function to generate array
def generate_array():
    result = []  # create array
    # iterate from 1 to 100 using for loop, 
    # add each number into the array except for those that fits the criteria
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:  # if divisible by 3 and 5, add BIGBANG into array
            result.append("BIGBANG")
        elif num % 3 == 0:  # if divisible by 3, add BIG into array
            result.append("BIG")
        elif num % 5 == 0:  # if divisible by 5, add BANG into array
            result.append("BANG")
        else:  # if does not fit any of the above, add the number into the array
            result.append(str(num))
    return result

#  function to generate .json file for output
def save_to_json(output):
    with open('result.json', 'w') as file:
        json.dump(output, file)

#  call functions
output = generate_array()
save_to_json(output)
