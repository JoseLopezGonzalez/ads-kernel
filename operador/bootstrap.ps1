<#
    BOOTSTRAP DEL ADS PARA WINDOWS  ·  lo que ocurre ANTES del clon
    ===============================================================

    EL PROBLEMA QUE ESTE FICHERO RESUELVE
    -------------------------------------
    Un ADS de control vive en un repositorio PRIVADO. Su asistente de
    incorporacion —`operador/arrancar.ps1`— sabe explicar que credencial hace
    falta, con que permisos exactos, capturarla sin mostrarla y custodiarla.
    Pero vive DENTRO del repositorio. Es decir: en el momento en que hace falta,
    todavia no existe.

    La orden anterior lo ignoraba. Hacia `git clone` de un repositorio privado y
    confiaba en que el gestor de credenciales de Git abriria una ventana y el
    Owner sabria que pestana elegir. Eso no es una incorporacion guiada: es
    dejar sola a la persona en el unico paso donde una equivocacion concede
    lectura Y ESCRITURA sobre todos sus repositorios.

    Este guion es el eslabon que faltaba. Se obtiene SIN autenticacion desde el
    ADS generico, que es PUBLICO, fijado a un SHA —no a una rama— y con su
    huella comprobada antes de ejecutarse. Y hace, en este orden:

        1  comprueba el entorno: Windows, PowerShell, Git y su gestor
        2  explica que credencial hace falta y que permisos NO conceder
        3  abre la pagina de creacion y ESPERA
        4  la captura OCULTA y la cifra con DPAPI en la custodia del sistema
        5  instala el ayudante de credencial de Git
        6  clona el ADS privado usando ese ayudante
        7  entrega el control al asistente completo
        8  borra todo temporal

    NO ES ESPECIFICO DE NINGUN PRODUCTO. El repositorio a clonar y los
    repositorios que la credencial debe alcanzar se le pasan como parametros: lo
    que sabe es COMO se hace, no PARA QUIEN.

    QUE NO HACE, Y ES DELIBERADO
        · no usa `gh auth login --web`, que concede el alcance clasico `repo`
          —lectura Y ESCRITURA sobre todos los repositorios de la cuenta—;
        · no cambia la politica de ejecucion de la maquina ni del usuario;
        · no desactiva ninguna proteccion de Git;
        · no pone la credencial en la URL, en un argumento, en el historial, en
          un registro ni en un fichero sin cifrar.
#>

[CmdletBinding()]
param(
    # El repositorio ADS de control que hay que clonar.
    [Parameter(Mandatory = $true)][string]$Repositorio,
    # Donde dejarlo. Por defecto, junto al perfil del usuario.
    [string]$Destino,
    # Los repositorios que la credencial debe alcanzar, para explicarlos uno a uno.
    [string[]]$Alcance,
    # Recorrido COMPLETO sin pedir ni guardar nada. Es lo que corre la CI.
    [switch]$Simular,
    # Muestra esta cabecera y sale.
    [switch]$Ayuda
)

$ErrorActionPreference = 'Stop'

function Titulo { param([string]$t)
    Write-Host ''; Write-Host ('=' * 78); Write-Host $t; Write-Host ('=' * 78) }
function Paso   { param([string]$t) Write-Host ''; Write-Host "-- $t" }
function Ok     { param([string]$t) Write-Host "   OK     $t" }
function Aviso  { param([string]$t) Write-Host "   aviso  $t" }
function Falla  { param([string]$t) Write-Host "   FALLA  $t"; exit 1 }

if ($Ayuda) {
    $propio = $MyInvocation.MyCommand.Path
    if ($propio) {
        $texto = Get-Content $propio -Raw
        $i = $texto.IndexOf('<#'); $j = $texto.IndexOf('#>')
        if ($i -ge 0 -and $j -gt $i) { Write-Host $texto.Substring($i + 2, $j - $i - 2) }
    }
    exit 0
}

if (-not $Destino) { $Destino = Join-Path $HOME 'ads-pesquerapp' }
if (-not $Alcance) { $Alcance = @($Repositorio -replace '^https://github\.com/', '' -replace '\.git$', '') }

# `USERPROFILE` es de Windows. Se usa el que hay y se cae a `$HOME` cuando no
# existe: eso permite ejercer este recorrido fuera de Windows —que es donde se
# desarrolla— sin fingir que se ejerce donde no se ha ejercido.
$Perfil   = if ($env:USERPROFILE) { $env:USERPROFILE } else { $HOME }
$Custodia = Join-Path $Perfil '.config/ads-pesquerapp'
$Cifrado  = Join-Path $Custodia 'github.dpapi'
$Ayudante = Join-Path $Custodia 'credencial-git.ps1'

Titulo "BOOTSTRAP DEL ADS  ·  lo anterior al clon$(if ($Simular) { '   [SIMULADO]' })"
Write-Host "  repositorio  $Repositorio"
Write-Host "  destino      $Destino"
Write-Host "  custodia     $Custodia"

# ============================================================================
Paso '1 · ENTORNO'
# ============================================================================
Write-Host "   PowerShell   $($PSVersionTable.PSVersion)"
Write-Host "   sistema      $([System.Environment]::OSVersion.VersionString)"

if ($PSVersionTable.PSVersion.Major -lt 5) {
    Falla "hace falta PowerShell 5.1 o superior. Este es $($PSVersionTable.PSVersion)."
}
Ok "PowerShell suficiente"

$git = Get-Command git -ErrorAction SilentlyContinue
if (-not $git) {
    Write-Host ''
    Write-Host '   Git NO esta instalado, y hace falta antes de nada. Instalalo desde:'
    Write-Host '       https://git-scm.com/download/win'
    Write-Host '   Acepta las opciones por defecto —incluido el Git Credential Manager—'
    Write-Host '   y vuelve a ejecutar esta misma orden.'
    if ($Simular) { Aviso 'en simulacion se continua para recorrer el resto'; }
    else { exit 1 }
} else {
    Ok "git $(& git --version 2>&1 | Select-Object -First 1)"
    # El gestor de credenciales viene con Git para Windows. Se comprueba, no se supone.
    $gestor = & git config --get credential.helper 2>$null
    if ($gestor) { Ok "gestor de credenciales de Git: $gestor" }
    else { Aviso 'Git no declara gestor de credenciales; el ADS usara el suyo propio' }
}

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) { $python = Get-Command python3 -ErrorAction SilentlyContinue }
if ($python) { Ok "python $(& $python.Source --version 2>&1)" }
else { Aviso 'Python no esta en el PATH. El asistente completo lo pedira; el clon no lo necesita' }

# ============================================================================
Paso '2 · LA CREDENCIAL · que se pide, y que NO hay que conceder'
# ============================================================================
$pagina = 'https://github.com/settings/personal-access-tokens/new'
Write-Host ''
Write-Host '   Hace falta UNA credencial de GitHub de GRANO FINO y de SOLO LECTURA.'
Write-Host '   Sirve para dos cosas a la vez: traerse el repositorio de control, que es'
Write-Host '   privado, y observar despues los repositorios del producto.'
Write-Host ''
Write-Host "   CREALA AQUI:  $pagina"
Write-Host ''
Write-Host '   1 · Token name        ads-<producto>-github-<este-ordenador>'
Write-Host '   2 · Expiration        90 dias. Caducar es una virtud, no una molestia.'
Write-Host '   3 · Repository access ->  Only select repositories, y EXACTAMENTE estos:'
foreach ($r in $Alcance) { Write-Host "                             $r" }
Write-Host '   4 · Permissions  ->  Repository permissions. Pon EN READ-ONLY estos cinco:'
Write-Host '                             Metadata          Read-only   (se activa solo)'
Write-Host '                             Contents          Read-only'
Write-Host '                             Pull requests     Read-only'
Write-Host '                             Actions           Read-only'
Write-Host '                             Commit statuses   Read-only'
Write-Host ''
Write-Host '      NO concedas NADA mas. En particular:'
Write-Host '          Administration        NO. Abriria la configuracion y los webhooks.'
Write-Host '          Contents: Read+Write  NO. El ADS observa; no escribe con esta.'
Write-Host '          cualquier Write       NO, en ningun permiso.'
Write-Host '          Account permissions   NO. Ninguno.'
Write-Host ''
Write-Host '   Con esta credencial el ADS NO puede fusionar, publicar, cambiar ajustes ni'
Write-Host '   mover ramas. Las escrituras futuras usaran una autorizacion aparte,'
Write-Host '   temporal y acotada, por la via de emergencia.'
Write-Host ''
Write-Host '   Y NO elijas «Sign in with your browser» si Git te lo ofrece despues: ese'
Write-Host '   camino concede el alcance clasico `repo`, que es lectura Y ESCRITURA sobre'
Write-Host '   TODOS tus repositorios.'

# ============================================================================
Paso '3 · CAPTURA'
# ============================================================================
if ($Simular) {
    Aviso 'SIMULACION: no se abre la pagina, no se pide nada y no se guarda nada'
} elseif (Test-Path $Cifrado) {
    Ok 'ya hay una credencial en la custodia de esta maquina; no se pide otra'
} else {
    Write-Host ''
    Write-Host '   Se abrira la pagina de creacion. Cuando tengas la credencial, vuelve'
    Write-Host '   aqui y pegala: NO se vera al escribir, NO queda en el historial de'
    Write-Host '   PowerShell y NO se escribe en ningun sitio sin cifrar.'
    Write-Host ''
    try { Start-Process $pagina | Out-Null; Ok 'pagina abierta en el navegador' }
    catch { Aviso "no se pudo abrir el navegador; abrela a mano: $pagina" }

    $segura = Read-Host '   credencial de GitHub' -AsSecureString
    if ($segura.Length -eq 0) { Falla 'no se capturo nada. Nada guardado.' }

    New-Item -ItemType Directory -Force -Path $Custodia | Out-Null
    $acl = Get-Acl $Custodia
    $acl.SetAccessRuleProtection($true, $false)
    $acl.Access | ForEach-Object { [void]$acl.RemoveAccessRule($_) }
    $acl.AddAccessRule((New-Object System.Security.AccessControl.FileSystemAccessRule(
        "$env:USERDOMAIN\$env:USERNAME", 'FullControl',
        'ContainerInherit,ObjectInherit', 'None', 'Allow')))
    Set-Acl -Path $Custodia -AclObject $acl

    # DPAPI, ligada a esta cuenta de Windows: otro usuario de la misma maquina no
    # puede descifrarlo aunque lea el fichero.
    ConvertFrom-SecureString $segura | Set-Content -Path $Cifrado -Encoding ASCII
    $segura.Dispose()
    Ok "credencial cifrada en la custodia de esta maquina"
}

# ============================================================================
Paso '4 · AYUDANTE DE CREDENCIAL'
# ============================================================================
# Se escribe en la CUSTODIA, no en el arbol: el arbol todavia no existe, y
# cuando exista traera su propia copia versionada. Este es el minimo para clonar.
$fuenteAyudante = @'
param([Parameter(Position = 0)][string]$Operacion = "get")
$ErrorActionPreference = 'Stop'
if ($Operacion -ne 'get') { exit 0 }
$peticion = @{}
while ($null -ne ($linea = [Console]::In.ReadLine())) {
    if ($linea -eq '') { break }
    $t = $linea.Split('=', 2); if ($t.Count -eq 2) { $peticion[$t[0]] = $t[1] }
}
if ("$($peticion['host'])".ToLower() -notin @('', 'github.com')) { exit 0 }
$perfil  = if ($env:USERPROFILE) { $env:USERPROFILE } else { $HOME }
$cifrado = Join-Path $perfil '.config/ads-pesquerapp/github.dpapi'
if (-not (Test-Path $cifrado)) { exit 0 }
try {
    $segura  = ConvertTo-SecureString (Get-Content -Path $cifrado -Raw)
    $puntero = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($segura)
    try {
        Write-Output "username=x-access-token"
        Write-Output "password=$([Runtime.InteropServices.Marshal]::PtrToStringAuto($puntero))"
    } finally {
        [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($puntero); $segura.Dispose()
    }
} catch { exit 0 }
'@
if ($Simular) {
    Aviso 'SIMULACION: el ayudante no se instala'
} else {
    New-Item -ItemType Directory -Force -Path $Custodia | Out-Null
    Set-Content -Path $Ayudante -Value $fuenteAyudante -Encoding UTF8
    Ok "ayudante de credencial instalado en la custodia"
}

# ============================================================================
Paso '5 · CLON'
# ============================================================================
# El token viaja por la TUBERIA entre el ayudante y git. No entra en la URL
# —que acabaria en .git/config y en `git remote -v`—, ni en argv, ni en el
# historial. `-c` afecta SOLO a esta invocacion: no toca la configuracion.
$ordenClon = @('-c', "credential.helper=!powershell -NoProfile -File `"$Ayudante`"",
               'clone', $Repositorio, $Destino)
if ($Simular) {
    Aviso 'SIMULACION: no se clona nada'
    Write-Host "   la orden habria sido:  git $($ordenClon -join ' ')"
} elseif (Test-Path (Join-Path $Destino '.git')) {
    Ok 'ya estaba clonado; se deja como esta'
} else {
    & git @ordenClon
    if ($LASTEXITCODE -ne 0) { Falla "el clon fallo con codigo $LASTEXITCODE" }
    Ok "clonado en $Destino"
}

# ============================================================================
Paso '6 · ENTREGA AL ASISTENTE COMPLETO'
# ============================================================================
$asistente = Join-Path $Destino 'operador\arrancar.ps1'
if ($Simular) {
    Aviso "SIMULACION: aqui se entregaria el control a $asistente"
} elseif (Test-Path $asistente) {
    Ok "entregando el control a $asistente"
    Write-Host ''
    & $asistente
    $codigo = $LASTEXITCODE
} else {
    Falla "el repositorio no trae operador\arrancar.ps1: no hay a quien entregar el control"
}

# ============================================================================
Paso '7 · TEMPORALES'
# ============================================================================
# El bootstrap NO se borra a si mismo. Se intento, con un proceso desatendido
# que esperaba dos segundos y lo borraba, y estaba mal por dos motivos: deja
# algo vivo DESPUES de que quien llamo crea que todo termino —justo lo que este
# aparato reprocha en otras partes—, y `Start-Process -WindowStyle` no existe
# fuera de Windows, de modo que la linea reventaba en el unico sitio donde este
# recorrido se puede ensayar antes de entregarlo.
#
# Lo borra QUIEN LO CREO: la orden que lo descargo, en su `finally`. Es la regla
# corriente —quien abre, cierra— y ademas se cumple aunque esto falle a mitad.
$propio = $MyInvocation.MyCommand.Path
if ($propio -and $env:TEMP -and $propio.StartsWith($env:TEMP)) {
    Ok 'este guion vive en un temporal; lo borra la orden que lo descargo'
} else {
    Ok 'este guion no esta en un temporal; no hay nada que borrar'
}

# La credencial NO deja rastro fuera de la custodia: ni fichero suelto, ni
# variable de entorno, ni argumento. Se comprueba, no se afirma.
foreach ($sospechoso in @($env:GITHUB_TOKEN, $env:GH_TOKEN)) {
    if ($sospechoso) { Aviso 'hay un token en el entorno de esta sesion; el ADS no lo usa' }
}

Titulo 'BOOTSTRAP TERMINADO'
if ($Simular) { Write-Host '  SIMULACION: no se pidio, no se guardo y no se clono nada.' }
exit 0
