def partition(N, max_num=None, current=None):
    if max_num is None:
        max_num = N
    if current is None:
        current = []
    if N == 0:
        return [current]
    result = []
    for i in range(1, min(max_num, N) + 1):
        result.extend(partition(N - i, i, current + [i]))
    return result

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    partitions = partition(N)
    partitions.sort(reverse= True)
    print(len(partitions))
    for p in partitions:
        print("(" + " ".join(map(str, p)) + ")", end=" ")
    print()
