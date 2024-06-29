def paso_por_referencia(x: list):
    x[0] = 1000


def paso_por_valor(x: list):
    y = x.copy()
    y[0] = 2000


ls = [1, 2]
paso_por_referencia(ls)
print(ls)

paso_por_valor(ls)
print(ls)
