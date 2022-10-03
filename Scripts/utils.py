from Scripts.memberships import Memberships
from Scripts.system import Data

class Utils:
    @staticmethod
    def fuzzification(data: Data) -> Data:
        distancia = data.obj_y - data.pos_y

        centrado = Memberships.triangle(distancia, -40, 0, 40)
        cerca_a = Memberships.trapezoid(distancia, 20, 80, 120, 180)
        normal_a = Memberships.trapezoid(distancia, 120, 160, 240, 280)
        lejos_a = Memberships.grade(distancia, 240, 300)

        cerca_b = Memberships.trapezoid(distancia, -180, -120, -80, -20)
        normal_b = Memberships.trapezoid(distancia, -280, -240, -160, -120)
        lejos_b = Memberships.grade_inverted(distancia, -300, -240)

        numerador = centrado * 9.8 + cerca_a * 4 + normal_a * 2 + lejos_a * 1 + cerca_b * 14 + normal_b * 15.5 + lejos_b * 18
        denominador = centrado + cerca_a + normal_a + lejos_a + cerca_b + normal_b + lejos_b
        data.ventilador = numerador / denominador

        return data

    @staticmethod
    def draw(data):
        pass
