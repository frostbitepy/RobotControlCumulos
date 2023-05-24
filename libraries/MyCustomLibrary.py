import datetime
from datetime import datetime,date
# Variables
montoVigente = 2850000000
limiteCumulo = 3000000000
montoRecbido = 400000000
montoExclusion = 0
montoInclusion = 0
formatterString = "%d-%m-%y"


# Funcion que me permita calcular el monto de inclusion y exclusion
# Teniendo en cuenta el monto recibido en la planilla, el monto total vigente
# y el monto limite de cumulo
# Devuelve el monto de inclusion y el monto de exclusion
def calcular_inclusion(montoRecibido):
    if montoVigente >= limiteCumulo:
        montoInclusion = 0
        montoExclusion = montoRecibido
    elif (limiteCumulo - montoVigente) < montoRecibido:
        montoInclusion = limiteCumulo - montoVigente
        montoExclusion = montoRecibido - montoInclusion
    else:
        montoInclusion = montoRecibido
        montoExclusion = 0
    return montoInclusion, montoExclusion


# Funcion que me permita comparar si una fecha es mayo o menor que otra
# recibe como parametro cuatro fechas
# devuelve un booleano
def vigencias_se_superponen(fechaInicio, fechaFin, fechaDesde, fechaHasta):
    
    fechaInicio = datetime.strptime(fechaInicio, '%d-%m-%Y').date()
    fechaFin = datetime.strptime(fechaFin, '%d-%m-%Y').date()
    fechaDesde = datetime.strptime(fechaDesde, '%d-%m-%Y').date()
    fechaHasta = datetime.strptime(fechaHasta, '%d-%m-%Y').date()

    if (fechaInicio >= fechaDesde or fechaInicio <= fechaHasta) and (fechaFin >= fechaDesde or fechaFin <= fechaHasta):
        return True
    else:
        return False



fechaInicio = "30-03-2022"
fechaFin = "09-03-2023"
fechaDesde = "21-04-2022"
fechaHasta = "12-04-2023"


print(vigencias_se_superponen(fechaInicio, fechaFin, fechaDesde, fechaHasta))