'''
Created on Feb 26, 2016

Given a string, find the length of the longest substring without repeating
 characters. For example, the longest substring without repeating letters for 
 "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring 
 is "b", with the length of 1.

@author: Cigarent
'''
class Solution(object):
    "Method that beats 68%"
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0 
        curr = ""
        for j in range (0, len(s)):
            if s[j] in curr:
                if (len(curr)>maxLen):
                    maxLen=len(curr)
                curr = curr[curr.index(s[j])+1:]+s[j]
            elif (j==len(s)-1):
                curr+=s[j]
                if (len(curr)>maxLen):
                    maxLen=len(curr)
            else:
                curr+=s[j]
        return maxLen
    
    "others which gets 99%"
    def lengthOfLongestSubstring_better(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        if s_len <= 1:
            return s_len
    
        table = {}
        max_length = -1
        tmp_length = 0
        start = 0
    
        for inx, char in enumerate(s):
            if char in table:
                former_inx = table[char]
                table[char] = inx
    
                if former_inx < start:
                    tmp_length += 1
                else:
                    start = former_inx + 1
                    tmp_length = inx - start + 1
            else:
                table[char] = inx
                tmp_length += 1
    
            if tmp_length > max_length:
                max_length = tmp_length
    
        return max_length
    