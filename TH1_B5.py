def count_digits_dp(a, b):
  """
  Hàm này đếm số lần xuất hiện của mỗi chữ số từ 0 đến 9 trong phạm vi từ a đến b sử dụng lập trình động.
  """
  MAX_VALUE = 10**8  # Giới hạn tối đa cho A và B
  dp = [[0] * 10 for _ in range(MAX_VALUE + 1)]
  for i in range(1, MAX_VALUE + 1):
    for j in range(10):
      dp[i][j] = dp[i // 10][j]
    dp[i][i % 10] += 1

  result = [0] * 10
  for d in range(10):
    result[d] = dp[b][d] - dp[a - 1][d]
  return result

# Đọc số lượng bộ test
t = int(input())

# Xử lý từng bộ test
for _ in range(t):
  a, b = map(int, input().split())
  result = count_digits_dp(a, b)
  print(*result)  # In kết quả ra màn hình