def convert(input_str):
    output_str = ""
    for char in input_str:
        if char.islower():
            num = ord(char) - 97
            output_str += str(num)
        elif char.isdigit():
            letter = chr(int(char) + 97)
            output_str += letter
        else:
            output_str += char
    return output_str

input_str = input()
converted_str = convert(input_str)
print(converted_str)
