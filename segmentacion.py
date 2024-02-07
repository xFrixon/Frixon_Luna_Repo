class Segmento:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano

class Proceso:
    def __init__(self, nombre, segmentos):
        self.nombre = nombre
        self.segmentos = segmentos

class MemoriaFisica:
    def __init__(self, tamano_total):
        self.tamano_total = tamano_total
        self.segmentos = []

    def asignar_proceso(self, proceso):
        espacio_disponible = self.tamano_total - sum(segmento.tamano for segmento in self.segmentos)
        if espacio_disponible >= sum(segmento.tamano for segmento in proceso.segmentos):
            for segmento in proceso.segmentos:
                self.segmentos.append(segmento)
            print(f"Proceso {proceso.nombre} asignado a la memoria.")
        else:
            print(f"No hay suficiente espacio contiguo para asignar el proceso {proceso.nombre}.")

    def imprimir_memoria(self):
        print(f"Tamaño total de la memoria: {self.tamano_total} KB")
        for i, segmento in enumerate(self.segmentos):
            print(f"Segmento {i}: {segmento.nombre} - Tamaño: {segmento.tamano} KB")
        print(f"Memoria libre: {self.tamano_total - sum(segmento.tamano for segmento in self.segmentos)} KB")

# Crear la memoria física
memoria = MemoriaFisica(tamano_total=20)

# Definir los segmentos de los procesos
segmento_juego = Segmento(nombre="Juego", tamano=11)
segmento_musica = Segmento(nombre="Música", tamano=4)
segmento_libre = Segmento(nombre="Libre", tamano=3)  # Segmento libre de 3 KB

# Crear los procesos
jugar = Proceso(nombre="Jugar", segmentos=[segmento_juego])
escuchar_musica = Proceso(nombre="Escuchar música", segmentos=[segmento_musica])

# Asignar los procesos a la memoria
memoria.asignar_proceso(jugar)
memoria.asignar_proceso(escuchar_musica)

# Agregar segmento libre a la memoria
memoria.segmentos.append(segmento_libre)

# Imprimir el estado de la memoria
memoria.imprimir_memoria()

# Crear el proceso "leer"
proceso_leer = Proceso(nombre="Leer", segmentos=[Segmento(nombre="Leer", tamano=4)])
print(f"Proceso '{proceso_leer.nombre}' creado, pero no asignado a la memoria.")