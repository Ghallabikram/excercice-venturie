import numpy as np
D1=float(input("la valeur du diamètre 1:"))
V1=float(input("la valeur de la vitesse 1:"))
alpha=float(input("lavaleur de l'angle en degre:"))
V2=1.5*V1
D2=np.sqrt(V1/V2)*D1
L=(-D1/2*np.tan(alpha))*(np.sqrt(V1/V2)-1)
print("la vitesse de section s2 est:",V2,"m/s")
print("la longueur est:",L,"m")