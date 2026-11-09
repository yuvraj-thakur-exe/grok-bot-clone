param(
  [Parameter(Mandatory=$true)][string]$Path,
  [long]$MinimumTotalBytes = 450000000000,
  [long]$MinimumFreeBytes = 200000000000,
  [switch]$SkipCapacityCheck
)
$ErrorActionPreference = 'Stop'
$resolved = [System.IO.Path]::GetFullPath($Path)
$driveRoot = [System.IO.Path]::GetPathRoot($resolved)
if (-not $driveRoot) { throw "Path has no drive root: $resolved" }
$driveLetter = $driveRoot.Substring(0,1)
if (-not $driveLetter) { throw "Unable to resolve drive letter from $resolved" }
$volume = Get-Volume -DriveLetter $driveLetter
if (-not $SkipCapacityCheck) {
  if ($volume.Size -lt $MinimumTotalBytes) { throw "Volume total capacity $($volume.Size) bytes is below $MinimumTotalBytes. Check that this is the dedicated 500 GB disk." }
  if ($volume.SizeRemaining -lt $MinimumFreeBytes) { throw "Volume free capacity $($volume.SizeRemaining) bytes is below $MinimumFreeBytes. Free space or choose another volume." }
}
$folders = @(
  @{path='00-control'; target_gb=10; purpose='manifests, operation docs and audit reports'},
  @{path='01-upstream-checkouts'; target_gb=100; purpose='50 pinned upstream repositories (selective clone)'},
  @{path='02-workspaces'; target_gb=100; purpose='ORBIT app worktrees and disposable tasks'},
  @{path='03-models'; target_gb=90; purpose='approved local model files and inference caches'},
  @{path='04-data-memory'; target_gb=35; purpose='encrypted and scoped user data/memory'},
  @{path='05-artifacts'; target_gb=25; purpose='user-visible reports and exports'},
  @{path='06-evaluations'; target_gb=20; purpose='golden datasets and benchmark outputs'},
  @{path='07-logs-cache'; target_gb=5; purpose='redacted logs and rebuildable cache'},
  @{path='08-backups'; target_gb=25; purpose='encrypted local snapshots, not disaster recovery'},
  @{path='09-quarantine'; target_gb=10; purpose='untrusted source packages and skills'},
  @{path='10-source-intake'; target_gb=20; purpose='selected upstream source awaiting review'}
)
New-Item -ItemType Directory -Force -Path $resolved | Out-Null
foreach ($f in $folders) { New-Item -ItemType Directory -Force -Path (Join-Path $resolved $f.path) | Out-Null }
$manifest = @{
  schema_version=1; baseline='ORBIT 1.0.0-draft'; root=$resolved; capacity_target_gb_decimal=500
  allocation_mode='soft_targets_not_hard_quotas'; target_allocated_gb=440; free_reserve_target_gb=60
  volume_total_bytes=$volume.Size; volume_free_bytes=$volume.SizeRemaining; folders=$folders
  security=@{encrypt_sensitive_data=$true; secrets_in_model_context=$false; same_disk_is_disaster_backup=$false}
  notes=@('This helper does not format, partition, encrypt or impose quotas.','Disk space does not increase RAM or VRAM.','Critical backups need a separate physical/cloud destination.')
}
$out = Join-Path $resolved '.orbit-storage.json'
if (Test-Path $out) { throw "Refusing to overwrite existing storage manifest: $out" }
$manifest | ConvertTo-Json -Depth 8 | Set-Content -Encoding UTF8 $out
Write-Host "Initialized ORBIT storage root: $resolved"
Write-Host "Soft allocation: 440 GB; free reserve target: 60 GB"
Write-Host "Volume free: $([math]::Round($volume.SizeRemaining/1GB,1)) GiB. No partition/format/encryption operation was performed."
