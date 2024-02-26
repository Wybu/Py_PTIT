def format_number_with_commas(number):
    s = str(number)
    parts = [s[max(i - 3, 0):i] for i in range(len(s), 0, -3)][::-1]
    formatted_number = ",".join(parts)
    return formatted_number

result = format_number_with_commas(input())
print(result)
