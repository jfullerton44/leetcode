class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        i=0
        for word in words:
            words[i] = word[::-1]
            i+=1
        return " ".join(words)