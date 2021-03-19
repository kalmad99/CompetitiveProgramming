class Node:
    def __init__(self):
        self.children = {}
        self.isEndofWord = False


class Trie:
    def __init__(self):
        self.trie = Node()

    def insert(self, word: str) -> None:
        def insertHelper(index, trie):
            if index == len(word):
                trie.isEndofWord = True
                return
            if word[index] not in trie.children:
                trie.children[word[index]] = Node()

            return insertHelper(index + 1, trie.children[word[index]])

        insertHelper(0, self.trie)

    def search(self, word: str) -> bool:
        def searchHelper(index, trie):
            if index == len(word):
                return trie.isEndofWord
            if word[index] in trie.children:
                return searchHelper(index + 1, trie.children[word[index]])
            return False

        return searchHelper(0, self.trie)

    def startsWith(self, prefix: str) -> bool:
        def searchHelper(index, trie):
            if index == len(prefix):
                return True
            if prefix[index] in trie.children:
                return searchHelper(index + 1, trie.children[prefix[index]])
            return False

        return searchHelper(0, self.trie)