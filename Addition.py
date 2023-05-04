class Addition:
    def __init__(self, firstentry, secondentry):
        self.firstentry = firstentry
        self.secondentry = secondentry

    def Add(self):
        return (self.firstentry + self.secondentry)

o1 = Addition(5,6)
print(o1.Add())
