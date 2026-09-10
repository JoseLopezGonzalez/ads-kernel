<#
    EL AYUDANTE DE CREDENCIAL DEL BOOTSTRAP, EJERCIDO
    =================================================

    El bootstrap instala un ayudante de credencial en la custodia de la maquina.
    Hasta ahora nada lo ejecutaba: se comprobaba que el fichero existia, y eso
    dejo pasar dos defectos seguidos —una lista de repositorios que no se
    ejercia nunca, y un descifrado que fallaba SIEMPRE y se callaba—.

    Aqui se ejerce. Se instala con un alcance conocido, se le pone una
    credencial de LABORATORIO en la custodia —cifrada con DPAPI igual que la de
    verdad, sin ningun valor real— y se le pregunta como le pregunta `git`: por
    la entrada estandar. Se exige que responda a lo autorizado y que se calle
    ante `store`, ante `erase`, ante otro host y ante otro repositorio.

    NO usa la red, NO clona nada remoto y NO introduce ninguna credencial real.
#>

$ErrorActionPreference = 'Stop'
$Raiz = Split-Path -Parent $PSScriptRoot
$script:Fallos = @()

trap {
    $donde = "$($_.InvocationInfo.ScriptName):$($_.InvocationInfo.ScriptLineNumber)"
    $que   = ("$($_.Exception.Message)" -replace '[\r\n]+', ' ' -replace 'password=\S*', 'password=<REDACTADO>')
    Write-Host "EXCEPCION en $donde -> $que"
    if ($env:GITHUB_ACTIONS) { Write-Host "::error title=ayudante::EXCEPCION en $donde -> $que" }
    exit 1
}

function Comprueba {
    param([bool]$Cond, [string]$Que, [string]$Detalle = '')
    if ($Cond) { Write-Host "  OK     $Que"; return }
    Write-Host "  FALLA  $Que"
    if ($Detalle) { Write-Host "         $Detalle" }
    if ($env:GITHUB_ACTIONS) {
        $limpio = ("$Que · $Detalle" -replace '[\r\n]+', ' ' -replace 'password=\S*', 'password=<REDACTADO>')
        if ($limpio.Length -gt 900) { $limpio = $limpio.Substring(0, 900) }
        Write-Host "::error title=ayudante::$limpio"
    }
    $script:Fallos += $Que
}

Write-Host ('=' * 78)
Write-Host "AYUDANTE DE CREDENCIAL, EJERCIDO  ·  PowerShell $($PSVersionTable.PSVersion)"
Write-Host ('=' * 78)

$base     = if ($env:RUNNER_TEMP) { $env:RUNNER_TEMP } else { [System.IO.Path]::GetTempPath() }
$Lab      = Join-Path $base "ayudante-$PID-$($PSVersionTable.PSVersion.Major)"
$Origen   = Join-Path $Lab 'repositorio-privado.git'
$Destino  = Join-Path $Lab 'clon'
$Perfil   = if ($env:USERPROFILE) { $env:USERPROFILE } else { $HOME }
$Custodia = Join-Path $Perfil '.config/ads-pesquerapp'
$Cifrado  = Join-Path $Custodia 'github.dpapi'
$Ayudante = Join-Path $Custodia 'credencial-git.ps1'
$HabiaCred = Test-Path $Cifrado
$HabiaAyud = Test-Path $Ayudante

New-Item -ItemType Directory -Force -Path $Lab | Out-Null
New-Item -ItemType Directory -Force -Path $Custodia | Out-Null

# --------------------------------------------------------------------------
Write-Host ''
Write-Host ' 1 · credencial de LABORATORIO en la custodia'
# --------------------------------------------------------------------------
# Se construye caracter a caracter y NO con `ConvertTo-SecureString -AsPlainText`,
# que PSScriptAnalyzer marca como ERROR y con razon.
$VALOR = 'valor-de-laboratorio-sin-valor-real'
if (-not $HabiaCred) {
    $falsa = New-Object System.Security.SecureString
    foreach ($c in $VALOR.ToCharArray()) { $falsa.AppendChar($c) }
    $falsa.MakeReadOnly()
    ConvertFrom-SecureString $falsa | Set-Content -Path $Cifrado -Encoding ASCII
    $falsa.Dispose()
}
Comprueba (Test-Path $Cifrado) 'hay credencial cifrada en la custodia'
Comprueba ((Get-Content $Cifrado -Raw) -notmatch 'laboratorio') 'y NO esta en claro'

# --------------------------------------------------------------------------
Write-Host ''
Write-Host ' 2 · el bootstrap instala el ayudante, con un alcance CONOCIDO'
# --------------------------------------------------------------------------
git clone --quiet --bare $Raiz $Origen 2>&1 | Out-Null
Comprueba (Test-Path (Join-Path $Origen 'HEAD')) 'el repositorio de laboratorio existe'

$boot = Join-Path $Raiz 'operador\bootstrap.ps1'
$salida = & $boot -Repositorio $Origen -Destino $Destino `
                  -Alcance @('duenno/autorizado') *>&1 | Out-String
Comprueba (-not [string]::IsNullOrWhiteSpace($salida)) 'el bootstrap habla' "longitud $($salida.Length)"
Comprueba ($salida -match 'ayudante de credencial instalado') 'instala el ayudante' "salida: $salida"
Comprueba (Test-Path $Ayudante) 'y queda en la custodia'
Comprueba ($salida -match 'clonado en') 'y clona el laboratorio' "salida: $salida"
# Este laboratorio es el PROPIO generico, que no es una instancia ADS y por eso
# no trae `operador\arrancar.ps1`. El bootstrap se queja de eso —y hace bien—,
# asi que aqui NO se le exige codigo 0: se le exige que la queja sea ESA y no
# otra, que es lo unico que distingue un fallo esperado de uno real.
Comprueba ($salida -match 'no hay a quien entregar el control') 'y su unica queja es que el laboratorio no es una instancia ADS' "salida: $salida"

# --------------------------------------------------------------------------
Write-Host ''
Write-Host ' 3 · se le pregunta como le pregunta git'
# --------------------------------------------------------------------------
$anfitrionPS = (Get-Process -Id $PID).Path
$env:ADS_AYUDANTE_DIAGNOSTICO = '1'

function Preguntar {
    param([string]$Operacion, [string[]]$Lineas)
    $anterior = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        if ($Lineas) {
            $texto = ($Lineas -join [Environment]::NewLine)
            return ($texto | & $anfitrionPS -NoProfile -File $Ayudante $Operacion 2>&1 | Out-String)
        }
        return (& $anfitrionPS -NoProfile -File $Ayudante $Operacion 2>&1 | Out-String)
    } finally { $ErrorActionPreference = $anterior }
}

$si = Preguntar 'get' @('protocol=https', 'host=github.com', 'path=duenno/autorizado.git', '')
Comprueba ($si -match 'username=x-access-token') 'responde al repositorio autorizado' "devolvio: [$si]"
if (-not $HabiaCred) {
    Comprueba ($si -match [regex]::Escape("password=$VALOR")) 'y DESCIFRA de verdad la custodia'
} else {
    Comprueba ($si -match 'password=.') 'y DESCIFRA de verdad la custodia'
}

$noStore = Preguntar 'store' @()
Comprueba ([string]::IsNullOrWhiteSpace($noStore)) 'se calla ante `store`' "devolvio: [$noStore]"
$noErase = Preguntar 'erase' @()
Comprueba ([string]::IsNullOrWhiteSpace($noErase)) 'se calla ante `erase`' "devolvio: [$noErase]"
$noHost = Preguntar 'get' @('protocol=https', 'host=gitlab.example.com', 'path=duenno/autorizado', '')
Comprueba ([string]::IsNullOrWhiteSpace($noHost)) 'se calla ante otro host' "devolvio: [$noHost]"
$noRepo = Preguntar 'get' @('protocol=https', 'host=github.com', 'path=duenno/OTRO', '')
Comprueba ([string]::IsNullOrWhiteSpace($noRepo)) 'se calla ante otro repositorio' "devolvio: [$noRepo]"

Remove-Item Env:\ADS_AYUDANTE_DIAGNOSTICO -ErrorAction SilentlyContinue

# --------------------------------------------------------------------------
Write-Host ''
Write-Host ' 4 · sin filtraciones, y el laboratorio se borra'
# --------------------------------------------------------------------------
foreach ($p in @('gh[pousr]_[A-Za-z0-9]{16,}', 'github_pat_[A-Za-z0-9_]{20,}',
                 '://[^/\s:@]+:[^/\s@]{6,}@', [regex]::Escape($VALOR))) {
    Comprueba ($salida -notmatch $p) "la salida del bootstrap no contiene: $p"
}
Remove-Item $Lab -Recurse -Force -ErrorAction SilentlyContinue
Comprueba (-not (Test-Path $Lab)) 'el laboratorio se borro'
if (-not $HabiaCred) { Remove-Item $Cifrado -Force -ErrorAction SilentlyContinue }
if (-not $HabiaAyud) { Remove-Item $Ayudante -Force -ErrorAction SilentlyContinue }

Write-Host ''
Write-Host ('=' * 78)
if ($script:Fallos.Count -gt 0) {
    Write-Host "FALLAN $($script:Fallos.Count):"
    $script:Fallos | ForEach-Object { Write-Host "  · $_" }
    exit 1
}
Write-Host "AYUDANTE EJERCIDO Y CORRECTO en PowerShell $($PSVersionTable.PSVersion)"
exit 0
