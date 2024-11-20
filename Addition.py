class Addition:
    def __init__(self, firstentry, secondentry):
        self.firstentry = firstentry
        self.secondentry = secondentry

    def Add(self):
        return (self.firstentry + self.secondentry)

try1 = Addition(10,6)
print(try1.Add())
