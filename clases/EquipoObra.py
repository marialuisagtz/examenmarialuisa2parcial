class EquipoObra:
    def __init__(self,nombre, identificador, consumoCombustible):
        self.nombre= nombre
        self.identificador= identificador
        self.consumoCombustible= consumoCombustible
        
    def __str__(self):
         return self.nombre +" "+ self.identificador+ " " + str(self.consumoCombustible)+ " "+
        
    def activar(self):
        print("activando")
        
    def detener(self)
        print("deteniendo")
        
    def mostrarInformacion(self):
        print("mostrando informaciom")
        
    
        