class Solution(object):
    def kthCharacter(self, k, word=['a']):
        if len(word) >= k:
            return word[k-1]
 
        for i in range(len(word)):
            char = word[i]
            word.append(chr(
                (ord(char) - ord('a') + 1) % 26 + ord('a')
            ))
 
        return self.kthCharacter(k, word)