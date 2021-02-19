class Birds:
    def __init__(self):
        self.members = ["Sparrow", "Robin", "Duck"]

    def printMembers(self):
        print("Printing members of the Bird class")
        for member in self.members:
            print(f"\t{member}")
