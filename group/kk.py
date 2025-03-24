class Multiplier:
    def multiply_integers(self, a, b):
        return a * b

    def multiply_textual(self, a, b):
        return a * b

if __name__ == "__main__":
    multiplier = Multiplier()
    print(multiplier.multiply_integers(5, 3))
    print(multiplier.multiply_textual("abs", 2))

