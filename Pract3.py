#llamar una libreria 
import random #numeros aleatorios
#Se requiere instalar
#python -m pip install -U pip
#python -m pip install -U matplotlib
import matplotlib.pyplot as plt
print(random.randint(1,20)) 

#reacomodar una lista al azar
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('lista original', lista)
random.shuffle(lista)
print('lista mix', lista)

#Genera un agrafica de campana de Gauss
campana = [random.gauss(1,0.5) for i in range(1000)]
plt.hist(campana, bins=15)
plt.show()