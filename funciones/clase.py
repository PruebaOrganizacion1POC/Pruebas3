class OperacionesNumeros:

    def __init__(self,a:float,b:float):
        self.a=a
        self.b=b
    
    def suma(self):
        return self.a+self.b
    
    def resta(self):
        return self.a-self.b
    
    def multiplicacion(self):
        return self.a*self.b

    def divicion(self):
        if self.b==0:
            raise ZeroDivisionError()


if __name__=="__main__":
    ope=OperacionesNumeros(a=1,b=3)
    print(ope.suma())
