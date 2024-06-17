from material_compozit import MaterialCompozit


class MaterialCompozitSandwich(MaterialCompozit):
    __invelis = None
    __miez = None

    def __init__(self, invelis, miez):
        super().__init__("sandwich")
        self.invelis = invelis
        self.miez = miez

    def get_rezistenta_la_tractiune(self):
        return (self.invelis.rezistenta_la_tractiune * self.invelis.grosime +
                self.miez.rezistenta_la_tractiune * self.miez.grosime) / (self.invelis.grosime + self.miez.grosime)

    def get_rezistenta_la_compresiune(self):
        return (self.invelis.rezistenta_la_compresiune * self.invelis.grosime +
                self.miez.rezistenta_la_compresiune * self.miez.grosime) / (self.invelis.grosime + self.miez.grosime)
