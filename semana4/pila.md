
Crear una pila a traves de una lista utilizando 3 funciones:

`def push(p: list, elemento: Any) -> True`

`def pop(p: list) -> Any`

`def top(p: list) -> Any`

```
p = [1, 2, 3] # cima sera el ultimo elemento
assert push(p, 4) is True
assert top(p) == 4
assert pop(p) == 4
assert pop(p) == 3
```