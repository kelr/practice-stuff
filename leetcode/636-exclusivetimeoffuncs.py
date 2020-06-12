
# Maintain a stack of funcs that have started, and pop then when their corresponding
# end appears. An end will always pop off its corresponding start func.
# Maintain a stack of previous function times, this serves to record
# How much time a func that has been pre-empted was waiting.
# O(N) time, single pass through logs
# O(N) space, the func and time stack can grow up to N/2 elements each.
def exclusiveTime(n: int, logs):
    out = [0] * n
    stack = []
    lastTimeStack = []
    
    for log in logs:
        id, action, endTime = log.split(":")
        id = int(id)
        endTime = int(endTime)

        if action == "start":
            stack.append(log)
            lastTimeStack.append(0)
        else:
            startTime = int(stack.pop().split(":")[2])
            lastFuncTime = lastTimeStack.pop()
            
            out[id] += endTime - startTime + 1 - lastFuncTime
            if lastTimeStack:
                lastTimeStack[-1] += endTime - startTime + 1
    return out
                
assert [3,4] == exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])