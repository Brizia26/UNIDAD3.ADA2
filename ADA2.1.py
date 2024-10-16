class Cola:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("La cola está vacía")

def sumar_colas(cola1, cola2):
    resultado = Cola()
    resultados_lista = []

    while not cola1.is_empty() and not cola2.is_empty():
        num1 = cola1.dequeue()
        num2 = cola2.dequeue()
        suma = num1 + num2
        resultado.enqueue(suma)
        resultados_lista.append((num1, num2, suma))

    return resultado, resultados_lista

cola1 = Cola()
cola2 = Cola()

n = int(input("Ingrese el número de elementos para la primera cola: "))
for i in range(n):
    numero = int(input(f"Ingrese el elemento {i+1} para la primera cola: "))
    cola1.enqueue(numero)

m = int(input("Ingrese el número de elementos para la segunda cola: "))
for i in range(m):
    numero = int(input(f"Ingrese el elemento {i+1} para la segunda cola: "))
    cola2.enqueue(numero)

resultado, resultados_lista = sumar_colas(cola1, cola2)

#TABLA
print(f"\n{'Cola 1':<10} {'Cola 2':<10} {'Cola Resultado':<15}")
print("-" * 35)
for num1, num2, suma in resultados_lista:
    print(f"{num1:<10} {num2:<10} {suma:<15}")