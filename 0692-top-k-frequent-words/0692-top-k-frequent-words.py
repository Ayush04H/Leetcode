class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        # Sort first by frequency (descending), then by lexicographical order (ascending)
        most_freq = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        # Extract the top k words
        res = [item[0] for item in most_freq[:k]]
        return res
        