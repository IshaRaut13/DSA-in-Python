def maxArea(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left  # distance = 5-1 = 4
        water = width * min(
            height[left], height[right]
        )  # water contained = 4 * (9,8) = 4 * 8 = 32
        max_water = max(max_water, water)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water


print(maxArea([2, 9, 1, 4, 7, 8]))

# Input: height = [2,9,1,4,7,8]
# Output: 32
# Explanation: Choosing the lines at index 1 (height 9) and index 5 (height 8) gives:
# Distance: 5 - 1 = 4
# Minimum height: min(9, 8) = 8
# Water contained: 4 * 8 = 32
