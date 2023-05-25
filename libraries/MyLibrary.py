import datetime
from datetime import datetime,date
from RPA.Excel.Files import Files
from RPA.Tables import Tables
from robot.api.deco import keyword, library
#import variables



# Variables

limiteCumulo = 3000000000




CI = 1554239

tbl = Tables()
exlib = Files()
tablelib = Tables()


class MyLibrary:
    # Funcion que me permita calcular el monto de inclusion y exclusion
    # Teniendo en cuenta el monto recibido en la planilla, el monto total vigente
    # y el monto limite de cumulo
    # Devuelve el monto de inclusion y el monto de exclusion
    
    def calcular_inclusion(self, montoRecibido,montoVigente):
        if montoVigente >= limiteCumulo:
            montoInclusion = 0
            montoExclusion = montoRecibido
        elif (limiteCumulo - montoVigente) < montoRecibido:
            montoInclusion = limiteCumulo - montoVigente
            montoExclusion = montoRecibido - montoInclusion
        else:
            montoInclusion = montoRecibido
            montoExclusion = 0
        return montoInclusion
    

    def calcular_exclusion(self, montoRecibido,montoVigente):
        if montoVigente >= limiteCumulo:
            montoInclusion = 0
            montoExclusion = montoRecibido
        elif (limiteCumulo - montoVigente) < montoRecibido:
            montoInclusion = limiteCumulo - montoVigente
            montoExclusion = montoRecibido - montoInclusion
        else:
            montoInclusion = montoRecibido
            montoExclusion = 0
        return montoExclusion


    # Funcion que me permita comparar si una fecha es mayor o menor que otra
    # recibe como parametro cuatro fechas
    # devuelve un booleano
    # De esta manera verifico si las vigencias se superponen y por ende corresponde 
    # o no incluir el monto de la operacion al calculo del cumulo
    
    def vigencias_se_superponen(self, fechaInicio, fechaFin, fechaDesde, fechaHasta):
    
        fechaInicio = datetime.strptime(fechaInicio, '%d-%m-%Y').date()    
        fechaFin = datetime.strptime(fechaFin, '%d-%m-%Y').date()
        #fechaDesde = datetime.strptime(fechaDesde, '%d-%m-%Y').date()         Comento esta seccion ya que el formato de fecha que recibo es datetime.date
        #fechaHasta = datetime.strptime(fechaHasta, '%d-%m-%Y').date()

        if (fechaInicio >= fechaDesde and fechaInicio <= fechaHasta) or (fechaFin >= fechaDesde and fechaFin <= fechaHasta):
            return True
        else:
            return False



    # Funcion que me permite iterar sobre los valores de la tabla, comparar las fechas si se encuentra en vigencia
    # y de acuerdo a si corresponde sumar los capitales y almacenarlas en una variable
    # devolver la suma asegurada total
    
    def calcular_suma_vigente_total(self, fechasInicio,fechasFin,capitales,polizas,endosos,fechaDesde,fechaHasta,montoRecibido):
        montoVigente = 0
        for (fechaInicio,fechaFin,capital,poliza,endoso) in zip(fechasInicio,fechasFin,capitales,polizas,endosos):
            if self.vigencias_se_superponen(fechaInicio, fechaFin, fechaDesde, fechaHasta):
                montoVigente += capital
        return montoVigente



    # Funcion que me permite convertir una lista de fechas en formato datetime a formato string
    # recibe como parametro una lista de fechas
    # devuelve una lista de fechas en formato string
    def convertir_fecha(self, fechas):
        fechasString = []
        for fecha in fechas:            
            fechaString = fecha.replace("datetime.","")
            fechaString = fecha.strftime("%d-%m-%Y")
            fechasString.append(fechaString)
        return fechasString

###############################################################################################

fecha = datetime.datetime(2011, 6, 24, 0, 0)
fecha = str(fecha)
print(fecha.replace("datetime.",""))

