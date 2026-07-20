print("NAMES: BABIERA | ATIGA | PONCE | TENOLLAR")
print("SCHOOL: FEU-TECH ")
print("Machine Problem 5 - Problem 3 ")

class NumberProcessor:
    def __init__(self):
        self.numbers = [
            30, 7, 30, 2, 88, 44, 60, 40, 1, 53, 100, 72, 86,
            64, 40, 85, 3, 19, 63, 84, 17, 31, 95, 84, 99, 60,
            85, 74, 65, 38, 43, 80, 39, 70, 8, 21, 32, 68, 64,
            55, 88, 84, 49, 68, 70, 98, 21, 51, 3, 97
        ]

    def replace_values(self):
        for i in range(len(self.numbers)):
            if self.numbers[i] > 10:
                self.numbers[i] = 666

    def count_values(self):
        equal_666 = 0
        not_equal_666 = 0

        for num in self.numbers:
            if num == 666:
                equal_666 += 1
            else:
                not_equal_666 += 1

        return equal_666, not_equal_666

    def display_output(self):
        self.replace_values()

        print("OUTPUT is:: ", self.numbers)

        equal_666, not_equal_666 = self.count_values()

        print("Total equal values: ", equal_666)
        print("Total not equal values: ", not_equal_666)

processor = NumberProcessor()
processor.display_output()
