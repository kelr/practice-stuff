# Create freq map of words. Sort the dict alphabetically ascending keywords and descending freq values.
# O(NlgN), sort takes O(NlgN) time.
# O(N) space. Freq map takes N elements and sorted map takes N elements as well.
def topKFrequent(words, k):
    freq = {}
    for word in words:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1

    # Sort by alphabetically ascending keywords and descending freq values
    sortedFreq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:k]
    return [pair[0] for pair in sortedFreq]

# Create a freq map of words. Create a heap out of the words where each element is
# sorted ascending by word and descending by frequency.
# Pop off the heap k times into an ouput list.
# O(N + KlgN) time, building the map takes N time, heapify takes N time. A pop off the heap is lg N and it is done K times for KlgN.
# O(N) space, freq map takes N elements, heap takes N elements.
def topKFrequentHeap(words, k):
    freq = {}
    for word in words:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
            
    # Sort ascending lexographically and descending by frequency.
    heap = [(-freq, word) for word, freq in freq.items()]
    heapq.heapify(heap)
    
    # Pop off the heap k times, save the word in output list.
    return [heapq.heappop(heap)[1] for _ in range(k)]