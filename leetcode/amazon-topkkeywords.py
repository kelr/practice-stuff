import re

# Strip punctuation and normalize each review to lowercase. Check if the keyword appears in the review.
# Increment that keywords frequency per occurance. Sort the resultant dict by frequency and lexographically if frequencies are equal.
# O(R*W + WlgW) time, R is number of reviews, W is number of keywords. Sort takes O(WlgW) time.
# O(W) space, freq map has number of elements equal to the number of keywords + W elements for sorted frequencies since the sort is not inplace.
def topKFreqKeywords(reviews, keywords, k):
    keywordFreq = {}
    for review in reviews:
        # Convert to lowercase, replace all non lowercase chars, split into word list
        cleanReview = review.lower().replace('[^a-z]', '').split()
        for keyword in keywords:
            if keyword in cleanReview:
                if keyword not in keywordFreq:
                    keywordFreq[keyword] = 1
                else:
                    keywordFreq[keyword] += 1

    # Sort by alphabetically ascending keywords and descending freq values
    kSortedFreqs = sorted(keywordFreq.items(), key=lambda x: (-x[1], x[0]))[:k]
    return [key[0] for key in kSortedFreqs]


k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]
result = topKFreqKeywords(reviews, keywords, k)
print(result)
assert ["anacell", "betacellular"] == result


k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]
result = topKFreqKeywords(reviews, keywords, k)
print(result)
assert ["betacellular", "anacell"] == result