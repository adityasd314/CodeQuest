def custom_base_to_int(s, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    value = 0

    for digit in s:
        value = value * base + digits.index(digit)

    return value

def find_max_all_ones_base(number):
    max_base = 2 
    max_length = 1
    current_base = 2

    while True:
        current_length = 1

        if current_base <= 35:
            current_value = int('1', current_base)
        else:
            current_value = custom_base_to_int('1', current_base)

        while current_value <= number:
            if current_value == number:
                return current_base

            current_length += 1

            if current_base <= 35:
                current_value = current_value * current_base + 1
            else:
                current_value = current_value * current_base + custom_base_to_int('1', current_base)

        current_base += 1

        if current_base > number:
            break

    return max_base

number_in_base_10 = int(input())
result_base = find_max_all_ones_base(number_in_base_10)
print(result_base)