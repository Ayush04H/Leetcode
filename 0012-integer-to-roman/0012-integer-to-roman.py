class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman = ""
        i = 0
        
        # Loop through each value in the `val` list
        while num > 0:
            # Find how many times the current Roman numeral fits into `num`
            count = num // val[i]
            # Append the Roman numeral `count` times to the result
            roman += syms[i] * count
            # Subtract the corresponding value from `num`
            num -= val[i] * count
            i += 1
        
        return roman
        