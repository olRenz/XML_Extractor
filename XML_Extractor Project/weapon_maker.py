import os



class weapon_maker:
    def __init__(self, weapon_data):
        self.weapon_data = weapon_data
        self.tester()

    def tester(self):
        print(self.weapon_data)