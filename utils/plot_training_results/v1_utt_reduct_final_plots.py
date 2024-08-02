import matplotlib.pyplot as plt
import numpy as np
#Datos
epochs_new = list(range(1, 21))
train_loss_new = [5.80, 4.26, 3.34, 2.60, 2.10, 1.67, 1.37, 1.10, 0.95, 0.78, 0.71, 0.60, 0.56, 0.48, 0.47, 0.41, 0.41, 0.35, 0.35, 0.31]
valid_loss_new = [5.05, 4.17, 3.15, 2.71, 2.22, 1.98, 1.73, 1.56, 1.54, 1.38, 1.30, 1.30, 1.24, 1.19, 1.15, 1.13, 1.12, 1.10, 1.08, 1.06]
error_rate_new = [89.3, 80.5, 66.0, 57.9, 48.7, 44.1, 38.5, 34.9, 35.1, 31.8, 30.5, 29.5, 28.1, 26.7, 25.7, 25.9, 26.1, 25.0, 24.4, 23.9]
execution_time_new = [71, 38, 52, 41, 51, 40, 55, 39, 55, 49, 55, 77, 71, 45, 63, 44, 66, 44, 67, 46]

#Plots
plt.figure(figsize=(10, 6))
plt.plot(epochs_new, train_loss_new, marker='o', label='Función de pérdida de entrenamiento', color='blue')
plt.plot(epochs_new, valid_loss_new, marker='o', label='Función de pérdida de validación', color='red')
plt.xlabel('Epoch')
plt.ylabel('Función de Pérdida')
plt.ylim(bottom=0)
plt.xticks(np.arange(1, 21, 1))
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(epochs_new, error_rate_new, marker='o', color='orange')
plt.xlabel('Epoch')
plt.ylabel('Porcentaje de Error de Validación (%)')
plt.ylim(bottom=0)
plt.xticks(np.arange(1, 21, 1))
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(epochs_new, execution_time_new, marker='o', color='green')
plt.xlabel('Epoch')
plt.ylabel('Tiempo de Ejecución (min)')
plt.grid(True)
plt.xticks(np.arange(1, 21, 1))
plt.show()
