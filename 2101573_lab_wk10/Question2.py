class Average:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method to calculate average
    def avg(self):
        return (x + y) // 2

# Main method
if __name__ == '__main__':
    # User to input x and y
    x = int(input("Enter value for x: "))
    y = int(input("Enter value for y: "))

    # Create Average object
    a = Average(x, y)

    # Call methods to calculate and return values
    print("Average of x and y = " + str(a.avg()))