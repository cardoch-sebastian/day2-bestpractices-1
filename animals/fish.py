class Fish:
    def __init__(self):
        self.members = ["Cod", "Salmon", "Albacore", "Catfish"]

    def printMembers(self):
        print("Printing members of the Fish class")
        for member in self.members:
            print(f"\t{member}")
