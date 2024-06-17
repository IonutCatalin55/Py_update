from material_compozit import MaterialCompozit
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Float, Delete, delete
from sqlalchemy.orm import  sessionmaker ,declarative_base

Base  = declarative_base()


class MaterialCompozitStratificat(Base):
    lamina = None
    __tablename__ = "Material_Compozit_Stratificat"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _fi = Column("fi", Float)
    _nxx = Column("nxx", Float)
    _nyy = Column("nyy", Float)
    _nxy = Column("nxy", Float)
    _grosime_totala = Column("grosime_totala", Float)
    _e_f = Column("e_f", Float)
    _niu_f = Column("niu_f", Float)
    _g_f = Column("g_f", Float)
    _e_m = Column("e_m", Float)
    _niu_m = Column("niu_m", Float)
    _g_m = Column("g_m", Float)
    _description = Column("description", String)
    _name = Column("name", String)
    _lamina_number = Column("lamina_number", Integer)
    _lamina_orientation = Column("lamina_orientation", String)

    def __init__(self, lista):
        #super().__init__("laminat")
        self._fi = lista[0]
        self._nxx = lista[1]
        self._nyy = lista[2]
        self._nxy = lista[3]
        self._grosime_totala = lista[4]
        self._e_f = lista[5]
        self._niu_f = lista[6]
        self._g_f = lista[7]
        self._e_m = lista[8]
        self._niu_m = lista[9]
        self._g_m = lista[10]
        self._description = lista[11]
        self._name = lista[12]
        self._lamina_number = lista[13]
        self._lamina_orientation = lista[14]

        session.add(self)
        session.commit()
    def __repr__(self):
        return f"name= {self._name}, description{self._description},\n lamina numbers= {self._lamina_number} , orientation= {self._lamina_orientation}"

#    ------------- Ex1 - marimi fundamentale elastice

    def marimi_elast(self):
        e_paralel = self._e_f * self._fi + self._e_m * (1 - self._fi)
        niu_perp = self._fi * self._niu_f + (1 - self._fi) * self._niu_m
        e_perp = (self._e_m / (1 - self._niu_m ** 2)) * ((1 + 0.85 * self._fi ** 2) / (
                (1 - self._fi) ** 1.25 + (self._fi * self._e_m) / ((1 - self._niu_m ** 2) * self._e_f)))
        niu_paralel = niu_perp * (e_perp / e_paralel)
        g_sharp = self._g_m * (
                (1 + 0.6 * self._fi ** 0.5) / ((1 - self._fi) ** 1.25 + self._fi * (self._g_m / self._g_f)))
        return [e_paralel, niu_perp, e_perp, niu_paralel, g_sharp]

    def tensiuni_stratificat(self):
        sigma_xx = self._nxx / self._grosime_totala
        sigma_yy = self._nyy / self._grosime_totala
        thau_xy = self._nxy / self._grosime_totala
        return [sigma_xx, sigma_yy, thau_xy]

    def alungiri_stratificat(self, lista_compliante, lista_tensiuni):
        epsilon_xx = (lista_compliante[0] * lista_tensiuni[0] + lista_compliante[3] * lista_tensiuni[1] +
                      lista_compliante[4] * lista_tensiuni[2])
        epsilon_yy = (lista_compliante[3] * lista_tensiuni[0] + lista_compliante[1] * lista_tensiuni[1] +
                      lista_compliante[5] * lista_tensiuni[2])
        gamma_xy = (lista_compliante[4] * lista_tensiuni[0] + lista_compliante[5] * lista_tensiuni[1] +
                    lista_compliante[2] * lista_tensiuni[2])
        return epsilon_xx, epsilon_yy, gamma_xy
engine = create_engine("sqlite:///db23.db", echo= True, pool_pre_ping=True)
Base.metadata.create_all(bind= engine)

Session = sessionmaker(bind=engine)
session= Session()

