class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = defaultdict(int)
        l = 0
        s1len = len(s1)
        for r in range(len(s2)):
            window[s2[r]] += 1
            if r >= s1len:
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1

            if window == need:
                return True

        return False