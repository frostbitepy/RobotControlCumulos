from datetime import datetime


TODAY = datetime.now()

# Variables para trabajar con las tablas
fechaInicio = "20-06-2023"
fechaFin = "19-06-2024"
fechaDesde = None 
fechaHasta = None  
capital = None
poliza = None
endoso = None
montoVigente = None
montoRecibido = 450000000
montoLimite = 3000000000
montoInclusion = None
montoExclusion = None
formatterString = "%d-%m-%y"
path = "datosAsegurado.xlsx"
worksheet = "Report"


# Variables Robot Control de Cumulos
result = None
cantidadAsegurados = None
cedulas = None
cedula = None
nroCedula = None
montosAsegurables = None
ubicacion = "datosAsegurado.xlsx"
logTime = datetime.now()
sumaPolizas = None
sumaTotal = None
maximoAsegurable = []
cotizacionE = None
varFila = None
nuevoMontoCapital = None
capitalExcluido = None
varFila2 = None
montoCapital = None
obtenidaSuma = []
sumaObtenida = None
totalCumulo = None
cotizacionDelDia = None
vencimientos = None
vencimiento = None
cotizacionDelDiaCarga = None

