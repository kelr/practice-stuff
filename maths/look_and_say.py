import sys

# Non Generator implementation of the Look and Say sequence A005150 in the OEIS

# Time complexity is O(n), where n is the size of the string
def get_next_iter(string):
    # First char in the string should be the test char
    char_under_test = string[0]
    curr_count = 0
    result = ""

    for char in string:
        # If another iteration of the char is found, increment
        if char == char_under_test:
            curr_count += 1
        # Otherwise append our results to the output string
        else:
            result += str(curr_count)
            result += str(char_under_test)

            # Reset count to 1 and not 0 since we're not the first char in the string
            curr_count = 1
            char_under_test = char

    # Append the rest of the data after we iterated through the string
    result += str(curr_count)
    result += string[-1]
    return result

def generate_weird_strings(iterations):
    curr_string = "1"
    output_list = []

    if iterations < 0:
        print("Can't have negative iterations")
        return output_list

    output_list.append(curr_string)
    for i in range(iterations):
        curr_string = get_next_iter(curr_string)
        output_list.append(curr_string)

    return output_list

def main(argv):
    result = generate_weird_strings(int(argv[1]))
    print(result)

if __name__ == '__main__':
    main(sys.argv)