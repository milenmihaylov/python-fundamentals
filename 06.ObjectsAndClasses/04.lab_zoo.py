class Zoo:
    __animals = 0  # total count of animals in the zoo

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        Zoo.__animals += 1
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species: str):
        if species == "mammal":
            return f"Mammals in {zoo.zoo_name}: {', '.join(self.mammals)} \nTotal animals: {self.__animals}"
        elif species == "fish":
            return f"Fish in {zoo.zoo_name}: {', '.join(self.fishes)} \nTotal animals: {self.__animals}"
        elif species == "bird":
            return f"Birds in {zoo.zoo_name}: {', '.join(self.birds)} \nTotal animals: {self.__animals}"


zoo = Zoo(input())
n = int(input())
for i in range(n):
    animal_species, animal_name = input().split()
    zoo.add_animal(animal_species, animal_name)

print(zoo.get_info(input()))
