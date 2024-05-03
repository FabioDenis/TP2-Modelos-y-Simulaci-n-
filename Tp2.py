import numpy as np
from scipy import stats

distribuciones = []

def determinar_distribucion():
    tipo_distribucion = input("Ingrese 'continua' si la distribución es continua o 'discreta' si es discreta: ")
    if tipo_distribucion.lower() == 'continua':
        entrada = input("Ingrese la lista de datos separados por comas: ")
        datos = [float(x.strip()) for x in entrada.split(',')]

        media = np.mean(datos)
        print("Media:", media)
        varianza = np.var(datos)
        print("Varianza:", varianza)
        coeficiente_simetria = stats.skew(datos)
        print("Coeficiente de simetria:", coeficiente_simetria)
        coeficiente_variacion = np.std(datos) / media
        


        if coeficiente_simetria == 0:  # Coeficiente de simetria
            distribuciones.append("Normal y Triangular debido a que sus Valores mínimos, máximos y modales conocidos")
        elif coeficiente_variacion > 1.05:  # Coeficiente de variacion
            distribuciones.append("Lognormal y Triangular debido a que sus Valores mínimos, máximos y modales conocidos")
        elif coeficiente_variacion < 0.95:
            distribuciones.append("Weibull , Gamma y Triangular debido a que sus Valores mínimos, máximos y modales conocidoscon")
        else:
            distribuciones.append("Exponencial")
    
    elif tipo_distribucion.lower() == 'discreta':
        entrada = input("Ingrese la lista de datos separados por comas: ")
        datos = [float(x.strip()) for x in entrada.split(',')]

        media = np.mean(datos)
        print("Media:", media)
        varianza = np.var(datos)
        print("Varianza:", varianza)
        coeficiente_variacion = np.std(datos) / media
        print("Coeficiente de variacion:", coeficiente_variacion)
        tau = varianza/media
        print("Tau",tau)
        

        if tau == 1: 
            distribuciones.append("Poisson")
        elif tau < 1:
            distribuciones.append("Binomial")
        elif tau > 1:
            distribuciones.append("Binomial Negativa")
        
    else:
        print("Tipo de distribución no válido")

determinar_distribucion()
print(f"Distribuciones encontradas: {distribuciones}")