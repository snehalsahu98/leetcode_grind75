class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sst = sorted(s)
        tst = sorted(t)

        if sst == tst:
            return True
        else: 
            return False

