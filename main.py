class Opcion:
    def __init__(self, operadores,valor1,valor2):
        self.operadores = operadores
        self.valor1 = valor1
        self.valor2 = valor2
        self.list_operadores = ['1','2','3','4']

    def suma(self):
        X = self.valor1 + self.valor2
        print(f'La Suma de {self.valor1} + {self.valor2} es igual {X}')
    
    def resta(self):
        X = self.valor1 - self.valor2
        print(f'La Resta de {self.valor1} - {self.valor2} es igual {X}')
    
    def Multiplicacion(self):
        X = self.valor1 * self.valor2
        print(f'La Multiplicacion de {self.valor1} X {self.valor2} es igual {X}')
    
    def run(self):
        if self.operadores in self.list_operadores:
            if self.operadores == '1':
                Opcion.suma(self)
  

            elif self.operadores == '2':
                Opcion.resta(self)

            elif self.operadores == '3':
                Opcion.Multiplicacion(self)



while True:
    operador = input('Elige 1:Sumar, 2:Restar, 3:Multiplicar, 4:Salir => ')
    if operador in ['1','2','3']:
        v1 = int(input('Eliga su primer Valor: '))
        v2 = int(input('Eliga su Segundo Valor: '))
        star = Opcion(operador,v1,v2)
        star.run()
        e = input('Quieres seguir, Si/No: ')
        e = e.capitalize()
        if e == 'No':
            print('Gracias Por utilizar Caculadora Gio')
            break

    else:
        print('acabas de Salir')
        break