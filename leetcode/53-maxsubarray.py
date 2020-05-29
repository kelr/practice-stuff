# this succs D:
def maxSubArrayGreedyDoesntWork(nums) -> int:
    max_sum = float('-inf')
    head = 0
    tail = 0
    curr_sum = 0
    out_sz = 0
    while head < len(nums):
        if head == tail:
            print("forced to add", nums[head])
            curr_sum += nums[head]
            out_sz += 1
            if curr_sum > max_sum and out_sz > 0:
                max_sum = curr_sum
                print("newmax", max_sum)
            head += 1
            continue

        if curr_sum + nums[head] < curr_sum - nums[tail]:
            print("cut", nums[tail])
            curr_sum -= nums[tail]
            out_sz -= 1
            if curr_sum > max_sum and out_sz > 0:
                max_sum = curr_sum
                print("newmax", max_sum)
            tail += 1
        else:
            print("add", nums[head])
            curr_sum += nums[head]
            out_sz += 1
            if curr_sum > max_sum and out_sz > 0:
                max_sum = curr_sum
                print("newmax", max_sum)
            head += 1

    while tail < len(nums):
        print("cut", nums[tail])
        curr_sum -= nums[tail]
        out_sz -= 1
        if curr_sum > max_sum and out_sz > 0:
            max_sum = curr_sum
            print("newmax", max_sum)
        tail += 1


    return max_sum

# Kadane's algorithm. O(N) since its single pass. O(1) space
def maxSubArray(nums) -> int:
    max_sum = float('-inf')
    curr_max = 0

    for num in nums:
        curr_max += num
        if curr_max > max_sum:
            max_sum = curr_max
        if curr_max < 0:
            curr_max = 0

    return max_sum

print(maxSubArray([2,-3,1,3,-3,2,2,1]))