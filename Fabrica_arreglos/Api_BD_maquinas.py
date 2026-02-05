class Api_BD_maquinas:
    def __init__(self):
        self.Api_maquina = [
            [ "codigo","nombre maquina","Modelo Maquina","Estado maquina"],
            ["cod 1834", "brazo mecanico","xrt2333","apagada"],
            ["cod 2952","cinta transportadora","M600","requiere mantenimiento"],
            ["cod 5948", "Monobrazo","AL100","Encendida"]
        ]
        
    def imprimir_info(self):
        for i in range(len(self.Api_maquina)):
            print(self.Api_maquina[i])
    
    def buscar_info(self):
        return self.Api_maquina[2][2]        