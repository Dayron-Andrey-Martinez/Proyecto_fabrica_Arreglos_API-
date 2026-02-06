class Api_BD_maquinas:
    def __init__(self):
        self.Api_maquina = [
            [ "codigo","nombre maquina","Modelo Maquina","Estado maquina"],
            ["cod 1234", "brazo mecanico","x200","apagada"],
            ["cod 2352","cinta transportadora","zx400","requiere mantenimiento"],
            ["cod 5648", "Monobrazo","jk100","Encendida"]
        ]
        
    def imprimir_info(self):
        for i in range(len(self.Api_maquina)):
            print(self.Api_maquina[i])
    
    def buscar_info(self):
        return self.Api_maquina[2][2]        
    
    def agregar_maquina(self,nueva_maquina):
        self.Api_maquina.append(nueva_maquina)

   
    def guardar_varias_maquinas(self,nueva_lista):
        self.Api_maquina.extend(nueva_lista)


    def eliminar_ele_maquina(self,data_i):
        self.Api_maquina.remove(data_i)

    def cambiar_ele_maquina(sefl):
        sefl.Api_maquina.pop()

 
