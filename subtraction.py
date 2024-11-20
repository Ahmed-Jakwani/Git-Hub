class Subtraction:
    def __init__(self, firstentry, secondentry):
        self.firstentry = firstentry
        self.secondentry = secondentry

    def Subtract(self):
        return (self.firstentry + self.secondentry)

try1 = Subtraction(10,6)
print(try1.Subtract())
