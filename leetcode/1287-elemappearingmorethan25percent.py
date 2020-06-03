# Find the threshold value for 25% of the array, linear search to find the first number whose count is greater than it.
# O(N) due to a single pass over arr
# O(1) space
def findSpecialInteger(arr) -> int:
    threshold = len(arr)/4
    count = 0
    curr = arr[0]
    for num in arr:
        if num == curr:
            count += 1
            if count > threshold:
                return curr
        else:
            curr = num
            count = 1

# Since the array is sorted the value thats greater than 25% should be contiguous. Find the first value whose length is > than 25% of arr.
# Assumes that there is at least one value that meets this condition and that theres at least 1 element in the array.
# O(N) due to single pass over arr. 
# O(1) space
def findSpecialIntegerLeap(arr) -> int:
    offset = len(arr)//4
    for i in range(len(arr)):
        if arr[i] == arr[i+offset]:
            return arr[i]


assert findSpecialIntegerLeap([1,2,2,6,6,6,6,7,10]) == 6
