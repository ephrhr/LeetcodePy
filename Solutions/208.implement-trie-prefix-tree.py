#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['#'] = '#'

    def search(self, word: str) -> bool:
        trie = self.trie
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]
        if '#' in trie:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for c in prefix:
            if c not in trie:
                return False
            trie = trie[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

