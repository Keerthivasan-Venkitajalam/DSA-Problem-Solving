class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip() #removes the leading and trailing whitespaces
        if not s:
            return 0 #return 0 if the string is empty after trimming
        words=s.split() #spliting of strings into words
        return len(words[-1]) #return the length of the last word
