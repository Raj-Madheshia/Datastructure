# Minimum window problem.
# Ignore repetion of words in Required String
class Solution:
    def __init__(self):
        self.left = 0
        self.right = 0 # not include last character
        self.unique = {}
        self.string = ""
        self.final = ""
        
    def checkAllCharacter(self, left, right):
        for i in self.unique:
            if i not in self.string[left : right]:
                return False
        return True
        
    def minWindow(self, s: str, t: str) -> str:
        self.unique = set(t)
        self.string = s
        strL = len(s)
        self.right = len(self.unique)  # count of unique character
        isPresent = self.checkAllCharacter(self.left, self.right)
        if isPresent:
            self.final = self.string[self.left: self.right]
            return self.final
    
        for i in range(strL - self.right):
            self.right+=1
            if self.checkAllCharacter(self.left, self.right):
                if self.final == "":
                    self.final = self.string[self.left:self.right]
                check = True
                while(check):
                    self.left+=1
                    check = self.checkAllCharacter(self.left, self.right)
                if len(self.final) > (self.right-self.left):
                    self.final = self.string[self.left -1 :self.right]
                
        return self.final
        

a = Solution()
print(a.minWindow("ADOBBANCECODE", "ABC"))
