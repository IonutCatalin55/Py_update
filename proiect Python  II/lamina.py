import math


class Lamina:
    def __init__(self, unghi_lamina):
        self._unghi_lamina = unghi_lamina
        # [e_paralel, niu_perp, e_perp, niu_paralel, g_sharp]

    def compliante_lamina(self, lista_elast):
        e_paralel = lista_elast[0]
        niu_perp = lista_elast[1]
        e_perp = lista_elast[2]
        g_sharp = lista_elast[4]

        c11 = ((math.cos(self._unghi_lamina) ** 4) / e_paralel + (math.sin(self._unghi_lamina) ** 4) /
               e_perp + 1 / 4 * ((1 / g_sharp) - (2 * niu_perp / e_paralel)) *
               (2 * math.sin(self._unghi_lamina) * math.cos(self._unghi_lamina)) ** 2)
        c22 = ((math.sin(self._unghi_lamina) ** 4) / e_paralel + (math.cos(self._unghi_lamina) ** 4) /
               e_perp + 1 / 4 * ((1 / g_sharp) - (2 * niu_perp / e_paralel)) *
               (2 * math.sin(self._unghi_lamina) * math.cos(self._unghi_lamina)) ** 2)
        c33 = (((1 - (2 * math.sin(self._unghi_lamina)) ** 2) ** 2) / g_sharp + ((1 / e_paralel) + (1 / e_perp) +
                                                                                 (2 * niu_perp / e_paralel)) *
               (2 * math.sin(self._unghi_lamina) * math.cos(self._unghi_lamina)) ** 2)
        c12 = 1 / 4 * (1 / e_paralel + 1 / e_perp - 1 / g_sharp) * (
                2 * math.sin(self._unghi_lamina) * math.cos(self._unghi_lamina)) ** 2 - (
                      niu_perp / e_paralel) * (
                      math.sin(self._unghi_lamina) ** 4 + math.cos(self._unghi_lamina) ** 4)
        c13 = ((2 / e_paralel + (2 * niu_perp / e_paralel) - 1 / g_sharp) * (math.sin(self._unghi_lamina) ** 3) *
               math.cos(self._unghi_lamina) - (2 / e_paralel + (2 * niu_perp) / e_paralel - 1 / g_sharp) *
               (math.cos(self._unghi_lamina) ** 3) * math.sin(self._unghi_lamina))
        c23 = (2 / e_perp + (2 * niu_perp) / e_paralel - 1 / g_sharp) * (math.cos(self._unghi_lamina) ** 3) * math.sin(
            self._unghi_lamina) - (2 / e_paralel + (2 * niu_perp) / e_paralel - 1 / g_sharp) * (
                      math.sin(self._unghi_lamina) ** 3) * math.cos(self._unghi_lamina)
        return [c11, c22, c33, c12, c13, c23]

    def lunecari_lamina(self, lista_alungiri_stratificat):
        epsilon_paralel = math.cos(self._unghi_lamina) ** 2 * lista_alungiri_stratificat[0] + math.sin(
            self._unghi_lamina) ** 2 * lista_alungiri_stratificat[1] + math.sin(self._unghi_lamina) * math.cos(
            self._unghi_lamina) * lista_alungiri_stratificat[2]
        epsilon_perp = math.sin(self._unghi_lamina) ** 2 * lista_alungiri_stratificat[0] + math.cos(
            self._unghi_lamina) ** 2 * lista_alungiri_stratificat[1] - math.cos(self._unghi_lamina) * math.sin(
            self._unghi_lamina) * lista_alungiri_stratificat[2]
        gamma_sharp = (-2 * math.sin(self._unghi_lamina) * math.cos(self._unghi_lamina) * lista_alungiri_stratificat[
            0] + 2 * math.sin(self._unghi_lamina) * math.cos(self._unghi_lamina) * lista_alungiri_stratificat[1] + (
                               math.cos(self._unghi_lamina) ** 2 - math.sin(self._unghi_lamina) ** 2) *
                       lista_alungiri_stratificat[2])
        return [epsilon_paralel, epsilon_perp, gamma_sharp]

    # [e_paralel, niu_perp, e_perp, niu_paralel, g_sharp]
    def tensiuni_lamine(self, lista_marimi_elast, lista_lunecari_lamina):
        sigma_paralel = (lista_marimi_elast[0] / (1 - lista_marimi_elast[1] * lista_marimi_elast[3]) *
                         lista_lunecari_lamina[0] + ((lista_marimi_elast[1] * lista_marimi_elast[2]) /
                                                     (1 - lista_marimi_elast[1] * lista_marimi_elast[3])) *
                         lista_lunecari_lamina[1] + 0 * lista_lunecari_lamina[2])
        sigma_perp = (lista_marimi_elast[1] * lista_marimi_elast[2]) / (
                1 - lista_marimi_elast[1] * lista_marimi_elast[3]) * lista_lunecari_lamina[0] + (
                             lista_marimi_elast[2] / (1 - (lista_marimi_elast[1] * lista_marimi_elast[3]))) * \
                     lista_lunecari_lamina[1] + 0 * lista_lunecari_lamina[2]
        thau_perp = 0 * lista_lunecari_lamina[0] + 0 * lista_lunecari_lamina[1] + lista_marimi_elast[4] * \
                    lista_lunecari_lamina[2]
        return [sigma_paralel, sigma_perp, thau_perp]