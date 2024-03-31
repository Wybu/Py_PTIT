class ThreeSumZero:
    def find_triplets(self, nums):
        triplets = []
        nums.sort()  # Sort the array to make the search easier
        n = len(nums)
        for i in range(n - 2):  # Loop through the array
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements
            left, right = i + 1, n - 1  # Pointers for two sum search
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1  # Skip duplicate elements
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1  # Skip duplicate elements
                elif total < 0:
                    left += 1  # Increment left pointer if sum is less than zero
                else:
                    right -= 1  # Decrement right pointer if sum is greater than zero

        return triplets


# Example usage:
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    three_sum = ThreeSumZero()
    print(three_sum.find_triplets(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
