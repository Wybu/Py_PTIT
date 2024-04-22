

filename="VANBAN.IN"
def thuannghich(n):
    n=str(n)
    if n==n[::-1]:
        return True
    return False
def find_longest_word(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        words = text.split()
        longest_word = max(words, key=len)
        return longest_word, words.count(longest_word)

longest_word, count = find_longest_word(filename) and thuannghich(find_longest_word(filename))
print(longest_word, count)