class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes
        self.grado = len(coeficientes) - 1

    def __str__(self):
        salida = ""
        for i in range(self.grado, -1, -1):
            salida += str(self.coeficientes[i]) + "x^" + str(i) + " + "
        return salida[:-3]
    
    def __add__(self, otro):
        if self.grado < otro.grado:
            self.coeficientes += [0] * (otro.grado - self.grado)
            self.grado = otro.grado
        elif self.grado > otro.grado:
            otro.coeficientes += [0] * (self.grado - otro.grado)
            otro.grado = self.grado
        return Polinomio([self.coeficientes[i] + otro.coeficientes[i] for i in range(self.grado + 1)])
    
    def __sub__(self, otro):
        if self.grado < otro.grado:
            self.coeficientes += [0] * (otro.grado - self.grado)
            self.grado = otro.grado
        elif self.grado > otro.grado:
            otro.coeficientes += [0] * (self.grado - otro.grado)
            otro.grado = self.grado
        return Polinomio([self.coeficientes[i] - otro.coeficientes[i] for i in range(self.grado + 1)])
    
    def __mul__(self, otro):
        salida = [0] * (self.grado + otro.grado + 1)
        for i in range(self.grado + 1):
            for j in range(otro.grado + 1):
                salida[i + j] += self.coeficientes[i] * otro.coeficientes[j]
        return Polinomio(salida)
    
    def __eq__(self, otro):
        if self.grado != otro.grado:
            return False
        for i in range(self.grado + 1):
            if self.coeficientes[i] != otro.coeficientes[i]:
                return False
        return True
    
    def __ne__(self, otro):
        return not self == otro
    
    def __call__(self, x):
        salida = 0
        for i in range(self.grado + 1):
            salida += self.coeficientes[i] * x ** i
        return salida
    
    def derivada(self):
        salida = []
        for i in range(1, self.grado + 1):
            salida.append(self.coeficientes[i] * i)
        return Polinomio(salida)
    
    def integral(self, constante = 0):
        salida = [constante]
        for i in range(self.grado + 1):
            salida.append(self.coeficientes[i] / (i + 1))
        return Polinomio(salida)
    
    def __eliminar_coeficientes__(self, i):
        self.coeficientes.pop(i)
        self.grado -= 1
        return self
    
    def __coeficientes_repetidos__(self):
        for i in range(self.grado):
            if self.coeficientes[i] == self.coeficientes[i + 1]:
                return True
        return False
    
    def __getitem__(self, i):
        return self.coeficientes[i]
    
    def __setitem__(self, i, valor):
        self.coeficientes[i] = valor
    

if __name__ == "__main__":
    p1 = Polinomio([1, 2, 3])
    p2 = Polinomio([1, 2, 3, 4])
    print("El polinomio 1 es: ", p1)
    print("El polinomio 2 es: ", p2)
    print("La suma del polinomio 1 mas el polinomio 2 es: ", p1 + p2)
    print("La resta del polinomio 1 menos el polinomio 2 es: ", p1 - p2)
    print("El producto del polinomio 1 por el polinomio 2 es: ", p1 * p2)
    print("Polinomio 1 es igual al polinomio 2: ", p1 == p2)
    print("Polinomio 1 es distinto al polinomio 2: ", p1 != p2)
    print("Eliminar un coeficiente del Polinomio 1: ", p1.__eliminar_coeficientes__(1))
    print("Eliminar un coeficiente del Polinomio 2: ", p2.__eliminar_coeficientes__(1))
    print("Coeficientes repetidos del Polinomio 1: ", p1.__coeficientes_repetidos__())
    print("Coeficientes repetidos del Polinomio 2: ", p2.__coeficientes_repetidos__())
    print("La derivada del Polinomio 1 es: ", p1.derivada())
    print("La derivada del Polinomio 2 es: ", p2.derivada())
    print("La integral del Polinomio 1 es: ", p1.integral())
    print("La integral del Polinomio 2 es: ", p2.integral())
  