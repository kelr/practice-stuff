# Do binary search on the weight range between the min possible ship
# capacity (the largest weight) and the max ship cap (the sum of all weights).
# Add weights to a ship until it exceeds the mid capacity, then add it to the next ship
# If the number of ships needed exceeds D, shrink binary search size by half.
# O(NlgM) where M is the sum of weights - the max weight.
# O(1) space
def shipWithinDays(weights, D):
    left = max(weights)
    right = sum(weights)
    
    while left < right:
        mid = (left + right) // 2
        shipCount = 1
        currWeight = 0
        
        # Add to the current ship until it exceeds the midpoint
        for w in weights:
            if currWeight + w > mid:
                shipCount += 1
                currWeight = 0
            currWeight += w
            
        if shipCount > D: 
            left = mid + 1
        else: 
            right = mid
    return left