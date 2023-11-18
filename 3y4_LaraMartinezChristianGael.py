# Examen Practico - Lara Martinez Christian Gael

def bubble_sort(list):
  # El bucle externo recorre la lista, comenzando en el primer elemento.
  for i in range(len(list) - 1):
    # El bucle interno compara los elementos adyacentes.
    for j in range(len(list) - i - 1):
      # Si el elemento actual es mayor que el siguiente, se intercambian.
      if list[j] > list[j + 1]:
        list[j], list[j + 1] = list[j + 1], list[j]
  return list


print(bubble_sort([95, 36, 42, 0, 32, 58, 73, 28, 43, 12, 50]))
