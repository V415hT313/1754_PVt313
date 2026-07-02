class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = Counter(s1)
        window = Counter()
        
        for i in range(len(s1)):
            window[s2[i]] += 1

        if window == need:
            return True

        left = 0

        # Slide the window
        for right in range(len(s1), len(s2)):
            # add new character
            window[s2[right]] += 1

            # remove leftmost character
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

            if window == need:
                return True
        return False