class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        # print(l)
        l=l[::-1]
        # print(l)
        return ' '.join(l)