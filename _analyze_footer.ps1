$files = Get-ChildItem -Path . -Filter "*.html" -File
$out = foreach ($f in $files) {
  $c = Get-Content $f.FullName -Raw
  if ($c -notmatch '1726050687930') { continue }
  $hasFB = [bool]($c -match 'tn-elem__7998193391726050687924')
  $recMatch = [regex]::Match($c, '#rec(\d+)\s+\.tn-elem\[data-elem-id="1726050687930"\]')
  $ytRec = if ($recMatch.Success) { $recMatch.Groups[1].Value } else { 'NONE' }
  $ovMatch = [regex]::Match($c, '#rec(\d+)\s+\.tn-elem\.tn-elem__7998193391726050687924\{left:calc')
  $ovRec = if ($ovMatch.Success) { $ovMatch.Groups[1].Value } else { 'NO-OVR' }
  $state = if (-not $hasFB) { 'NO-FB-ELEM' } elseif ($ytRec -eq $ovRec) { 'OK' } else { 'MISMATCH' }
  [PSCustomObject]@{ File = $f.Name; YTrec = $ytRec; FB = $hasFB; OVrec = $ovRec; State = $state }
}
$out | Format-Table -AutoSize | Out-String -Width 200
