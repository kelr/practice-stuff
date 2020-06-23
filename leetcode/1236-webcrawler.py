#14:16

# Perform BFS starting from startUrl. Only add valid hostnames that have not been crawled to the queue.
# O(N) time, where N is the number of URLs that share a hostname with startUrl.
# O(N) space, queue is has at worst N-1 elements + history has N elements max.
def crawl(startUrl, htmlParser):
    queue = [startUrl]
    history = {}
    while queue:
        url = queue.pop(0)
        history[url] = True
        targetHostname = getHostname(url)
        validUrls = filter(lambda u: u.startswith(targetHostname), htmlParser.getUrls(url))
        for u in validUrls:
            if u not in history:
                queue.append(u)
                
    return history


def getHostname(url: str):
    return url.split("/")[2]

from collections import deque
# Speedup attempt, use deque, dont split the url, dont use filter, don't add the queue url to history
# unless it has confirmed that its not in there.
def crawl(startUrl, htmlParser):
    queue = deque()
    queue.append(startUrl)
    history = { url:True }
    target = "http://" + startUrl.split("/")[2]
    while queue:
        url = queue.popleft()
        for u in htmlParser.getUrls(url):
            if u.startswith(target) and u not in history:
                queue.append(u)
                history[u] = True
                
    return history.keys()
