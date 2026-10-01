class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        ta = [0] * 128
        for ch in t:
            ta[ord(ch)] += 1
        re = [0] * 128
        l = 0
        r = 0
        h = 0
        n = len(t)
        ans_len = float('inf')
        ans_s = 0
        while r < len(s):
            # Add s[r] to the window
            re[ord(s[r])] += 1
            # This character is still needed
            if re[ord(s[r])] <= ta[ord(s[r])]:
                h += 1
            # Window is valid
            while h == n:
                # Save smallest window
                if r - l + 1 < ans_len:
                    ans_len = r - l + 1
                    ans_s = l
                # Remove s[l]
                re[ord(s[l])] -= 1
                if re[ord(s[l])] < ta[ord(s[l])]:
                    h -= 1
                l += 1
            r += 1
        if ans_len == float('inf'):
            return ""
        return s[ans_s:ans_s + ans_len]