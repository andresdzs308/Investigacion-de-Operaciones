!pip install scipy
from scipy.optimize import linprog
c = [3, 8] #Coeficientes función objetivo
A_ub = [[-1, -1], [1, -1]] #Coeficientes de restricciones
b_ub = [-50, 20] #Constantes de restricciones
bounds = [(0, None), (0, None)] #Restrcciones de variables para que sean mayores que cero
resultado1 = linprog(c, A_ub, b_ub, bounds=bounds, method="simplex",)
print("Valor óptimo 1", resultado1.fun, "Solución óptima 1 ","x= ", resultado1.x[0], "y= ", resultado1.x[1])

resultado2 = linprog(c, A_ub, b_ub, bounds=bounds, method="interior-point")
print("Valor óptimo 2", resultado2.fun, "Solución óptima 2 ","x= ",resultado2.x[0], "y= ", resultado2.x[1])

print("Diferencia valor óptimo", resultado1.fun-resultado2.fun, "Diferencia en x=", resultado1.x[0]-resultado2.x[0], "Diferencia en y=", resultado1.x[1]-resultado2.x[1])
