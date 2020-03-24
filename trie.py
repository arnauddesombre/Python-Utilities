ALPHABET = 26

class TrieNode:
    def __init__(self):
        self.children = [None] * ALPHABET
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        # declare variables for needed computations
        self.words = []

    def __charToIndex(self, char):
        return ord(char) - ord('a')

    def __indexToChar(self, index):
        return chr(index + ord('a'))

    def __searchNode(self, key):
        pCrawl = self.root
        for level in range(len(key)):
            index = self.__charToIndex(key[level])
            if not pCrawl.children[index]:
                return None
            pCrawl = pCrawl.children[index]
        return pCrawl

    def search(self, key):
        pCrawl = self.__searchNode(key)
        return pCrawl != None and pCrawl.isEndOfWord

    def insert(self, key):
        pCrawl = self.root
        for level in range(len(key)):
            index = self.__charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = TrieNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True

    def bfs(self, word='', pCrawl=0):
        # print all words in trie starting with word (using BFS)
        if pCrawl == 0:
            self.words = []
            if word == '':
                pCrawl = self.root
            else:
                pCrawl = self.__searchNode(word)
                if pCrawl == None:
                    self.words.append('n/a')
                    return
        for index, child in enumerate(pCrawl.children):
            if child != None:
                w = word + self.__indexToChar(index)
                if child.isEndOfWord:
                    self.words.append(w)
                self.bfs(w, child)

# driver function
def main():
    keys = ["the", "then", "there", "tie", "a", "an", "any", "and"]
    output = ["Not present in trie", "Present in trie"]
    t = Trie()
    for key in keys:
        t.insert(key)
    # search for different keys
    for word in ["the", "these", "their", "thaw"]:
        print("{} ---- {}".format(word, output[t.search(word)]))
    print('print all words in trie:')
    t.bfs()
    print(t.words)
    print('print all words starting with "th" in trie:')
    t.bfs('th')
    print(t.words)
    print('print all words starting with "b" in trie:')
    t.bfs('b')
    print(t.words)
    
if __name__ == '__main__':
    main()

