class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        # Sort characters by frequency (descending) and then lexicographically
        sorted_chars = sorted(count.items(), key=lambda x: -x[1])
        # Build the result string
        result = ''.join([char * freq for char, freq in sorted_chars])
        return result

        