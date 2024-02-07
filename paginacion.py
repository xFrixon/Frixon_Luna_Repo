import random

class Pagina:
    def __init__(self, id_pagina, proceso=None):
        self.id_pagina = id_pagina
        self.proceso = proceso


class Proceso:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano


class MemoriaFisica:
    def __init__(self, tamano_total, tamano_pagina):
        self.tamano_total = tamano_total
        self.tamano_pagina = tamano_pagina
        self.num_paginas = tamano_total // tamano_pagina
        self.paginas = [Pagina(i) for i in range(self.num_paginas)]

    def asignar_proceso(self, proceso):
        tamano_restante = proceso.tamano
        paginas_disponibles = [pagina for pagina in self.paginas if pagina.proceso is None]
        random.shuffle(paginas_disponibles)
        for pagina in paginas_disponibles:
            if tamano_restante <= 0:
                break
            if tamano_restante >= self.tamano_pagina:
                pagina.proceso = proceso
                tamano_restante -= self.tamano_pagina
            else:
                pagina.proceso = proceso
                break

    def memoria_libre(self):
        return sum(1 for pagina in self.paginas if pagina.proceso is None) * self.tamano_pagina

    def imprimir_memoria(self):
        print(f"Tamaño total de la memoria: {self.tamano_total} KB")
        for i, pagina in enumerate(self.paginas):
            print(f"Página {i}: ", end="")
            if pagina.proceso is None:
                print("Libre")
            else:
                print(f"Proceso: {pagina.proceso.nombre} ({pagina.proceso.tamano} KB)")
        print(f"Memoria libre: {self.memoria_libre()} KB")

# Crear la memoria física
memoria = MemoriaFisica(tamano_total=20, tamano_pagina=4)

# Crear procesos
print("Creando procesos...")
jugar = Proceso(nombre="Jugar", tamano=11)
print("Proceso 'Jugar' creado (tamaño: 11 KB)")
escuchar_musica = Proceso(nombre="Escuchar música", tamano=4)
print("Proceso 'Escuchar música' creado (tamaño: 4 KB)")

# Asignar los procesos a la memoria
memoria.asignar_proceso(jugar)
memoria.asignar_proceso(escuchar_musica)

# Imprimir el estado de la memoria
print("\nEstado de la memoria después de asignar procesos:")
memoria.imprimir_memoria()
