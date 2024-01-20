class House():
    """Опис будинку"""
    def __init__(self, street, number):
        """Властивості будинку"""
        self.street = street
        self.number = number
        self.age = 0
        
    def build(self):
        """Будувати будинок"""
        print(" Будинок на вулиці " + self.street + " під номером " + str(self.number) + " побудований.")

    def age_of_house(self, year):
        """Вік будинку"""
        self.age += year


class ProspectHouse(House):
    """Будинки на проспекті"""
    def __init__(self, prospect, number):
        "super використовується для по'вязання батьківського класу"
        super().__init__(self,number)
        self.prospect = prospect
        
PrHouse = ProspectHouse("Червоної калини", 30)
print(PrHouse.prospect)