import unittest
import sys,os
sys.path.append(os.getcwd())
from funciones.app import OperacionesNumeros

class test_clase(unittest.TestCase):
    
    # def test_suma(self):
    #     valor_a=2
    #     valor_b=2
    #     ope=OperacionesNumeros(a=valor_a,b=valor_b)
    #     resultado_suma=ope.suma()
    #     self.assertEqual(resultado_suma,valor_a+valor_b)
        
    def test_multiplicacion(self):
        valor_a=2
        valor_b=2
        ope=OperacionesNumeros(a=valor_a,b=valor_b)
        resultado_multiplicacion=ope.multiplicacion()
        self.assertEqual(resultado_multiplicacion,valor_a*valor_b)
        
    def test_resta(self):
        valor_a=2
        valor_b=2
        ope=OperacionesNumeros(a=valor_a,b=valor_b)
        resultado_resta=ope.resta()
        self.assertEqual(resultado_resta,valor_a-valor_b)
        
    def test_divicion(self):
        valor_a=2
        valor_b_no_cero=2
        valor_b_cero=0
        ope_no_cero=OperacionesNumeros(a=valor_a,b=valor_b_no_cero)
        resultado_divicion_no_cero=ope_no_cero.divicion()
        self.assertEqual(resultado_divicion_no_cero,valor_a/valor_b_no_cero)
        self.assertRaises(ZeroDivisionError,OperacionesNumeros(a=valor_a,b=valor_b_cero).divicion)
        