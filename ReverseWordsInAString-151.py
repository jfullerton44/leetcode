class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        i=0
        while i < len(words):
            if words[i]=='':
                words.pop(i)
            else:
                i+=1
        return " ".join(words[::-1])