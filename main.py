class Pokemon():
    def __init__(self,number, name,type,type2,total,HP,Attack,Defense,SpAtk,SpDef,Speed,Generation,Legendary):
        self.name = name
        self.type = type
        self.type2 = type2
        self.fullhp = int(HP)
        self.hp = int(HP)
    def __str__(self):
        return f"The pokemons name is {self.name} it is a {self.type} and {self.type2} pokemon"
    def __lt__(self, other):
        return self.number < other.weight
    def takeDamage(self, damage):
        self.hp -= damage
        return f"The attack did {damage} damage, your hp is now {self.hp}"
    def heal(self):
        self.hp = self.fullhp
        return f"Your hp is now back to {self.hp}"

def makeObject(list):
    list = (Pokemon(list[0], list[1], list[2], list[3], list[4], list[5], list[5], list[6], list[7], list[8],
                            list[9], list[10], list[11]))
    return list
def readFile():
    pokemonList= []
    with open('pokemon.csv', 'r') as text:
        list = []
        for line in text:
            if "#" not in line:
                list.append(line)
    for i in range(len(list)):
        list[i] = list[i].strip().split(",")
    for i in range(len(list)):
        pokemonList.append(makeObject(list[i]))
    return pokemonList
def search():
    list = readFile()
    print("Vill du söka med namn eller nummer? 1= nummer 2= namn")
    choice = int(input("Skriv in här"))
    if choice == 1:
        number = int(input("Vad för pokemon söker du efter"))
        print(list[number])
    if choice == 2:
        name = str(input("Vad för pokemon söker du efter"))
        for i in list:
            if i.name == name:
                print(i)

search()

