'''
Created on Feb 26, 2016

@author: Cigarent
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1=nums1[:m]+nums2[:n]
        print(nums1)
        nums1.sort()
        print (nums1)
        
    merge(object,[0],0,[1],1)