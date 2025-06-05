'''Class Calculation is found here and referenced in init'''

class Calculation:
    def __init__(self,c,d,operation):
        self.c = c
        self.d = d
        self.operation = operation 

    def result(self):
        return self.operation(self.c,self.d) #aka add(3,3)

if __name__ == "__main__":
    c = Calculation(3, 3, lambda x, y: x + y)
    print(c.result())  # Should print 6
