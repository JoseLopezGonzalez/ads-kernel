<#
    UP-04 · UN VALIDADOR INVOCADO DIRECTAMENTE EN WINDOWS TIENE QUE HABLAR
    =====================================================================

    Antes de la correccion, esto era lo que pasaba en un runner de Windows real:

        PS> python kernel\operativo\validadores\comprobar_rutas_portables.py
        PS> $LASTEXITCODE
        1                              <- un codigo, y NI UNA LINEA de salida

    La guarda `G-03` reejecutaba con `os.execve`, que en Windows no sustituye el
    proceso: lanza uno nuevo y mata el padre en el acto. Quien llamaba recogia el
    codigo del padre, no el del punto, y la salida del hijo se perdia.

    Este guion invoca validadores REALES, SIN banderas de aislamiento —que es como
    los invoca una persona— y exige lo que antes no se cumplia. Se ejecuta dos
    veces: en pwsh 7 y en Windows PowerShell 5.1, que es el que trae Windows de
    fabrica.
#>

$ErrorActionPreference = 'Stop'
$Raiz    = Split-Path -Parent $PSScriptRoot
$script:Fallos = @()

function Comprueba {
    param([bool]$Condicion, [string]$Que, [string]$Detalle = '')
    if ($Condicion) { Write-Host "  OK     $Que" }
    else {
        Write-Host "  FALLA  $Que"
        if ($Detalle) { Write-Host "         $Detalle" }
        $script:Fallos += $Que
    }
}

Write-Host ('=' * 78)
Write-Host "UP-04 · validadores invocados DIRECTAMENTE"
Write-Host "  raiz       $Raiz"
Write-Host "  PowerShell $($PSVersionTable.PSVersion)"
Write-Host ('=' * 78)

# --------------------------------------------------------------------------
# 1 · EXITO · un validador que pasa: salida NO VACIA y codigo 0
# --------------------------------------------------------------------------
Write-Host ''
Write-Host ' 1 · un validador que PASA'
$punto  = Join-Path $Raiz 'kernel\operativo\validadores\comprobar_rutas_portables.py'
$salida = & python $punto *>&1 | Out-String
$codigo = $LASTEXITCODE
Comprueba ($codigo -eq 0) 'codigo 0' "codigo obtenido: $codigo"
Comprueba (-not [string]::IsNullOrWhiteSpace($salida)) 'la salida NO esta vacia' `
          "longitud: $($salida.Length)"
Comprueba ($salida -match 'T153') 'y contiene el veredicto del escenario T153'
Comprueba ($salida -match 'T154') 'y el de T154'
# Ejecucion UNICA: el veredicto de T153 aparece una sola vez.
$veces = ([regex]::Matches($salida, 'T153')).Count
Comprueba ($veces -eq 1) 'el validador se ejecuto UNA sola vez' "T153 aparece $veces veces"

# --------------------------------------------------------------------------
# 2 · FALLO · un validador que falla: salida NO VACIA y codigo distinto de 0
# --------------------------------------------------------------------------
# El fallo tiene que ser REAL, no simulado, y provocarlo sin pelearse con el
# sistema de ficheros: se copia el kernel a un laboratorio y se le EDITA un
# fichero que la huella cubre. `comprobar_integridad` tiene entonces que decir
# que el kernel DIVERGE de su release, y decirlo EN VOZ ALTA.
Write-Host ''
Write-Host ' 2 · un validador que FALLA'
$lab = Join-Path $env:RUNNER_TEMP "up04-lab-$PID-$($PSVersionTable.PSVersion.Major)"
if (Test-Path $lab) { Remove-Item $lab -Recurse -Force -ErrorAction SilentlyContinue }
New-Item -ItemType Directory -Force -Path $lab | Out-Null
foreach ($d in @('kernel', 'packs', 'tooling')) {
    $origen = Join-Path $Raiz $d
    if (Test-Path $origen) { Copy-Item $origen (Join-Path $lab $d) -Recurse -Force }
}
Add-Content -Path (Join-Path $lab 'kernel\VERSIONES.md') -Value '# EDITADO PARA QUE DIVERJA'
$puntoMal  = Join-Path $lab 'kernel\operativo\validadores\comprobar_integridad.py'
$salidaMal = & python $puntoMal --raiz $lab *>&1 | Out-String
$codigoMal = $LASTEXITCODE
Comprueba ($codigoMal -ne 0) 'codigo distinto de 0 cuando el kernel esta editado' `
          "codigo obtenido: $codigoMal"
Comprueba (-not [string]::IsNullOrWhiteSpace($salidaMal)) 'y la salida del FALLO tampoco esta vacia' `
          "longitud: $($salidaMal.Length)"
Comprueba ($salidaMal -match 'T150') 'y nombra el escenario que se pone rojo'
Comprueba ($salidaMal -match 'DIVERGE|FALLIDA') 'y dice que el kernel diverge'

# --------------------------------------------------------------------------
# 3 · RUTA CON ESPACIOS Y CARACTERES NO ASCII
# --------------------------------------------------------------------------
Write-Host ''
Write-Host ' 3 · desde una ruta con espacios y caracteres no ASCII'
$raro = Join-Path $env:RUNNER_TEMP "lab con espacios y acentos ñ á $PID-$($PSVersionTable.PSVersion.Major)"
if (Test-Path $raro) { Remove-Item $raro -Recurse -Force -ErrorAction SilentlyContinue }
New-Item -ItemType Directory -Force -Path $raro | Out-Null
Copy-Item (Join-Path $Raiz 'kernel') (Join-Path $raro 'kernel') -Recurse -Force
$puntoRaro  = Join-Path $raro 'kernel\operativo\validadores\comprobar_rutas_portables.py'
$salidaRara = & python $puntoRaro *>&1 | Out-String
$codigoRaro = $LASTEXITCODE
Comprueba ($codigoRaro -eq 0) 'codigo 0 desde una ruta con espacios y acentos' `
          "codigo obtenido: $codigoRaro"
Comprueba (-not [string]::IsNullOrWhiteSpace($salidaRara)) 'y la salida tampoco esta vacia' `
          "longitud: $($salidaRara.Length)"
Comprueba ($salidaRara -match 'T153') 'y contiene su veredicto'

# --------------------------------------------------------------------------
# 4 · OTRO VALIDADOR CUALQUIERA · no es una propiedad de uno solo
# --------------------------------------------------------------------------
Write-Host ''
Write-Host ' 4 · no es una propiedad de un unico validador'
foreach ($otro in @('comprobar_fuentes.py', 'comprobar_referencias.py')) {
    $ruta = Join-Path $Raiz "kernel\operativo\validadores\$otro"
    if (-not (Test-Path $ruta)) { continue }
    $s = & python $ruta *>&1 | Out-String
    Comprueba (-not [string]::IsNullOrWhiteSpace($s)) "$otro habla al invocarlo directamente" `
              "longitud: $($s.Length)"
}

# --------------------------------------------------------------------------
# limpieza y veredicto
# --------------------------------------------------------------------------
foreach ($d in @($lab, $raro)) {
    if (-not (Test-Path $d)) { continue }
    Remove-Item $d -Recurse -Force -ErrorAction SilentlyContinue
    if (Test-Path $d) { cmd /c rmdir /s /q "$d" 2>&1 | Out-Null }
}

Write-Host ''
Write-Host ('=' * 78)
if ($script:Fallos.Count -gt 0) {
    Write-Host "FALLAN $($script:Fallos.Count) comprobaciones:"
    $script:Fallos | ForEach-Object { Write-Host "  · $_" }
    exit 1
}
Write-Host "UP-04 COMPROBADO en PowerShell $($PSVersionTable.PSVersion)"
exit 0
