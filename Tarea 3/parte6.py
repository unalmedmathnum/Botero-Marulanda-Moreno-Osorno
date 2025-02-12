import math
#Vamos a seguir los pasos descritos en nuestro documento.tex
#Condiciones iniciales (Temporales)
u0 = 0.1
v0 = 0.0
t0 = 0.0
h = 0.01
t_parada = 20.0 
#Proporcionemos dos conjuntos de datos:
#CONJUNTO1 (Temporales)
epsilon1 = 0.1
lam1 = 0.2
omega1 = 1.0
#Empezaremos por definir nuestro sistema de EDOs 
def f(t,u,v):
    # Aquí u' = v
    return v
def g(t,u,v,epsilon,lam,omega):
    # Aqui tenemos u'' = v' 
    return -(1+epsilon*lam*omega**2*math.cos(omega*t))*(u-(epsilon**2*u**3)/6.0)
#Nuestro siguiente paso sera construir el metodo de Euler modificado para resolver nuestro sistema de EDOs. 
def metodoEmodificado(epsilon,lam,omega,u0,v0,t0,t_parada):
    t = t0
    u = u0
    v = v0
    resultados = [] #Creamos este vector para seguir una trayectoria de los resultados obtenidos
    resultados.append((t,u,v)) #Vamos almanecando la tripleta a medida que avanza el tiempo. 
    while t < t_parada:
        #Realizamos los pasos predictores
        u_pred = u + h*f(t,u,v) 
        v_pred = v + h*g(t,u,v,epsilon,lam,omega)
        t = t + h
        # 
    return