#Creacion de la clase abstracta

class Servicio:
        
    servicios = {
    "RESERVA": 5000,
    "ALQUILER": 25000,
    "ASESORIA": 15000
    }
    
    def __init__(self, nombre, tiempo):
        self.nombre = nombre.upper()
        self.precio = self.servicios[self.nombre]
        self.tiempo = int(tiempo)

    def precio_total(self):
        return self.precio * self.tiempo
        
        

def registro():
    
    while True:
        nombre = input("Ingresa el nombre del servicio: ")
        if not nombre.upper() in Servicio.servicios:
            print ("El servicio no existe, intenta de nuevo")
            continue
        tiempo = int(input("Ingresa el numero de horas que requieres el servicio: "))
        break
    
    servicio1 = Servicio(nombre,tiempo)

registro()
