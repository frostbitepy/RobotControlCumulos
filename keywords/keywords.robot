*** Settings ***
Documentation       Template keyword resource.

Variables           variables.py

Library             RPA.Excel.Files
Library             RPA.Tables


*** Keywords ***
Abrir listado de polizas del asegurado
    Open Workbook    ${ubicacion}
    ${table}=    Read Worksheet As Table  


Obtener datos del asegurado
    Obtener numero de documento
    Obtener capital recibido
    Control de cumulo


Obtener numero de documento


Obtener capital recibido 



Control de cumulo
    Leer vigentes
    Leer poliza

Leer vigentes


Leer poliza


