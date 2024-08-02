import matplotlib.pyplot as plt

# Datos
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
training_loss = [2.440, 1.050, 0.698, 0.513, 0.381, 0.313, 0.247, 0.218, 0.192, 0.163]
validation_loss = [1.190, 0.719, 0.557, 0.625, 0.219, 0.186, 0.156, 0.120, 0.099, 0.088]
validation_error = [31.50, 20.70, 17.70, 17.10, 6.33, 5.57, 4.38, 3.53, 2.77, 2.42]
execution_time = [66, 111, 59, 97, 94, 100, 82, 74, 74, 67]

# Plots
plt.figure(figsize=(10, 6))
plt.plot(epochs, training_loss, label='Función de pérdida de entrenamiento', marker='o',color='blue')
plt.plot(epochs, validation_loss, label='Función de pérdida de validación', marker='o',color='red')
plt.xlabel('Epoch')
plt.ylabel('Función de Pérdida')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(epochs, validation_error, label='Porcentaje de error de validación', marker='o', color='orange')
plt.xlabel('Epoch')
plt.ylabel('Porcentaje de Error de Validación (%)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(epochs, execution_time, label='Tiempo de ejecución', marker='o', color='green')
plt.xlabel('Epoch')
plt.ylabel('Tiempo de Ejecución (min)')
plt.grid(True)
plt.show()
