class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        col1, row1, col2, row2 = s[0], s[1], s[3], s[4]
        result = []

        for col in range(ord(col1), ord(col2) + 1):
            for row in range(int(row1), int(row2) + 1):
                result.append(chr(col) + str(row))

        return result
        