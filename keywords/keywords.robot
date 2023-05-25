*** Settings ***
Documentation       Template keyword resource.

Variables           variables.py

Library             RPA.Excel.Files
Library             RPA.Tables
Library             ../libraries/MyLibrary.py


*** Keywords ***
Extraer datos del listado de operaciones
    Open Workbook    datosAsegurado.xlsx     
    ${table}=    Read Worksheet As Table    Report    header=True    
    ${fechasInicio}=    Obtener fechas de operaciones    Desde    ${table} 
    ${fechasFin}=    Obtener fechas de operaciones    Hasta    ${table}
    ${capitales}=    Obtener capitales de operaciones    Poliza    ${table} 
    ${polizas}=    Obtener numero de poliza de operaciones    Póliza    ${table}
    ${endosos}=    Obtener numero de endoso de poliza    Endoso    ${table}
    ${montoVigente}=    Calcular Suma Vigente Total    ${fechasInicio}    ${fechasFin}    
    ...    ${capitales}   ${polizas}   ${endosos}    ${fechaDesde}    ${fechaHasta}    ${montoRecibido}
    Calcular monto de inclusion y exclusion    ${montoVigente}    ${montoRecibido}


Calcular monto de inclusion y exclusion    
    [Arguments]    ${montoVigente}    ${montoRecibido}
    ${montoInclusion}=    Calcular Inclusion    ${montoVigente}    ${montoRecibido}
    ${montoExclusion}=    Calcular Exclusion   ${montoVigente}    ${montoRecibido}


Obtener fechas de operaciones
    [Arguments]    ${columna}    ${table}
    ${fechas}=    Get Table Column    ${table}    ${columna}
    [Return]    ${fechas}


Obtener capitales de operaciones
    [Arguments]    ${columna}    ${table}
    ${capitales}=    Get Table Column    ${table}    ${columna}
    [Return]    ${capitales}


Obtener numero de poliza de operaciones
    [Arguments]    ${columna}    ${table}
    ${polizas}=    Get Table Column    ${table}    ${columna}
    [Return]    ${polizas}


Obtener numero de endoso de poliza
    [Arguments]    ${columna}    ${table}
    ${endosos}=    Get Table Column    ${table}    ${columna}
    [Return]    ${endosos}





