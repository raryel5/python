# 3304. Find the K-th Character in String Game I
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/?envType=problem-list-v2&envId=recursion
 
import time
 
class Solution(object):
    def kthCharacter(self, k, word:str='a'):
        if len(word) >= k:
            return word[k-1]
 
        for char in word:
            word += chr(
                (ord(char) - ord('a') + 1) % 26 + ord('a')
            )
 
        return self.kthCharacter(k, word)
    
k = 1000
 
start_time = time.time()
 
result = (Solution()).kthCharacter(k)
 
time_end = time.time() - start_time
 
print(f'k = {k} -> {result}')
print(f'\n\n--- Run time: {time_end :.3f} s ---')
 