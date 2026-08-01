
# Listas en Python

Una **lista** guarda varios valores en una variable y puede modificarse.

frutas = ["manzana", "pera", "naranja"]

## Acceder a elementos

Los índices empiezan en `0`.

frutas[0]   # primer elemento  
frutas[-1]  # último elemento

## Modificar

frutas[1] = "kiwi"

## Agregar elementos

frutas.append("uva")            # agrega al final  
frutas.insert(1, "plátano")     # agrega en una posición  
frutas.extend(["kiwi", "uva"])  # agrega varios elementos

## Eliminar elementos

frutas.remove("pera")  # elimina por valor  
frutas.pop(1)          # elimina por posición  
frutas.pop()           # elimina el último

## Buscar y contar

frutas.index("pera")  # devuelve su posición  
"pera" in frutas      # True o False  
len(frutas)           # cantidad de elementos

## Extraer parte de una lista

numeros = [10, 20, 30, 40, 50]

numeros[1:4]  # [20, 30, 40]

**Importante:** el índice final no se incluye.

## Unir listas

lista_3 = lista_1 + lista_2

## Lo esencial

- Los índices comienzan en `0`.
- `-1` representa el último elemento.
- `append()` agrega al final.
- `insert()` agrega en una posición.
- `extend()` agrega varios elementos.
- `remove()` elimina por valor.
- `pop()` elimina por posición.
- `index()` devuelve la posición.
- `in` comprueba si existe.
- `len()` cuenta los elementos.
- `[inicio:fin]` extrae una parte.
- `+` une listas.
```

