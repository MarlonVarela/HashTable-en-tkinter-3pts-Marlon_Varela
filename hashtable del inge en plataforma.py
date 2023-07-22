class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        # Función de hash simple: suma de los caracteres ASCII de la clave
        return sum(ord(char) for char in key) % self.size

    def add(self, key, value):
        # Obtener el índice de la lista donde se almacenará el par clave-valor
        index = self._hash_function(key)

        # Si la posición está vacía, crear un nuevo bucket (lista) en esa posición
        if self.table[index] is None:
            self.table[index] = []

        # Agregar el par clave-valor al bucket
        self.table[index].append((key, value))

    def get(self, key):
        # Obtener el índice de la lista donde se encuentra el par clave-valor
        index = self._hash_function(key)

        # Si la posición está vacía, la clave no existe en la tabla
        if self.table[index] is None:
            raise KeyError("Clave no encontrada")

        # Buscar la clave en el bucket correspondiente y devolver su valor
        for k, v in self.table[index]:
            if k == key:
                return v

        # Si la clave no se encuentra en el bucket
        raise KeyError("Clave no encontrada")

    def remove(self, key):
        # Obtener el índice de la lista donde se encuentra el par clave-valor
        index = self._hash_function(key)

        # Si la posición está vacía, la clave no existe en la tabla
        if self.table[index] is None:
            raise KeyError("Clave no encontrada")

        # Buscar la clave en el bucket correspondiente y eliminarla
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

        # Si la clave no se encuentra en el bucket
        raise KeyError("Clave no encontrada")


# Ejemplo de uso:
hash_table = HashTable(10)

hash_table.add("nombre", "Juan")
hash_table.add("edad", 30)
hash_table.add("ciudad", "Madrid")

print(hash_table.get("nombre"))  # Salida: "Juan"
print(hash_table.get("edad"))    # Salida: 30

#hash_table.remove("ciudad")
print(hash_table.get("ciudad"))  # Salida: KeyError: 'Clave no encontrada'