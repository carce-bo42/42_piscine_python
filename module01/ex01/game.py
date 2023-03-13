class GotCharacter:

    def __init__(self) -> None:
        pass

    def __init__(self, first_name: str, is_alive = True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):

    """Class representing the Stark family"""

    def __init__(self) -> None:
        pass

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def die(self):
        self.is_alive = False
    
    def print_house_words(self):
        print(self.house_words)
    
class Lannister(GotCharacter):

    """Class representing the Lannister family"""

    def __init__(self) -> None:
        pass

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear Me Roar!"

    def die(self):
        self.is_alive = False

    def print_house_words(self):
        print(self.house_words)

arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print(arya.is_alive)
arya.die()
print(arya.is_alive)

jaime = Lannister("Jaime")
print(arya.__doc__)
print(jaime.__doc__)
