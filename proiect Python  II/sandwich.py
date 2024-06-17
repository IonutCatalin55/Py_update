from material_compozit import MaterialCompozit


class Sandwich(MaterialCompozit):

    def __init__(self, material_miez, material_invelis, lista_geometrie, incarcare):
        super().__init__("sandwich")
        self._dens_miez = material_miez['Dens']
        self._ec_miez = material_miez['Ec']
        self._gc_miez = material_miez['Gc']
        self._thau_miez = material_miez['Tc']
        self._cost_miez = material_miez['Cost']
        self._dens_invelis = material_invelis['Dens']
        self._ef_invelis = material_invelis['Ef']
        self._sigma_invelis = material_invelis['Sigf']
        self._cost_invelis = material_invelis['Cost']
        self._lungime = lista_geometrie[0]
        self._latime = lista_geometrie[1]
        self._tc = lista_geometrie[2]
        self._tf = lista_geometrie[3]
        self._forta = incarcare
        self._d_sandwich = self._tf + self._tc

    ###################### Calcul masa sandwich #####################
    def calcul_volum_invelis(self):
        return (self._lungime * self._latime * self._tf) / 10 ** 9

    def calcul_volum_miez(self):
        return (self._lungime * self._latime * self._tc) / 10 ** 9

    def calcul_masa(self):
        mass = 2 * (self.calcul_volum_invelis() * self._dens_invelis) + self.calcul_volum_miez() * self._dens_miez
        return mass.__round__(2)

    def calcul_deformatii(self):
        w_b = (2 * (self._forta * 10) * self._lungime ** 3) / (3 * self._ef_invelis * self._tf * self._d_sandwich ** 2* self._latime)
        w_s = ((self._forta * 10) * self._lungime ) / (((self._gc_miez * self._d_sandwich ** 2)/ self._tc) * self._latime)
        return w_b, w_s

    def calcul_rigiditate(self):
        k_total = self._forta * 10 / sum(self.calcul_deformatii())
        # k_total = (3 * self._ef_invelis * self._latime * (self._d_sandwich ** 3)) / (12 * self._lungime ** 3)
        return k_total.__round__(2)

    def calcul_cost(self):
        cost_total = (self._cost_miez * (self.calcul_volum_miez() * self._dens_miez) + 2 * (self._cost_invelis *
                                                                                            (self.calcul_volum_invelis() * self._dens_invelis)))
        return cost_total.__round__(2)

    def calcul_tensiuni(self):
        thau_c = self._forta / (self._d_sandwich * self._latime)
        sigma_f = self._forta * self._lungime / (self._tf * self._d_sandwich * self._latime)
        return thau_c.__round__(2), sigma_f.__round__(2)
