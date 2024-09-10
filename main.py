class Package:
    def __init__(self, width, height, length, mass):
        self.width = width
        self.height = height
        self.length = length
        self.mass = mass

    def sort(self):
        volume = self.width * self.height * self.length
        is_bulky = (volume >= 1000000 or 
                    self.width >= 150 or 
                    self.height >= 150 or 
                    self.length >= 150)
        is_heavy = (self.mass >= 20)

        if is_bulky and is_heavy:
            return "REJECTED"
        elif is_bulky or is_heavy:
            return "SPECIAL"
        else:
            return "STANDARD"

def main():
    p1 = Package(200, 100, 100, 19.5)
    p2 = Package(50, 50, 50, 25.0)
    p3 = Package(100, 100, 100, 15.0)
    p4 = Package(150, 150, 150, 30.0)

    print(p1.sort())  # SPECIAL
    print(p2.sort())  # SPECIAL
    print(p3.sort())  # STANDARD
    print(p4.sort())  # REJECTED

if __name__ == "__main__":
    main()
