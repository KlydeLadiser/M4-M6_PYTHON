print ("BABIERA | ATIGA | PONCE | TENOLLAR")
print("School: FEU-TECH")
print("Machine Problem number - 2 ")

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14  

    def compute_area(self):
        return self.pi * (self.radius ** 2)

    def compute_perimeter(self):
        return 2 * self.pi * self.radius

def main():
    user_input = input("Enter radius:")
    
    try:
        radius_val = float(user_input)
        
        if radius_val < 0:
            print("You use enter positive number")
        elif radius_val % 1 != 0:
            print("You use input whole number value:")
        else:
           
            circle = Circle(int(radius_val))
            
            
            print(f"The answer is {circle.compute_area()}")
            print(f"Here is the Answer: {circle.compute_perimeter()}")
            
    except ValueError:
        print("Please enter a valid numeric value.")

if __name__ == "__main__":
    main()