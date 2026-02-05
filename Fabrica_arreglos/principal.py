from Empleado_modelo import Empleado_modelo 
from base_datos import Api_BD
from Api_BD_maquinas import Api_BD_maquinas

# codigo principal 
obj_Api = Api_BD()
obj_Api_maquina = Api_BD_maquinas()
obj_Api_maquina.imprimir_info()
print(obj_Api_maquina.buscar_info())
obj_Empleado = Empleado_modelo("Jose","Martinez","109092","310-5839")
obj_Empleado2 = Empleado_modelo("Maria","perez","809008","320-83463")
obj_Empleado3 = Empleado_modelo("juan","maduro","1083729200","322-7579")
obj_Api.guardar_empleado(obj_Empleado)
obj_Api.guardar_empleado(obj_Empleado2)
obj_Api.guardar_empleado(obj_Empleado3)
obj_Api.imprimir_Api()
