import math 
#Empezaremos por definir nuestro sistema de EDOs 
def f(t,u,v):
    # Aquí u' = v
    return v
def g(t,u,v,epsilon,lam,omega):
    # Aqui tenemos u'' = v' 
    return -(1+epsilon*lam*omega**2*math.cos(omega*t))*(u-(epsilon**2*u**3)/6.0)
