class heroine:
    def __init__(self):
        self.name="alia"
        self.age=32
    def act(self):
        print("alia acts well")
h1=heroine()
print(h1.name)
print(h1.age)
h1.act()
h1.numOfMovies=20
print(h1.numOfMovies)
h1.age=35
print(h1.age)
h2=h1
h3=h2
print(h1.name)
print(h2.name)
print(h3.name)
del h1.numOfMovies
print(h1.numOfMovies)


