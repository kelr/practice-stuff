from collections import deque
from threading import Lock, Thread
# 23:20
class Solution:
    def __init__(self):
        self.lock = Lock()
        self.queue = deque()
        self.history = {}
        self.target = ""
    
    # Generate a list of urls to visit from the current url. 
    # If a url has not been visited before and shares a hostname, add it to the queue.
    # Protect queue and history shared access.
    def get(self, baseUrl, htmlParser):
        searchUrls = htmlParser.getUrls(baseUrl)
        
        with self.lock:
            for url in searchUrls:
                if url.startswith(self.target) and url not in self.history:
                    self.queue.append(url)
                    self.history[url] = True
    
    def crawl(self, startUrl, htmlParser):
        self.queue.append(startUrl)
        self.history = { startUrl:True }
        self.target = "http://" + startUrl.split("/")[2]

        # For each url in the queue, spawn a thread to process it and wait until all the threads have finished.
        # If the queue is empty after a pass, there is nothing left to crawl.
        while self.queue:
            threads = [Thread(target=self.get, args=(url, htmlParser)) for url in self.queue]
            self.queue = []
                
            for t in threads:
                t.start()
            
            for t in threads:
                t.join()

        return self.history.keys()