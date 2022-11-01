class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26


sol = Solution()
print(sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
