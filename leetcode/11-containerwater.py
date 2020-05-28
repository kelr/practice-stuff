
# Compare each height to each subsequent height and calculate the area. Save and return the maximum area.
# O(N^2) time complexity since it needs to make N(N-1)/2 comparisons.
# O(1) space
def max_area_brute(height) -> int:
    if len(height) == 2:
        return calc_area(0, 1, height[0], height[1])
    max_area = 0

    for i, val in enumerate(height):
        for curr_idx in range(i+1, len(height)):
            area = calc_area(i, curr_idx, val, height[curr_idx])
            if area > max_area:
                max_area = area
    return max_area

# Start with the first and last heights and calculate the area. Move the lower height towards the opposite height's direction
# until the heights meet each other. Save and return the max area. If heights are equal just move the left one.

# O(N) time since both indicies will move at most N-1 times in total.
def max_area_scan(height) -> int:
    # Constraint is that N >= 2, so if N = 2 only one area can be formed.
    if len(height) == 2:
            return calc_area(0, 1, height[0], height[1])
    max_area = 0
    left_idx = 0
    right_idx = len(height) - 1

    while left_idx != right_idx:
        area = calc_area(left_idx, right_idx, height[left_idx], height[right_idx])
        if area > max_area:
            max_area = area

        # Move the lower height towards the opposite end.
        if height[left_idx] <= height[right_idx]:
            left_idx += 1
        else:
            right_idx -= 1

    return max_area

# Index 2 must be >= index 1 and all values should be non negative ints.
def calc_area(index1, index2, val1, val2) -> int:
    return (index2-index1) * min(val1, val2)

print(max_area_scan([1,8,6,2,5,4,8,3,7]))