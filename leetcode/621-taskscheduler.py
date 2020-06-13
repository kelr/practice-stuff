def leastInterval(self, tasks, n: int) -> int:
    # Count the frequency for each task
    taskList = [0] * 26
    for task in tasks:
        taskList[ord(task)-ord('A')] += 1
    
    # Find the task that occurs most frequently
    maxVal = 0
    for task in taskList:
        if task > maxVal:
            maxVal = task
    
    # Find how many tasks occur with the max freq
    numMax = 0
    for task in taskList:
        if task == maxVal:
            numMax += 1
    
    # An optimal schedule can be maxVal - 1 occurances of n+1 values, or the maxVal itself + n different values.
    # There will be numMax number of tasks remaining afterwards, so add them at the end.
    # If this schedule is actually shorter than the lengths of the tasks, at minimum we need the length of all tasks
    # to schedule them all, so the optimal schedule will just be the length of tasks.
    return max(len(tasks), (maxVal - 1) * (n + 1) + numMax)