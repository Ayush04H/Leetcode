class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l = title.split()
        for i in range(len(l)):
            if len(l[i]) >= 3:
                l[i] = l[i].capitalize()
            else:
                l[i] = l[i].lower()  
    
        return ' '.join(l)