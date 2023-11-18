# Examen Practico - Lara Martinez Christian Gael

def quick_sort(list):
  # Si la lista tiene un solo elemento, ya está ordenada.
  if len(list) <= 1:
    return list

  # El pivote es el elemento central de la lista.
  pivot = list[len(list) // 2]

  # Los elementos menores que el pivote se almacenan en una lista.
  less = []

  # Los elementos mayores que el pivote se almacenan en otra lista.
  greater = []

  # Se recorre la lista y se almacenan los elementos en las listas correspondientes.
  for i in range(len(list)):
    if list[i] < pivot:
      less.append(list[i])
    elif list[i] > pivot:
      greater.append(list[i])

  # Se llama recursivamente a la función `quick_sort()` para ordenar las dos listas.
  return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([95, 36, 42, 0, 32, 58, 73, 28, 43, 12, 50]))
