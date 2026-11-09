param(
  [string[]]$Selectors = @('--product-base')
)
$ErrorActionPreference = 'Stop'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$bash = Get-Command bash -ErrorAction SilentlyContinue
if (-not $bash) {
  $candidates = @(
    "$env:ProgramFiles\Git\bin\bash.exe",
    "$env:ProgramFiles\Git\usr\bin\bash.exe",
    "${env:ProgramFiles(x86)}\Git\bin\bash.exe"
  ) | Where-Object { $_ -and (Test-Path $_) }
  if ($candidates.Count -gt 0) { $bash = @{ Source = $candidates[0] } }
}
if (-not $bash) { throw 'Git Bash was not found. Install Git for Windows or run this command from WSL.' }
& $bash.Source (Join-Path $scriptDir 'clone_upstreams.sh') @Selectors
if ($LASTEXITCODE -ne 0) { throw "Upstream clone command failed with exit code $LASTEXITCODE" }
