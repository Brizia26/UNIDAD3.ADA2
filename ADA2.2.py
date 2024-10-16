class Cola:
    def __init__(self):
        self.cola = []

    def encolar(self, elemento):
        self.cola.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)
        else:
            return None

    def esta_vacia(self):
        return len(self.cola) == 0

class SistemaDeColas:
    def __init__(self):
       
        self.servicios = {}
       
        self.ultimo_numero = {}

    def llegada_cliente(self, servicio):
        if servicio not in self.servicios:
            
            self.servicios[servicio] = Cola()
            self.ultimo_numero[servicio] = 0

        self.ultimo_numero[servicio] += 1
        numero_atencion = self.ultimo_numero[servicio]

        self.servicios[servicio].encolar(numero_atencion)
        print(f"Cliente asignado al servicio {servicio} con número {numero_atencion}.")

    def atender_cliente(self, servicio):
        if servicio in self.servicios:
            numero_atencion = self.servicios[servicio].desencolar()
            if numero_atencion is not None:
                print(f"Atendiendo cliente del servicio {servicio} con número {numero_atencion}.")
            else:
                print(f"No hay clientes en espera para el servicio {servicio}.")
        else:
            print(f"El servicio {servicio} no existe.")

sistema = SistemaDeColas()

while True:
    entrada = input("Ingrese C o A seguido del número de servicio: ")
    if entrada[0].upper() == "C":
        servicio = int(entrada[1:])
        sistema.llegada_cliente(servicio)
    elif entrada[0].upper() == "A":
        servicio = int(entrada[1:])
        sistema.atender_cliente(servicio)
    else:
        print("Entrada no válida. Use 'C' para cliente o 'A' para atención.")
