
from datetime import datetime
from RPA.Excel.Files import Files
from RPA.Tables import Tables
from robot.api.deco import keyword, library


# Variables

limiteCumulo = 3000000000

CI = 1554239


class MyLibrary:
    # Funcion que me permita calcular el monto de inclusion y exclusion
    # Teniendo en cuenta el monto recibido en la planilla, el monto total vigente
    # y el monto limite de cumulo
    # Devuelve el monto de inclusion y el monto de exclusion
    
    def calcular_inclusion(self, montoVigente, montoRecibido):
        if montoVigente >= limiteCumulo:
            montoInclusion = 0
            montoExclusion = montoRecibido
        elif (limiteCumulo - montoVigente) < montoRecibido:
            if (limiteCumulo - montoVigente) <= 0:
                montoInclusion = 0
                montoExclusion = montoRecibido
            else:
                montoInclusion = limiteCumulo - montoVigente
                montoExclusion = montoRecibido - montoInclusion
        elif (limiteCumulo - montoVigente) >= montoRecibido:
            montoInclusion = montoRecibido
            montoExclusion = 0
        return montoInclusion
    

    def calcular_exclusion(self, montoVigente, montoRecibido):
        if montoVigente >= limiteCumulo:
            montoInclusion = 0
            montoExclusion = montoRecibido
        elif (limiteCumulo - montoVigente) < montoRecibido:
            if (limiteCumulo - montoVigente) <= 0:
                montoInclusion = 0
                montoExclusion = montoRecibido
            else:
                montoInclusion = limiteCumulo - montoVigente
                montoExclusion = montoRecibido - montoInclusion
        elif (limiteCumulo - montoVigente) >= montoRecibido:
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
        fechaDesde = fechaDesde.strftime("%d-%m-%Y")
        fechaHasta = fechaHasta.strftime("%d-%m-%Y")
        fechaDesde = datetime.strptime(fechaDesde, '%d-%m-%Y').date()        # Comento esta seccion ya que el formato de fecha que recibo es datetime.date
        fechaHasta = datetime.strptime(fechaHasta, '%d-%m-%Y').date()
        
        if (fechaInicio >= fechaDesde and fechaInicio <= fechaHasta) or (fechaFin >= fechaDesde and fechaFin <= fechaHasta):
            return True
        else:
            return False



    # Funcion que me permite iterar sobre los valores de la tabla, comparar las fechas si se encuentra en vigencia
    # y de acuerdo a si corresponde sumar los capitales y almacenarlas en una variable
    # devolver la suma asegurada total
    
    def calcular_suma_vigente_total(self, fechaInicio, fechaFin, capitales, polizas, endosos, fechasDesde, fechasHasta, montoRecibido):
        montoVigente = 0
        # Por el momento no utilizo los valores de poliza y endoso, pero próximamente los utilizare, aun no tengo definido como
        for (fechaDesde,fechaHasta,capital,poliza,endoso) in zip(fechasDesde,fechasHasta,capitales,polizas,endosos):
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



    # Funcion que convierte una lista de capitales en nuevo monto por la cotizacion del dia mas 500 puntos
    # recibe como parametro una lista de capitales
    # devuelve una lista de capitales con el nuevo monto
    def convertir_capitales(self, capitales, cotizacionDelDia):
        capitalesConvertidos = []
        for capital in capitales:
            capitalConvertido = (capital / cotizacionDelDia) * (cotizacionDelDia + 500)
            capitalesConvertidos.append(capitalConvertido)
        return capitalesConvertidos
    

    # Funcion que devuelve el nuevo capital consiliado en guaranies teniendo en cuenta la cotizacion mas 
    # alta entre cotizacion del dia y cotizacion del dia de carga
    def convertir_capital_mayor(self, capitales, cotizacionesDelDia, cotizacionesDelDiaDeCarga):
        capitalesConvertidos = []
        for (capital,cotizacionDelDia,cotizacionDelDiaDeCarga) in zip(capitales,cotizacionesDelDia,cotizacionesDelDiaDeCarga):
            if cotizacionDelDia >= cotizacionDelDiaDeCarga:
                capitalConvertido = (capital / cotizacionDelDia) * (cotizacionDelDia + 500)
            else:
                capitalConvertido = (capital / cotizacionDelDiaDeCarga) * (cotizacionDelDiaDeCarga + 500)

            capitalesConvertidos.append(capitalConvertido)
        return capitalesConvertidos
###############################################################################################

# print(MyLibrary.vigencias_se_superponen(fechaInicio, fechaFin, fechaDesde, fechaHasta))

