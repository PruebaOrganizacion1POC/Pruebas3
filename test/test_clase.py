import unittest
import sys,os
sys.path.append(os.getcwd())
from funciones.clase import OperacionesNumeros

class test_clase(unittest.TestCase):
    
    def test_suma(self):
        valor_a=2
        valor_b=2
        ope=OperacionesNumeros(a=valor_a,b=valor_b)
        resultado_suma=ope.suma()
        self.assertEqual(resultado_suma,valor_a+valor_b)
        
    def test_multiplicacion(self):
        valor_a=2
        valor_b=2
        ope=OperacionesNumeros(a=valor_a,b=valor_b)
        resultado_multiplicacion=ope.multiplicacion()
        self.assertEqual(resultado_multiplicacion,valor_a*valor_b)