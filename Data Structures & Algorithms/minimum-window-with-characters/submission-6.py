class Solution:
    def minWindow(self, s: str, t: str) -> str:
        stringInT = Counter(t)
        stringInS = defaultdict(int)
        l = 0
        minLen = 100001
        ans = ""
        required = len(stringInT)
        formed = 0
        for r in range(len(s)):
            char = s[r]
            stringInS[char] += 1
            if char in stringInT and stringInS[char] == stringInT[char]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    ans = s[l : r+1]
                
                leftChar = s[l]
                stringInS[leftChar] -= 1
                if leftChar in stringInT and stringInS[leftChar] < stringInT[leftChar]:
                    formed -= 1
                l += 1
            
        return ans