print("NAMES:  | BABIERA | PONCE | ATIGA | TENOLLAR") 
print("SCHOOL: FEU-TECH ") 
print("Machine Problem number - 1") 

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def area(self) -> int:
        return self.length * self.width

def main():
    l_str = input("\nEnter length: ")
    w_str = input("Enter width: ")

    try:
        l = int(l_str)
        w = int(w_str)
    except ValueError:
        print("\nInput the correct data format is not a Positive integer.")
        return

    if l <= 0 or w <= 0:
        print("\nThe number is not a positive integer.")
        return

    rect = Rectangle(l, w)
    print(f"\nThe Area of the Rectangle is: {rect.area()}")


if __name__ == "__main__":
    main()
