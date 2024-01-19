import numpy as np

calificaciones = np.array([
   [1, 60, 63, 63, 99, 69],
   [2, 79, 81, 96, 83, 66],
   [3, 84, 84, 72, 61, 98],
   [4, 99, 83, 84, 77, 97],
   [5, 85, 73, 68, 69, 80],
   [6, 76, 65, 75, 60, 78],
   [7, 95, 84, 89, 79, 79],
   [8, 74, 99, 92, 61, 69],
   [9, 92, 91, 70, 83, 95],
   [10, 71, 88, 94, 60, 60]
])

#promedio de calificaciones por alumno
print(np.average(calificaciones[:,1:],0))

#Calificación promedio de cada Estudiante
promedio_estudiante = np.average(calificaciones[:,1:], 1)
print((np.average(calificaciones[:,1:], 1)))

#Mejor calificacion
mejor_alumno = np.max(np.average(calificaciones[:,1:], 1))
print(mejor_alumno)

#Peor alumno
peor_alumno = np.min(np.average(calificaciones[:,1:], 1))
print(peor_alumno)


