def count_occurrences(S, N):
    count = 0
    n_length = len(str(N))
    i = 0
    while i < len(S):
        if S[i] == str(N)[0]:
            if S[i:i+n_length] == str(N):
                count += 1
                i += n_length - 1
        i += 1
    return count

for _ in range(int(input())):
    S = input()
    N = input()
    print(count_occurrences(S, N))  # Output: 3
