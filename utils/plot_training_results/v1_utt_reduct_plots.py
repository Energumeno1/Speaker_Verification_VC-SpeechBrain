import matplotlib.pyplot as plt

# Datos
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train_loss = [5.83, 4.29, 3.35, 2.59, 2.07, 1.71, 1.39, 1.18, 1.03, 0.89]
valid_loss = [5.05, 4.14, 3.27, 2.71, 2.34, 1.93, 1.77, 1.62, 1.48, 1.37]
error_rate = [89.6, 78.7, 67.4, 56.6, 50.3, 42.3, 38.7, 36.2, 32.7, 30.9]
execution_time = [74, 66, 99, 97, 61, 73, 69, 77, 111, 112]  

# Plots
plt.figure(figsize=(10, 6))
plt.plot(epochs, train_loss, marker='o', label='Función de pérdida de entrenamiento', color='blue')
plt.plot(epochs, valid_loss, marker='o', label='Función de pérdida de validación',color='red')
plt.xlabel('Epoch')
plt.ylabel('Función de Pérdida')
plt.ylim(bottom=0)
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(epochs, error_rate, marker='o', color='orange')
plt.xlabel('Epoch')
plt.ylabel('Porcentaje de Error de Validación (%)')
plt.ylim(bottom=0)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(epochs, execution_time, marker='o', color='green')
plt.xlabel('Epoch')
plt.ylabel('Tiempo de Ejecución (min)')
plt.grid(True)
plt.show()
