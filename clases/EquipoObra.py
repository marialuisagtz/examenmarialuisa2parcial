class EquipoObra:
    def __init__(self,nombre, identificador, consumoCombustible):
        self.nombre= nombre
        self.identificador= identificador
        self.consumoCombustible= consumoCombustible
        
    def iniciar(self):
        self.estado= "operativo"
        
    def detener(self):
        self.estado= "detenido"
        
    def mostrarInformacion(self):
        print("nombre", self.nombre)
        print("identificador", self.identificador)
        print("Consumo del combustible", self.consumoCombustible)
        print("Operativo", self.estado)
        print("detenido", self.estado)
        
    
        