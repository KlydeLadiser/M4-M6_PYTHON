print("NAMES: BABIERA | ATIGA | PONCE | TENOLLAR")
print("SCHOOL: FEU-TECH ")
print("Machine Problem 4 - Problem 3 ")

class RomanNumeralConverter:
    def __init__(self):
        self.roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        self.int_to_roman_conversion = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

    def integer_to_roman(self, number):
        if number < 1 or number > 5000:
            raise ValueError("ERROR. Values Accepted only range from 1 to 5000.")

        result = ""

        for value, symbol in self.int_to_roman_conversion:
            while number >= value:
                result += symbol
                number -= value

        return result

    def roman_to_integer(self, roman):
        roman = roman.upper()

        for char in roman:
            if char not in self.roman_values:
                raise ValueError("Invalid Roman Numeral.")

        total = 0
        prev_value = 0

        for char in reversed(roman):
            current_value = self.roman_values[char]

            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            prev_value = current_value

        if total > 5000:
            raise ValueError("Roman numeral exceeds maximum value of 5000.")

        return total

class RomanNumeralApp:
    def __init__(self):
        self.converter = RomanNumeralConverter()

    def display_menu(self):
        print("\n================================================")
        print("|                THE CONVERTER                    |")
        print("================================================")
        print("| 1. Convert an Integer to a Roman Numeral     |")
        print("| 2. Convert a Roman Numeral to an Integer     |")
        print("| 3. Exit?                                      |")
        print("================================================")

    def run(self):
        while True:
            self.display_menu()

            try:
                choice = int(input("\nEnter your choice: "))

                if choice == 1:
                    try:
                        number = int(input("Enter Integer: "))

                        roman = self.converter.integer_to_roman(number)
                        print("Output in Roman Numerals is: ", roman)

                    except ValueError as e:
                        print("Error:", e)

                elif choice == 2:
                    try:
                        roman = input("Enter Roman Numeral: ")

                        integer_value = self.converter.roman_to_integer(roman)
                        print("Output in Integer is: ", integer_value)

                    except ValueError as e:
                        print("Error:", e)

                elif choice == 3:
                    print("Program terminated.")
                    break

                else:
                    print("Invalid choice. Accepted Values range from 1 to 3.")

            except ValueError:
                print("ERROR: Whole Numbers Only.")

# Main Program
app = RomanNumeralApp()
app.run()
