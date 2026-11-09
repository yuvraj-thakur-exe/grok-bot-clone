$ErrorActionPreference = 'Stop'
$OrbitRoot = $PSScriptRoot
$env:PYTHONPATH = if ($env:PYTHONPATH) { (Join-Path $OrbitRoot 'src') + [IO.Path]::PathSeparator + $env:PYTHONPATH } else { Join-Path $OrbitRoot 'src' }

if (Get-Command py.exe -ErrorAction SilentlyContinue) {
    & py.exe -3 -m orbit_cli @args
    exit $LASTEXITCODE
}
if (Get-Command python.exe -ErrorAction SilentlyContinue) {
    & python.exe -m orbit_cli @args
    exit $LASTEXITCODE
}
Write-Error 'ORBIT requires Python 3.11 or newer. Install Python or uv, then rerun.'
exit 9009
