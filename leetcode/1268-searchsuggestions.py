# Build a prefix with each char in searchWord. Check every product for that prefix and consider the ones that startwith the prefix.
# Sort the potential prefixes and return the first 3 elements.
# O(PN^2) time, where P is the number of products and N is the length of the search word.
# Finding which product starts with a certain prefix is O(P*L) where L is the length of the prefix.
# 1 <= L <= N and increases by 1 each loop iteration, leading to each prefix find looking like P*1 + P*2 + ... + P*(N-1) + P*N = P*(N*N+1/2) = P*N^2
# Sort is O(PlgP) in the worst case
# O(N*M) space where N is the length of the search word and M is the average length of a product.
def suggestedProducts(products, searchWord):
    prefix = ""
    out = []
    for char in searchWord:
        prefix += char
        suggested = []
        for product in products:
            if product.startswith(prefix):
                suggested.append(product)
                
        suggested.sort()
        
        out.append(suggested[:3])
    return out

class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestion = []

# Create a trie with all the products that saves sorted suggestions per node.
# Traverse the trie with each character in searchWord and output the suggestions.
# O(P*M + N) time, where P is the number of products, M is the average length of the products and N is the length of searchWord.
# O(P*M + N*M) space, ~P*M + 1 number of nodes in the trie. Output array has N elements of at most 3 strings that are on average M characters.
def suggestedProductsTrie(products, searchWord):
    out = []
    root = TrieNode()

    for product in products:
        insertTrieNode(product, root)
    
    # Traverse the trie with chars in searchword and append suggestions along the way
    for char in searchWord:
        if root:
            root = root.children.get(char)
            
        if root:
            out.append(root.suggestion)
        else:
            out.append([])
    
    return out
        
        
def insertTrieNode(product, node):
    for char in product:
        # Create a new child TrieNode if it doesn't exist
        if char not in node.children:
            node.children[char] = TrieNode()
            
        # Go to the child and add a suggestion to it
        node = node.children[char]
        node.suggestion.append(product)
        
        # Ensure that the suggestion list is lexographically sorted and has at most 3 elems
        node.suggestion.sort()
        if len(node.suggestion) > 3:
            node.suggestion.pop()

# Sort the product array. Find the index that a prefix can fit into the sorted products array.
# Check the next 3 elements if they are valid suggestions and add them to the output.
# O(PlgP + NlgP + N^2) time where P is the length of products, N is the length of searchWord.
# O(N*M) space, where N is the length of searchWord and M is the average length of a product.
def suggestedProductsBinary(products, searchWord):
    out = []
    prefix = ""

    products.sort()

    for char in searchWord:
        currSuggestions = []
        prefix += char

        # Find the index that the prefix can be inserted into products
        insertIndex = binary_search(products, prefix) 

        for i in range(insertIndex, min(len(products), insertIndex + 3)):
            if products[i].startswith(prefix):
                currSuggestions.append(products[i])

        out.append(currSuggestions)
    return out

def binary_search(array, target):
    lo = 0
    hi = len(array)

    while lo < hi:
        mid = (lo + hi) // 2

        if array[mid] < target: 
            lo = mid + 1
        else: 
            hi = mid
    return lo