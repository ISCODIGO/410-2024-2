'''
Algoritmo:
1. Bucle para leer linea a linea
2. Dividir la linea en campos (por medio de la ,)
3. Registrar la cuenta
    3.1 Comparamos si la linea es la misma, agregar a una sublista
    3.2 Si es diferente registrar la nueva cuenta
4. Recorrer cada sublista para calcular las sumatorias
5. Obtener el promedio por alumno


Estructura de sublista:
[cuenta1, [uv, nota], [uv, nota], [uv, nota]]

[cuenta2, [uv, nota], [uv, nota], [uv, nota]]

Estructura de resultado:
[[cuenta, promedio], [cuenta2, promedio]]
'''
def resumir_contenido() -> list:
    """
    Lee el contenido del archivo y genera una estructura:
    ```
    [
        [cuenta1, [uv, nota], [uv, nota], [uv, nota]]
        [cuenta2, [uv, nota], [uv, nota], [uv, nota]]
    ]
    ```
    """
    lista = []
    sublista = []
    with open("notas.txt") as archivo:
        archivo.readline()  # leer el titulo para no procesarlo
        cuenta_anterior = None
        for linea in archivo:
            campos = linea.split(",")
            cuenta = campos[0]
            uv = int(campos[2])
            nota = int(campos[3])

            if cuenta == cuenta_anterior:
                # sigo agrupando
                sublista.append([uv, nota])
            else:
                # la linea no pertenece al alumno anterior y comienza de nuevo
                if sublista:
                    lista.append(sublista)
                sublista = [cuenta, [uv, nota]]
                cuenta_anterior = cuenta
        # queda un remanente
        if sublista:
            lista.append(sublista)
    return lista


def promedio(notas: list) -> list:
    """
    Solicita notas con la estructura:
    ```
    [
        [cuenta1, [uv, nota], [uv, nota], [uv, nota]]
        [cuenta2, [uv, nota], [uv, nota], [uv, nota]]
    ]
    ```

    Y lo trasforma en esta estructura
    `[[cuenta, promedio], [cuenta2, promedio]]`

    Donde promedio es:
    `promedio = Sum(uv * nota) / Sum(uv)`
    """
    lista = []
    for linea in notas:
        cuenta = linea[0]
        resto = linea[1:]  # [[uv, nota], [uv, nota], ...]

        sum_uv = 0
        for columna in resto:
            # columna = [uv, nota]
            sum_uv += columna[0]
            # sum_uv_por_nota = columna[0] * columna[1]

        # sum_uv = sum([columna[0] for columna in resto])
        sum_uv_por_nota = sum([columna[0] * columna[1] for columna in resto])
        promedio = round(sum_uv_por_nota / sum_uv, 0)
        lista.append([cuenta, promedio])
    return lista




# Test
lst = resumir_contenido()
esperado = [
    ["1234", [5, 90], [4, 78]],
    ["3456", [5, 67], [4, 80]],
]
assert lst == esperado, f"Esperado: {esperado}, obtenido: {lst}"

lst2 = promedio(lst)
esperado2 = [["1234", 85], ["3456", 73]]
assert lst2 == esperado2, f"Esperado: {esperado2}, obtenido: {lst2}"

print(lst2)
