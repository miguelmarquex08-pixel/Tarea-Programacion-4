from abc import ABC, abstractmethod # importamos la libreria que nos permitira crear la clase abstracta 

# ==========================================
# ARCHIVO DE LOGS Y EXCEPCIONES PERSONALIZADAS
# ==========================================

def registrar_evento(mensaje, es_error=False):# Por medio de esta funcion guardaremos los eventos en texto plano 
    try:
        tipo = "ERROR" if es_error else "INFO" # este condicional nos permite guardar un evento discriminandolo entre error o informacion
        with open("log_errores.txt", "a", encoding="utf-8") as archivo: #por medio de la funcion open creamos el archivo llamado "log_errores" y lo administramos con with
            archivo.write(f"[{tipo}] {mensaje}\n") #este sera el texto a ingresar en el log, contiene el tipo y el mensaje recibidos desde cada llamada de la funcion
    except Exception as e: #capturamos las excepciones entregadas por el sistema en la variable "e"
        print("No se pudo escribir en el archivo de log:", e)


class ErrorSoftwareFJ(Exception): 
 # creando una clase heredada de la clase del sistema Exception damos la capacidad a ErrorSoftwareFJ de tomar atributos y metodos de su clase padre 
    pass

class DatoInvalidoError(ErrorSoftwareFJ):
# nuevamente, creando una clase nueva heredamos atributos y metodos de la anterior clase llamada ErrorSoftwareFJ, esto para gestionar los posibles errores que se van a presentar durante la ejecucion en un escenario especifico, un tipo de dato erroneo por ejemplo
    pass

class ServicioNoDisponibleError(ErrorSoftwareFJ):
    pass

class ReservaFallidaError(ErrorSoftwareFJ):
    pass


# ==========================================
# CLASE ABSTRACTA GENERAL (ENTIDAD BASE)
# ==========================================

class Servicio(ABC): #Esta sera la clase abstracta que nos permitira tener una plantilla aplicable a cada uno de los servicios ofrecidos por la empresa
    
    @abstractmethod
    def obtener_info(self): # nos permite obtener la informacion del objeto creado a partir de la instancia de esta clase
        pass
