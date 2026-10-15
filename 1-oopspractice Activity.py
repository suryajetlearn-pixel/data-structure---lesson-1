class fruit:
    def __init__(self,color,taste,shape,preference):
        self.color = color
        self.taste = taste
        self.shape = shape


    def getshape(self):
        return self.shape

    def getcolor(self):
        return self.color

apple = fruit("red","sour","round",1)
print(apple.getshape())
print(apple.getcolor())