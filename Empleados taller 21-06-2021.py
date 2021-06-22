#!Ejercicio 2
#empleados

from cargos import Cargo

class Empleado:
    def __init__(self,nom,ced,sue,cargos):
        self.codigo=self.generarCodigo()
        self.codigo=Empleado.secuencia
        self.nombre=nom
        self.cedula=ced
        self.sueldo=sue
        self.cargo=cargos(codigo,descripcion)
    
    def mostrar(self):
        print("codigo:{} nombre:{}cargo:{}-{}".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.descripcion))

    def generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuencia

cargo1=Cargo("Docente")
emp1=Empleado("Luis","0989166306",500,cargo1)
emp1.mostrar()

cargo2=Cargo("Analista")
emp2=Empleado("Ana","0989166306",500,cargo2)
emp2.mostrar()



