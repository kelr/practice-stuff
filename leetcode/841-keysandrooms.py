# Create a queue of rooms to visit and a set of keys that we have.
# Pop a room from the queue and visit it. For each key in the room,
# add it to the queue if we don't already have the key.
# If we have the same number of keys than we do rooms, we can visit all of them.
# O(N) time, visits every openable room once.
# O(N) space, queue can be at most N-1 next rooms and the keySet can have at most N keys.
def canVisitAllRooms(rooms) -> bool:
    queue = deque()
    keySet = set()
    
    # Door 0 is always unlocked, so we can pretend we have the key
    keySet.add(0)
    queue.append(0)
    
    while queue:
        room = queue.popleft()
        
        for key in rooms[room]:
            # Add new keys to the queue so we can check those rooms
            if key not in keySet:
                queue.append(key)
            keySet.add(key)
            
    return len(keySet) == len(rooms)


# Recursive implementation. Maintain a keyset similar to the iterative answer.
# Recurse to enter a room if we have a new key for it.
# O(N) time, visits all rooms once.
# O(N) space, potentially N calls on the call stack and keySet can have at most N keys.
def canVisitAllRoomsRec(rooms) -> bool:
    keySet = set()
    enter(0, rooms, keySet)
    return len(keySet) == len(rooms)
        
def enter(roomNumber, rooms, keySet):
    keySet.add(roomNumber)
    
    keys = rooms[roomNumber]
    for key in keys:
        if key not in keySet:
            enter(key, rooms, keySet)