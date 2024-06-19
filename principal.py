#Archivo principal del Proyecto Final
# Primera version
class Empleado():
    def __init__(self):
        def _init_(self, nom, apell, edad, sal, dni, fecha_vin):
            self.nombre = nom
            self.apellido = apell
            self.edad = edad
            self.salario = sal
            self.dni = dni
            self.fecha_vinculacion = fecha_vin
        
        def obtener_nombre_completo(self):
            return f"{self.nombre} {self.apellido}"
    
class Jefe(Empleado):
    def __init__(self, nom, apell, edad, sal, dni, fecha_vin, nEmple):
        super().__init__(self, nom, apell, edad, sal, dni, fecha_vin)
        self.numEmple = nEmple
        
class Area:
    def _init_(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)    
        
    
        
        
        
