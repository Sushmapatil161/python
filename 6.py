class bike:
    def __init__(self):
        self.brand="TVS"
        self.color="green"
    def move(self):
        print("bike is moving")
        print(self)
        print(self.brand)
b1=bike()
print(b1.brand)
b1.move()
print(b1)