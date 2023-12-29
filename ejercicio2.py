class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def obtener_nombre(self):
        """Obtiene el nombre del empleado."""
        return self.nombre

    def obtener_salario(self):
        """Obtiene el salario del empleado."""
        return self.salario

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        """Agrega un empleado al departamento."""
        self.empleados.append(empleado)

    def obtener_salario_total(self):
        """Calcula el salario total de todos los empleados en el departamento."""
        return sum(empleado.obtener_salario() for empleado in self.empleados)

def main():
    # Crear empleados
    empleado1 = Empleado("Alice", 50000)
    empleado2 = Empleado("Bob", 60000)

    # Crear departamento y agregar empleados
    departamento = Departamento("Ventas")
    departamento.agregar_empleado(empleado1)
    departamento.agregar_empleado(empleado2)

    # Mostrar información del departamento
    print(f"Departamento: {departamento.nombre}")
    for empleado in departamento.empleados:
        print(f"Empleado: {empleado.obtener_nombre()}, Salario: {empleado.obtener_salario()}")

    # Calcular salario total del departamento
    salario_total = departamento.obtener_salario_total()
    print(f"Salario total del departamento: {salario_total}")

if __name__ == "__main__":
    main()
