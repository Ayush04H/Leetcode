class Solution:
    def toLowerCase(self, s: str) -> str:
        lower_case = ""
        for i in s:
            ascii_val = ord(i)
            if ascii_val >= 65 and ascii_val <= 90:
                lower_case += chr(ascii_val + 32)
            else:
                lower_case += i

        return lower_case

        