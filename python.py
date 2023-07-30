import json


def generate_array():
    result = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            result.append("BIGBANG")
        elif num % 3 == 0:
            result.append("BIG")
        elif num % 5 == 0:
            result.append("BANG")
        else:
            result.append(str(num))
    return result

def save_to_json(output_array):
    with open('output.json', 'w') as file:
        json.dump(output_array, file)

output_array = generate_array()
save_to_json(output_array)
