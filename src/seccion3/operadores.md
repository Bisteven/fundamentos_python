# fundamentos_python

## Ejercicio 1

**Expresión:** `5 + 3 * 2`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

Paso a paso:

1. Identificar las operaciones y su prioridad:
   - Suma (`+`)
   - Multiplicación (`*`)
   - La multiplicación tiene mayor prioridad que la suma.
2. Realizar la multiplicación primero: `3 * 2 = 6`
3. Realizar la suma: `5 + 6 = 11`

**Resultado:**

```python
11
```

---

## Ejercicio 2

**Expresión:** `8 / 2 + 4 * 3`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

Paso a paso:

1. Identificar las operaciones y su prioridad:
   - División (`/`) y Multiplicación (`*`) tienen igual prioridad (se resuelven de izquierda a derecha)
   - Suma (`+`) tiene menor prioridad
2. Realizar la división primero (izquierda a derecha): `8 / 2 = 4.0`
3. Realizar la multiplicación: `4 * 3 = 12`
4. Realizar la suma: `4.0 + 12 = 16.0`

**Resultado:**

```python
16.0
```

---

## Ejercicio 3

**Expresión:** `(7 + 3) * 2 - 5`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

Paso a paso:

1. Los paréntesis tienen la mayor prioridad, se resuelven primero: `7 + 3 = 10`
2. Multiplicación: `10 * 2 = 20`
3. Resta: `20 - 5 = 15`

**Resultado:**

```python
15
```

---

## Ejercicio 4

**Expresión:** `10 - 4 + 2 * 3`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

Paso a paso:

1. La multiplicación tiene mayor prioridad: `2 * 3 = 6`
2. Resta y suma tienen igual prioridad, se resuelven de izquierda a derecha:
   - `10 - 4 = 6`
   - `6 + 6 = 12`

**Resultado:**

```python
12
```

---

## Ejercicio 5

**Expresión:** `(10 / 2) * (3 + 2) - 4`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

Paso a paso:

1. Resolver los paréntesis primero (de izquierda a derecha):
   - `10 / 2 = 5.0`
   - `3 + 2 = 5`
2. Multiplicación: `5.0 * 5 = 25.0`
3. Resta: `25.0 - 4 = 21.0`

**Resultado:**

```python
21.0
```

---

## Ejercicio 6

**Expresión:** `2 + 3 * (4 - 1)`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

Paso a paso:

1. Paréntesis primero: `4 - 1 = 3`
2. Multiplicación: `3 * 3 = 9`
3. Suma: `2 + 9 = 11`

**Resultado:**

```python
11
```

---

## Ejercicio 7

**Expresión:** `5 * 2 ** 3`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

Paso a paso:

1. La potencia (`**`) tiene mayor prioridad que la multiplicación: `2 ** 3 = 8`
2. Multiplicación: `5 * 8 = 40`

**Resultado:**

```python
40
```

---

## Ejercicio 8

**Expresión:** `6 + 4 / 2 ** 2`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

Paso a paso:

1. La potencia tiene la mayor prioridad: `2 ** 2 = 4`
2. División: `4 / 4 = 1.0`
3. Suma: `6 + 1.0 = 7.0`

**Resultado:**

```python
7.0
```

---

## Ejercicio 9

**Expresión:** `10 % 3 + 2 * 5`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

Paso a paso:

1. Módulo (`%`) y multiplicación (`*`) tienen igual prioridad, se resuelven de izquierda a derecha:
   - `10 % 3 = 1` (el residuo de dividir 10 entre 3)
   - `2 * 5 = 10`
2. Suma: `1 + 10 = 11`

**Resultado:**

```python
11
```

---

## Ejercicio 10

**Expresión:** `(8 + 2) * 3 ** 2`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

Paso a paso:

1. Paréntesis primero: `8 + 2 = 10`
2. Potencia: `3 ** 2 = 9`
3. Multiplicación: `10 * 9 = 90`

**Resultado:**

```python
90
```

---

## Ejercicio 11

**Expresión:** `7 + 2 * (3 + 5) / 4`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

Paso a paso:

1. Paréntesis primero: `3 + 5 = 8`
2. Multiplicación y división tienen igual prioridad, de izquierda a derecha:
   - `2 * 8 = 16`
   - `16 / 4 = 4.0`
3. Suma: `7 + 4.0 = 11.0`

**Resultado:**

```python
11.0
```

---

## Ejercicio 12

**Expresión:** `2 ** 3 * 4 / 2`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

Paso a paso:

1. Potencia primero: `2 ** 3 = 8`
2. Multiplicación y división de izquierda a derecha:
   - `8 * 4 = 32`
   - `32 / 2 = 16.0`

**Resultado:**

```python
16.0
```

---

## Ejercicio 13

**Expresión:** `9 - 6 + 3 ** 2`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

Paso a paso:

1. Potencia primero: `3 ** 2 = 9`
2. Resta y suma tienen igual prioridad, de izquierda a derecha:
   - `9 - 6 = 3`
   - `3 + 9 = 12`

**Resultado:**

```python
12
```

---

## Ejercicio 14

**Expresión:** `(7 - 2) * 5 + 3 ** 2`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

Paso a paso:

1. Paréntesis primero: `7 - 2 = 5`
2. Potencia: `3 ** 2 = 9`
3. Multiplicación: `5 * 5 = 25`
4. Suma: `25 + 9 = 34`

**Resultado:**

```python
34
```

---

## Ejercicio 15

**Expresión:** `4 * 2 ** 3 / 8 + 1`

**Pregunta:** ¿Cuál es el resultado? ¿Por qué?

**Solución:**

```python
4 * 2 ** 3 / 8 + 1
```

Paso a paso:

1. Potencia primero: `2 ** 3 = 8`
2. Multiplicación y división de izquierda a derecha:
   - `4 * 8 = 32`
   - `32 / 8 = 4.0`
3. Suma: `4.0 + 1 = 5.0`

**Resultado:**

```python
5.0
```

---
