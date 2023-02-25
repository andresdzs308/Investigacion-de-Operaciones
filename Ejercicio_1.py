import cvxpy as cp

# Definir las variables de optimización x e y
x = cp.Variable()
y = cp.Variable()

# Definir la función objetivo
objetivo = cp.Minimize(3*x + 8*y)

# Definir las restricciones
Restricciones = [x + y >= 50, x - y <= 20, x >= 0, y >= 0]

# Crear el objeto problema
problem = cp.Problem(objetivo, Restricciones)

# Resolver el problema utilizando el solver ECOS
s1 = problem.solve(solver=cp.ECOS)

# Resolver el problema utilizando el solver SCS
s2 = problem.solve(solver=cp.SCS)

# Comparar las soluciones generadas por cada solver y calcular las diferencias
print("Solución 1 (ECOS): x = {}, y = {}, valor objetivo = {}".format(x.value, y.value, s1))
print("Solución 2 (SCS): x = {}, y = {}, valor objetivo = {}".format(x.value, y.value, s2))
print("Diferencia en el valor objetivo: {}".format(s1 - s2))
